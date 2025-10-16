---
argument-hint: <directory> <source_url>
description: Scrape source URL and save to collection directory
allowed-tools: Bash(find:*), Bash(uv run:scripts/add_doc.py:*), Read, Edit
---

Scrape "$2" and add to "$1" collection directory with INDEX.xml entry.

## Context

This adds documentation to curated collections that AI agents search efficiently. Each collection directory contains:

- `INDEX.xml` - structured index mapping markdown files to searchable metadata
- `*.md` - scraped documentation files
- `README.md` - collection overview

The script scrapes the URL, creates the markdown file, and appends a new `<source>` entry to INDEX.xml. You will replace that entry's `<description>` `PLACEHOLDER` value after script success.

**Existing collections:** !`find . -maxdepth 1 -type d -exec test -f {}/INDEX.xml \; -printf '%P\n'`

**Invalid directories (non-empty, missing INDEX.xml):** !`find . -maxdepth 1 -type d ! -empty -exec sh -c '[ ! -f "$1/INDEX.xml" ]' _ {} \; -printf '%P\n'`

**Before** (existing INDEX.xml):

```xml
<docs_index>
  <source>
    <title>Existing Document</title>
    <description>Existing content summary...</description>
    <source_url>https://example.com/docs/existing</source_url>
    <local_file>existing-document.md</local_file>
    <scraped_at>2025-08-25</scraped_at>
  </source>
</docs_index>
```

**After** (new source appended):

```xml
<docs_index>
  <source>
    <title>Existing Document</title>
    <description>Existing content summary...</description>
    <source_url>https://example.com/docs/existing</source_url>
    <local_file>existing-document.md</local_file>
    <scraped_at>2025-08-25</scraped_at>
  </source>
  <source>
    <title>New Document Title</title>
    <description>PLACEHOLDER</description> <!-- You replace PLACEHOLDER -->
    <source_url>$2</source_url>
    <local_file>new-document-title.md</local_file>
    <scraped_at>2025-10-15</scraped_at>
  </source>
</docs_index>
```

## Workflow

Present just enough information to the overwhelmed new user, well-structured with strategic emojis.

### 1. Pre-flight validation

First, state existing collections for contextual awareness e.g. `collection1/`, `collection2/` etc.

Then, validate arguments and recommend an alternative with clear format e.g. `/add-doc2.try <recommended> SOURCE_URL` (use literal "SOURCE_URL"):

- **Invalid directory:** If "$1" is an "Invalid directory" above, reject it—non-empty directories without INDEX.xml risk inadvertent file overwrites
- **Typo detection:** Check if "$1" is similar to (but doesn't match) an existing collection
- **Semantic validation:** Analyse "$2" URL to determine topic/framework and check "$1" collection name is semantically appropriate

### 2. Run the script

Only after validation passes:

```bash
uv run scripts/add_doc.py "$1" "$2"
```

### 3. On error

Script errors print actionable information. If recovery is possible, propose specific fixes but wait for explicit user approval.

### 4. On success

When script outputs `✅ Successfully added` or `♻️ Re-scraped and updated`:

1. Read the scraped markdown file
2. Write a 15-25 word dense summary optimised for semantic search (single line, no line breaks).
3. In INDEX.xml, find the `<source>` entry where `<source_url>` matches `$2` (the URL argument)
4. In that entry's `<description>` element, replace the value `PLACEHOLDER` with your dense summary (single line, no line breaks). Ensure the closing `</description>` tag remains on the same line after editing for consistent index formatting.

Example:

```xml
<description>Covers Next.js routing, layouts, and file conventions including dynamic routes, metadata, and project organisation strategies.</description>
```
