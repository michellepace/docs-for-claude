# Curated Docs For Clean Claude Code Context

Curated documentation for Claude Code projects. Each collection is indexed for targeted AI context and kept up to date with automation. Crawled via [FireCrawl MCP](https://docs.firecrawl.dev/mcp-server).

## Available Docs

| Tool | Description | Source | Updated | Docs Path | Docs Index |
|:-----|:------------|:------------|:-------------|:----------|:------|
| **UV** | Python projects | [Official](https://docs.astral.sh/uv/) | 2025.07.31 | 📁 [`uv/`](uv/) | 📄 [`uv/INDEX.xml`](uv/INDEX.xml) |
| **Tailwind** | CSS framework | [Official](https://tailwindcss.com/docs/) | ⚠️ TODO | 📁 [`tailwind/`](tailwind/) | 📄 - |

*NB: For all Anthropic docs, use [this tool](https://github.com/ericbuess/claude-code-docs)*

## Install

1. Clone this repo: `git clone https://github.com/michellepace/docs-for-claude.git`
2. FireCrawl is pre-configured in [.mcp.json](.mcp.json) and requires an API key
3. Get a free FireCrawl API key: [firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)
4. Add it to your shell profile (`.zshrc`, `.bashrc`, etc.):

   ```bash
   echo 'export API_KEY_MCP_FIRECRAWL=your-api-key-here' >> ~/.zshrc
   source ~/.zshrc  # reload shell profile
   echo $API_KEY_MCP_FIRECRAWL  # check it's set
   ```

## Usage

### 🔵 Daily Use

⚠️ **TODO** - Ask Questions: `/ask-dir-docs <repo-dir> <question>`

```bash
# Searches <repo-dir>/INDEX.xml to find relevant docs
# Analyses chosen docs to answer your question

# UV example
/ask-dir-docs uv What does "init --package" do?

# Tailwind example
/ask-dir-docs tailwind Is "tailwind.config" still used?
```

### 🟢 Update Docs

⚠️ **TODO** - Update Single Doc: `/update-dir-doc <repo-dir> <filename>`

```bash
# Crawls for a single doc file and overwrites .md content
# Updates <source> elements in INDEX.xml if needed: <title>, <description>
/update-dir-doc uv concepts_projects_build.md
```

⚠️ **TODO** - Update Directory Docs: `/update-dir-docs <repo-dir>`

```bash
# Crawls for all docs in directory and overwrites .md content
# Updates <source> elements in INDEX.xml if needed: <title>, <description>
/update-dir-docs uv
```

### 🟠 Expand Docs

⚠️ **TODO** - Add New Directory Doc: `/add-new-dir-doc <repo-dir> <new-doc-url-to-crawl>`

```bash
# Crawls for new doc and creates .md file
# Adds <source> element to existing INDEX.xml: <title>, <description>, <url>, <file>
/add-new-dir-doc uv https://docs.astral.sh/uv/concepts/preview/
```

⚠️ **TODO** - Create Directory Index: `/create-dir-index <repo-dir>`

```bash
# Creates INDEX.xml from existing .md files in directory
# Scans directory and generates <source> elements for each .md file
/create-dir-index reflex
```

⚠️ **TODO** - Validate Directory: `/validate-dir <repo-dir>`

```bash
# Verifies bidirectional sync: INDEX.xml ↔ .md files
# Reports any problems found
/validate-dir uv
```

**Add New Directory of Documents** (manual + automatic workflow):

1. Add a new row to the README.md table
2. Create the new root directory e.g., `mkdir reflex`
3. Create directory README.md following established pattern
4. Add docs (.md) files manually and name as desired
5. Create an index, run: `/create-dir-index reflex`
6. Optional verification, run: `/validate-dir reflex`
7. Optional to add more docs, run: `/add-new-dir-doc reflex <new-doc-url-to-crawl>`
