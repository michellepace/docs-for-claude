---
argument-hint: [directory] [source_url]
description: Scrape URL and save to directory
---

Please scrape "$2" and save into "$1" directory and update INDEX.xml.

This script adds a scraped document to a document collection directory. The purpose of the collection is to provide clean context in markdown for AI Coding Agents. The happy path is that the source url is scraped and saved to file and a new `<source>` appended to `INDEX.xml`.

**Before** (existing INDEX.xml):

```xml
<docs_index>
  <source>
    <title>Existing Document</title>
    <description>Existing content summary...</description>
    <source_url>https://example.com/docs/existing</source_url>
    <local_file>existing-document.md</local_file>
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
  </source>
  <source>
    <title>New Document Title</title>
    <description>PLACEHOLDER</description>
    <source_url>$2</source_url>
    <local_file>new-document-title.md</local_file>
  </source>
</docs_index>
```

1. Run this script:

   ```bash
   uv run scripts/add_doc.py "$1" "$2"
   ```

2. Analyse the script output:

- If "✅ Successfully added and indexed: [filename.md]" or "♻️ Re-scraped and updated: [filename.md]": then analyse the file and replace placeholder content in `<description>` with a 2-3 sentence dense summary optimised for AI semantic search to help agents locate relevant docs.

- ❌ Otherwise: investigate what went wrong starting from the script output. Think of how you can best help the user and make suggestions. Await for confirmation before self-healing.
