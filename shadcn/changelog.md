---
title: Changelog
description: Latest updates and announcements.
toc: false
---

## December 2025 - npx shadcn create

From the very first commit, the goal of shadcn/ui was to make it customizable.

The idea is to give you solid defaults, spacing, color tokens, animations, accessibility, and then let you take it from there. Tweak the code. Add new components. Change the colors. Build your own version.

But somewhere along the way, all apps started looking the same. I guess the defaults were a little _too_ good. My bad.

Today, we're changing that: **npx shadcn create**.

Customize Everything. Pick your component library, icons, base color, theme, fonts and create your own version of shadcn/ui.

We're starting with **5 new visual styles,** designed to help your UI actually feel like _your_ UI.

- **Vega** – The classic shadcn/ui look.
- **Nova** – Reduced padding and margins for compact layouts.
- **Maia** – Soft and rounded, with generous spacing.
- **Lyra** – Boxy and sharp. Pairs well with mono fonts.
- **Mira** – Compact. Made for dense interfaces.

**This goes beyond theming**.

Your config doesn’t just change colors, it rewrites the component code to match your setup. Fonts, spacing, structure, even the libraries you use, everything adapts to your preferences.

The new CLI takes care of it all.

Start with a component library. Choose between Radix or Base UI.

We rebuilt every component for Base UI, keeping the same abstraction.
They are fully compatible with your existing components, even those pulled from remote registries.

When you pull down components, we auto-detect your library and apply the right transformations.

**It's time to build something that doesn't look like everything else.**

Now available for Next.js, Vite, TanStack Start and v0.

<Button asChild>
  <Link href="/create" className="mt-6 no-underline!">
    Get Started
  </Link>
</Button>

---

## November 2025 - Registry directory

We just published the Registry Directory: a list of code registries you can browse and pull code and components from.

<https://ui.shadcn.com/docs/directory>

Built into the CLI. No config required.

---

## October 2025 - New Components

For this round of components, I looked at what we build every day, the boring stuff we rebuild over and over, and made reusable abstractions you can actually use.

**These components work with every component library, Radix, Base UI, React Aria, you name it. Copy and paste to your projects.**

