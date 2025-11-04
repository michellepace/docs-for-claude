# Slash Commands vs Skills in Claude Code

A comprehensive guide to understanding the differences between Slash Commands and Agent Skills, when to use each, and how they complement one another.

---

## 📋 Executive Summary

Claude Code offers two powerful mechanisms for extending Claude's capabilities:

- **Slash Commands** are **user-invoked** prompt templates that you explicitly trigger (like `/commit` or `/review`)
- **Agent Skills** are **model-invoked** capabilities that Claude autonomously discovers and uses based on context

Both can be project-specific or personal, both can be shared via git or plugins, but they serve fundamentally different purposes in your workflow.

---

## 🎯 Core Concept: Invocation Model

The fundamental difference between slash commands and Skills lies in **who decides when they're used**:

### Slash Commands: Explicit Invocation

You type `/command-name` to trigger a pre-defined prompt. Claude executes the instruction, but you control when it happens.

**Example:**

```bash
> /review
# Claude immediately executes the review command
```

### Agent Skills: Autonomous Discovery

Claude reads your request, evaluates available Skills, and automatically uses the appropriate one without you naming it.

**Example:**

```bash
> Can you help me with this PDF form?
# Claude discovers and uses the PDF Processing Skill automatically
```

---

## 🔍 Detailed Comparison

### Slash Commands

#### What They Are

Markdown files containing prompt templates that expand when you invoke them via `/command-name` syntax. They're stored in either:

- **Project**: `.claude/commands/` (shared with team via git)
- **Personal**: `~/.claude/commands/` (your personal collection)
- **Plugins**: Distributed via plugin marketplaces

#### Structure

**Single file per command:**

```text
.claude/commands/
├── review.md
├── optimize.md
└── frontend/
    └── component.md
```

**With frontmatter:**

```markdown
---
argument-hint: [message]
description: Create a git commit
allowed-tools: Bash(git add:*), Bash(git commit:*)
model: claude-3-5-haiku-20241022
---

Create a git commit with message: $ARGUMENTS
```

#### Key Features

| Feature | Description | Example |
|---------|-------------|---------|
| **Arguments** | Accept dynamic input via `$ARGUMENTS`, `$1`, `$2`, etc. | `/fix-issue 123` where `$1` = "123" |
| **Bash Execution** | Run shell commands before expansion using `!` prefix | `!git status` |
| **File References** | Include file contents with `@` prefix | `@src/utils/helpers.js` |
| **Namespacing** | Organise in subdirectories for clarity | `/frontend/component` |
| **Tool Restrictions** | Limit allowed tools via `allowed-tools` frontmatter | `allowed-tools: Read, Grep, Glob` |

#### Usage Examples

**Simple prompt:**

```markdown
# .claude/commands/review.md
Review this code for security vulnerabilities, performance issues, and style violations.
```

**With arguments:**

```markdown
# .claude/commands/fix-issue.md
---
argument-hint: <issue-number> <priority>
---
Fix issue #$1 with priority $2 following our coding standards.
```

**With bash context:**

```markdown
# .claude/commands/commit.md
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
---

## Context
- Current status: !`git status`
- Current diff: !`git diff HEAD`
- Recent commits: !`git log --oneline -10`

## Task
Create a git commit based on the above changes.
```

#### When to Use

✅ **Perfect for:**

- Frequently-used prompt snippets you trigger manually
- Quick reminders or templates
- Standardised workflows you want to invoke explicitly
- Commands that need precise timing control

❌ **Not ideal for:**

- Complex multi-file capabilities
- Situations where Claude should decide when to use them
- Workflows requiring extensive reference documentation

---

### Agent Skills

#### What They Are

Modular capability packages that Claude autonomously discovers and invokes based on your requests. They consist of a `SKILL.md` file plus optional supporting resources, stored in:

- **Project**: `.claude/skills/` (shared with team via git)
- **Personal**: `~/.claude/skills/` (your personal collection)
- **Plugins**: Distributed via plugin marketplaces

