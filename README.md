# Curate Docs For Claude Code

Curate documentation collections using slash commands and FireCrawl. Reference indexes to get answers efficiently e.g. `@INDEX.xml what's a utility?`.

**Why?** Cleaner than web-fetch, smaller context, curated persistence.

## 📦 Repo Collections

*Examples in this repo, but curate your own. For fresh Anthropic docs use [this tool](https://github.com/ericbuess/claude-code-docs).*

| Tool | Description | Source | Scraped | Path | Index |
|:-----|:------------|:-------|:--------|:-----|:------|
| **Shiny** | Python web apps | [Official](https://shiny.posit.co/py/) | 2025-10-16 | 📁 [`shiny/`](shiny/) | 📄 [`shiny/INDEX.xml`](shiny/INDEX.xml) |
| **Tailwind** | CSS framework | [Official](https://tailwindcss.com/docs/) | 2025-10-15 | 📁 [`tailwind/`](tailwind/) | 📄 [`tailwind/INDEX.xml`](tailwind/INDEX.xml) |
| **UV** | Python projects | [Official](https://docs.astral.sh/uv/) | 2025-10-15 | 📁 [`uv/`](uv/) | 📄 [`uv/INDEX.xml`](uv/INDEX.xml) |
| **Anything** | Add your own | ~ | ~ | 📁 | 📄 |

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

## 📖 Curate With Slash Commands

| Command | Purpose | .md Files | INDEX `<source>` |
|:--------|:--------|:----------|:----------|
| `/add-doc <directory> <url>` | Add / re-scrape doc | ✅ Write | ✅ Add/replace |
| `/rescrape-docs <directory>` | 🚧 TODO: Re-scrape all | ✅ Write all | ✅ Replace all |

## 💡 Usage Examples

To curate and keep docs fresh in this repo:

```bash
# Add a new doc by scraping a URL
/add-doc tailwind https://tailwindcss.com/docs/customizing-colors
# → Scrapes page, writes .md file, adds source to INDEX.xml

# Re-scrape existing doc (same URL)
/add-doc tailwind https://tailwindcss.com/docs/customizing-colors
# → Re-scrapes, writes .md file, replaces source in INDEX.xml

# Start a new collection
/add-doc reflex https://reflex.dev/docs/getting-started/installation
# → Creates reflex/ directory, README.md, INDEX.xml, and first doc

# Re-scrape all docs in collection (monthly maintenance)
/rescrape-docs tailwind
# → Re-scrapes all URLs in INDEX.xml, writes all .md files, replaces all sources
```

To use the docs (from other projects):

```bash
# From a different project

# 1. Give Claude Code access to the repo
/add-dir /home/mp/projects/docs-for-claude

# 2. Then reference as normal to ask your question
@/home/mp/projects/docs-for-claude/tailwind/INDEX.xml what's a utility?
```

## 🏗️ How This Repo Works

The `/add-doc <directory> <url>` command handles everything. It calls a Python script for deterministic operations (scraping, file I/O, XML updates) and prints progress so Claude Code can self-heal. Claude Code writes a dense index `<description>` for the doc. When you `@INDEX.xml [your question]` it uses the descriptions to find docs to analyse.

Running `./add-doc <directory> <url>` or `/rescrape-docs <directory>` will re-scrape and replace doc(s) and index sources — so fresh again.

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

The script uses the FireCrawl Python SDK. But the project has the MCP configured anyway: [.mcp.json](.mcp.json), [.claude/settings.json](.claude/settings.json). This is so it's available to Claude Code to self-heal if needed.
