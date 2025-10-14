# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository curates documentation collections that AI coding agents can search and retrieve efficiently. Each collection contains markdown files with an INDEX.xml that enables semantic search - AI agents query descriptions to load only relevant docs into context.

## Structure

Documentation is organised by tool/framework in collection directories:

```text
<tool-name>/
├── INDEX.xml              # Structured index for targeted doc retrieval
├── README.md              # Directory overview
└── *.md                   # Documentation markdown files
```

Each INDEX.xml maps markdown files to searchable metadata:

```xml
<docs_index>
  <source>
    <title>Document title</title>
    <description>Content summary for context matching</description>
    <source_url>https://original-docs-url</source_url>
    <local_file>filename.md</local_file>
  </source>
  <!-- Multiple <source> entries, one per markdown file -->
</docs_index>
```

Documentation is scraped using FireCrawl.

## Development Workflow (Python 3.13)

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
