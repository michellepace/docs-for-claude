---
argument-hint: <directory> <source_url>
description: Scrape source URL and save to collection directory
allowed-tools: Bash(find:*), Bash(uv run:scripts/add_doc.py:*), Read, Edit
---

Scrape $2 and add to $1 collection directory with INDEX.xml entry.

## Context

This adds documentation to curated collections that AI agents search efficiently. Each `collection/` contains:

- `INDEX.xml` - structured index mapping markdown files to searchable metadata
- `*.md` - scraped documentation files
- `README.md` - collection overview

The script scrapes the URL, creates the markdown file, and appends a new `<source>` entry to INDEX.xml. You will replace that entry's `<description>` `PLACEHOLDER` value after script success.

**Existing collections:** !`find . -maxdepth 1 -type d -exec test -f {}/INDEX.xml \; -printf '%P\n'`

The script modifies INDEX.xml in this pattern:

<example_structure>

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

</example_structure>

## Workflow

**Communication style always:** Be brief and write simply. Format for readability and use emojis.

### 1. 🤔 Validate arguments

First, validate in this order:

1. **Missing args:** If either $1 or $2 is missing → show inline collections list and suggest alternative
2. **Typo detection:** If $1 similar to existing collection → suggest correction
3. **Semantic mismatch:** If $2 URL topic/framework doesn't match $1 collection name → warn and suggest appropriate collection

If all validation checks pass, output a success message and proceed to step 2 directly "just do it, don't wait":

<example_output_success>

```
## 🙂 Super! Scraping Shiny doc to shiny/ collection...
```

</example_output_success>

Example output on validation failures:

<example_output_failure>

This are examples, adjust as needed.

- Missing args (generic):

  ```
  ## 🤔 Missing arguments!
  - Usage: `/add-doc <collection> <url>`
  - Existing collections: `shiny`, `uv`, `tailwind`
  - Example: `/add-doc shiny https://shiny.posit.co/py/docs/overview.html`

  [Friendly recommendation in 1 short sentence]
  ```

- Missing args (URL as $1, smart inference):

  ```
  ## 🤔 Missing collection argument!
  - URL detected: `https://nextjs.org/docs/app/getting-started/caching`
  - Suggested collection: `nextjs`
  - Try: `/add-doc nextjs https://nextjs.org/docs/app/getting-started/caching`

  [Friendly recommendation in 1 short sentence]
  ```

- Typo detection:

  ```
  ## 🤔 Collection "shiyy" doesn't exist, but you have "shiny".
  - Did you mean: `/add-doc shiny https://example.com/docs` ?

  [Friendly recommendation in 1 short sentence]
  ```

- Semantic mismatch:

  ```
  ## 🤔 Collection mismatch!
  - Collection: `shiny`
  - URL: `https://tailwindcss.com/docs/installation`
  - This appears to be Tailwind CSS docs, not Shiny
  - Did you mean: `/add-doc tailwind https://tailwindcss.com/docs/installation` ?

  [Friendly recommendation in 1 short sentence]
  ```

</example_output_failure>

### 2. 🚀 Run the script

```bash
uv run scripts/add_doc.py "$1" "$2"
```

### 3. ❌ On script error

Script errors print actionable information. If recovery is possible, propose specific fixes but wait for explicit user approval.

### 4. ✨ On success

When script outputs `✨ Collection Success!`:

1. Read the scraped markdown file
2. Write a 20-30 word dense summary optimised for semantic search (single line, no line breaks).
3. In INDEX.xml, find the `<source>` entry where `<source_url>` matches `$2` (the URL argument)
4. In that entry's `<description>` element, replace the value `PLACEHOLDER` with your dense summary (single line, no line breaks). Ensure the closing `</description>` tag remains on the same line after editing for consistent index formatting.

Example:

<example>

- Description format:

  ```xml
  <description>Covers Next.js routing, layouts, and file conventions including dynamic routes, metadata, and project organisation strategies.</description>
  ```

- Final success message:

  ```
  ## ✨ Collection Success! overwrote and re-indexed:

  🎯 What happened
  - In Collection:         `collection`
  - Scraped and overwrote: `collection/document.md`
  - Updated the index:     `collection/INDEX.xml`
  - Dense description:     (see below)

  *your actual 15-25 word summary here*
  ```

</example>
