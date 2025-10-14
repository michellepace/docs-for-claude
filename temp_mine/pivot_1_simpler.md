# 📚 Documentation Index Management System

**Purpose:** One-way sync system where markdown files are the source of truth, and INDEX.xml is an AI-generated index for efficient documentation discovery.

**Date:** 2025-10-14

---

## 🎯 Core Philosophy

### The Design

This system uses **one-way generation** (.md files → INDEX.xml) where markdown files are the single source of truth.

**Why?**

- ✅ **Simpler mental model**: Users manage only markdown files
- ✅ **Less friction**: No sync conflicts, no dual maintenance
- ✅ **AI-powered intelligence**: Claude Code generates optimal metadata
- ✅ **Natural workflow**: "I have docs" → "Index them" (not "maintain both")

### Source of Truth Hierarchy

```text
1. Markdown files (.md)     ← Content (raw documentation)
2. INDEX.xml                 ← Generated index for efficient doc discovery
3. Claude Code               ← AI intelligence layer (reads docs, generates metadata)
```

**Key Principle:** INDEX.xml is a *derived artifact*, not a co-equal source of truth. Claude Code reads markdown content to intelligently extract metadata.

**No Format Required:** Markdown files need no special format. Claude Code uses AI to understand document structure contextually and extract metadata intelligently.

---

## 📋 Command Specifications

### Summary Table

| Command *(1)* | Purpose | Generates INDEX.xml | Modifies .md | User Approval |
|---------|---------|---------------------|--------------|---------------|
| `/generate-index` | Create complete new index | ✅ Full regeneration | ❌ | No |
| `/sync-index` | Incremental sync | ✅ Adds missing ✅ removes orphaned sources | ❌ | ✅ All changes *(2)* |
| `/add-new-doc` | Crawl & add single doc | ✅ Adds one source | ✅ Creates .md | No |
| `/recrawl-docs` | Re-crawl existing docs | ✅ If content changed | ✅ Overwrites | ✅ All changes *(2)* |
| `/ask-docs` | Query docs | ❌ Read-only | ❌ Read-only | ❌ |

- *Note (1): All commands require `<directory>` as first argument*
- *Note (2): Claude Code analyses script output and summarizes changes for user approval*

---

### 1️⃣ `/generate-index <dir>`

**Purpose:** Create a complete INDEX.xml from scratch by analyzing all .md files in directory.

**Behavior:**

1. Scan directory for all `*.md` files (excludes `README.md`)
2. Claude Code reads each file and generates metadata:
   - `<title>`: Extracted by reading document structure and content
   - `<description>`: AI-generated summary optimized for context matching
   - `<source_url>`: Extracted by analyzing document content and structure
   - `<local_file>`: Filename
3. Create new INDEX.xml (overwrites if exists)

**Use Cases:**

- ✅ Initial setup of new doc directory
- ✅ Recovery from corrupted INDEX.xml
- ✅ Major refactoring (discard all old metadata)

**Example:**

```bash
/generate-index uv
# → Claude: "Analyzing 23 markdown files..."
# → Claude: "Generated INDEX.xml with 23 sources"
```

**Output Format:**

```xml
<docs_index>
  <source>
    <title>Projects and Packaging</title>
    <description>Explains UV project structure, pyproject.toml configuration, and build system integration</description>
    <source_url>https://docs.astral.sh/uv/concepts/projects/</source_url>
    <local_file>concepts_projects.md</local_file>
  </source>
  <!-- ... more sources -->
</docs_index>
```

---

### 2️⃣ `/sync-index <dir>`

**Purpose:** Incrementally sync INDEX.xml with current .md files (non-destructive).

**Behavior:**

**Phase 1: Structural Sync**

1. Check INDEX.xml is valid (root element `<docs_index>`)
2. Identify new .md files not in INDEX.xml → Add skeleton `<source>` entries
3. Identify orphaned `<source>` elements (no matching .md) → Remove them
4. Verify 1:1 correspondence between .md files and `<source>` elements

**Phase 2: Schema Validation**

1. Check existing complete `<source>` elements have all 4 required fields
2. Report incomplete sources (those added in Phase 1 or manually edited)

**Phase 3: AI Enrichment (User-Initiated)**

1. Claude Code prompts: "Found N incomplete sources. Populate metadata?"
2. On approval: AI analyzes those .md files and fills in missing fields
3. **Preservation**: Existing complete `<source>` elements are NEVER overwritten

**Use Cases:**

- ✅ User manually added .md files to directory
- ✅ Periodic maintenance (check for drift)
- ✅ Validate INDEX.xml reflects current directory state

**Example:**

