# Curate Docs For AI (with Claude Code)

Curate and index documentation from any website into collections like `tailwind/`, `horses/`, etc. Reference collection indexes in your AI chats (e.g. `@tailwind/INDEX.xml what's a utility?`) so that only relevant docs are analysed. Much cleaner than a web-fetch and more focussed than a web-search. Keep your AI context sharp.

## 📦 Repo Collections

| Collection | Collection Index | Description | Scraped | Source |
|:-----------|:-----------------|:------------|:--------|:-------|
| 📦 [`anthropic/`](anthropic/) | 📄 [`anthropic/INDEX.xml`](anthropic/INDEX.xml) | Claude Agent SDK | 2025-11-06 | [Official](https://docs.claude.com) |
| 📦 [`biome/`](biome/) | 📄 [`biome/INDEX.xml`](biome/INDEX.xml) | Fast linter/formatter | 2025-11-04 | [Official](https://biomejs.dev) |
| 📦 [`marimo/`](marimo/) | 📄 [`marimo/INDEX.xml`](marimo/INDEX.xml) | Reactive Python notebooks | 2025-11-11 | [Official](https://docs.marimo.io) |
| 📦 [`nextjs/`](nextjs/) | 📄 [`nextjs/INDEX.xml`](nextjs/INDEX.xml) | React framework | 2025-11-05 | [Official](https://nextjs.org) |
| 📦 [`playwright/`](playwright/) | 📄 [`playwright/INDEX.xml`](playwright/INDEX.xml) | Browser testing | 2025-11-07 | [Official](https://playwright.dev) |
| 📦 [`shiny/`](shiny/) | 📄 [`shiny/INDEX.xml`](shiny/INDEX.xml) | Python web apps | 2025-11-02 | [Official](https://shiny.posit.co/py/) |
| 📦 [`tailwind/`](tailwind/) | 📄 [`tailwind/INDEX.xml`](tailwind/INDEX.xml) | CSS framework | 2025-10-15 | [Official](https://tailwindcss.com/docs/) |
| 📦 [`tailwindplus/`](tailwindplus/) | 📄 [`tailwindplus/INDEX.xml`](tailwindplus/INDEX.xml) | Paid UI Components | 2025-11-16 | [Official](https://tailwindcss.com/plus) |
| 📦 [`uv/`](uv/) | 📄 [`uv/INDEX.xml`](uv/INDEX.xml) | Python projects | 2025-10-15 | [Official](https://docs.astral.sh/uv/) |
| 📦 [`vercel/`](vercel/) | 📄 [`vercel/INDEX.xml`](vercel/INDEX.xml) | Deployment platform | 2025-10-20 | [Official](https://vercel.com) |
| 📦 [`vitest/`](vitest/) | 📄 [`vitest/INDEX.xml`](vitest/INDEX.xml) | Testing framework | 2025-11-05 | [Official](https://vitest.dev) |
| 📦 [`zustand/`](zustand/) | 📄 [`zustand/INDEX.xml`](zustand/INDEX.xml) | State management | 2025-11-18 | [Official](https://zustand.docs.pmnd.rs) |

*Curate your own collections. For most Anthropic docs use [this tool](https://github.com/ericbuess/claude-code-docs).*

---

## 🚀 Setup

```bash
# 1. Install UV
# 👉 https://docs.astral.sh/uv/getting-started/installation/

# 2. Clone repository
git clone https://github.com/michellepace/docs-for-ai.git
cd docs-for-ai

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

<div align="center">
  <img src="x_docs/images/example_usage.jpg" alt="Terminal showing three-step workflow: (1) Running /curate-doc biome command, (2) Curation success output showing scraped documentation and generated INDEX.xml entry, (3) Reference command @biome/INDEX.xml to ask questions. Handwritten annotations highlight each step." width="900">
  <p><em>Complete workflow: curate → scrape → reference</em></p>
</div>

## 💡 Usage Examples

### Curate

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

### Use the docs

You can reference as you would any other file, e.g. *"`@/home/mp/projects/docs-for-ai/tailwind/INDEX.xml` what's a utility?"*. But the BEST way is to setup a personal slash command:

```bash
# 1. Ensure this Claude Code directory exists
mkdir -p ~/.claude/commands

# 2. Copy slash-command to your personal slashes
cp x_docs/personal-slash/ask-docs.md ~/.claude/commands/.

# 3. Open file for changing in Cursor IDE ("code" for VSCode)
cursor ~/.claude/commands/ask-docs.md

# 4. Change "`~/projects/python/docs-for-ai/" to your own
echo -e "\n🔥 Change paths to yours (in ask-docs.md)" && sed -n '17,19p' ~/.claude/commands/ask-docs.md | nl -v 17

# 5. Start a new Claude
claude
```

Then you can just run `/add-docs` from anywhere e.g.

- "`/ask-docs tailwind` what are the responsive sizes?"
- "`/ask-docs nextjs` how are images now optimised?"

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

---

## 🎯🔥 Notes to Improve later

Instead of crawling, rather go GitHub to find docs there because its cleaner. If in .mdx format then keep it like so (don't convert it breaks)

```markdown
Your instinct is correct:
- FireCrawl scraped HTML → configuration-biome.md = good but has scraper artefacts
- GitHub source .mdx → keep as .mdx = best (canonical, clean)
- GitHub source .mdx → converted to .md = worst (broken, lossy conversion)

For future collections, you should:
1. Check if docs are on GitHub
2. If yes, grab the .mdx or .md files directly
3. Keep them in their original format
4. Only use FireCrawl as a fallback when source files aren't available
```
