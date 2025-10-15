---
argument-hint: <directory> <source_url>
description: Scrape URL and save to collection directory
---

Scrape "$2" and add to "$1" collection directory with INDEX.xml entry.

## Context

This adds documentation to curated collections that AI agents search efficiently. Each collection directory contains:

- `INDEX.xml` - structured index mapping markdown files to searchable metadata (title, description, source_url, local_file, scraped_at timestamp)
- `*.md` - scraped documentation files
- `README.md` - collection overview

The script scrapes the URL, creates the markdown file, and appends a new `<source>` entry to INDEX.xml with `<description>PLACEHOLDER</description>` that you'll replace with an AI-generated summary.

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

### 1. Run the script

```bash
uv run scripts/add_doc.py "$1" "$2"
```

### 2. On error

If the script fails:

**Missing INDEX.xml:**

- `❌ Directory '[dir]' is not empty and missing INDEX.xml`

Then help the user:

1. Find existing collections: `find . -name "INDEX.xml" -type f`
2. Recommend appropriate numbered options based on the source URL, include full command with "SCRAPE_URL" for brevity e.g `/add-doc <recommendation> SCRAPE_URL`. Use "$2" to inform recommendation.
3. Keep output brief and clear for new users, well-structured with some emojis

**Other errors:**

- Investigate from script output and suggest fixes
- Wait for user confirmation before attempting repairs

### 3. On success

When script outputs `✅ Successfully added` or `♻️ Re-scraped and updated`:

1. Read the scraped markdown file
2. Write a 15-25 word dense summary optimised for semantic search (single line, no line breaks).
3. In INDEX.xml, find the `<source>` entry where `<source_url>` matches `$2` (the URL argument)
4. In that entry's `<description>` element, replace the value `PLACEHOLDER` with your dense summary (single line, no line breaks). Ensure the closing `</description>` tag remains on the same line after editing.

Example:

```xml
<description>Covers Next.js routing, layouts, and file conventions including dynamic routes, metadata, and project organisation strategies.</description>
```
