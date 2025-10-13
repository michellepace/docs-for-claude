# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Architecture

This repository curates documentation for AI context. Documentation is organised by tool/framework in subdirectories:

```text
<tool-name>/
├── INDEX.xml              # Structured index for targeted doc retrieval
├── README.md              # Subdirectory overview
└── *.md                   # Documentation markdown files
```

### INDEX.xml Schema

Each subdirectory contains an `INDEX.xml` file that maps documentation files to metadata:

```xml
<docs_index>
  <source>
    <title>Document title</title>
    <description>Content summary for context matching</description>
    <source_url>https://original-docs-url</source_url>
    <local_file>filename.md</local_file>
  </source>
</docs_index>
```

The index enables targeted document retrieval rather than loading entire documentation sets into context.

### External Tools

- **FireCrawl MCP**: Used for documentation crawling. Pre-configured but requires `API_KEY_MCP_FIRECRAWL` environment variable.

## Development Workflow

**Package Management:** This project uses [uv](https://docs.astral.sh/uv/)

**Strict Rules:**

- Use `uv run` - never activate venv
- Use `uv add` - never pip
- Use `pyproject.toml` - never requirements.txt

**Common Commands:**

```bash
# Setup & Dependencies
uv sync                           # Match packages to lockfile
uv tree                           # Show dependency tree
uv add --dev <pkg>                # Add dev dependency
uv lock --upgrade-package <pkg>   # Update specific package
uv lock --upgrade && uv sync      # Update all packages and apply

# Code Quality
# Python (config in pyproject.toml)
uv run ruff check --fix           # Lint and auto-fix
uv run pyright                    # Type checking
uv run ruff format                # Format code

# Markdown (config in .markdownlint.yaml)
npx markdownlint-cli2 --fix "**/*.md"  # Lint and auto-fix
```
