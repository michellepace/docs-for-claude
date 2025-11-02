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

## Phase 1: Write Tests FIRST (RED) 🔴

**File:** `tests/test_sync_index.py`

**Helper function:**

```python
def run_sync_script(collection_dir: str) -> tuple[int, str]:
    """Run sync_index.py via uv and return (exit_code, output)."""
    cmd = ["uv", "run", "python", "scripts/sync_index.py", collection_dir]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    return result.returncode, result.stdout + result.stderr
```

### Class: TestDescriptionRestoration (6 tests)

1. **test_unchanged_files_restore_original_descriptions()**
   - Setup: Create temp collection, add 2 docs with real descriptions
   - Action: Run sync_index.py (no git changes)
   - Assert: INDEX.xml both descriptions preserved (not PLACEHOLDER)

2. **test_changed_files_become_placeholder()**
   - Setup: Temp collection with 2 docs with descriptions
   - Action: Modify one .md file, git add/commit, run sync_index.py
   - Assert: Changed file→PLACEHOLDER, unchanged→original description

3. **test_all_placeholder_when_all_files_changed()**
   - Setup: Collection with descriptions
   - Action: Modify all .md files, git commit, run sync_index.py
   - Assert: All descriptions are PLACEHOLDER

4. **test_new_collection_all_placeholder()**
   - Setup: Fresh collection (first scrape, all PLACEHOLDER in backup)
   - Action: Run sync_index.py
   - Assert: All remain PLACEHOLDER (nothing to restore)

5. **test_whitespace_only_changes_restore_description()**
   - Setup: Modify file with only whitespace changes (spaces, newlines)
   - Action: Git commit, run sync_index.py
   - Assert: Description restored (git -w ignores whitespace)

6. **test_readme_changes_dont_affect_descriptions()**
   - Setup: Modify only README.md
   - Action: Git commit, run sync_index.py
   - Assert: All doc descriptions restored normally

### Class: TestErrorHandling (1 test)

1. **test_malformed_xml_exits_with_clear_error()**
   - Setup: Create INDEX.xml with invalid XML (unclosed tags, etc)
   - Action: Run sync_index.py
   - Assert: Exit code ≠ 0, output contains line number/parse error context

**Expected:** All 7 tests FAIL initially (functionality doesn't exist yet)

---

## Phase 2: Implement to Pass Tests (GREEN) 🟢

**File:** `scripts/sync_index.py`

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
        [git_path, "diff", "--name-only", "-w", str(collection_dir)],
        capture_output=True,
        text=True,
        check=False
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

Add imports at top:

```python
import shutil  # If not already imported
```

Insert in main() after validation, before scraping loop:

```python
# NEW: Backup before scraping (around line 205, after sync)
backup_path = _backup_index_xml(index_path)
```

Insert in main() after git changes summary (around line 228):

```python
# NEW: Restore unchanged descriptions
changed_files = _get_changed_markdown_files(collection_dir)
restored_count = _restore_unchanged_descriptions(index_path, backup_path, changed_files)
print(f"📝 Restored {restored_count} unchanged description(s)")

# NEW: Cleanup backup file
_cleanup_backup(backup_path)
```

**Iterative development:** Run `uv run pytest tests/test_sync_index.py -v` after each function until all pass.

---

## Phase 3: Update Command Documentation

**File:** `.claude/commands/rescrape-docs.md`

**Modify Step 3 (lines 57-83):** Replace entire section with:

```markdown
### 3. Generate descriptions for PLACEHOLDER entries only

Parse `$1/INDEX.xml` to get all `<source>` entries where `<description>PLACEHOLDER</description>`.

For each PLACEHOLDER source, read the corresponding markdown file and write a 20-30 word dense description (single line, no line breaks) following the example patterns in between `<example_description>`.

Write all descriptions to `descriptions.txt` in this format:

```

<https://example.com/url1>
Description for url1 here
<https://example.com/url2>
Description for url2 here

```

<example_description>

[Keep existing examples unchanged]

</example_description>
```

**Critical:** Only generate for PLACEHOLDER entries. Unchanged files already have descriptions restored by sync_index.py.

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

- [ ] Phase 1: Write all 7 tests in test_sync_index.py
- [ ] Verify all tests FAIL (red)
- [ ] Phase 2: Implement _backup_index_xml()
- [ ] Phase 2: Implement _get_changed_markdown_files()
- [ ] Phase 2: Implement _restore_unchanged_descriptions()
- [ ] Phase 2: Implement _cleanup_backup()
- [ ] Phase 2: Modify main() to call new functions
- [ ] Verify all tests PASS (green)
- [ ] Phase 3: Update rescrape-docs.md Step 3
- [ ] Manual integration test: Run /rescrape-docs on real collection
- [ ] Verify descriptions only regenerated for changed files

---

## Success Criteria

1. All pytest tests pass
2. `/rescrape-docs` command only generates descriptions for PLACEHOLDER entries
3. Unchanged files preserve original descriptions
4. Token usage significantly reduced for collections with few changes
