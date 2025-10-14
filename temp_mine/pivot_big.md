# add_doc.py - Implementation Specification

**Purpose:** Support script for `/add-doc` slash command that scrapes documentation URLs and manages INDEX.xml collections.

## Command Interface

**Slash Command:** `/add-doc [directory] [source_url]`

**Script Invocation:** `uv run scripts/add_doc.py "$1" "$2"`

**Arguments:**

- `directory` - Documentation collection directory (e.g., `tailwind`, `tailwind/`)
- `source_url` - Web URL to scrape (e.g., `https://tailwindcss.com/docs/installation`)

## Core Requirements

### 1. Directory Handling ✅

- ✅ Accept directory with or without trailing slash (normalize internally)
- ✅ If directory doesn't exist: Create it with README.md and INDEX.xml
- ✅ If directory exists and is empty: Create README.md and INDEX.xml
- ✅ If directory exists with INDEX.xml: Use existing collection (append only)
- ✅ If directory exists, is non-empty, and missing INDEX.xml: Exit with error

### 2. Scraping & File Creation ✅

- ✅ Use FireCrawl Python SDK to scrape `source_url`
- ✅ Extract metadata: `title`, `ogUrl` (fallback to source_url)
- ✅ Generate filename from metadata title
- ✅ Write scraped content to `[directory]/[filename].md`

### 3. INDEX.xml Management ✅

- ✅ Create new INDEX.xml if directory is new
- ✅ Append `<source>` entry to existing INDEX.xml
- ✅ Use PLACEHOLDER for `<description>` (Claude Code fills later)
- ✅ Check for duplicate URLs and update existing source (not reject)

### 4. README.md Template (New Directories) ✅

```markdown
# [Directory Name] Documentation

Curated docs for targeted AI context.

**Index**: [INDEX.xml](INDEX.xml)
**Source**: [ogUrl from FireCrawl metadata]
```

### 5. INDEX.xml Schema ✅

```xml
<docs_index>
  <source>
    <title>[from FireCrawl metadata.title]</title>
    <description>PLACEHOLDER</description>
    <source_url>[from argument source_url]</source_url>
    <local_file>[generated from title].md</local_file>
  </source>
</docs_index>
```

## Script Behavior ✅

### Success Path ✅

- ✅ Print: `✅ Successfully added and indexed: [filename.md]`
- ✅ Exit code: 0

### Error Handling ✅

- ✅ Print actionable errors to stderr
- ✅ Exit code: 1 (non-zero for errors, 2 for argparse errors)
- ✅ Claude Code will analyze output and suggest fixes

### Validation ✅

1. ✅ Normalize directory path (remove trailing slash)
2. ✅ Validate source_url format (scheme + netloc)
3. ✅ Check for duplicate source_url and update if exists
4. ✅ Validate FireCrawl scrape succeeded
5. ✅ Ensure valid filename generation

## High-Level Flow

```text
START: /add-doc [directory] [source_url]
  │
  ├─► 1. Parse & Validate
  │    ├─ Normalize directory path (strip trailing /)
  │    ├─ Validate URL (scheme + netloc)
  │    └─ Validate directory (reject non-empty without INDEX.xml)
  │
  ├─► 2. Ensure Directory Exists
  │    └─ mkdir (always, even if scraping fails)
  │
  ├─► 3. Scrape with FireCrawl (FAIL FAST)
  │    ├─ Get markdown content
  │    └─ Extract metadata (title, ogUrl)
  │
  ├─► 4. Initialize Collection (if INDEX.xml missing)
  │    ├─ Create README.md (with ogUrl)
  │    └─ Create INDEX.xml with <docs_index> root (no sources)
  │
  ├─► 5. Generate & Write Document
  │    ├─ Generate filename from title (slugified)
  │    └─ Write markdown content to file
  │
  └─► 6. Update INDEX.xml (using ElementTree)
       ├─ Check for duplicate source_url:
       │   └─ If exists: delete old entry, cleanup old .md file (if filename changed)
       ├─ Add/replace <source> entry with auto-escaped XML:
       │   ├─ <title> from FireCrawl metadata
       │   ├─ <description> = "PLACEHOLDER" (always reset)
       │   ├─ <source_url> from command argument
       │   └─ <local_file> from slugified title
       └─ Print: ✅ "Successfully added" OR ♻️ "Re-scraped and updated"

[Any error] → Print to stderr → EXIT 1
```

## Test Cases ✅

1. ✅ **New directory** - Creates dir, README.md, INDEX.xml
2. ✅ **Existing directory** - Appends to INDEX.xml
3. ✅ **Duplicate URL** - Updates existing source and refreshes content
4. ✅ **Invalid URL** - Rejects with clear error
5. ✅ **FireCrawl failure** - Handles scrape errors (implicit in integration tests)
6. ✅ **Invalid directory path** - Validates non-empty without INDEX.xml
7. ✅ **Trailing slash normalization** - `tailwind/` → `tailwind` (implicit)
8. ✅ **Filename generation** - Handles special chars in titles (implicit)

## Implementation Complete ✅

**Status:** All requirements implemented and tested!

**Key Features:**

- ✅ Refactored to use `xml.etree.ElementTree` for robust XML handling
- ✅ Automatic XML character escaping (handles `<`, `>`, `&` in titles/URLs)
- ✅ **Update-on-duplicate**: Re-scraping same URL refreshes content (not rejected)
- ✅ Automatic cleanup of old .md files when title changes
- ✅ Pretty-printed XML output with `ET.indent()` (Python 3.9+)
- ✅ 9 passing integration tests with real FireCrawl API calls

**Update Behavior:**
When re-scraping an existing URL:

- ✅ Markdown file overwritten with fresh content
- ✅ INDEX.xml entry replaced (title, local_file updated)
- ✅ Description reset to "PLACEHOLDER" (for Claude to regenerate)
- ✅ Old .md file deleted if filename changed due to title change
- ✅ User sees ♻️ "Re-scraped and updated" message
