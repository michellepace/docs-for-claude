# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## UV Workflow

**Package Management**: This project uses [uv](https://docs.astral.sh/uv/)

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