```bash
/sync-index uv
# → Script output:
#    ✓ INDEX.xml is valid
#    + Added skeleton source for: new_feature.md
#    - Removed orphaned source: deleted_doc.md
#    ⚠ 1 incomplete source found
# → Claude: "1 new source added (new_feature.md). Populate metadata? [Y/n]"
# → User: Y
# → Claude: "Analyzing new_feature.md... Metadata populated ✓"
```

**Script Output Format (for Claude Code to parse):**

```text
STATUS: structural_sync_complete
ADDED: new_feature.md
REMOVED: deleted_doc.md
INCOMPLETE: 1
COMPLETE: 22
```

---

### 3️⃣ `/add-new-doc <dir> <url>`

**Purpose:** Crawl a single documentation page and add it to the collection.

**Behavior:**

1. Crawl specified URL using FireCrawl MCP
2. Generate filename from URL slug (e.g., `concepts_preview.md`)
3. Write markdown content to `<dir>/<filename>.md`
4. Claude Code reads the crawled content and generates complete metadata
5. Add complete `<source>` element to INDEX.xml with all fields populated

**Implementation:** Fully atomic - one command completes everything.

**Use Cases:**

- ✅ Adding single new documentation page
- ✅ Expanding existing doc collection

**Example:**

```bash
/add-new-doc uv https://docs.astral.sh/uv/concepts/preview/

# → Claude: "Crawling https://docs.astral.sh/uv/concepts/preview/..."
# → Claude: "Analyzing content and generating metadata..."
# → Claude: "✓ Created concepts_preview.md"
# → Claude: "✓ Added source to INDEX.xml (title: 'Preview Features', description: '...')"
```

---

### 4️⃣ `/recrawl-docs <dir> [filename]`

**Purpose:** Re-crawl existing documentation to detect upstream changes.

**Behavior:**

**For all docs (no filename specified):**

1. Read INDEX.xml to extract all `<source_url>` values
2. Crawl each URL using FireCrawl MCP
3. Write crawled content to temporary files
4. Diff each temp file against current .md file (semantic comparison)
5. Report changes and present for user approval:
   - Content unchanged → Skip
   - Content changed (minor) → Overwrite .md, preserve INDEX.xml metadata
   - Content changed (major) → Overwrite .md, suggest updating `<description>`
   - Title changed → Suggest updating `<title>` and `<description>`
6. Apply approved updates

**For single doc (filename specified):**

1. Find `<source>` in INDEX.xml where `<local_file>` matches filename
2. Extract `<source_url>` from that element
3. Crawl that URL
4. Apply same diff logic as above

**Use Cases:**

- ✅ Periodic refresh (docs updated upstream)
- ✅ Before publishing doc collection updates
- ✅ Verify specific doc is current

**Example:**

```bash
/recrawl-docs uv

# → Claude: "Crawling 23 docs from INDEX.xml..."
# → Claude: "Changes detected in 3 files:"
# → Claude: "  1. concepts_projects.md - Minor updates (preserve metadata)"
# → Claude: "  2. cli_init.md - Major changes (suggest new description)"
# → Claude: "  3. guides_preview.md - Title changed: 'Preview Features' → 'Experimental Features'"
# → Claude: "Apply updates? [Y/n]"
# → User: Y
# → Claude: "✓ Updated 3 files"
# → Claude: "Recommendation: Update <title> and <description> for guides_preview.md"
```

**Single file example:**

```bash
/recrawl-docs uv concepts_projects.md

# → Claude: "Crawling https://docs.astral.sh/uv/concepts/projects/..."
# → Claude: "Content changed (minor updates detected)"
# → Claude: "Apply update? [Y/n]"
# → User: Y
# → Claude: "✓ Updated concepts_projects.md"
```

---

### 5️⃣ `/ask-docs <dir> <question>`

**Purpose:** Query documentation collection using AI (read-only).

**Behavior:**

1. Parse INDEX.xml to build doc catalog
2. Semantic search: match question against all `<description>` fields
3. Rank sources by relevance
4. Read top N most relevant .md files
5. Generate answer using doc content as context

**Use Cases:**

- ✅ Daily development queries
- ✅ Quick reference lookup
- ✅ Understanding specific concepts

**Example:**

```bash
/ask-docs uv "What does init --package do?"

# → Claude: "Searching uv documentation..."
# → Claude: "Found relevant docs: cli_init.md, concepts_projects.md"
# → Claude: [Reads those files]
# → Claude: "The `uv init --package` command creates a new..."
```

---

## 🗺️ User Flows

### Flow 1: Fresh Start - Create New Doc Directory 📦

