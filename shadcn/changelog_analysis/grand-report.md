# Grand Report: shadcn/ui Changelog Analysis

## Summary

Analysis of 27 changelog sections (Dec 2025 → June 2023) identifying knowledge gaps for Claude Code (Jan 2025 cutoff) and guide recommendations for a shadcn skill.

---

## New Concepts - super to know

### Post-Cutoff (After Jan 2025) - Critical Knowledge Gaps

#### CLI Evolution

- **npx shadcn create (Dec 2025)**: New command for complete customisation - choose component library (Radix/Base UI), icons, base colour, theme, fonts, and visual styles. Rewrites component code, not just colours.

- **shadcn CLI 3.0 (Aug 2025)**: Major rewrite with namespaced registries (`@registry/name`), decentralised system, private registry auth support, cross-registry dependencies, new commands (`view`, `search`, `list`), MCP server integration, 3x faster resolution.

- **Local file support (July 2025)**: CLI accepts local JSON for `init` and `add` commands (`npx shadcn init ./template.json`). Enables zero-setup workflows and private libraries.

- **Radix migration (June 2025)**: `npx shadcn@latest migrate radix` auto-updates imports after Radix unified all `@radix-ui/react-*` packages into single `radix-ui` package.

- **Resolve anywhere (March 2025)**: v2.5.0 allows registries to place files anywhere with proper import resolution.

#### Component Libraries & Styles

- **Base UI support (Dec 2025)**: All components rebuilt for Base UI as Radix alternative. CLI auto-detects and applies appropriate transformations.

- **Visual styles system (Dec 2025)**: Five styles beyond theming - Vega (classic), Nova (compact), Maia (soft/rounded), Lyra (boxy/sharp), Mira (dense). Affects spacing, padding, structure.

- **New utility components (Oct 2025)**: Spinner, Kbd/KbdGroup, Button Group, Input Group, Field (form-building), Item (flex container), Empty (empty states). Framework-agnostic (Radix, Base UI, React Aria).

#### Registry System

- **Registry Directory (Nov 2025)**: Published directory of code registries built into CLI, no config required.

- **Registry Index (Sep 2025)**: Install from open source registries via `npx shadcn add @namespace/name`.

- **Universal Registry Items (July 2025)**: Distribute to any project without framework/Tailwind/React requirements.

- **MCP integration (April 2025)**: `npx shadcn registry:mcp` makes any registry MCP-compatible for AI workflows.

#### Framework & Styling Updates

- **Tailwind v4 support (Feb 2025)**: New `@theme` directive, `@theme inline`, `data-slot` attributes, HSL→OKLCH colours, deprecated toast (→Sonner), buttons use default cursor, deprecated default style (→new-york).

- **React 19 compatibility (Feb 2025)**: forwardRef removal, type adjustments across all components.

- **React DayPicker upgrade (June 2025)**: Calendar upgraded with 30+ blocks in Blocks Library.

- **Cross-framework routes (March 2025)**: Auto-detects Laravel, Vite, React Router and adapts routes.

### Around/Before Cutoff (Claude May Know) - Context Enrichment

#### CLI Features (2024)

- **Major CLI rewrite (Aug 2024)**: `npx shadcn init` and `npx shadcn add`. Multi-framework (Next.js, Remix, Vite, Laravel), non-destructive Tailwind updates, remote URL installation, framework detection.

- **Import aliases requirement (Aug 2024)**: `components.json` needs explicit aliases for components, utils, ui, lib, hooks. Supports custom prefixes (`~` instead of `@`).

- **Monorepo support (Dec 2024)**: CLI handles monorepo paths, dependencies, and import resolution.

#### Components & Features (2024)

- **Sidebar system (Oct 2024)**: New `sidebar.tsx` with 25+ variations. Cross-framework support.

- **Blocks (March 2024)**: Ready-made dashboards, auth pages, layouts. Open source, responsive, accessible.

- **Lift Mode (April 2024)**: Extract smaller components from block templates.

- **v0 integration**: "Edit in v0" opens code in Vercel's AI UI generator.

- **Lucide default (Nov 2024)**: New York style uses Lucide icons by default.

#### Foundational Concepts (2023)

- **components.json (June 2023)**: Central config controlling installation location, import paths, styling, base colour, RSC.

- **Styles concept (June 2023)**: `default` (lucide-react, tailwindcss-animate) vs `new-york` (smaller buttons, card shadows, Radix Icons).

- **CSS Variables vs Utility Classes (June 2023)**: `cssVariables` boolean in config. Variables use semantic tokens, utilities use direct Tailwind.

- **Base colour config (June 2023)**: gray, neutral, slate, stone, or zinc options.

- **RSC opt-out (June 2023)**: `rsc: false` manages `use client` directive.

- **Tailwind prefix support (Dec 2023)**: Auto-prefixes utilities for existing project integration.

---

## Functionality - call for a guide

### High Priority (Major Changes/New Components)

| Guide | Reason |
|:------|:-------|
| **Calendar** | June 2025 major upgrade to React DayPicker with 30+ blocks |
| **Form** | Oct 2025 Field component - Server Actions, React Hook Form, TanStack Form integration |
| **Input** | Oct 2025 Input Group - icons, buttons, labels, tooltips, textarea support |
| **Button** | Oct 2025 Button Group + Feb 2025 cursor change + June 2023 icon variant |
| **Sonner** | Feb 2025 deprecates toast in favour of Sonner |

### Medium Priority (Newer Components)

| Guide | Reason |
|:------|:-------|
| **Breadcrumb** | March 2024 - accessible, collapsed items, custom separators |
| **Input OTP** | March 2024 - input-otp library, numeric/alphanumeric, copy-paste |
| **Carousel** | Dec 2023 - Embla Carousel, swipe, keyboard, infinite, autoplay |
| **Drawer** | Dec 2023 - Vaul library, mobile-optimised |
| **Pagination** | Dec 2023 - framework Link compatible |
| **Resizable** | Dec 2023 - react-resizable-panels, mouse/touch/keyboard |
| **Sidebar** | Oct 2024 - 25+ component variations, cross-framework |

### Lower Priority (Incremental Updates)

| Guide | Reason |
|:------|:-------|
| **Sheet** | June 2023 - `position`→`side` prop, size via className |
| **Accordion** | Aug 2024 - example of self-contained Tailwind keyframes |
| **Checkbox** | Oct 2025 - Field component integration patterns |
| **Avatar** | Oct 2025 - Item and Empty component patterns |

---

## Actionable Recommendations

### For shadcn Skill Context

1. **Critical**: Document CLI 3.0 commands, namespaced registries, and Base UI support
2. **Important**: Explain Tailwind v4 migration (OKLCH, data-slot, @theme)
3. **Useful**: Cover visual styles system (Vega, Nova, Maia, Lyra, Mira)
4. **Foundation**: Ensure components.json configuration is well-documented

### Guide Scraping Priority

1. Calendar (major overhaul)
2. Form (new Field component ecosystem)
3. Input (Input Group additions)
4. Button (multiple changes across versions)
5. Sonner (toast replacement)
6. Sidebar (new system, widely used)
