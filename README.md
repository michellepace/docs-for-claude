# 📚 Curate Docs For Claude Code

Curate documentation using Claude Code slash commands and FireCrawl. Each collection is indexed for semantic AI search. Curate and keep it fresh with a slash.

The benefit is cleaner and focussed context for Claude Code. The index helps target the right docs to answer your question. Markdown is cleaner than web-fetch. No need to keep MCPs on.

## 🎯 Philosophy

- **Markdown files are source of truth** - INDEX.xml is a derived artifact from the collection
- **Deterministic** - Heavy lifting with Python scripts, output for Claude Code to self-heal
- **INDEX.xml metadata generation** - Claude Code generates semantic descriptions from docs
- **Efficient search** - INDEX.xml descriptions optimised for AI context matching

## 📦 Repo Collections

| Tool | Description | Source | Updated | Path | Index |
|------|-------------|--------|---------|------|-------|
| **UV** | Python projects | [Official](https://docs.astral.sh/uv/) | 2025.07.31 | [`uv/`](uv/) | [`uv/INDEX.xml`](uv/INDEX.xml) |
| **Tailwind** | CSS framework | [Official](https://tailwindcss.com/docs/) | empty | [`tailwind/`](tailwind/) | empty |

*For Anthropic docs use [this tool](https://github.com/ericbuess/claude-code-docs).*

## 🚀 Setup

```bash
# 1. Install UV
# https://docs.astral.sh/uv/getting-started/installation/

# 2. Clone repository
git clone https://github.com/michellepace/docs-for-claude.git
cd docs-for-claude

# 3. Get free FireCrawl API key
# Visit: https://www.firecrawl.dev/app/api-keys

# 4. Add to shell profile
echo 'export API_KEY_MCP_FIRECRAWL=your-api-key-here' >> ~/.zshrc
source ~/.zshrc
```

## 📖 Slash Command Reference

| Command | Purpose | INDEX.xml | .md Files | Done |
|---------|---------|-----------|-----------|------|
| `/ask-docs` | Query docs with AI | ❌ Read-only | ❌ Read-only | - |
| `/add-doc` | Crawl & add single doc | ✅ Add source | ✅ Create | 👍 yes |
| `/sync-index` | Sync index with current files | ✅ Add/remove | ❌ | - |
| `/recrawl-docs` | Refresh from upstream | ✅ If changed | ✅ Overwrite | - |
| `/generate-index` | Create new index from scratch | ✅ Full regen | ❌ | - |

*All commands require `<directory>` as first argument*

## 💡 Usage Examples

```bash
# Daily usage - ask questions about documentation
/ask-docs tailwind "How do I customise colors?"
# → Searches INDEX.xml descriptions, reads relevant docs, answers question

# Add a new doc by crawling a URL
/add-doc tailwind https://tailwindcss.com/docs/customizing-colors
# → Crawls page, creates .md file, adds to INDEX.xml (fully atomic)

# Manually added .md files? Sync the index
/sync-index tailwind
# → Finds new files, removes orphans, offers to populate metadata

# Refresh docs from upstream (monthly maintenance)
/recrawl-docs tailwind
# → Re-crawls all URLs, detects changes, updates .md files

# Start a new collection from existing markdown files
mkdir reflex/ && cp ~/docs/*.md reflex/
/generate-index reflex
# → Analyses all .md files, generates INDEX.xml with AI metadata
```

## 🏗️ How It Works

### Directory Structure

```text
uv/
├── INDEX.xml              # AI-generated index for semantic search
├── README.md              # Collection overview
├── concepts_projects.md   # Documentation content
├── cli_init.md
└── ...
```

### INDEX.xml Schema

```xml
<docs_index>
  <source>
    <title>Projects and Packaging</title>
    <description>Explains UV project structure, pyproject.toml...</description>
    <source_url>https://docs.astral.sh/uv/concepts/projects/</source_url>
    <local_file>concepts_projects.md</local_file>
  </source>
</docs_index>
```

**How metadata is generated:**

- **Title**: Extracted from document structure and headings
- **Description**: AI-generated summary (2-3 sentences, optimised for semantic search)
- **URL**: Extracted from content or crawl source
- **File**: Direct mapping to .md filename

**No format required**: Claude Code uses AI to understand any markdown structure.
