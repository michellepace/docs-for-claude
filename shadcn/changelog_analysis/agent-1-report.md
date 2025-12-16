# Agent 1 Report: Dec 2025 - July 2025

## New Concepts - super to know

Things Claude Code likely doesn't know that would be useful context:

- **npx shadcn create (Dec 2025)**: New CLI command that allows complete customisation of shadcn/ui installations. Users can now choose component library (Radix or Base UI), icons, base colour, theme, fonts, and visual styles. The config rewrites component code to match user preferences, not just colours.

- **Visual styles system**: Five new visual styles introduced - Vega (classic), Nova (compact), Maia (soft/rounded), Lyra (boxy/sharp), Mira (dense). These go beyond theming and affect spacing, padding, structure, and component code generation.

- **Base UI support**: shadcn/ui now supports Base UI as an alternative to Radix UI. All components have been rebuilt for Base UI whilst maintaining the same abstraction. The CLI auto-detects which library is in use and applies appropriate transformations.

- **Framework support expansion**: Now available for Next.js, Vite, TanStack Start, and v0.

- **Registry Directory (Nov 2025)**: Published directory of code registries that can be browsed and pulled from. Built into CLI with no config required.

- **New component library (Oct 2025)**: Seven new utility components designed to be framework-agnostic (work with Radix, Base UI, React Aria):
  - Spinner: Loading state indicator
  - Kbd/KbdGroup: Keyboard key display components
  - Button Group: Container for related buttons with split button support via ButtonGroupSeparator
  - Input Group: Adds icons, buttons, labels to inputs; works with textareas
  - Field: Complex form-building component compatible with Server Actions, React Hook Form, TanStack Form. Includes FieldGroup, FieldSet, FieldLegend. Supports responsive orientation switching.
  - Item: Flex container for lists/cards with ItemMedia, ItemContent, ItemTitle, ItemDescription, ItemGroup
  - Empty: Empty state component with EmptyMedia, EmptyTitle, EmptyDescription, EmptyContent

- **Registry Index (Sep 2025)**: Index of open source registries allowing installation without manual `.components.json` configuration. Items can be installed using `npx shadcn add @namespace/name` format. Registry list available at https://ui.shadcn.com/r/registries.json.

- **shadcn CLI 3.0 (Aug 2025)**: Major CLI rewrite with:
  - Namespaced registries: `@registry/name` format for component installation
  - Decentralised registry system (no central registrar)
  - Private registry support with authentication (bearer tokens, API keys, custom headers, basic auth)
  - Cross-registry dependencies in registry items
  - New commands: `view`, `search`, `list` for registry discovery
  - MCP server integration (improved from April 2025 version) - works with all registries, zero config, supports multiple registries
  - 3x faster dependency resolution
  - Registry-level custom error messages
  - Programmatic API changes: `fetchRegistry` → `getRegistry`, `resolveRegistryTree` → `resolveRegistryItems`, schema moved from `shadcn/registry` to `shadcn/schema` package

- **Universal Registry Items (July 2025)**: Registry items that can be distributed to any project without framework, components.json, Tailwind, or React requirements. Enables distribution of code, config, rules, docs to any codebase.

## Functionality - call for a guide

Changes that relate to these available guides (only list if relevant):

- **Button**: Button Group component introduced (Oct 2025) provides related functionality - grouping buttons, split buttons with dropdown patterns, nested button groups for complex layouts.

- **Form**: Field component (Oct 2025) represents major form-building functionality - works with Server Actions, React Hook Form, TanStack Form; includes FieldGroup, FieldSet, FieldLegend; supports responsive layouts and choice cards.

- **Input**: Input Group component (Oct 2025) extends input functionality significantly - adds icons, buttons, labels, tooltips; works with textareas; enables complex input compositions with spinners and multiple addons.

- **Checkbox**: Field component (Oct 2025) includes checkbox field examples and integration patterns for form layouts.

- **Avatar**: Item and Empty components (Oct 2025) both demonstrate avatar integration patterns for lists and empty states.
