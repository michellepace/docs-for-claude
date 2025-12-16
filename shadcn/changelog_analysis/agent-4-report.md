# Agent 4 Report: April 2024 - June 2023

## New Concepts - super to know

Things Claude Code likely doesn't know that would be useful context:

- **Lift Mode (April 2024)**: Feature for Blocks that automatically "lifts" smaller components from block templates for copy-paste. Allows extracting cards, buttons, and forms from larger block templates individually.

- **Blocks (March 2024)**: Ready-made components (dashboards, auth pages, layouts) built with same principles as shadcn/ui. Open source, fully responsive, accessible, and composable. Different from individual components - these are complete page sections/layouts.

- **Request a Block feature**: Community-driven feature allowing users to request specific blocks via GitHub, with upvoting and community building.

- **v0 integration**: "Edit in v0" feature for Blocks that opens code in v0.dev (Vercel's AI UI generation tool) for prompting and further generation.

- **Input OTP component (March 2024)**: Fully featured one-time password input. Built on input-otp by @guilherme_rodz. Supports numeric/alphanumeric codes, custom length, copy-paste, fully accessible.

- **Tailwind prefix support (December 2023)**: CLI automatically prefixes utility classes when adding components. Allows shadcn/ui integration into existing projects (Docusaurus, Nextra) without conflicts. Works with `cn`, `cva`, and CSS variables.

- **tailwind.config.ts support**: CLI auto-detects TypeScript config files and adds TypeScript version.

- **JavaScript opt-out (July 2023)**: Despite TypeScript recommendation, CLI provides JavaScript versions via `tsx: false` flag in components.json. Uses jsconfig.json for import aliases.

- **components.json configuration file (June 2023)**: Central configuration introduced controlling component installation location, import paths, styling method, base colour, RSC usage. Foundation for all CLI operations.

- **diff command (June 2023)**: Experimental CLI command for tracking upstream component updates. Shows which components have updates and displays diffs for specific components.

- **Styles concept (June 2023)**: Visual foundation layer (shapes, icons, animations, typography). Two initial styles: `default` (lucide-react icons, tailwindcss-animate) and `new-york` (smaller buttons, card shadows, Radix Icons). Style selected during init.

- **CSS Variables vs Utility Classes theming choice (June 2023)**: Configure via `cssVariables` boolean in components.json. CSS variables use semantic tokens (`bg-background`), utility classes use direct Tailwind classes (`bg-zinc-950 dark:bg-white`).

- **Base colour configuration (June 2023)**: Choose between gray, neutral, slate, stone, or zinc. CLI generates appropriate colour palette whether using CSS variables or utility classes.

- **RSC opt-out (June 2023)**: `rsc: false` flag in components.json automatically appends/removes `use client` directive for frameworks without React Server Components support.

- **Exit animations (June 2023)**: Added to all components with customisable utility classes. Subtle animations when components close/unmount.

## Functionality - call for a guide

Changes that relate to these available guides (only list if relevant):

- **Breadcrumb**: New component added March 2024. Accessible, flexible, supports collapsed items, custom separators, bring-your-own routing Link, composable with other shadcn/ui components.

- **Input OTP**: New component added March 2024. Built on input-otp library. Supports numeric and alphanumeric codes, custom length, copy-paste functionality, fully accessible.

- **Carousel**: New component added December 2023. Built on Embla Carousel. Features motion, swipe gestures, keyboard support, infinite looping, autoplay, vertical orientation.

- **Drawer**: New component added December 2023. Built on Vaul by emilkowalski. Optimised for mobile with impressive UX.

- **Pagination**: New component added December 2023. Page navigation with previous/next buttons. Simple, flexible, works with framework Link components.

- **Resizable**: New component added December 2023. Built using react-resizable-panels by bvaughn. Supports mouse, touch, and keyboard for building resizable panel groups/layouts.

- **Sonner**: New component added December 2023. Toast component by emilkowalski. Described as "the last toast component you'll ever need".

- **Button**: Added new `icon` size variant (June 2023). Height and width both 10 (`h-10 w-10`) for square icon buttons.

- **Sheet**: Renamed `position` prop to `side` (June 2023). Removed `size` prop - use className for responsive sizing (`w-[200px] md:w-[450px]`). Updated component code with new variants structure using `side` instead of `position`.
