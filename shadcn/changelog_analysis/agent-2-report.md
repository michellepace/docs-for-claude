# Agent 2 Report: July 2025 - Feb 2025

## New Concepts - super to know

Things Claude Code likely doesn't know that would be useful context:

- **Local file support (July 2025)**: The shadcn CLI now accepts local JSON files for `init` and `add` commands (`npx shadcn init ./template.json` and `npx shadcn add ./block.json`). Enables zero-setup workflows, local testing before publishing, and private component libraries without remote registries.

- **Radix UI unified package (June 2025)**: Radix UI consolidated all separate `@radix-ui/react-*` packages into a single `radix-ui` package. The `npx shadcn@latest migrate radix` command automatically updates imports across UI components.

- **React DayPicker major upgrade (June 2025)**: Calendar component upgraded to latest React DayPicker version with 30+ calendar blocks available in the Blocks Library.

- **MCP integration (April 2025)**: Working on zero-config MCP (Model Context Protocol) support via `npx shadcn registry:mcp` command to make any registry MCP-compatible for agent/AI workflows.

- **Resolve anywhere (March 2025)**: shadcn 2.5.0 introduced ability for registries to place files anywhere in an app with proper import resolution via multi-pass tracking, removing fixed file structure constraints.

- **Cross-framework route support (March 2025)**: CLI now auto-detects framework (Laravel, Vite, React Router, etc.) and adapts routes accordingly.

- **Tailwind v4 support (Feb 2025)**: CLI initialises projects with Tailwind v4, supports new `@theme` directive and `@theme inline` option, removed forwardRefs, added `data-slot` attributes to all primitives for styling, converted HSL colours to OKLCH, deprecated toast component (favouring Sonner), buttons use default cursor, deprecated default style (new projects use new-york).

- **React 19 compatibility (Feb 2025)**: All components updated for React 19 with forwardRef removal and type adjustments.

- **Next.js 15.3 (May 2025)**: The ui.shadcn.com site upgraded to Next.js 15.3 and Tailwind v4 with new-york components.

## Functionality - call for a guide

Changes that relate to these available guides (only list if relevant):

- **Calendar**: June 2025 major upgrade to React DayPicker with 30+ blocks and upgrade guide needed

- **Button**: Feb 2025 change to default cursor behaviour (from pointer to default cursor)

- **Sonner**: Feb 2025 change deprecates toast component in favour of Sonner going forward
