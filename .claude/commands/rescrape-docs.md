---
argument-hint: <collection-dir>
description: Re-scrape all docs in collection and regenerate descriptions
allowed-tools: Read, Write, Bash(find:*), Bash(uv run:*), Bash(uv run:scripts/sync_index.py:*), Bash(uv run:scripts/update_index_descriptions.py:*)
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
- Preserves existing index descriptions for unchanged/whitespace-only content
- Sets PLACEHOLDER index descriptions only for new or content changed docs
- Specifies pending documents with PLACEHOLDER needing generated description

### 3. Generate descriptions for PLACEHOLDER entries only

Parse `$1/INDEX.xml` to get all `<source>` entries where `<description>PLACEHOLDER</description>`.

Review example description patterns:

<example_description>

```xml
<!-- Example 1 (30 words, single line, no line breaks) -->
<description>Folder and file conventions including top-level folders, routing files (layout, page, loading, error, route), dynamic routes, route groups, private folders, parallel and intercepted routes, metadata conventions, colocation patterns, component hierarchy.</description>

<!-- Example 2 (23 words, single line, no line breaks) -->
<description>Dependency fields, uv add/remove commands, dependency sources (Git, URL, path, workspace), optional dependencies, development groups, build dependencies, editable installations, and dependency specifiers syntax.</description>

<!-- Example 3 (27 words, single line, no line breaks) -->
<description>Advanced reactive patterns including `@reactive.event` and `isolate` for event-driven execution, `req` for conditional execution, `invalidate_later` for scheduled updates, `@reactive.file_reader` for monitoring files, and `@reactive.poll` for conditional polling.</description>
```

</example_description>

Now, for each PLACEHOLDER source:

1. Analyse the corresponding markdown file
2. Draft a description (20-30 words) following the example patterns above
3. **COUNT THE WORDS** using `echo "description text" | wc -w` to verify it's 20-30 words - if not, rewrite until it is
4. Append the validated description to `$1/descriptions.txt` in this format:

   ```text
   https://example.com/url1
   Description for url1 here
   ```

### 4. Update INDEX.xml

Run the update script to apply all descriptions:

```bash
uv run scripts/update_index_descriptions.py "$1" "$1/descriptions.txt"
```

Verify `PLACEHOLDER` no longer appears in `$1/INDEX.xml`, otherwise suggest self-healing action and await user confirmation.

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
- [Analyse script output section "## Git Content Changes" and list files here]

*NB: excludes files with only whitespace changes*
```

</example_summary_message>
