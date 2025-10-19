---
argument-hint: <collection-dir> <source_url>
description: Scrape source URL and save to collection directory
allowed-tools: Bash(find:*), Bash(uv run:scripts/curate_doc.py:*), Read, Edit
model: claude-sonnet-4-5-20250929
---

Scrape $2 and add to $1 collection directory with INDEX.xml entry.

## Context

This adds documentation to curated collections that AI agents search efficiently. Each `collection/` contains:

- `INDEX.xml` - structured index mapping markdown files to searchable metadata
- `*.md` - scraped documentation files
- `README.md` - collection overview

The script scrapes the URL, creates the markdown file, and appends a new `<source>` entry to INDEX.xml. You will replace that entry's `<description>` `PLACEHOLDER` value after script success.

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

### 1. 🤔 Validate arguments

You are helping a new user curate a document from source URL $2 into an existing or new collection directory $1.

**Existing collections:** !`find . -maxdepth 1 -type d -exec test -f {}/INDEX.xml \; -printf '%P\n'`

Here are just a few examples what new users can inadvertantly get wrong - you are to help them do what they intend:

<validation_examples>

Examples of validation failures:

<validation_failure>

- Missing args (generic):

  ```
  ## 🤔 Missing arguments!
  - Usage: `/curate-doc <collection> <url>`
  - Existing collections: `shiny`, `uv`, `tailwind`
  - Example: `/curate-doc shiny https://shiny.posit.co/py/docs/overview.html`

  [Friendly suggestion. Ask for confirmation.]
  ```

- Missing args (URL as $1, smart inference):

  ```
  ## 🤔 You didn't give me a collection?
  - URL detected: `https://vite.dev/guide/cli.html`
  - My Suggestion: A new `vite` collection looks ideal!
  - Try: `/curate-doc vite https://vite.dev/guide/cli.html`

  [Shall we proceed with `vite` as a new collection? It will get created automatically 🙂]
  ```

- Typo detection:

  ```
  ## 🤔 Collection "shiyy" doesn't exist, but you have "shiny"!
  - Did you mean: `/curate-doc shiny https://example.com/docs` ?

  [Friendly suggestion. Ask for confirmation.]
  ```

- Semantic mismatch:

  ```
  ## 🤔 Mmm.. are you sure you meant `shiny`?
  - Collection: `shiny`
  - URL: `https://tailwindcss.com/docs/installation`
  - This appears to be Tailwind CSS docs, not Shiny
  - Did you mean: `/curate-doc tailwind https://tailwindcss.com/docs/installation` ?

  [Friendly recommendation in 1-2 short sentence, ask for confirmation]
  ```

</validation_failure>

Success:

<validation_success>

```
## 🙂 Super! Scraping Shiny doc to shiny/ collection...
```

</validation_success>

</validation_examples>

Be emoji led, brief, and helpful for an overwhelmed new user. Analyse "Existing Collections" and both arguments $1 (proposed collection directory) and $2 (URL). Determine if the arguments should fail validation. Use the above examples as a guide and adapt for user experience (think emojis, structure, `highlighting`). Otherwise output a success message and proceed without confirmation.

### 2. 🚀 Run the script

```bash
uv run scripts/curate_doc.py "$1" "$2"
```

### 3. ❌ On script error

Script errors print actionable information. If recovery is possible, propose specific fixes but wait for explicit user approval.

### 4. 🎉 On success

When script outputs `🎉 Curation Success!`:

1. Read the scraped markdown file shown in the `🎉 Curation Success!` output
2. Write a 20-30 word dense description optimised for semantic search (single line, no line breaks).
3. In `$1/INDEX.xml`, find the `<source>` entry where `<source_url>` matches `$2` (the URL argument)
4. In that entry's `<description>` element, replace the value `PLACEHOLDER` with your dense description (single line, no line breaks). Ensure the closing `</description>` tag remains on the same line after editing for consistent index formatting.

Example:

<example>

- Description format:

  ```xml
  <description>Next.js folder structure covering top-level folders (`app`, `pages`, `public`, `src`), routing files (`page.js`, `layout.js`, `loading.js`, `error.js`), dynamic routes, route groups, private folders, parallel/intercepted routes, colocation patterns, component hierarchy, and metadata file conventions.</description>
  ```

- Final success message:

  ```
  ## 🎉 Curation Success!

  🎯 What happened
  - Scraped source URL: https://shiny.posit.co/py/docs/overview.html
  - Overwrote document: `shiny/overview.md`
  - Generated description: *actual 20-30 word dense description here*
  - Updated index: `shiny/INDEX.xml`

  ```

</example>
