# add_doc.py - Implementation Specification

**Purpose:** Support script for `/add-doc` slash command that scrapes documentation URLs and manages INDEX.xml collections.

## Command Interface

**Slash Command:** `/add-doc [root_directory] [source_url]`

**Script Invocation:** `uv run scripts/add_doc.py "$1" "$2"`

**Arguments:**

- `root_directory` - Documentation collection directory (e.g., `tailwind`, `tailwind/`)
- `source_url` - Web URL to scrape (e.g., `https://tailwindcss.com/docs/installation`)

## Core Requirements

### 1. Directory Handling

- Accept directory with or without trailing slash (normalize internally)
- If directory doesn't exist: Create it with README.md and INDEX.xml
- If directory exists: Use existing structure

### 2. Scraping & File Creation

- Use FireCrawl MCP to scrape `source_url`
- Extract metadata: `title`, `ogUrl` (fallback to source_url)
- Generate filename from metadata title
- Write scraped content to `[root_directory]/[filename].md`

### 3. INDEX.xml Management

- Create new INDEX.xml if directory is new
- Append `<source>` entry to existing INDEX.xml
- Use PLACEHOLDER for `<description>` (Claude Code fills later)
- Check for duplicate URLs (prevent re-adding same source)

### 4. README.md Template (New Directories)

```markdown
# [Directory Name] Documentation

Curated docs for targeted AI context.

**Index**: [INDEX.xml](INDEX.xml)
**Source**: [ogUrl from FireCrawl metadata]
```

### 5. INDEX.xml Schema

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

## Script Behavior

### Success Path

- Print: `✅ Successfully added [filename.md]`
- Exit code: 0

### Error Handling

- Print actionable errors to stderr
- Exit code: 1 (non-zero)
- Claude Code will analyze output and suggest fixes

### Validation

1. Normalize directory path (remove trailing slash)
2. Validate source_url format (scheme + netloc)
3. Check for duplicate source_url in INDEX.xml (if exists)
4. Validate FireCrawl scrape succeeded
5. Ensure valid filename generation

## Design Decisions

**Q1: Description Generation**

- Script creates `<description>PLACEHOLDER</description>`
- Claude Code analyzes file and generates optimized description afterward

**Q2: Directory Creation Documentation**

- Not explicitly documented in slash command
- Script handles creation transparently

**Q3: INDEX.xml Example in Slash Command**

- Use before/after example to show append behavior

## High-Level Flow

```text
┌─────────────────────────────────────────────────────────────┐
│ START: /add-doc [root_directory] [source_url]              │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │ Parse & Validate Args│
            │  - Normalize dir path│
            │  - Validate URL      │
            └──────────┬───────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │ Check Directory      │
            └──────────┬───────────┘
                       │
         ┌─────────────┴─────────────┐
         │                           │
         ▼                           ▼
    [NOT EXISTS]               [EXISTS]
         │                           │
         ▼                           ▼
┌────────────────┐         ┌────────────────┐
│ Create Dir     │         │ Load INDEX.xml │
│ Create README  │         │ Check for dups │
│ Create INDEX   │         └────────┬───────┘
└────────┬───────┘                  │
         │                           │
         └─────────────┬─────────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │ Scrape with FireCrawl│
            │  - Get content       │
            │  - Extract metadata  │
            └──────────┬───────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │ Generate Filename    │
            │  from metadata.title │
            └──────────┬───────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │ Write .md File       │
            └──────────┬───────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │ Update INDEX.xml     │
            │  - Add <source>      │
            │  - description:      │
            │    PLACEHOLDER       │
            └──────────┬───────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │ Print Success Message│
            │ ✅ Successfully added│
            │    [filename.md]     │
            └──────────┬───────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │ EXIT 0               │
            └──────────────────────┘


     Error at any step:
         ▼
    ┌────────────────┐
    │ Print Error    │
    │ to stderr      │
    └────────┬───────┘
             │
             ▼
    ┌────────────────┐
    │ EXIT 1         │
    └────────────────┘
```

## Test Cases to Cover

1. **New directory** - Creates dir, README.md, INDEX.xml
2. **Existing directory** - Appends to INDEX.xml
3. **Duplicate URL** - Detects and prevents re-adding
4. **Invalid URL** - Rejects with clear error
5. **FireCrawl failure** - Handles scrape errors
6. **Invalid directory path** - Validates parent exists
7. **Trailing slash normalization** - `tailwind/` → `tailwind`
8. **Filename generation** - Handles special chars in titles

## Next Steps

1. Write pytest tests for each case
2. Implement script incrementally
3. Test with real FireCrawl MCP
4. Update slash command XML example (before/after)
