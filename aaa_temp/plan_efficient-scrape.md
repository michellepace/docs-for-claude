# TDD Plan: Selective Description Regeneration - Branch "refactor/efficient-rescrape"

## Problem

`/rescrape-docs` command regenerates ALL descriptions even when only few files changed, wasting LLM tokens.

## Solution

Backup INDEX.xml before scraping → restore descriptions for unchanged files → Claude only fills PLACEHOLDER for changed files.

---

## Critical Context for Implementation

### Codebase Patterns (MUST FOLLOW)

- **Testing style:** Follow `tests/test_curate_doc.py` exactly
  - No pytest fixtures - use `tempfile.TemporaryDirectory()` directly
  - Helper function: `run_sync_script(collection_dir)` pattern
  - Integration tests - run actual scripts via subprocess
  - Class-based test organization
  - Test business logic, NOT Python stdlib functionality
- **Python:** Use uv, British spelling, no venv activation
- **Code style:** pyproject.toml config, ruff + pyright

### Key Technical Decisions

1. **Matching logic:** Git diff gives filenames → match by `<local_file>` in INDEX.xml (NOT by URL)
2. **Git command:** Use `git diff --name-only -w` (simpler parsing than --stat)
3. **Unchanged file handling:**
   - Whitespace-only changes count as unchanged (git -w flag)
   - Unchanged file with PLACEHOLDER backup stays PLACEHOLDER
4. **Error handling:** Malformed XML exits with clear error for Claude Code self-healing

### Current Workflow (sync_index.py)

```
1. Validate collection_dir and INDEX.xml exist
2. Sync INDEX.xml to filesystem (remove stale entries)
3. Scrape all docs → ALL descriptions become "PLACEHOLDER"
4. Output structured results
5. Run git diff --stat -w and print GIT_CHANGES blocks
```

### Critical Finding

`curate_doc.py:176` ALWAYS resets `<description>` to "PLACEHOLDER" when scraping:

```python
ET.SubElement(source, "description").text = "PLACEHOLDER"
```

This is acceptable for individual curation, but breaks batch re-scraping. Solution: backup/restore at workflow level, NOT in curate_doc.py.

---

## Phase 1: Write Tests FIRST (RED) 🔴 ✅ COMPLETE

**File:** `tests/test_sync_index.py`

**Approach:** Hybrid testing strategy

- **6 unit tests** - Test `_restore_unchanged_descriptions()` directly with mocked changed_files (fast, no git/scraping)
- **1 integration test** - Full end-to-end with real git + scraping (validates complete workflow)
- **1 error handling test** - Malformed XML validation

**Helper functions:**

```python
def create_index_xml(index_path: Path, sources: list[dict]) -> None:
    """Create INDEX.xml with given source entries."""

def get_descriptions_from_index(index_path: Path) -> dict[str, str]:
    """Parse INDEX.xml and return {local_file: description} mapping."""
```

### Class: TestDescriptionRestorationUnit (6 unit tests)

1. **test_unchanged_files_restore_descriptions()**
   - Direct test of restoration function with changed_files=set()
   - Assert: All descriptions restored from backup

2. **test_changed_files_keep_placeholder()**
   - Direct test with changed_files={"doc-a.md"}
   - Assert: Changed file stays PLACEHOLDER

3. **test_mixed_changed_and_unchanged()**
   - Test with 2 changed, 2 unchanged files
   - Assert: Selective restoration works correctly

4. **test_placeholder_backup_no_restoration()**
   - Backup has PLACEHOLDER (new collection scenario)
   - Assert: Nothing restored (PLACEHOLDER stays)

5. **test_whitespace_only_not_in_changed_set()**
   - Simulate git -w behavior (whitespace not in changed_files)
   - Assert: Description restored

6. **test_readme_excluded_from_restoration_logic()**
   - Test defensive logic if README.md appears in changed_files
   - Assert: Doc descriptions restored normally

### Class: TestIntegration (1 test)

1. **test_full_rescrape_workflow()**
   - Full end-to-end with real git repo and Firecrawl scraping
   - Validates complete workflow including git detection
   - Handles Firecrawl cache gracefully (tests both changed/unchanged scenarios)

### Class: TestErrorHandling (1 test)

1. **test_malformed_xml_exits_with_clear_error()**
   - Setup: Create INDEX.xml with invalid XML (unclosed tags)
   - Action: Run sync_index.py
   - Assert: Exit code ≠ 0, output contains INVALID_XML error with context

**Result:** All 8 tests pass in <2 seconds

---

