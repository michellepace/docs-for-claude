# Curate Docs For Claude Code

Build curated documentation collections for Claude Code using slash commands and FireCrawl. The indices help target the right docs to analyse when you run `/ask-docs`.

**Why?** Cleaner context than web-fetch, find the relevant docs faster, no MCPs needed, persists.

## 📦 Repo Collections

*Examples in this repo, but curate your own. For Anthropic docs use [this tool](https://github.com/ericbuess/claude-code-docs).*

| Tool | Description | Source | Updated | Path | Index |
|------|-------------|--------|---------|------|-------|
| **UV** | Python projects | [Official](https://docs.astral.sh/uv/) | 2025.07.31 | [`uv/`](uv/) | [`uv/INDEX.xml`](uv/INDEX.xml) |
| **Tailwind** | CSS framework | [Official](https://tailwindcss.com/docs/) | empty | [`tailwind/`](tailwind/) | empty |

## 🚀 Setup

```bash
# 1. Install UV
# https://docs.astral.sh/uv/getting-started/installation/

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

The `/add-doc <directory> <url>` command handles everything (scrape, write, index). It calls a Python script for deterministic operations (scraping, file I/O, XML updates) that print progress so Claude Code can self-heal when needed. Claude Code completes the index by writting a dense `<description>` for the doc. When you run `/ask-docs`, it uses these descriptions to choose which docs to analyse. To refresh a collection when upstream docs change, just run `/recrawl-docs`. To refresh one doc, just add it again `/add-doc`.

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
    <description>2-3 sentence summary optimised for AI semantic search...</description>
    <source_url>https://docs.example.com/hello</source_url>
    <local_file>hello-document-title.md</local_file>
  </source>
  <!-- Multiple <source> entries, one per .md file -->
</docs_index>
```

**How `/add-doc` generates metadata:**

1. **Scrapes URL** with FireCrawl (extracts title, content, canonical URL)
2. **Writes .md file** with slugified filename from title
3. **Adds/replaces source in INDEX.xml** with placeholder description
4. **Claude analyses content** and writes semantic description
