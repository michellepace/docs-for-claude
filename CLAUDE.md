# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Documentation collections scraped via FireCrawl. INDEX.xml maps markdown files to semantic descriptions for targeted context retrieval.

Documentation is organised by tool/framework in collection directories:

```text
<tool-name>/
├── INDEX.xml              # Structured index for targeted doc retrieval
├── README.md              # Directory overview
└── *.md                   # Documentation markdown files
```

## Development Workflow (Python 3.13)

**Package Management:** This project uses [uv](https://docs.astral.sh/uv/)

**Strict Rules:**

- Use British spelling - never American
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
uv run pre-commit run --all-files # Run all hooks manually

# Markdown (config in .markdownlint.yaml)
npx markdownlint-cli2 --fix "filename.md"  # Lint and auto-fix
```
