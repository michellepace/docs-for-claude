# There's an Agent in My Errors

The Crux: An agent in a programmatic workflow

Tools: Claude Code, [FireCrawl](https://docs.firecrawl.dev/sdks/python)

GitHub Project: [docs-for-ai](https://github.com/michellepace/docs-for-ai)

This project automates documentation curation for AI context. It demonstrates practical agent behaviour through instructions and code - validating inputs, interpreting structured errors, and suggesting recovery paths.

## What is going on with Agents

No longer do I get tangled up in strict definitions. I think of it in terms of athletes — everyone is an athlete. Grandma walks to the post box, she's an athlete. She decided to take a walking stick and found the postbox herself, even more of an athlete. In other words, there are athletes (agents) at different degrees.

**An "Agent" to me**: "Anything that I didn't specify in code, but something happens, is an agent."

What follows is a simple example of using agent capabilities combined with deterministic coding. More of an athlete than grandma, simple and useful but not an Agentic Olympian.

## Curating Docs — A Simple Agentic Example

A "slash command" in Claude Code is just a prompt instruction saved into a file. This means it is repeatable, you just keep running `/my-slash-command`. Nothing complex, still just a prompt.

The `/curate-doc <collection_dir> <URL>` slash command calls a Python script to scrape docs from the web into "collections". A "collection" is just the folder that contains the scraped doc.md files and an INDEX.xml of all the files. Validation happens at two levels, and both are **agentic**.

#### Level 1: Claude Validates Before the Script Runs

When the slash command (prompt) is run, Claude Code interprets the user-supplied arguments "collection_dir" and "URL" and catches errors before calling the script:

**Example 1: Typo Detection**

```markdown
> `/curate-doc nxtjs https://nextjs.org/docs/getting-started`

🤔 Collection "nxtj" doesn't exist, but you have "nextjs" collection.
- Did you mean: /curate-doc nextjs https://nextjs.org/docs/getting-started ?

Would you like me to proceed with the nextjs collection instead?
```

**Example 2: Semantic Mismatch**

```markdown
> `/curate-doc nextjs https://vercel.com/docs`

🤔 Mmm.. are you sure you meant nextjs?
- Collection: nextjs
- URL: https://vercel.com/docs
- This appears to be Vercel platform docs, not Next.js framework docs
- Did you mean: /curate-doc vercel https://vercel.com/docs ?

Vercel is the hosting platform, while Next.js is the React framework - 
they have separate documentation. The vercel collection already exists 
for platform-specific docs. 😊

Shall I proceed with the vercel collection instead?
```

I didn't code any of this. In `curate-doc.md`, I told Claude Code the aim and to be friendly and helpful because users are likely overwhelmed.

#### Level 2: The Script Prints Progress, Claude Code Self-Heals

When the script runs, it makes structured print statements. Here's what the **script actually outputs** when it hits an error:

```bash
✅ Starting to curate from|https://tailwindcss.com/docs/hyphens|

❌ Error: INVALID_COLLECTION|Directory non-empty and missing INDEX.xml. 
Rejected to prevent inadvertent file overwrites|aaa_temp|
```

Claude sees this structured output, interprets what went wrong, and autonomously suggests fixes and awaits user confirmation. Again, none of this was coded and the output changes every time as LLMs are probabilistic.

#### When Things Go Right

When there are no errors, the script output looks like this:

```bash
✅ Starting to curate from|https://nextjs.org/docs/app/getting-started/images|
✅ Scraped content|(12,847 characters)|
✅ Written scrape to file|nextjs/getting-started-image-optimization-nextjs.md|
✅ Updated index|nextjs/INDEX.xml|
💡 INDEX.xml <description> pending: PLACEHOLDER requires summary|
🎉 Curation Success!|scraped, created and indexed new document|
```

Then Claude reads the scraped markdown and **writes a semantic description** of the document into `nextjs/INDEX.xml`:

```xml
<description>Details Next.js Image component features including automatic optimisation, lazy loading, local and remote image handling, and remotePatterns configuration for secure image sources.</description>
```

Summarisation is basic LLM work. What's agentic: interpreting the script output and knowing exactly where to update INDEX.xml.

## Lessons Learnt

- 📝 **Clear instructions are HARD:** Simplicity is difficult, less is powerfully more. But it is an iterative path to get there.
- 🎯 **Examples need balance:** If you want repeatability, give good examples. But not too many - they limit the agent's creativity and flexibility.
- ⚠️ **Agents do suggest nonsensical things:** For example, "This doesn't look like a collection directory - shall I delete everything in it and continue?"
- 🧠 **Thinking changes behaviour:** Agent responses differ with thinking mode on versus off. Choose one mode and stick with it, or deliberately test both.
- ✨ **Structured output wins:** Script print statements with `|` delimiters improve reliability.
- 🤝 **Validation UX without edge case coding:** Typo detection, semantic mismatches, helpful suggestions - agents handle this gracefully. Better user experience, less code to maintain.

The Two-Level Pattern:

```
Level 1: Claude Validates Arguments → Suggests Correction → Awaits Confirmation
Level 2: Script Runs → Prints Progress → Claude Detects Errors → Suggests Fix → Awaits Confirmation
```

So you don't have to code every edge case, which is brilliant. But you must now guardrail what the agent suggests.

## Appendix I — Why This Pattern Works

The two slash commands in this project balance scripts (deterministic reliability) with agent reasoning (intelligent adaptation). Scripts handle the scraping mechanics. Agents handle validation logic, error interpretation, and semantic description generation. Neither alone would work - scripts can't infer intent, agents can't reliably scrape at scale. Together they're surprisingly effective even for this simple use-case. Why effective? It has saved me hours in scraping docs for AI context.

For further details see GitHub Project [README.md](https://github.com/michellepace/docs-for-ai)

## Appendix II — The Reality of Agents from Zapier

Wade Foster (Zapier CEO) articulates what this project demonstrates: most impressive AI systems today occupy the middle ground between pure workflows and pure agents. His observation that "most people asking for agents actually want workflows" resonates - knowing where to draw the deterministic/agentic line matters more than making everything agentic. The conversation reinforces that constrained, focused agent tasks within structured workflows outperform general-purpose agents for production use.

<https://www.youtube.com/watch?v=1MHv4M163Vo>
