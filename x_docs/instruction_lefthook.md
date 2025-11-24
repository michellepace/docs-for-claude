Download and index documentation from a GitHub directory into a local collection.

## Input Parameters

- GitHub URL: <collection-download>https://github.com/evilmartians/lefthook/tree/master/docs/mdbook</collection-download>
- Collection name: <collection-name>lefthookagain</collection-name>

## Task 1: Download Documentation

1. Examine the GitHub directory structure at `<collection-download>`
2. Download all `.md` and `.mdx` files using curl/wget from raw.githubusercontent.com URLs
3. Save to `<collection-name>/` directory
4. **Path mapping rule:** Strip the final path segment from `<collection-download>` (e.g., "mdbook"), preserve all subdirectory structure beneath it
   - Example: `docs/mdbook/src/usage.md` ➜ `lefthook/src/usage.md`

## Task 2: Generate INDEX.xml

Create `<collection-name>/INDEX.xml` using a one-off Python script.

**XML structure requirements:**

```xml
<docs_index>
  <!-- Mirror the directory structure with nesting elements -->
  <source>
    <title>[document title from file]</title>
    <description>PLACEHOLDER</description>
    <source_url>[raw.githubusercontent.com URL]</source_url>
    <local_file>[path relative to collection root]</local_file>
    <scraped_at>[today's date: YYYY-MM-DD]</scraped_at>
  </source>
</docs_index>
```

**Structure design:** Create XML nesting that mirrors the file system directory hierarchy.

**Description field:** Use literal text "PLACEHOLDER" (not actual descriptions).

## Output

1. The generated `INDEX.xml` file
2. Brief explanation (2-3 sentences):
   - Confirm the XML structure mirrors directory hierarchy
   - State why this structure enables effective semantic search for `/ask-docs`

## Context

The INDEX.xml enables the `/ask-docs` command to search for relevant documentation files and answer questions about the collection.

## Get docs from GitHub

Use this later as part of a new solution, example urls:

- <https://github.com/evilmartians/lefthook/tree/master/docs/mdbook>
- <https://github.com/tailwindlabs/tailwindcss.com/tree/main/src/docs>
- <https://github.com/biomejs/website/tree/main/src/content/docs>

```python
def _download_github_files(github_url: str, collection_dir: Path) -> None:
    """Download files from GitHub using sparse checkout."""
    repo = _parse_github_url(github_url)
    download_temp = collection_dir / "download_temp"

    script = f"""
mkdir -p {download_temp} && cd {download_temp}
git init
git remote add origin {repo.clone_url}
git config core.sparseCheckout true
echo "{repo.docs_path}/*" > .git/info/sparse-checkout
git pull origin {repo.branch} --depth=1
rsync -av --include='*/' --include='*.mdx' --include='*.md' --exclude='*' \
    {download_temp}/{repo.docs_path}/ {collection_dir}/
cd {collection_dir}
rm -rf {download_temp}
"""
    subprocess.run(["bash", "-c", script], check=True)
```