## Phase 2: Implement to Pass Tests (GREEN) 🟢 ✅ COMPLETE

**File:** `scripts/sync_index.py`

**Key Bug Fix:** Git CWD Issue

- Fixed `_get_changed_markdown_files()` to run git from collection_dir: `cwd=collection_dir`
- Fixed `_print_git_changes_summary()` to run git from collection_dir: `cwd=collection_dir`
- This ensures git detects changes in temporary test directories correctly

### New Functions (add before main())

#### 1. _backup_index_xml(index_path: Path) -> Path

```python
def _backup_index_xml(index_path: Path) -> Path:
    """Validate XML structure and create backup file.

    Returns:
        Path to backup file (INDEX.xml.backup)

    Raises:
        SystemExit(1): On XML parse error with structured message
    """
    # Try to parse XML to validate structure
    try:
        ET.parse(index_path)
    except ET.ParseError as e:
        print(f"❌ Error: INVALID_XML|{e}|{index_path}|")
        sys.exit(1)

    # Create backup
    backup_path = index_path.with_suffix('.xml.backup')
    shutil.copy2(index_path, backup_path)
    return backup_path
```

#### 2. _get_changed_markdown_files(collection_dir: Path) -> set[str]

```python
def _get_changed_markdown_files(collection_dir: Path) -> set[str]:
    """Get set of changed .md filenames (excluding README.md) from git diff.

    Returns:
        Set of filenames only, e.g. {"spend-management.md", "ai-sdk.md"}
    """
    git_path = shutil.which("git")
    if not git_path:
        return set()  # No git = treat all as unchanged

    result = subprocess.run(
        [git_path, "diff", "--name-only", "-w"],  # ✅ FIXED: Removed path, using cwd
        capture_output=True,
        text=True,
        check=False,
        cwd=collection_dir,  # ✅ FIXED: Run git from collection directory
    )

    changed_files = set()
    for line in result.stdout.strip().split('\n'):
        if line.endswith('.md') and not line.endswith('README.md'):
            # Extract filename only (not full path)
            changed_files.add(Path(line).name)

    return changed_files
```

#### 3. _restore_unchanged_descriptions(index_path: Path, backup_path: Path, changed_files: set[str]) -> int

```python
def _restore_unchanged_descriptions(
    index_path: Path,
    backup_path: Path,
    changed_files: set[str]
) -> int:
    """Restore descriptions for unchanged files from backup.

    Args:
        index_path: Current INDEX.xml path
        backup_path: Backup INDEX.xml path
        changed_files: Set of changed .md filenames

    Returns:
        Number of descriptions restored
    """
    # Parse backup to get original descriptions
    backup_tree = ET.parse(backup_path)
    backup_root = backup_tree.getroot()
    backup_descriptions = {}

    for source in backup_root.findall("source"):
        local_file_elem = source.find("local_file")
        desc_elem = source.find("description")

        if local_file_elem is not None and desc_elem is not None:
            backup_descriptions[local_file_elem.text] = desc_elem.text

    # Parse current INDEX.xml
    tree = ET.parse(index_path)
    root = tree.getroot()
    restored_count = 0

    # Restore descriptions for unchanged files
    for source in root.findall("source"):
        local_file_elem = source.find("local_file")
        desc_elem = source.find("description")

        if local_file_elem is None or desc_elem is None:
            continue

        local_file = local_file_elem.text

        # Restore if: file unchanged AND backup has non-PLACEHOLDER description
        if (local_file not in changed_files and
            local_file in backup_descriptions and
            backup_descriptions[local_file] != "PLACEHOLDER"):

            desc_elem.text = backup_descriptions[local_file]
            restored_count += 1

    # Write back to INDEX.xml
    if restored_count > 0:
        ET.indent(root, space="  ")
        tree.write(index_path, encoding="unicode", xml_declaration=False)

    return restored_count
```

#### 4. _cleanup_backup(backup_path: Path) -> None

```python
def _cleanup_backup(backup_path: Path) -> None:
    """Delete backup file with error handling (non-fatal)."""
    try:
        backup_path.unlink(missing_ok=True)
    except OSError as e:
        print(f"⚠️  Could not delete backup: {e}", file=sys.stderr)
```

### Modify main() function

**Note:** All required imports (`shutil`, `subprocess`, `sys`, `ET`, `Path`) are already present in `sync_index.py`.

**Implemented changes:**

1. **After validation, BEFORE sync** (moved earlier to catch XML errors):

```python
# Backup INDEX.xml (validates XML structure)
backup_path = _backup_index_xml(index_path)
```

1. **After git changes summary**:

