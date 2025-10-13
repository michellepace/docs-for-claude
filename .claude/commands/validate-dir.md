---
allowed-tools: Bash(test:*), Bash(uv run:*)
argument-hint: <dir>
description: Validate INDEX.xml synchronization with markdown files
---

## Validate Documentation Directory

Test `$1` is a non-empty directory. If not, suggest directories that have an `INDEX.xml` and stop.

Otherwise, else run the validation script to verify the bidirectional synchronisation between INDEX.xml and markdown files in:

```bash
uv run scripts/validate_dir.py "$1"
```

## What This Script Checks

**INDEX.xml validation:**

- File exists and is well-formed XML
- Root element is `<docs_index>`
- Contains at least one `<source>` element
- Each source has: title, description, source_url, local_file (all non-empty)
- URLs start with http:// or https://

**File synchronization (two-way check):**

- Missing files: Does every file in INDEX.xml exist on disk?
- Orphan files: Are there .md files not listed in INDEX.xml? (ignores README.md)

**Metadata synchronization:**

- Does markdown first line match `# [Title](URL)` format?
- Does title in INDEX.xml match title in markdown?
- Does URL in INDEX.xml match URL in markdown? (ignores #fragments)

## When Validation Fails

Present findings concisely in this actionable format:

<format>
# Issues Found: N

## 1. [filename]

- Type: General issue type
- What: Brief description
- 💡 Fix: Specific action to take

## 2. [filename]

- Type: General issue type
- What: Brief description
- 💡 Fix: Specific action to take
</format>

Group related issues types together. After presenting all issues with fixes, ask: "Approve fixes?"

After fixing, immediately re-run `/validate-dir <dir>` to verify. Continue until all validations pass.
