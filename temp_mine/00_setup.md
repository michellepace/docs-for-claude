# FireCrawl Scraping Analysis Findings

## FireCrawl Configuration

```python
mcp__firecrawl__firecrawl_scrape(
    url="<target_url>",
    formats=["markdown"],
    onlyMainContent=True, # False is v.verbose
    removeBase64Images=True,
    waitFor=2000, # 2 secs
    maxAge=172800000 # 2 days
)
```

Note: Pending possible use of `excludeTags`

## URLs To Be Scraped and Saved

| Technology | URL # | Scrape URL | Filename |
|------------|-------|------------|----------|
| Nextjs | 1 | <https://nextjs.org/docs/app/getting-started/project-structure> | nextjs_01.md |
| Nextjs | 2 | <https://nextjs.org/docs/app/getting-started/updating-data> | nextjs_02.md |
| Nextjs | 3 | <https://nextjs.org/docs/app/api-reference/config/typescript> | nextjs_03.md |
| Shiny | 1 | <https://shiny.posit.co/py/get-started/create-run.html> | shiny_01.md |
| Shiny | 2 | <https://shiny.posit.co/py/api/express/express.ui.input_radio_buttons.html> | shiny_02.md |
| Shiny | 3 | <https://shiny.posit.co/py/docs/genai-inspiration.html> | shiny_03.md |
| Tailwind | 1 | <https://tailwindcss.com/docs/styling-with-utility-classes> | tailwind_01.md |
| Tailwind | 2 | <https://tailwindcss.com/docs/dark-mode> | tailwind_02.md |
| Tailwind | 3 | <https://tailwindcss.com/docs/font-family> | tailwind_03.md |
| Zustand | 1 | <https://zustand.docs.pmnd.rs/guides/immutable-state-and-merging> | zustand_01.md |
| Zustand | 2 | <https://zustand.docs.pmnd.rs/guides/how-to-reset-state> | zustand_02.md |
| Zustand | 3 | <https://zustand.docs.pmnd.rs/apis/create-store> | zustand_03.md |

---

---

## Key Questions

Q1. What is the document "# Title" in each file? Analyse scraped document and summarise in a table with 12 rows and columns "Document, Title A, Title B, Scraped URL". Put concise comment in the Title field if it was not obvious / clear. Summarise findings in 1-2 crisp sentences.

Q2. What is the document source URL in each file? Analyse scraped document and summarise in a table with 12 rows and columns "Document, SourceURL A, SourceURL B, Scraped URL". Put concise comment in the SourceURL field if it was not obvious / clear. Summarise findings in 1-2 crisp sentences.

Q3. Do a diff between each A and B pair - What additional info is held in B? Any valuable information for Claude Code assuming docs will be provided as context to implement using these tools?

Q4. Will `maxAge` be beneficial during testing, that is, will it help me speed up my development cycle where I will be testing on the same commands? Will it help me save tokens? Is it deterimental to keep this setting when I go into "production"?

Q5. For Config A only: What does "`removeBase64Images: true`" do, and does it make the documentation cleaner? *Method: Search Config A files for base64 image data, assess if removing would reduce token bloat without losing valuable visual context.*

Q6. For Config A only: Are there any HTML tags that would be useful to exclude using "`excludeTags`" arrays? Useful meaning, it will remove content that is not useful to Claude Code context and thus reduce noise. *Method: Analyse Config A files for noisy HTML elements, then test `excludeTags` on 2 representative URLs to validate if exclusion improves content quality.*
