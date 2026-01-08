---
argument-hint: <collection-dir> <source_url>
description: Scrape source URL and save to collection directory
allowed-tools: Read, Write, Bash(find:*), Bash(uv run:scripts/curate_doc.py:*), Bash(uv run:scripts/update_index_descriptions.py:*)
---

Scrape $2 and add to $1 collection directory with INDEX.xml entry.

## Context

Documentation curation enables targeted, efficient context retrieval for AI agents. Rather than searching entire documentation sites, curated collections provide semantic descriptions in INDEX.xml that map specific topics to relevant markdown files.

The script scrapes content from $2, writes it to a markdown file in $1/, and adds a new `<source>` entry to INDEX.xml with a PLACEHOLDER description. Your task is to replace PLACEHOLDER with a semantic summary after successful scraping.

## Workflow

### 1. Validate arguments

You are helping a new user curate a document from source URL $2 into an existing or new collection directory $1.

**Existing collections:** !`find . -maxdepth 1 -type d -exec test -f {}/INDEX.xml \; -printf '%P\n'`

Here are just a few examples what new users can inadvertently get wrong - you are to help them do what they intend:

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

### 2. Run the script

```bash
uv run scripts/curate_doc.py "$1" "$2"
```

### 3. On script error

Script errors print actionable information. If recovery is possible, propose specific fixes but wait for explicit user approval. Proceed ONLY when script outputs `🎉 Curation Success!` - don't waste effort if the script failed.

### 4. Generate descriptions for PLACEHOLDER entries only

Descriptions must be optimised for **Claude Code semantic search**, not human readability:

1. **High-signal keyword density** - Include specific API names, function names, patterns, and technical terms Claude will search for
2. **Conceptual enumeration** - List the main topics/concepts covered, not just paraphrase the title
3. **Backticks for code** - ALWAYS use backticks for code elements: `config.json`, `useQuery()`, `--flag`, etc.

**Preserve high-value terms:** Retain "best practices", "anti-patterns", "patterns", "gotchas" when the document covers these topics.

**Avoid:** Do NOT include "Does not cover..." or similar exclusions — these create false positive matches in semantic search.

<example_description>

```xml
<!-- Good: 24 words, backticks for code, high keyword density -->
<description>Convex database fundamentals: tables, JSON-like documents, optional schemas with `defineSchema`/`defineTable`, document IDs, `v` validators. Entry point for reading/writing data.</description>

<!-- Good: 30 words, enumerates concepts with backticks -->
<description>Folder and file conventions including top-level folders, routing files (`layout`, `page`, `loading`, `error`, `route`), dynamic routes, route groups, private folders, parallel and intercepted routes, metadata conventions, colocation patterns.</description>

<!-- Good: 23 words, technical terms with backticks -->
<description>`uv add`/`uv remove` commands, dependency sources (Git, URL, path, workspace), optional dependencies, development groups, build dependencies, editable installations, dependency specifiers syntax.</description>
```

</example_description>

Now, write a description:

1. Analyse the scraped markdown file
2. Draft a description (20-30 words) following the 3 quality criteria above
3. **COUNT THE WORDS** using `echo "description text" | wc -w` to verify it's 20-30 words - if not, rewrite until it is
4. Write the validated description to `$1/description.txt` in this format:

      ```text
      overview-shiny-for-python.md
      Description for this file here
      ```

5. Run the update script to apply the description:

   ```bash
   uv run scripts/update_index_descriptions.py "$1" "$1/description.txt"
   ```

### 5. Report success

Output the final success message following the `<example_success_message>` format:

<example_success_message>

```
## 🎉 Curation Success!

🎯 What happened
- Scraped source URL: https://shiny.posit.co/py/docs/overview.html
- [Created/Overwrote] document: `shiny/overview.md`
- Generated description: (see below!)
- [Added/Updated] index: `shiny/INDEX.xml`

"_[your generated description]_" = [actual word count] words ✓
```

</example_success_message>