```text
User creates directory ➜ Manually adds .md files ➜ /generate-index <dir> ➜
Claude Code analyzes all .md ➜ Generates INDEX.xml with complete metadata ➜ Done
```

**Details:**

- .md files have no required format
- Claude Code extracts titles and URLs intelligently from content
- Descriptions optimized for semantic search

**Example:**

```bash
mkdir reflex/
cp ~/downloads/*.md reflex/
/generate-index reflex

# → Claude: "Found 12 markdown files in reflex/"
# → Claude: "Analyzing content..."
# → Claude: "Generated INDEX.xml with 12 sources ✓"
```

---

### Flow 2: Add Single New Doc via Crawl 🕷️

```text
/add-new-doc <dir> <url> ➜ Crawl page ➜
Claude Code analyzes content ➜ Generates metadata ➜
Create .md + Add complete <source> to INDEX.xml ➜ Done
```

**Details:**

- Fully atomic - one command, no user approval needed
- Claude Code intelligently extracts title, URL, and generates description
- Both .md file and INDEX.xml entry created in single operation

**Example:**

```bash
/add-new-doc uv https://docs.astral.sh/uv/guides/integration/

# → Claude: "Crawling documentation page..."
# → Claude: "✓ Created guides_integration.md"
# → Claude: "✓ Added to INDEX.xml"
```

---

### Flow 3: Incremental Sync - User Added Files Manually 📝

```text
User drops 3 .md files into uv/ ➜ /sync-index uv ➜
Script adds 3 skeleton <sources> ➜ Prints "3 new sources added" ➜
Claude Code prompts: "Populate metadata? [Y/n]" ➜ User: Y ➜
Claude Code analyzes 3 files ➜ Fills <title>, <description>, <source_url> ➜ Done
```

**Details:**

- Existing complete `<source>` elements untouched
- Only new files trigger AI analysis
- User can decline and manually edit INDEX.xml instead

**Example:**

```bash
cp ~/new-docs/*.md uv/
/sync-index uv

# → Claude: "Structural sync complete"
# → Claude: "Added 3 new sources: feature_a.md, feature_b.md, feature_c.md"
# → Claude: "Populate metadata for 3 new sources? [Y/n]"
# → User: Y
# → Claude: "Analyzing 3 files... ✓ Metadata populated"
```

---

### Flow 4: Refresh Docs from Upstream 🔄

**Full directory refresh:**

```text
/recrawl-docs uv ➜ Extract 23 URLs from INDEX.xml ➜
Crawl all 23 pages ➜ Save to temp files ➜
Diff temp vs current .md files ➜
Report: "3 changed, 20 unchanged" ➜
Show change summary ➜ User approves ➜
Overwrite 3 .md files ➜
Suggest INDEX.xml updates for major changes ➜ Done
```

**Single file refresh:**

```text
/recrawl-docs uv concepts_projects.md ➜
Find source_url in INDEX.xml ➜ Crawl page ➜
Diff temp vs current ➜ Show changes ➜ User approves ➜
Overwrite .md ➜ Suggest description update if major change ➜ Done
```

**Change Detection:**

- **Minor changes (< 20% diff):** Update .md only, preserve INDEX.xml metadata
- **Major changes (≥ 20% diff):** Update .md, suggest regenerating `<description>`
- **Title changes:** Update .md, suggest regenerating `<title>` and `<description>`

**Example:**

```bash
/recrawl-docs uv

# → Claude: "Crawling 23 documentation pages..."
# → Claude: "3 files changed, 20 unchanged"
# → Claude: "Changes:"
# → Claude: "  • concepts_projects.md (minor)"
# → Claude: "  • cli_init.md (major - suggest description update)"
# → Claude: "  • guides_preview.md (title changed)"
# → Claude: "Apply updates? [Y/n]"
# → User: Y
# → Claude: "✓ Files updated"
# → Claude: "💡 Tip: Run /sync-index uv to update metadata for major changes"
```

---

### Flow 5: Complete Regeneration 🔥

```text
User notices INDEX.xml is outdated ➜ /generate-index uv ➜
Claude Code analyzes all 23 .md files ➜ Creates fresh INDEX.xml ➜
All metadata AI-generated ➜ Done
```

**Details:**

- Nuclear option: discards all INDEX.xml content
- Useful for recovery or major refactoring
- All metadata regenerated from current .md content

**Example:**

```bash
/generate-index uv

# → Claude: "⚠️  This will overwrite INDEX.xml. Continue? [Y/n]"
# → User: Y
# → Claude: "Analyzing 23 files..."
# → Claude: "✓ Generated fresh INDEX.xml"
```

---

### Flow 6: Validation & Self-Healing 🩹

**Successful sync:**