```python
# Restore unchanged descriptions
changed_files = _get_changed_markdown_files(collection_dir)
restored_count = _restore_unchanged_descriptions(index_path, backup_path, changed_files)
print(f"📝 Restored {restored_count} unchanged description(s)")

# Cleanup backup file
_cleanup_backup(backup_path)
```

**Test Results:** All 8 tests pass, average runtime <2 seconds

---

## Phase 3: Update Command Documentation ✅ COMPLETE

**File:** `.claude/commands/rescrape-docs.md`

**Status:** Implemented - command now generates descriptions for PLACEHOLDER entries only

**Modify Step 3 (lines 57-83):** Replace entire section with content between `<replace_with>` tags:

<replace_with>

### 3. Generate descriptions for PLACEHOLDER entries only

Parse `$1/INDEX.xml` to get all `<source>` entries where `<description>PLACEHOLDER</description>`.

For each PLACEHOLDER source, read the corresponding markdown file and write a 20-30 word dense description (single line, no line breaks) following the example patterns in between `<example_description>`.

Write all descriptions to `descriptions.txt` in this format:

```text
https://example.com/url1
Description for url1 here
https://example.com/url2
Description for url2 here
```

<example_description>

[Keep existing examples unchanged]

</example_description>

**Critical:** Only generate for PLACEHOLDER entries. Unchanged files already have descriptions restored by sync_index.py.

</replace_with>

---

## Testing Notes

### Setup Test Collections

Use real Firecrawl API for integration tests (like test_curate_doc.py does).
Each test should:

1. Create temp directory
2. Initialize as git repo (`git init`, `git config user.email/name`)
3. Run curate_doc.py to create initial collection
4. Manually set descriptions in INDEX.xml (not PLACEHOLDER)
5. Git commit the collection
6. Make changes as needed for test scenario
7. Git commit changes
8. Run sync_index.py and assert results

### Running Tests

```bash
# Run all sync tests
uv run pytest tests/test_sync_index.py -v

# Run specific test
uv run pytest tests/test_sync_index.py::TestDescriptionRestoration::test_unchanged_files_restore_original_descriptions -v

# Run with output
uv run pytest tests/test_sync_index.py -v -s
```

---

## Implementation Checklist

### Phase 1: Tests ✅ COMPLETE

- [x] Rewrote test suite with hybrid approach (8 tests: 6 unit + 1 integration + 1 error)
- [x] Verify all tests initially FAIL (red)
- [x] All tests now PASS (green) in <2 seconds

### Phase 2: Implementation ✅ COMPLETE

- [x] Implement _backup_index_xml()
- [x] Implement _get_changed_markdown_files() + fix git cwd bug
- [x] Implement _restore_unchanged_descriptions()
- [x] Implement _cleanup_backup()
- [x] Modify main() to call new functions
- [x] Fix _print_git_changes_summary() git cwd bug
- [x] All tests PASS with correct behavior
- [x] Code passes ruff linting and formatting

### Phase 3: Command Update ✅ COMPLETE

- [x] Update rescrape-docs.md Step 3 to only generate for PLACEHOLDER
- [x] Manual integration test: Run /rescrape-docs on real collection (nextjs)
- [x] Verify descriptions only regenerated for changed files (2 PLACEHOLDER, 1 restored)
- [x] Token savings confirmed: 33% reduction (2/3 descriptions vs all 3)

---

## Success Criteria

1. ✅ All pytest tests pass (8/8 passing in ~1.8 seconds)
2. ✅ `sync_index.py` preserves descriptions for unchanged files
3. ✅ Git change detection works correctly (cwd bug fixed)
4. ✅ Unit tests provide fast feedback loop
5. ✅ `/rescrape-docs` command integration complete
6. ✅ Token usage reduction confirmed (33% savings on nextjs test)

## Current Status: ✅ ALL PHASES COMPLETE

**Implemented & Tested:**

- ✅ Backend logic fully implemented and tested
- ✅ `sync_index.py` correctly restores descriptions for unchanged files
- ✅ Changed files get PLACEHOLDER as expected
- ✅ All edge cases covered (whitespace, README, new collections, etc.)
- ✅ Command file updated to generate only PLACEHOLDER descriptions
- ✅ Real-world validation: `/rescrape-docs nextjs` demonstrated token savings

**Efficiency Gains Achieved:**

- ✅ Selective description regeneration working as designed
- ✅ 33% token reduction confirmed (nextjs: 2/3 descriptions regenerated)
- ✅ Scalable: Savings increase with collection size and lower change frequency
