# Agent 3 Report: Feb 2025 - Aug 2024

## New Concepts - super to know

Things Claude Code likely doesn't know that would be useful context:

- **Updated Registry Schema (Feb 2025)**: Registry schema now supports defining code as flat JSON files distributed via CLI. Enables custom styles, third-party registry support, mixing/matching components, and installing themes, CSS vars, hooks, animations, and Tailwind layers/utilities.

- **Blocks (Jan 2025)**: Community contribution system for sharing reusable component blocks. Supports application, marketing, and product blocks. Documented at `/docs/blocks`.

- **Monorepo Support (Dec 2024)**: CLI now understands monorepo structure, automatically handles component installation paths, dependency management, and import path resolution in monorepo environments. Documented at `/docs/monorepo`.

- **Lucide Icons Default (Nov 2024)**: New York style changed to use Lucide as default icon set. No breaking changes for existing projects. CLI supports optional migration of primitives to Lucide.

- **React 19 Compatibility (Oct 2024)**: Full React 19 and Next.js 15 support. Upgrade guide available at `/docs/react-19`.

- **Sidebar Component System (Oct 2024)**: New `sidebar.tsx` foundation with 25+ component variations. Cross-framework support (Next.js, Remix, Vite, Laravel).

- **Major CLI Rewrite (Aug 2024)**: Complete CLI overhaul with `npx shadcn init` and `npx shadcn add`. Key features:
  - Multi-framework support (Next.js, Remix, Vite, Laravel) out of the box
  - Non-destructive Tailwind config updates (merges instead of overrides)
  - Components ship with their own dependencies (e.g., Tailwind keyframes)
  - Remote component installation via URL: `npx shadcn add https://acme.com/registry/navbar.json`
  - Framework detection in init command
  - Single-command Next.js app initialisation: `npx shadcn init sidebar-01 login-01`
  - Custom component registry schema for private/third-party distribution
  - Enhanced error handling and monorepo support

- **Import Aliases Requirement (Aug 2024)**: `components.json` now requires explicit import alias definitions for components, utils, ui, lib, and hooks. Supports custom prefixes (e.g., `~` instead of `@`).

## Functionality - call for a guide

Changes that relate to these available guides (only list if relevant):

- **Accordion**: Mentioned as example of components shipping their own Tailwind keyframes dependencies in Aug 2024 CLI update.

- **Sidebar**: New Oct 2024 component system - would benefit from dedicated implementation guide for the 25-component sidebar.tsx foundation.
