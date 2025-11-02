# Curate Docs For Claude Code

Curate documentation collections using slash commands and FireCrawl. Reference indexes to get answers efficiently e.g. `@tailwind/INDEX.xml what's a utility?`.

**Why?** Cleaner than web-fetch, focussed context, curated persistence.

## 📦 Repo Collections

| Tool | Description | Source | Scraped | Path | Index |
|:-----|:------------|:-------|:--------|:-----|:------|
| **Next.js** | React framework | [Official](https://nextjs.org) | 2025-10-18 | 📁 [`nextjs/`](nextjs/) | 📄 [`nextjs/INDEX.xml`](nextjs/INDEX.xml) |
| **Shiny** | Python web apps | [Official](https://shiny.posit.co/py/) | 2025-10-16 | 📁 [`shiny/`](shiny/) | 📄 [`shiny/INDEX.xml`](shiny/INDEX.xml) |
| **Tailwind** | CSS framework | [Official](https://tailwindcss.com/docs/) | 2025-10-15 | 📁 [`tailwind/`](tailwind/) | 📄 [`tailwind/INDEX.xml`](tailwind/INDEX.xml) |
| **UV** | Python projects | [Official](https://docs.astral.sh/uv/) | 2025-10-15 | 📁 [`uv/`](uv/) | 📄 [`uv/INDEX.xml`](uv/INDEX.xml) |
| **Vercel** | Deployment platform | [Official](https://vercel.com) | 2025-10-20 | 📁 [`vercel/`](vercel/) | 📄 [`vercel/INDEX.xml`](vercel/INDEX.xml) |
| **Anything** | Add your own | ~ | ~ | 📁 | 📄 |

*Examples in this repo, but curate your own. For fresh Anthropic docs use [this tool](https://github.com/ericbuess/claude-code-docs).*

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
| `/curate-doc <directory> <url>` | Add / re-scrape doc | ✅ Write | ✅ Add/replace |
| `/rescrape-docs <directory>` | Re-scrape all docs | ✅ Write all | ✅ Selective update |

*Note: `/rescrape-docs` only regenerates descriptions for files with non-whitespace changes, reducing token usage.*

## 💡 Usage Examples

To curate and keep docs fresh in this repo:

```bash
# Curate a new doc from a URL
/curate-doc tailwind https://tailwindcss.com/docs/customizing-colors
# → Scrapes page, writes .md file, adds source to INDEX.xml

# Re-scrape existing doc (refresh content from same URL)
/curate-doc tailwind https://tailwindcss.com/docs/customizing-colors
# → Re-scrapes, writes .md file, replaces source in INDEX.xml

# Start a new collection
/curate-doc reflex https://reflex.dev/docs/getting-started/installation
# → Creates reflex/ directory, README.md, INDEX.xml, and first curated doc

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

**Workflow:** Python script scrapes URL → writes .md file → creates INDEX.xml entry with `PLACEHOLDER` description → Claude Code generates semantic description.

- `/curate-doc` - Always regenerates description for the doc
- `/rescrape-docs` - Only regenerates descriptions for files with content changes (ignores whitespace)

**Usage:** Reference `@INDEX.xml [question]` to let Claude Code use descriptions to find relevant docs.

**Directory Structure:**

```text
uv/
├── INDEX.xml               # Index of all docs
├── README.md
├── api-reference.md        # Scraped doc
├── getting-started.md      # Scraped doc
└── ...
```

**INDEX.xml Schema:**

```xml
<docs_index>
  <source>
    <title>Hello Document Title</title>
    <description>20-30 word dense summary optimised for semantic search...</description>
    <source_url>https://docs.example.com/hello</source_url>
    <local_file>hello-document-title.md</local_file>
    <scraped_at>2025-10-15</scraped_at>
  </source>
  <!-- Multiple <source> entries, one per .md file -->
</docs_index>
```

Scripts use FireCrawl Python SDK for scraping. MCP server configured ([.mcp.json](.mcp.json), [.claude/settings.json](.claude/settings.json)) for Claude Code self-healing beyond scripts.