- [Spinner](#spinner): An indicator to show a loading state.
- [Kbd](#kbd): Display a keyboard key or group of keys.
- [Button Group](#button-group): A group of buttons for actions and split buttons.
- [Input Group](#input-group): Input with icons, buttons, labels and more.
- [Field](#field): One component. All your forms.
- [Item](#item): Display lists of items, cards, and more.
- [Empty](#empty): Use this one for empty states.

### Spinner

Okay let's start with the easiest ones: **Spinner** and **Kbd**. Pretty basic. We all know what they do.

Here's how you render a spinner:

```tsx
import { Spinner } from "@/components/ui/spinner"
```

```tsx
<Spinner />
```

Here's what it looks like:

<ComponentPreview
  name="spinner-basic"
  className="[&_.preview]:h-[250px] [&_pre]:!h-[250px]"
/>

Here's what it looks like in a button:

<ComponentPreview
  name="spinner-button"
  className="[&_.preview]:h-[250px] [&_pre]:!h-[250px]"
/>

You can edit the code and replace it with your own spinner.

<ComponentPreview
  name="spinner-custom"
  className="[&_.preview]:h-[250px] [&_pre]:!h-[250px]"
/>

### Kbd

Kbd is a component that renders a keyboard key.

```tsx
import { Kbd, KbdGroup } from "@/components/ui/kbd"
```

```tsx
<Kbd>Ctrl</Kbd>
```

Use `KbdGroup` to group keyboard keys together.

```tsx showLineNumbers
<KbdGroup>
  <Kbd>Ctrl</Kbd>
  <Kbd>B</Kbd>
</KbdGroup>
```

<ComponentPreview
  name="kbd-demo"
  className="[&_.preview]:h-[250px] [&_pre]:!h-[250px]"
/>

You can add it to buttons, tooltips, input groups, and more.

### Button Group

I got a lot of requests for this one: Button Group. It's a container that groups related buttons together with consistent styling. Great for action groups, split buttons, and more.

<ComponentPreview
  name="button-group-demo"
  className="[&_.preview]:h-[250px] [&_pre]:!h-[250px]"
/>

Here's the code:

```tsx
import { ButtonGroup } from "@/components/ui/button-group"
```

```tsx showLineNumbers
<ButtonGroup>
  <Button>Button 1</Button>
  <Button>Button 2</Button>
</ButtonGroup>
```

You can nest button groups to create more complex layouts with spacing.

```tsx showLineNumbers
<ButtonGroup>
  <ButtonGroup>
    <Button>Button 1</Button>
    <Button>Button 2</Button>
  </ButtonGroup>
  <ButtonGroup>
    <Button>Button 3</Button>
    <Button>Button 4</Button>
  </ButtonGroup>
</ButtonGroup>
```

Use `ButtonGroupSeparator` to create split buttons. Classic dropdown pattern.

<ComponentPreview
  name="button-group-dropdown"
  className="[&_.preview]:h-[250px] [&_pre]:!h-[250px]"
/>

You can also use it to add prefix or suffix buttons and text to inputs.

<ComponentPreview
  name="button-group-select"
  className="[&_.preview]:h-[250px] [&_pre]:!h-[250px]"
/>

```tsx showLineNumbers
<ButtonGroup>
  <ButtonGroupText>Prefix</ButtonGroupText>
  <Input placeholder="Type something here..." />
  <Button>Button</Button>
</ButtonGroup>
```

### Input Group

Input Group lets you add icons, buttons, and more to your inputs. You know, all those little bits you always need around your inputs.

```tsx
import {
  InputGroup,
  InputGroupAddon,
  InputGroupInput,
} from "@/components/ui/input-group"
```

```tsx showLineNumbers
<InputGroup>
  <InputGroupInput placeholder="Search..." />
  <InputGroupAddon>
    <SearchIcon />
  </InputGroupAddon>
</InputGroup>
```

Here's a preview with icons:

<ComponentPreview
  name="input-group-icon"
  className="[&_.preview]:h-[300px] [&_pre]:!h-[300px]"
/>

You can also add buttons to the input group.

<ComponentPreview
  name="input-group-button"
  className="[&_.preview]:h-[300px] [&_pre]:!h-[300px]"
/>

Or text, labels, tooltips,...

<ComponentPreview
  name="input-group-text"
  className="[&_.preview]:h-[350px] [&_pre]:!h-[350px]"
/>

It also works with textareas so you can build really complex components with lots of knobs and dials or yet another prompt form.

<ComponentPreview
  name="input-group-textarea"
  className="[&_.preview]:h-[450px] [&_pre]:!h-[450px]"
/>

Oh here are some cool ones with spinners:

<ComponentPreview
  name="input-group-spinner"
  className="[&_.preview]:h-[350px] [&_pre]:!h-[350px]"
/>

### Field

Introducing **Field**, a component for building really complex forms. The abstraction here is beautiful.

It took me a long time to get it right but I made it work with all your form libraries: Server Actions, React Hook Form, TanStack Form, Bring Your Own Form.

```tsx
import {
  Field,
  FieldDescription,
  FieldError,
  FieldLabel,
} from "@/components/ui/field"
```

Here's a basic field with an input:

```tsx showLineNumbers
<Field>
  <FieldLabel htmlFor="username">Username</FieldLabel>
  <Input id="username" placeholder="Max Leiter" />
  <FieldDescription>
    Choose a unique username for your account.
  </FieldDescription>
</Field>
```

<ComponentPreview
  name="field-input"
  className="[&_.preview]:h-[350px] [&_pre]:!h-[350px]"
/>

It works with all form controls. Inputs, textareas, selects, checkboxes, radios, switches, sliders, you name it. Here's a full example:

<ComponentPreview
  name="field-demo"
  className="[&_.preview]:h-[850px] [&_pre]:!h-[850px]"
/>

Here are some checkbox fields:

<ComponentPreview
  name="field-checkbox"
  className="[&_.preview]:h-[500px] [&_pre]:!h-[500px]"
/>

You can group fields together using `FieldGroup` and `FieldSet`. Perfect for
multi-section forms.

```tsx showLineNumbers
<FieldSet>
  <FieldLegend />
  <FieldGroup>
    <Field />
    <Field />
  </FieldGroup>
</FieldSet>
```

<ComponentPreview
  name="field-fieldset"
  className="[&_.preview]:h-[500px] [&_pre]:!h-[500px]"
/>

Making it responsive is easy. Use `orientation="responsive"` and it switches
between vertical and horizontal layouts based on container width. Done.

<ComponentPreview
  name="field-responsive"
  className="[&_.preview]:h-[600px] [&_pre]:!h-[600px]"
/>

Wait here's more. Wrap your fields in `FieldLabel` to create a selectable field group. Really easy. And it looks great.

<ComponentPreview
  name="field-choice-card"
  className="[&_.preview]:h-[600px] [&_pre]:!h-[600px]"
/>

### Item

This one is a straightforward flex container that can house nearly any type of content.

I've built this so many times that I decided to create a component for it. Now I use it all the time. I use it to display lists of items, cards, and more.

```tsx
import {
  Item,
  ItemContent,
  ItemDescription,
  ItemMedia,
  ItemTitle,
} from "@/components/ui/item"
```

Here's a basic item:

```tsx showLineNumbers
<Item>
  <ItemMedia variant="icon">
    <HomeIcon />
  </ItemMedia>
  <ItemContent>
    <ItemTitle>Dashboard</ItemTitle>
    <ItemDescription>Overview of your account and activity.</ItemDescription>
  </ItemContent>
</Item>
```

<ComponentPreview
  name="item-demo"
  className="[&_.preview]:h-[300px] [&_.preview]:p-4 [&_pre]:!h-[300px]"
/>

You can add icons, avatars, or images to the item.

<ComponentPreview
  name="item-icon"
  className="[&_.preview]:h-[300px] [&_.preview]:p-4 [&_pre]:!h-[300px]"
/>

<ComponentPreview
  name="item-avatar"
  className="[&_.preview]:h-[300px] [&_.preview]:p-4 [&_pre]:!h-[300px]"
/>

And here's what a list of items looks like with `ItemGroup`:

<ComponentPreview
  name="item-group"
  className="[&_.preview]:h-[500px] [&_.preview]:p-4 [&_pre]:!h-[500px]"
/>

Need it as a link? Use the `asChild` prop:

```tsx showLineNumbers
<Item asChild>
  <a href="/dashboard">
    <ItemMedia variant="icon">
      <HomeIcon />
    </ItemMedia>
    <ItemContent>
      <ItemTitle>Dashboard</ItemTitle>
      <ItemDescription>Overview of your account and activity.</ItemDescription>
    </ItemContent>
  </a>
</Item>
```

<ComponentPreview
  name="item-link"
  className="[&_.preview]:h-[400px] [&_.preview]:p-4 [&_pre]:!h-[400px]"
/>

### Empty

Okay last one: **Empty**. Use this to display empty states in your app.

```tsx
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyMedia,
  EmptyTitle,
} from "@/components/ui/empty"
```

Here's how you use it:

```tsx showLineNumbers
<Empty>
  <EmptyMedia variant="icon">
    <InboxIcon />
  </EmptyMedia>
  <EmptyTitle>No messages</EmptyTitle>
  <EmptyDescription>You don't have any messages yet.</EmptyDescription>
  <EmptyContent>
    <Button>Send a message</Button>
  </EmptyContent>
</Empty>
```

<ComponentPreview
  name="empty-demo"
  className="[&_.preview]:h-[400px] [&_.preview]:p-4 [&_pre]:!h-[400px]"
/>

You can use it with avatars:

<ComponentPreview
  name="empty-avatar"
  className="[&_.preview]:h-[400px] [&_pre]:!h-[400px]"
/>

Or with input groups for things like search results or email subscriptions:

<ComponentPreview
  name="empty-input-group"
  className="[&_.preview]:h-[450px] [&_pre]:!h-[450px]"
/>

That's it. Seven new components. Works with all your libraries. Ready for your projects.

---

## September 2025 - Registry Index

We've created an index of open source registries that you can install items from.

You can search, view and add items from the registry index without configuring the `.components.json` file.

They'll be automatically added to your `components.json` file for you.

```bash
npx shadcn add @ai-elements/prompt-input
```

The full list of registries is available at [https://ui.shadcn.com/r/registries.json](https://ui.shadcn.com/r/registries.json).

To add a registry to the index, submit a PR to the `shadcn/ui` repository. See the [registry index documentation](/docs/registry/registry-index) for more details.

---

## August 2025 - shadcn CLI 3.0 and MCP Server

We just shipped shadcn CLI 3.0 with support for namespaced registries, advanced authentication, new commands and a completely rewritten registry engine.

### What's New

- [Namespaced Registries](#namespaced-registries) - Install components using `@registry/name` format.
- [Private Registries](#private-registries) - Secure your registry with advanced authentication.
- [Search & Discovery](#search--discovery) - New commands to find and view code before installing.
- [MCP Server](#mcp-server) - MCP server for all registries.
- [Faster Everything](#faster-everything) - Completely rewritten registry resolution.
- [Improved Error Handling](#improved-error-handling) - Better error messages for users and LLMs.
- [Upgrade Guide](#upgrade-guide) - Migration notes for existing users.

### Namespaced Registries

The biggest change in 3.0 is namespaced registries. You can now install components from registries: a community registry, your company's private registry or internal registry, using the `@registry/name` format.

This makes it easier to distribute code across teams and projects.

Configure registries in your `components.json`:

```json title="components.json"
{
  "registries": {
    "@acme": "https://acme.com/r/{name}.json",
    "@internal": {
      "url": "https://registry.company.com/{name}",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_TOKEN}"
      }
    }
  }
}
```

Then use the `@registry/name` format to install components:

```bash
npx shadcn add @acme/button @internal/auth-system
```

It's completely decentralized. There's no central registrar. Create any namespace you want and organize components however makes sense for your team.

```json title="components.json" showLineNumbers
{
  "registries": {
    "@design": "https://registry.company.com/create/{name}.json",
    "@engineering": "https://registry.company.com/eng/{name}.json",
    "@marketing": "https://registry.company.com/marketing/{name}.json"
  }
}
```

Components can even depend on resources from different registries. Everything gets resolved and installed automatically from the right sources.

```json title="registry-item.json" showLineNumbers
{
  "name": "dashboard",
  "type": "registry:block",
  "registryDependencies": [
    "@shadcn/card", // From default registry
    "@v0/chart", // From v0 registry
    "@acme/data-table", // From acme registry
    "@lib/data-fetcher", // Utility library
    "@ai/analytics-prompt" // AI prompt resource
  ]
}
```

### Private Registries

Need to keep your components private? We've got you covered. Configure authentication with tokens, API keys, or custom headers:

```json title="components.json"
{
  "registries": {
    "@private": {
      "url": "https://registry.company.com/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_TOKEN}"
      }
    }
  }
}
```

Your private components stay private. Perfect for enterprise teams with proprietary UI libraries.

We support all major authentication methods: basic auth, bearer token, api key query params and custom headers.

See the [authentication docs](/docs/registry/authentication) for more details.

### Search & Discovery

Three new commands make it easy to find exactly what you need:

1. View items from the registry before installing

```bash
npx shadcn view @acme/auth-system
```

1. Search items from registries

```bash
npx shadcn search @tweakcn -q "dark"
```

1. List all items from a registry

```bash
npx shadcn list @acme
```

Preview components before installing them. Search across multiple registries. See the code and all dependencies upfront.

### MCP Server

<Image
  src="/images/mcp.jpeg"
  width="1432"
  height="1050"
  alt="Lift Mode"
  className="mt-6 w-full overflow-hidden rounded-lg border"
/>

Back in April, we [introduced](https://x.com/shadcn/status/1917597228513853603) the first version of the MCP server. Since then, we've taken everything we learned and built a better MCP server.

Here's what's new:

- Works with all registries. Zero config
- One command to add to your favorite MCP clients
- We improved the underlying tools
- Better integration with the CLI and registries
- Support for multiple registries in the same project

Add the MCP server to your project:

```bash
npx shadcn@latest mcp init
```

See the [docs](/docs/mcp) for more details.

### Faster Everything

We completely rewrote the registry resolution engine from scratch. It's faster, smarter, and handles even the trickiest dependency trees.

- Up to 3x faster dependency resolution
- Smarter file deduplication and merging
- Better monorepo support out of the box
- Updated `build` command for registry authors

### Improved Error Handling

Registry developers can now provide custom error messages to help guide users (and LLMs) when things go wrong. The CLI displays helpful, actionable errors for common issues:

```txt
Unknown registry "@acme". Make sure it is defined in components.json as follows:
{
  "registries": {
    "@acme": "[URL_TO_REGISTRY]"
  }
}
```

Missing environment variables? The CLI tells you exactly what's needed:

```txt
Registry "@private" requires the following environment variables:
  • REGISTRY_TOKEN

Set the required environment variables to your .env or .env.local file.
```

Registry authors can provide custom error messages in their responses to help users and AI agents understand and fix issues quickly.

```txt
Error:
You are not authorized to access the item at http://example.com/r/component.

Message:
[Unauthorized] Your API key has expired. Renew it at https://example.com/api/renew-key.
```

### Upgrade Guide

Here's the best part: there are no breaking changes for users. Your existing `components.json` works exactly the same. All your installed components work exactly the same.

For developers, if you're using the programmatic APIs directly, we've deprecated a few functions in favor of better ones:

- `fetchRegistry` → `getRegistry`
- `resolveRegistryTree` → `resolveRegistryItems`
- Schema moved from `shadcn/registry` to `shadcn/schema` package

```diff
- import { registryItemSchema } from "shadcn/registry"
+ import { registryItemSchema } from "shadcn/schema"
```

That's it. Seriously. Everything else just works.

---

## July 2025 - Universal Registry Items

We've added support for universal registry items. This allows you to create registry items that can be distributed to any project i.e. no framework, no components.json, no tailwind, no react required.

This new registry item type unlocks a lot of new workflows. You can now distribute code, config, rules, docs, anything to any code project.

See the [docs](/docs/registry/examples) for more details and examples.

---

## July 2025 - Local File Support

The shadcn CLI now supports local files. Initialize projects and add components, themes, hooks, utils and more from local JSON files.

```bash
# Initialize a project from a local file
npx shadcn init ./template.json

# Add a component from a local file
npx shadcn add ./block.json
```

This feature enables powerful new workflows:

- **Zero setup** - No remote registries required
- **Faster development** - Test registry items locally before publishing
- **Enhanced workflow for agents and MCP** - Generate and run registry items locally
- **Private components** - Keep proprietary components local and private.

---

## June 2025 - `radix-ui`

We've added a new command to migrate to the new `radix-ui` package. This command will replace all `@radix-ui/react-*` imports with `radix-ui`.

```bash
npx shadcn@latest migrate radix
```

It will automatically update all imports in your `ui` components and install `radix-ui` as a dependency.

```diff showLineNumbers title="components/ui/alert-dialog.tsx"
- import * as AlertDialogPrimitive from "@radix-ui/react-dialog"
+ import { AlertDialog as AlertDialogPrimitive } from "radix-ui"
```

Make sure to test your components and project after running the command.

**Note:** To update imports for newly added components, run the migration command again.

## June 2025 - Calendar Component

We've upgraded the `Calendar` component to the latest version of [React DayPicker](https://daypicker.dev).

This is a major upgrade and includes a lot of new features and improvements. We've also built a collection of 30+ calendar blocks that you can use to build your own calendar components.

See all calendar blocks in the [Blocks Library](/blocks/calendar) page.

<Image src="/images/calendar-2.png" alt="Calendar" width={676} height={895} />

To upgrade your project to the latest version of the `Calendar` component, see the [upgrade guide](/docs/components/calendar#upgrade-guide).

## January–May 2025 (Summary)

**May** – Site upgraded to Next.js 15.3 + Tailwind v4, using `new-york` components.

**April** – Initial MCP work: `npx shadcn registry:mcp` for zero-config MCP support.

**March** – CLI 2.5.0 with "resolve anywhere" (registries can place files anywhere, multi-pass import resolution). Cross-framework route auto-detection (Laravel, Vite, React Router).

**February** – Tailwind v4 + React 19 preview. Key changes: `@theme` directive, `data-slot` attributes on primitives, HSL→OKLCH colours, sonner replaces toast, `new-york` is now default style. Updated registry schema for custom styles, themes, CSS vars, hooks.

**January** – Community blocks library launched. See [/docs/blocks](/docs/blocks).
