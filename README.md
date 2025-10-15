# Curate Docs For Claude Code

Build curated documentation collections for Claude Code using slash commands and FireCrawl. The indices help target the right docs to analyse when you run `/ask-docs`.

**Why?** Cleaner context than web-fetch, find the relevant docs faster, persists.

## 📦 Repo Collections

*Examples in this repo, but curate your own. For Anthropic docs use [this tool](https://github.com/ericbuess/claude-code-docs).*

| Tool | Description | Source | Updated | Path | Index |
|------|-------------|--------|---------|------|-------|
| **Tailwind** | CSS framework | [Official](https://tailwindcss.com/docs/) | 2025-10-15 | 📁 [`tailwind/`](tailwind/) | 📄 [`tailwind/INDEX.xml`](tailwind/INDEX.xml) |
| **UV** | Python projects | [Official](https://docs.astral.sh/uv/) | 2025-10-15 | 📁 [`uv/`](uv/) | 📄 [`uv/INDEX.xml`](uv/INDEX.xml) |
| **Anything** | Add your own | ? | ? | 📁 ? | 📄 ? |

## 🚀 Setup

```bash
# 1. Install UV
# 👉 https://docs.astral.sh/uv/getting-started/installation/

# 2. Clone repository
git clone https://github.com/michellepace/docs-for-claude.git
cd docs-for-claude

# 3. Get free FireCrawl API key
# Visit: https://www.firecrawl.dev/app/api-keys

# 4. Add to shell profile (.zshrc, .bashrc, .profile)
echo 'export API_KEY_MCP_FIRECRAWL=your-api-key-here' >> ~/.zshrc
source ~/.zshrc
```

## 📖 Slash Commands

| Command | Purpose | .md Files | INDEX.xml | Done |
|---------|---------|-----------|-----------|------|
| `/add-doc <directory> <url>` | Crawl & add single doc | ✅ Write | ✅ Add/replace | 👍 yes |
| `/ask-docs <directory> [question]` | Query index & analyse docs | ✅ Read | ✅ Search | - |
| `/recrawl-docs <directory>` | Refresh from upstream | ✅ Write all | ✅ Replace all | - |

## 💡 Usage Examples

```bash
# Add a new doc by scraping a URL
/add-doc tailwind https://tailwindcss.com/docs/customizing-colors
# → Scrapes page, writes .md file, adds source to INDEX.xml

# Update existing doc (re-scrape same URL)
/add-doc tailwind https://tailwindcss.com/docs/customizing-colors
# → Re-scrapes, writes .md file, replaces source in INDEX.xml

# Start a new collection
/add-doc reflex https://reflex.dev/docs/getting-started/installation
# → Creates reflex/ directory, README.md, INDEX.xml, and first doc

# Refresh all docs in collection (monthly maintenance)
/recrawl-docs tailwind
# → Re-scrapes all URLs in INDEX.xml, writes all .md files, replaces all sources
```

## 🏗️ How It Works

The `/add-doc <directory> <url>` command handles everything. It calls a Python script for deterministic operations (scraping, file I/O, XML updates) and print progress so Claude Code can self-heal. Claude Code completes the index by writing a dense `<description>` for the doc. When you run `/ask-docs`, it uses these descriptions to choose which docs to analyse. To refresh an entire collection, run `/recrawl-docs`. To refresh one doc, just run `/add-doc` again.

Directory Structure:

```text
uv/
├── INDEX.xml               # Index of all docs
├── README.md
├── hello-document-title.md # Scraped doc
├── overview.md             # Scraped doc
└── ...
```

INDEX.xml Schema

```xml
<docs_index>
  <source>
    <title>Hello Document Title</title>
    <description>15-25 word dense summary optimised for semantic search...</description>
    <source_url>https://docs.example.com/hello</source_url>
    <local_file>hello-document-title.md</local_file>
    <scraped_at>2025-10-15</scraped_at>
  </source>
  <!-- Multiple <source> entries, one per .md file -->
</docs_index>
```

The script uses the FireCrawl Python SDK. But the project has the MCP configured anyway: [.mcp.json](.mcp.json), [.claude/settings.json](.claude/settings.json). This is so its available to Claude Code to self-heal when needed.
