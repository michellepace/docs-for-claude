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

⚠️ **TODO** - Ask Questions: `/ask-subdir-docs <repo-subdir> <question>`

```bash
# Searches <repo-subdir>/INDEX.xml to find relevant docs
# Analyses chosen docs to answer your question

# UV example
/ask-subdir-docs uv What does "init --package" do?

# Tailwind example
/ask-subdir-docs tailwind Is "tailwind.config" still used?
```

### 🟢 Update Docs

⚠️ **TODO** - Update Single Doc: `/update-subdir-doc <repo-subdir> <filename>`

```bash
# Crawls for a single doc file and overwrites .md content
# Updates <source> elements in INDEX.xml if needed: <title>, <description>
/update-subdir-doc uv concepts_projects_build.md
```

⚠️ **TODO** - Update Subdir Docs: `/update-subdir-docs <repo-subdir>`

```bash
# Crawls for all docs in subdirectory and overwrites .md content
# Updates <source> elements in INDEX.xml if needed: <title>, <description>
/update-subdir-docs uv
```

### 🟠 Expand Docs

⚠️ **TODO** - Add New Subdir Doc: `/add-new-subdir-doc <repo-subdir> <new-doc-url-to-crawl>`

```bash
# Crawls for new doc and creates .md file
# Adds <source> element to existing INDEX.xml: <title>, <description>, <url>, <file>
/add-new-subdir-doc uv https://docs.astral.sh/uv/concepts/preview/
```

⚠️ **TODO** - Create Subdir Index: `/create-subdir-index <repo-subdir>`

```bash
# Creates INDEX.xml from existing .md files in subdirectory
# Scans subdirectory and generates <source> elements for each .md file
/create-subdir-index reflex
```

⚠️ **TODO** - Validate Subdir: `/validate-subdir <repo-subdir>`

```bash
# Verifies bidirectional sync: INDEX.xml ↔ .md files
# Reports any problems found
/validate-subdir uv
```

**Add New Subdir of Documents** (manual + automatic workflow):

1. Add a new row to the README.md table
2. Create the new root subdirectory e.g., `mkdir reflex`
3. Create subdirectory README.md following established pattern
4. Add docs (.md) files manually and name as desired
5. Create an index, run: `/create-subdir-index reflex`
6. Optional verification, run: `/validate-subdir reflex`
7. Optional to add more docs, run: `/add-new-subdir-doc reflex <new-doc-url-to-crawl>`
