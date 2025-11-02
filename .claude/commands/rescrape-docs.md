---
argument-hint: <collection-dir>
description: Re-scrape all docs in collection and regenerate descriptions
allowed-tools: Read, Write, Bash(find:*), Bash(uv run:*)
model: claude-sonnet-4-5-20250929
---

Re-scrape all documents in $1 collection directory and batch-regenerate descriptions.

## Context

Documentation curation enables targeted, efficient context retrieval for AI agents. Rather than searching entire documentation sites, curated collections provide semantic descriptions in INDEX.xml that map specific topics to relevant markdown files.

This command re-scrapes all sources in $1, syncs INDEX.xml to the filesystem, and batch-regenerates dense descriptions optimised for semantic search.

## Workflow

### 1. Validate argument

Validate $1 is an existing collection (reject if not). If it looks like a typo, suggest the correct collection name.

**Existing collections:** !`find . -maxdepth 1 -type d -exec test -f {}/INDEX.xml \; -printf '%P\n'`

<example_validation_success>

```
## 🙂 Super! Re-scraping $1 collection...
```

</example_validation_success>

<example_validation_failure>

```
## 🤔 Missing argument!
- Usage: `/rescrape-docs <collection>`
- Existing: `shiny`, `uv`, `tailwind`

[Friendly recommendation/suggestion in 1 short sentence]
```

</example_validation_failure>

### 2. Run sync and scrape

```bash
uv run scripts/sync_index.py "$1"
```

This script:

- Syncs INDEX.xml to filesystem (removes stale entries)
- Re-scrapes all docs via curate_doc.py
- Outputs structured results
- Script errors print actionable information

### 3. Generate descriptions for PLACEHOLDER entries only

Parse `$1/INDEX.xml` to get all `<source>` entries where `<description>PLACEHOLDER</description>`.

For each PLACEHOLDER source, read the corresponding markdown file and write a 20-30 word dense description (single line, no line breaks) following the example patterns in between `<example_description>`.

Write all descriptions to `descriptions.txt` in this format:

```
https://example.com/url1
Description for url1 here
https://example.com/url2
Description for url2 here
```

<example_description>

```xml
<!-- Example 1 (single line, no line breaks) -->
<description>Folder structure covering top-level folders (`app`, `pages`, `public`, `src`), routing files (`page.js`, `layout.js`, `loading.js`, `error.js`), dynamic routes, route groups, private folders, parallel/intercepted routes, colocation patterns, component hierarchy, and metadata file conventions.</description>

<!-- Example 2 (single line, no line breaks) -->
<description>Dependency fields, uv add/remove commands, dependency sources (Git, URL, path, workspace), optional dependencies, development groups, build dependencies, editable installations, and dependency specifiers syntax.</description>

<!-- Example 3 (single line, no line breaks) -->
<description>Advanced reactive patterns including `@reactive.event` and `isolate` for event-driven execution, `req` for conditional execution, `invalidate_later` for scheduled updates, `@reactive.file_reader` for monitoring files, and `@reactive.poll` for conditional polling.</description>
```

</example_description>

**Critical:** Only generate for PLACEHOLDER entries. Unchanged files already have descriptions restored by sync_index.py.

### 4. Update INDEX.xml

Run the update script to apply all descriptions:

```bash
uv run scripts/update_index_descriptions.py "$1" descriptions.txt
```

### 5. Report completion

Parse structured output from the script and report completion following the `<example_summary_message>` format:

<example_summary_message>

```
## ✅ Re-scrape Complete!

📊 Statistics
- Collection:            `$1`
- Stale sources removed: [N]
- Total docs:            [M]
- Successfully scraped:  [X]
- Failed to scrape:      [Y]
- Descriptions updated:  [X]

💡 Collection Content Changes for `$1`:
- [List files from GIT_CHANGES block]

*NB: excludes files with whitespace changes*
```

</example_summary_message>