#### Structure

**Directory with multiple files:**

```text
.claude/skills/pdf-processing/
├── SKILL.md          # Main instructions (required)
├── FORMS.md          # Supporting documentation
├── REFERENCE.md      # API reference
├── templates/        # Template files
└── scripts/
    ├── fill_form.py  # Utility scripts
    └── validate.py
```

**SKILL.md with frontmatter:**

```markdown
---
name: PDF Processing
description: Extract text, fill forms, merge PDFs. Use when working with PDF files, forms, or document extraction. Requires pypdf and pdfplumber packages.
allowed-tools: Read, Write, Bash(python:*)
---

# PDF Processing

## Quick Start
[Instructions for Claude...]

## Advanced Usage
See [FORMS.md](FORMS.md) for form filling.
See [REFERENCE.md](REFERENCE.md) for complete API reference.
```

#### Key Features

| Feature | Description | Example |
|---------|-------------|---------|
| **Auto-Discovery** | Claude selects Skills based on description matching | User mentions "PDF" → PDF Skill activates |
| **Multi-File** | Organise complex capabilities across multiple files | Scripts, templates, references, examples |
| **Progressive Loading** | Claude reads additional files only when needed | Reads REFERENCE.md only for advanced queries |
| **Tool Restrictions** | Control available tools via `allowed-tools` | Read-only Skills use only `Read, Grep, Glob` |
| **Rich Context** | Package domain expertise, standards, checklists | Security checklist, performance patterns, style guides |

#### Usage Examples

**Simple focused Skill:**

```markdown
# ~/.claude/skills/commit-helper/SKILL.md
---
name: Generating Commit Messages
description: Generate clear commit messages from git diffs. Use when writing commit messages or reviewing staged changes.
---

## Instructions
1. Run `git diff --staged` to see changes
2. Generate commit message with:
   - Summary under 50 characters
   - Detailed description
   - Affected components

## Best Practices
- Use present tense
- Explain what and why, not how
```

**Read-only analysis Skill:**

```markdown
# .claude/skills/code-reviewer/SKILL.md
---
name: Code Reviewer
description: Review code for best practices and potential issues. Use when reviewing code, checking PRs, or analysing code quality.
allowed-tools: Read, Grep, Glob
---

## Review Checklist
1. Code organisation and structure
2. Error handling
3. Performance considerations
4. Security concerns
5. Test coverage
```

**Complex multi-file Skill:**

```text
.claude/skills/excel-analysis/
├── SKILL.md              # Overview and quick start
├── PIVOT-TABLES.md       # Pivot table guide
├── CHARTS.md             # Charting reference
├── FORMULAS.md           # Formula library
├── templates/
│   ├── sales-report.xlsx
│   └── dashboard.xlsx
└── scripts/
    ├── generate_report.py
    └── export_charts.py
```

#### When to Use

✅ **Perfect for:**

- Comprehensive capabilities requiring structured knowledge
- Workflows where Claude should decide when they're relevant
- Multi-step processes with reference materials
- Team standards and conventions
- Complex domain expertise (security reviews, data analysis, etc.)

❌ **Not ideal for:**

- Simple one-line prompts
- Workflows requiring explicit timing control
- Commands you want to invoke manually

---

## 📊 Side-by-Side Comparison