```text
/sync-index uv ➜
Script: Check XML validity ✓ ➜
Script: Add missing sources (2 found) ➜
Script: Remove orphaned sources (1 found) ➜
Script: Validate existing sources ✓ ➜
Claude Code: "Added 2 new sources, removed 1 orphan. Populate new sources? [Y/n]"
```

**Error scenario:**

```text
/sync-index uv ➜
Script: Check XML validity ✗ ➜
Script exits with error ➜
Claude Code: "INDEX.xml is malformed (invalid root element)" ➜
Claude Code: "Options:"
  1. Fix manually
  2. Run /generate-index to rebuild
```

**Example:**

```bash
/sync-index uv

# → Claude: "✓ INDEX.xml is valid"
# → Claude: "✓ Structural sync complete"
# → Claude: "  + Added: new_feature.md, new_guide.md"
# → Claude: "  - Removed: old_deprecated.md"
# → Claude: "Populate metadata for 2 new sources? [Y/n]"
# → User: Y
# → Claude: "✓ Metadata populated"
```

---

### Flow 7: Daily Q&A Usage 💬

```text
/ask-docs uv "What is init --package?" ➜
Parse INDEX.xml (23 sources) ➜
Semantic search on <description> fields ➜
Rank by relevance ➜
Read top 2 .md files (cli_init.md, concepts_projects.md) ➜
Generate answer with citations ➜
Return answer to user
```

**Details:**

- Read-only operation (no modifications)
- Uses `<description>` fields for efficient semantic matching
- Only loads relevant docs into context (not entire collection)

**Example:**

```bash
/ask-docs uv "How do I add a development dependency?"

# → Claude: "Searching uv documentation..."
# → Claude: "Found relevant docs: cli_add.md, concepts_dependencies.md"
# → Claude: "To add a development dependency, use:"
# → Claude: "  uv add --dev <package>"
# → Claude: ""
# → Claude: "This adds the package to the [dependency-groups] section..."
# → Claude: "(Source: cli_add.md:45, concepts_dependencies.md:128)"
```

---

## 📊 INDEX.xml Schema

### Structure

```xml
<docs_index>
  <source>
    <title>Document Title</title>
    <description>Summary optimized for semantic search and context matching</description>
    <source_url>https://original-docs-url</source_url>
    <local_file>filename.md</local_file>
  </source>
  <!-- ... more sources -->
</docs_index>
```

### Field Descriptions

| Field | Purpose | Generated By | Example |
|-------|---------|--------------|---------|
| `<title>` | Human-readable document title | AI extraction from .md content | "Projects and Packaging" |
| `<description>` | Semantic search-optimized summary | AI generation from .md content | "Explains UV project structure, pyproject.toml..." |
| `<source_url>` | Original documentation URL | AI extraction from .md content | "<https://docs.astral.sh/uv/concepts/projects/>" |
| `<local_file>` | Filename on disk | Direct mapping | "concepts_projects.md" |

### Validation Rules

**Required:**

- Root element must be `<docs_index>`
- Each `<source>` must have all 4 child elements
- All field values must be non-empty
- `<source_url>` must start with `http://` or `https://`

**1:1 Mapping:**

- Each .md file (except README.md) must have exactly one `<source>` entry
- Each `<source>` entry must reference an existing .md file

---

## 🔧 Technical Implementation Notes

### Metadata Extraction

Claude Code uses AI to extract metadata from markdown files:

**Title Extraction:**

- Analyzes document structure and headings
- Considers first `#` heading, filename, and content context
- No rigid format required

**URL Extraction:**

- Searches for URLs in document content
- Analyzes link patterns and references
- May use filename conventions as hints

**Description Generation:**

- Reads entire document content
- Generates concise summary (2-3 sentences)
- Optimizes for semantic search and context matching
- Focuses on "what" and "why" rather than "how"

### Phase 2 Schema Validation Logic

```python
# Phase 1: Structural sync (modifies INDEX.xml)
existing_sources = parse_existing_sources()  # Snapshot BEFORE modifications
newly_added = add_skeleton_sources_for_new_md_files()
orphaned = remove_sources_without_md_files()

# Phase 2: Schema validation (report only)
incomplete_existing = []
for source in existing_sources:
    if not has_all_required_fields(source):
        incomplete_existing.append(source)

# Separate reporting
print(f"Added {len(newly_added)} new sources (incomplete, need population)")
print(f"Removed {len(orphaned)} orphaned sources")
if incomplete_existing:
    print(f"⚠ {len(incomplete_existing)} pre-existing sources have schema issues")
```

This ensures newly added skeleton sources aren't reported as "errors" - they're expected to be incomplete.

---

**End of Document**
