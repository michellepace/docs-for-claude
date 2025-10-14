
# Slash Command Arguments

Documented Q&A conversations between Michelle and Anthropic AI Assistant from <https://docs.claude.com>. Michelle is asking for advise on using arguments in slash commands.

<conversation_1>

<michelle_question_1>

🙂 Slash commands, I need help understanding how to use "argument-hint". For example: I want claude code to scrape a URL into a target directory both provided by the user. There are two optinos I am thinking of for usage of this command, I am unsure if both are feasible and both equally recommended:

Option 1: `/get-doc Please get https://tailwindcss.com/docs/installation/using-vite and save into "tailwind" directory.`

Option 2: `/get-doc tailwind https://tailwindcss.com/docs/installation/using-vite`

Are both feasible, and is one recommended over the other? Does it make a difference?

</michelle_question_1>

<claude_answer_1>

🤖 Based on the documentation, I can help clarify how `argument-hint` works with custom slash commands and address your two options.

The `argument-hint` is frontmatter that shows users what arguments are expected when they auto-complete the slash command [(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#plugin-commands).

For your use case, **both options are feasible**, but they work differently:

## Option 1: Natural Language Approach

```text
/get-doc Please get https://tailwindcss.com/docs/installation/using-vite and save into "tailwind" directory.
```

This uses the `$ARGUMENTS` placeholder, which captures all arguments passed to the command [(2)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands). Your command file would look like:

```markdown
---
argument-hint: <natural language instruction>
---
$ARGUMENTS
```

[(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#plugin-commands)

## Option 2: Structured Arguments Approach  

```text
/get-doc tailwind https://tailwindcss.com/docs/installation/using-vite
```

This uses individual positional parameters like `$1`, `$2`, etc. [(2)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands). Your command file would be:

```markdown
---
argument-hint: <directory> <url>
---
Scrape the URL $2 and save the content to directory $1
```

[(2)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands)

## Recommendation

**Option 2 is generally recommended** for several reasons:

1. **Clearer structure**: The `argument-hint` shows users exactly what parameters are expected [(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#plugin-commands)
2. **More predictable**: Individual arguments (`$1`, `$2`) give you precise control over where each parameter appears in your command [(2)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands)
3. **Better for reusability**: Structured arguments make the command more consistent and easier to use repeatedly

The documentation shows that positional arguments are useful when you need to "access arguments individually in different parts of your command" or "provide defaults for missing arguments" [(2)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands).

For your scraping command, Option 2 would provide a cleaner, more maintainable slash command that users can easily understand and use consistently.

</claude_answer_1>

<michelle_question_2>

🙂 For both Option 2, if my user were to do this:

`/get-doc tailwind https://tailwindcss.com/docs/installation/using-vite please don't save the table of contents`

How would this be handled given the frontmatter you have suggested?

</michelle_question_2>

<claude_answer_2>

🤖 Good question! With the frontmatter I suggested for Option 2, your example would be handled like this:

```text
/get-doc tailwind https://tailwindcss.com/docs/installation/using-vite please don't save the table of contents
```

Given the frontmatter:

```markdown
---
argument-hint: <directory> <url>
---
Scrape the URL $2 and save the content to directory $1
```

The arguments would be parsed as:

- `$1` = "tailwind"
- `$2` = "<https://tailwindcss.com/docs/installation/using-vite>"
- `$3` = "please"
- `$4` = "don't"
- `$5` = "save"
- etc.

**This creates a problem** - the additional instruction "please don't save the table of contents" gets broken into individual positional parameters that aren't captured by your command template [(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands).

## Better Solutions

**Option A: Combine structured + flexible arguments**

```markdown
---
argument-hint: <directory> <url> [additional instructions]
---
Scrape the URL $2 and save the content to directory $1. 

Additional instructions: $3 $4 $5 $6 $7 $8 $9
```

**Option B: Use $ARGUMENTS for everything after the structured parts**
Unfortunately, the documentation doesn't show a way to mix `$1`,`$2` with `$ARGUMENTS` for remaining parameters [(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands).

**Option C: Go back to Option 1 approach**

```markdown
---
argument-hint: <natural language instruction>
---
$ARGUMENTS
```

This would capture the entire instruction: "tailwind <https://tailwindcss.com/docs/installation/using-vite> please don't save the table of contents" and let Claude parse the intent naturally [(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands).

For your use case with potentially variable additional instructions, **Option 1 with `$ARGUMENTS` might actually be more flexible**, even though Option 2 is generally recommended for simpler, more structured commands.

</claude_answer_2>

<michelle_question_3>

🙂 Slash commands: I need help understanding how to use "argument-hint" when creating slash commands.

## For example

I want claude code to scrape a URL into a target directory both provided by the user. There are the options I am thinking of for usage of this command:

1. Option 1: `/get-doc tailwind https://tailwindcss.com/docs/installation/using-vite`
2. Option 2: `/get-doc tailwind https://tailwindcss.com/docs/installation/using-vite and please excluded the TOC`
3. Option 3: `/get-doc Please scrape https://tailwindcss.com/docs/installation/using-vite and save into "tailwind" directory, and use file name "get-horse.md".`

Q1. How would I write the front-matter for each option and the use the arguments?

Q2. Is any approach preferred over the other?

Q3. If I were to implement the most deterministic option (option 1), what would happen if my user uses the slash command in the manner of option 2 and option 3? As in, is "$1" and "$2" just helpful to claude but not strict like a python function parameters? Is that why it is called an "argument-hint"

</michelle_question_3>

<claude_answer_3>

🤖 Excellent questions! Let me break down how `argument-hint` works with custom slash commands for each of your options.

## Q1: Front-matter for Each Option

**Option 1: Structured arguments**

```markdown
---
argument-hint: <directory> <url>
description: Scrape URL and save to directory
---
Scrape the URL $2 and save the content to directory $1
```

[(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands)

**Option 2: Mixed structured + additional instructions**

```markdown
---
argument-hint: <directory> <url> [additional instructions]
description: Scrape URL with optional instructions
---
Scrape the URL $2 and save the content to directory $1. 
Additional instructions: $3 $4 $5 $6 $7 $8 $9
```

[(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands)

**Option 3: Natural language approach**

```markdown
---
argument-hint: <natural language instruction>
description: Scrape URL with full natural language instructions
---
$ARGUMENTS
```

[(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands)

The documentation shows that `$ARGUMENTS` captures all arguments passed to the command, while individual arguments use positional parameters like `$1`, `$2`, etc. [(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands)

## Q2: Preferred Approach

The documentation suggests **Option 1 is generally preferred** for structured commands. Positional arguments are recommended when you need to "access arguments individually in different parts of your command" or "provide defaults for missing arguments" [(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands).

However, for your specific use case with variable additional instructions, **Option 3 with `$ARGUMENTS` provides more flexibility** since it captures the entire instruction naturally [(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands).

## Q3: Understanding Argument Behavior

You've identified a key insight! The `$1` and `$2` parameters are **not strict like Python function parameters**. Here's what happens:

When a user runs:

```text
/get-doc tailwind https://tailwindcss.com/docs/installation/using-vite and please excluded the TOC
```

With Option 1's frontmatter, the arguments would be parsed as:

- `$1` = "tailwind"
- `$2` = "<https://tailwindcss.com/docs/installation/using-vite>"
- `$3` = "and"
- `$4` = "please"
- etc.

The extra arguments (`$3`, `$4`, etc.) would simply be ignored if not referenced in your command template [(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands).

The name `argument-hint` is indeed descriptive - it's a **hint shown to users during auto-completion**, not a strict parameter validation system [(2)](https://docs.claude.com/en/docs/claude-code/slash-commands#plugin-commands). The hint "is shown to the user when auto-completing the slash command" [(2)](https://docs.claude.com/en/docs/claude-code/slash-commands#plugin-commands).

There's actually an open GitHub issue requesting more flexible argument handling, where one user suggests you can "program" argument parsing in natural language within your command [(3)](https://github.com/anthropics/claude-code/issues/5520):

```markdown
break up '$ARGUMENTS' into components, like it's a zero-based array;
let:
- PR_NAME = ARGUMENTS[0]
- FEATURE = ARGUMENTS[1]
```

[(3)](https://github.com/anthropics/claude-code/issues/5520)

This approach gives you the flexibility to handle variable arguments while still providing structure when needed.

</claude_answer_3>

</conversation_1>

---

**conversation 2:**

<conversation_2>

<michelle_question_1>

🙂 **Slash commands and "argument-hint" in front-matter:** I need help understanding how to use "argument-hint" when creating slash commands.

## Example

I want claude code to scrape a URL into a target directory both provided by the user. There are the options I am thinking of for usage of this command:

1. Option 1: `/get-doc tailwind https://tailwindcss.com/docs/installation/using-vite`
2. Option 2: `/get-doc tailwind https://tailwindcss.com/docs/installation/using-vite and please excluded the TOC`
3. Option 3: `/get-doc Please scrape https://tailwindcss.com/docs/installation/using-vite and save into "tailwind" directory, and use file name "get-horse.md".`

Q1. How would I write the front-matter for each option and the use the arguments?

Q2. Is any approach preferred over the other?

Q3. If I were to implement the most deterministic option (option 1), what would happen if my user uses the slash command in the manner of option 2 and option 3? As in, is "$1" and "$2" just helpful to Claude Code but not strict like a python function parameters? Is that why it is called an "argument-hint"

</michelle_question_1>

<claude_answer_1>

🤖 Based on the documentation, I can help you understand how to use `argument-hint` in custom slash commands.

## Q1: The Front-matter for Each Option

### Option 1 (Structured arguments)

```text
---
argument-hint: [directory] [url]
description: Scrape URL and save to directory
---

Please scrape $2 and save into "$1" directory.
```

[(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands)

### Option 2 (Mixed structured/natural)

```text
---
argument-hint: [directory] [url] [additional instructions]
description: Scrape URL with optional instructions
---

Please scrape $2 and save into "$1" directory. Additional instructions: $3
```

[(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands)

### Option 3 (Natural language)

```text
---
argument-hint: [natural language instructions]
description: Scrape URL based on natural language instructions
---

$ARGUMENTS
```

[(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands)

## Q2: The Preferred Approach

The documentation shows both approaches are valid. The structured approach (Option 1) using positional parameters like `$1`, `$2`, etc. is demonstrated when you need "to access arguments individually in different parts of your command" or "build more structured commands with specific parameter roles"[(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands).

The `$ARGUMENTS` approach captures all arguments and is useful for more flexible, natural language instructions[(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands).

## Q3: Understanding "argument-hint" Behavior

You're correct that `argument-hint` is indeed a "hint" rather than strict enforcement. The documentation explains that `argument-hint` is "shown to the user when auto-completing the slash command"[(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands).

If you implement Option 1 with `[directory] [url]` but users invoke it like Options 2 or 3:

- `$1` would still capture the first argument
- `$2` would capture the second argument  
- Any additional text would be available but not captured by the positional parameters

The system is flexible - it provides structure when users follow the hint, but doesn't break when they don't. This is why it's called an "argument-hint" rather than required parameters[(1)](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands).

For your use case, Option 1 provides the most predictable behavior while still allowing flexibility for users who want to add natural language instructions.

</claude_answer_1>

</conversation_2>