| Aspect | Slash Commands | Agent Skills |
|--------|---------------|--------------|
| **Invocation** | Manual (`/command`) | Automatic (Claude decides) |
| **Complexity** | Simple prompts | Comprehensive capabilities |
| **File Structure** | Single `.md` file | Directory with `SKILL.md` + resources |
| **Discovery** | User types exact command | Claude matches description to context |
| **Best For** | Explicit, repeatable tasks | Autonomous, context-aware assistance |
| **Arguments** | ✅ Yes (`$ARGUMENTS`, `$1`, `$2`) | ❌ No |
| **Multiple Files** | ❌ No | ✅ Yes (scripts, docs, templates) |
| **Bash Commands** | ✅ Yes (`!` prefix) | ✅ Yes (via instructions) |
| **File References** | ✅ Yes (`@` prefix) | ✅ Yes (via instructions) |
| **Tool Control** | ✅ Yes (`allowed-tools`) | ✅ Yes (`allowed-tools`) |
| **Sharing Method** | Git or plugins | Git or plugins |
| **Location (Project)** | `.claude/commands/` | `.claude/skills/` |
| **Location (Personal)** | `~/.claude/commands/` | `~/.claude/skills/` |
| **Progressive Loading** | ❌ All loaded at invocation | ✅ Additional files loaded on demand |
| **Context Efficiency** | Medium (all content in one file) | High (progressive disclosure) |

---

## 🎪 Real-World Examples

### Example 1: Code Review

**As a Slash Command:**

```markdown
# .claude/commands/review.md
Review this code for:
- Security vulnerabilities
- Performance issues
- Code style violations
```

**Usage:** You type `/review` when you want a review.

**As an Agent Skill:**

```text
.claude/skills/code-review/
├── SKILL.md              # Overview & workflows
├── SECURITY.md           # Security checklist
├── PERFORMANCE.md        # Performance patterns
├── STYLE.md              # Style guide reference
└── scripts/
    └── run-linters.sh
```

```markdown
# SKILL.md
---
name: Code Reviewer
description: Review code for best practices and potential issues. Use when reviewing code, checking PRs, or analysing code quality.
allowed-tools: Read, Grep, Glob, Bash(scripts/run-linters.sh:*)
---

# Code Review Skill

## Workflow
1. Analyse code structure
2. Check security (see SECURITY.md)
3. Review performance (see PERFORMANCE.md)
4. Validate style (see STYLE.md)
5. Run automated linters

## Instructions
[Detailed review process...]
```

**Usage:** You say "Can you review this code?" and Claude automatically uses the Skill.

**When to choose:**

- **Slash Command**: Quick, manual reviews when you explicitly want one
- **Skill**: Claude should review code whenever you're checking PRs, analysing quality, or discussing code improvements

---

### Example 2: Git Commits

**As a Slash Command:**

```markdown
# .claude/commands/commit.md
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
description: Create a git commit
---

## Context
- Current status: !`git status`
- Current diff: !`git diff HEAD`
- Recent commits: !`git log --oneline -10`

## Task
Create a git commit based on the above changes.
```

**Usage:** You type `/commit` when ready to commit.

**As an Agent Skill:**

```markdown
# .claude/skills/commit-helper/SKILL.md
---
name: Generating Commit Messages
description: Generate clear commit messages from git diffs. Use when writing commit messages or reviewing staged changes.
---

## Instructions
1. Run `git diff --staged` to see changes
2. Generate commit message with:
   - Summary under 50 characters
   - Detailed description
   - Affected components

## Best Practices
- Use present tense
- Explain what and why, not how
```

**Usage:** You say "Help me write a commit message" and Claude uses the Skill.

**When to choose:**

- **Slash Command**: You control exactly when commits happen (safer, more explicit)
- **Skill**: Claude helps craft messages whenever you're discussing commits (more conversational)

---

### Example 3: PDF Processing

**As a Slash Command:**

```markdown
# .claude/commands/pdf-extract.md
Extract text from the PDF file using pdfplumber:

```python
import pdfplumber
with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

**Usage:** Type `/pdf-extract` when you need to extract text.

**As an Agent Skill:**

```text
.claude/skills/pdf-processing/
├── SKILL.md          # Overview & quick start
├── FORMS.md          # Form filling guide
├── EXTRACTION.md     # Text extraction patterns
├── MERGING.md        # PDF merging strategies
├── templates/
│   ├── form-w9.pdf
│   └── invoice-template.pdf
└── scripts/
    ├── fill_form.py
    ├── extract_tables.py
    └── merge_pdfs.py
```

```markdown
# SKILL.md
---
name: PDF Processing
description: Extract text, fill forms, merge PDFs, extract tables. Use when working with PDF files, forms, or document extraction. Requires pypdf and pdfplumber.
---

# PDF Processing Skill

## Quick Start
Extract text:
```python
import pdfplumber
with pdfplumber.open("doc.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

## Advanced Features

- Form filling: See [FORMS.md](FORMS.md)
- Table extraction: See [EXTRACTION.md](EXTRACTION.md)
- PDF merging: See [MERGING.md](MERGING.md)

## Scripts

- `scripts/fill_form.py` - Automated form filling
- `scripts/extract_tables.py` - Extract tables to CSV
- `scripts/merge_pdfs.py` - Merge multiple PDFs

**Usage:** Say "Can you extract data from this PDF?" and Claude uses the Skill automatically.

**When to choose:**

- **Slash Command**: Simple, one-off PDF operations
- **Skill**: Comprehensive PDF workflows with forms, tables, merging, validation

---

## 🧭 Decision Guide: Which Should I Use?

Use this flowchart to decide:

```text
Start
  │
  ├─ Is this a simple prompt I use frequently?
  │    └─ YES → Slash Command
  │
  ├─ Do I need explicit control over when it runs?
  │    └─ YES → Slash Command
  │
  ├─ Is this a complex capability with multiple files?
  │    └─ YES → Agent Skill
  │
  ├─ Should Claude decide when to use this?
  │    └─ YES → Agent Skill
  │
  ├─ Does this represent domain expertise or standards?
  │    └─ YES → Agent Skill
  │
  └─ Not sure?
       └─ Start with Slash Command, upgrade to Skill if complexity grows
```

### Quick Decision Matrix

| Your Need | Recommended Solution |
|-----------|---------------------|
| "I want to type `/commit` whenever I'm ready to commit" | Slash Command |
| "Claude should help with commits when I'm discussing changes" | Agent Skill |
| "Quick code review when I type `/review`" | Slash Command |
| "Comprehensive code reviews with security, performance, and style checks" | Agent Skill |
| "Extract text from PDFs when I say so" | Slash Command |
| "Complete PDF toolkit for forms, extraction, merging, validation" | Agent Skill |
| "Generate test boilerplate on demand" | Slash Command |
| "Testing expertise with patterns, frameworks, and best practices" | Agent Skill |
| "Format JSON when I type `/format-json`" | Slash Command |
| "Data analysis across multiple formats (JSON, CSV, Excel)" | Agent Skill |

---

## 🔄 How They Work Together

Slash Commands and Skills are **complementary**, not competing. You can (and should) use both:

### Example: Testing Workflow

**Slash Command for explicit test generation:**

```markdown
# .claude/commands/test.md
---
argument-hint: <file-path>
---
Generate unit tests for $1 following our testing standards.
```

**Agent Skill for testing expertise:**

```text
.claude/skills/testing/
├── SKILL.md              # Testing overview
├── UNIT-TESTS.md         # Unit testing patterns
├── INTEGRATION.md        # Integration testing guide
├── MOCKS.md              # Mocking strategies
└── templates/
    ├── test-template.py
    └── fixture-examples.py
```

**How they work together:**

1. You type `/test src/utils.py` to explicitly generate tests
2. During conversation, when you discuss test coverage or quality, Claude automatically uses the Testing Skill
3. The Skill provides richer context, standards, and patterns
4. The Command gives you precise control over test generation timing

### Example: Documentation Workflow

**Slash Command for quick doc generation:**

```markdown
# .claude/commands/doc.md
---
argument-hint: <function-name>
---
Generate documentation for $1 following our doc standards.
```

**Agent Skill for documentation expertise:**

```text
.claude/skills/documentation/
├── SKILL.md              # Doc standards overview
├── API-DOCS.md           # API documentation style
├── TUTORIALS.md          # Tutorial writing guide
├── EXAMPLES.md           # Example library
└── templates/
    ├── api-template.md
    ├── tutorial-template.md
    └── changelog-template.md
```

**Usage pattern:**

- Quick docs: `/doc myFunction`
- Comprehensive docs: "Help me document this API" (Skill activates)
- During PR reviews: Claude references the Documentation Skill automatically

---

## 📚 Best Practices

### For Slash Commands

1. **Keep them focused and simple**
   - One command = one clear purpose
   - Use concise, actionable prompts

2. **Use meaningful names**
   - `/review` not `/r`
   - `/format-json` not `/fj`

3. **Document arguments clearly**

   ```markdown
   ---
   argument-hint: <issue-number> <priority>
   description: Fix issue with specified priority
   ---
   ```

4. **Include usage examples**

   ```markdown
   # Usage
   # /fix-issue 123 high
   # /fix-issue 456 medium
   ```

5. **Leverage bash pre-execution for context**

   ```markdown
   Current status: !`git status`
   Recent commits: !`git log --oneline -5`
   ```

### For Agent Skills

1. **Write specific, trigger-rich descriptions**

   ❌ **Vague:**

   ```yaml
   description: Helps with documents
   ```

   ✅ **Specific:**

   ```yaml
   description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files, forms, document extraction, or when user mentions PDFs.
   ```

2. **Organise content progressively**
   - `SKILL.md`: Overview and quick start
   - Additional `.md` files: Detailed references, loaded on demand
   - Scripts: Utilities and automation

3. **Use `allowed-tools` for safety**

   ```yaml
   # Read-only analysis Skill
   allowed-tools: Read, Grep, Glob
   ```

4. **Include concrete examples**
   - Show code snippets
   - Demonstrate workflows
   - Provide templates

5. **Document dependencies clearly**

   Show package requirements in your documentation with escaped code blocks.

6. **Test with varied phrasings**
   - "Can you help with this PDF?"
   - "Extract data from this document"
   - "Fill out this form"
   - All should trigger the same PDF Skill

### For Both

1. **Share via git for team workflows**

   ```bash
   # Commit to repo
   git add .claude/
   git commit -m "Add team commands and Skills"
   git push
   ```

2. **Use plugins for distribution**
   - Package related commands/Skills together
   - Distribute via plugin marketplaces
   - Version and document changes

3. **Start simple, evolve as needed**
   - Begin with slash command
   - Upgrade to Skill when complexity grows
   - Keep both if explicit invocation is valuable

4. **Keep documentation current**
   - Update descriptions when behaviour changes
   - Document version history
   - Include migration notes for breaking changes

---

## 🔧 Technical Details

### Slash Command Tool (`SlashCommand`)

Claude can programmatically invoke custom slash commands using the `SlashCommand` tool. This allows Claude to trigger commands during conversation without you typing them.

**Requirements for tool invocation:**

- Only custom slash commands (not built-in like `/compact`)
- Must have `description` in frontmatter
- Must not have `disable-model-invocation: true`

**Permission control:**

```bash
# Deny all slash command tool usage
/permissions
# Add to deny rules: SlashCommand

# Allow specific command only
# Approve: SlashCommand:/commit
# Approve: SlashCommand:/review-pr:*  # with any arguments
```

**Context budget:**

- Default: 15,000 characters for command metadata
- Customise: `SLASH_COMMAND_TOOL_CHAR_BUDGET` environment variable
- When exceeded: Warning in `/context` showing "M of N commands"

### Skill Discovery

Skills are automatically discovered from:

1. **Personal Skills**: `~/.claude/skills/`
2. **Project Skills**: `.claude/skills/`
3. **Plugin Skills**: Installed plugin directories

**How Claude selects Skills:**

1. User makes a request
2. Claude evaluates all available Skill descriptions
3. Matches based on keywords, context, and triggers
4. Loads `SKILL.md` for matched Skill(s)
5. Progressively loads additional files as needed

**Debugging discovery:**

```bash
# Run with debug mode
claude --debug

# Check Skill loading errors in output
# Verify YAML syntax, file paths, descriptions
```

---

## ❓ Common Questions

### Can slash commands invoke Skills?

No. Slash commands expand to prompts, but they don't directly invoke Skills. However, the prompt from a slash command could mention topics that trigger Claude to use a relevant Skill.

### Can Skills use slash commands?

Skills can instruct Claude to use tools and reference files, but they don't directly invoke slash commands. If you need precise command execution, use `allowed-tools` with specific Bash commands.

### Should I convert my slash commands to Skills?

Only if:

- ✅ The command has grown complex (multiple concepts, workflows)
- ✅ You want Claude to use it automatically based on context
- ✅ You need to organise multiple files (docs, scripts, templates)
- ✅ It represents domain expertise that benefits from rich context

Keep as slash command if:

- ✅ It's simple and focused
- ✅ You want explicit timing control
- ✅ Single file is sufficient

### Can I have both a command and Skill with similar purposes?

Yes! This is a valid pattern:

- **Slash Command**: Explicit invocation when you want precise control
- **Skill**: Automatic assistance when discussing the topic

Example: `/commit` for explicit commits + Commit Helper Skill for conversational assistance.

### How do I share these with my team?

**Via Git (recommended for team projects):**

```bash
# Project scope (shared automatically)
.claude/commands/     # Team slash commands
.claude/skills/       # Team Skills

git add .claude/
git commit -m "Add team commands and Skills"
git push
```

**Via Plugins (recommended for distribution):**

1. Create plugin with `commands/` and/or `skills/` directories
2. Add to plugin marketplace
3. Team installs plugin

### Do Skills increase context usage?

Skills are designed for **progressive loading**:

- Only `SKILL.md` loaded initially
- Additional files loaded on demand
- More context-efficient than putting everything in one file
- Slash commands load all content at invocation

### Can I use both in the same project?

Absolutely! Most projects benefit from both:

- **Commands**: Explicit, repeatable workflows
- **Skills**: Autonomous expertise and standards

They complement each other and handle different use cases.

---

## 🎓 Learning Path

### Getting Started

1. **Start with slash commands**
   - Create simple, frequently-used prompts
   - Learn frontmatter options
   - Practice argument handling

2. **Add your first Skill**
   - Pick a complex workflow from your slash commands
   - Convert to Skill with `SKILL.md`
   - Write specific, trigger-rich description

3. **Organise and refine**
   - Add supporting files to Skills
   - Use `allowed-tools` for safety
   - Share with team via git

### Intermediate

1. **Create multi-file Skills**
   - Organise complex expertise across files
   - Add scripts and templates
   - Use progressive loading

2. **Combine commands and Skills**
   - Keep commands for explicit control
   - Let Skills handle autonomous assistance
   - Build complementary workflows

### Advanced

1. **Distribute via plugins**
   - Package related capabilities
   - Publish to marketplaces
   - Version and document

2. **Optimise for your team**
   - Standardise workflows
   - Document conventions
   - Iterate based on feedback

---

## 📖 Further Reading

**Official Documentation:**

- [Slash Commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- [Agent Skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Plugins](https://docs.anthropic.com/en/docs/claude-code/plugins)
- [Best Practices for Agent Skills](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/best-practices)

**Engineering Blog:**

- [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

---

## ✨ Summary

| When You Want... | Use This |
|------------------|----------|
| Explicit control over timing | Slash Command |
| Claude to decide when to help | Agent Skill |
| Simple, repeatable prompts | Slash Command |
| Complex, structured expertise | Agent Skill |
| Single-file capability | Slash Command |
| Multi-file organisation | Agent Skill |
| Manual invocation | Slash Command |
| Automatic discovery | Agent Skill |

**Key Takeaway:** Slash Commands and Skills are complementary tools that work together. Commands give you explicit control, Skills give Claude autonomous capabilities. Use both to build efficient, powerful workflows in Claude Code.

---

*Last updated: 2025-10-17*
