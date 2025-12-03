---
title: Themes
description: Clerk currently offers six prebuilt themes for you to customize the
  overall appearance of your Clerk app.
lastUpdated: 2025-12-02T20:12:39.000Z
sdkScoped: "false"
canonical: /docs/guides/customizing-clerk/appearance-prop/themes
sourceFile: /docs/guides/customizing-clerk/appearance-prop/themes.mdx
---

Clerk currently offers [six prebuilt themes](#available-themes) for you to customize the overall appearance of your Clerk application.

## Installation

1. To get started, install the `@clerk/themes` package.

   ```npm
   npm install @clerk/themes
   ```

2. To use a theme, import it from `@clerk/themes` and apply it using the [`appearance` prop](/docs/guides/customizing-clerk/appearance-prop/overview).

## Usage

You can apply themes at **different levels** depending on your needs:

* Across all Clerk components
* All instances of a Clerk component
* A single Clerk component

For more customization options, refer to the [Advanced usage](#advanced-usage) section.

### Apply a theme to all Clerk components

To apply a theme to all Clerk components, pass the `appearance` prop to the <SDKLink href="/docs/:sdk:/reference/components/clerk-provider" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>\<ClerkProvider></SDKLink> component. The `appearance` prop accepts the property `theme`, which can be set to a theme.

In the following example, the "Dark" theme is applied to all Clerk components.

```tsx {{ filename: '/src/app/layout.tsx', mark: [2, [7, 9]] }}
import { ClerkProvider } from '@clerk/nextjs'
import { dark } from '@clerk/themes'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <ClerkProvider
      appearance={{
        theme: dark,
      }}
    >
      <html lang="en">
        <body>{children}</body>
      </html>
    </ClerkProvider>
  )
}
```

### Apply a theme to all instances of a Clerk component

You can apply a theme to all instances of a Clerk component by passing the component to the `appearance` prop of the `<ClerkProvider>`. The `appearance` prop accepts the name of the Clerk component you want to style as a key.

In the following example, the "Neobrutalism" theme is applied to all instances of the <SDKLink href="/docs/:sdk:/reference/components/authentication/sign-in" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<SignIn /></SDKLink> component.

```tsx {{ filename: '/src/app/layout.tsx', mark: [2, [7, 10]] }}
import { ClerkProvider } from '@clerk/nextjs'
import { dark, neobrutalism } from '@clerk/themes'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <ClerkProvider
      appearance={{
        theme: dark,
        signIn: { theme: neobrutalism },
      }}
    >
      <html lang="en">
        <body>{children}</body>
      </html>
    </ClerkProvider>
  )
}
```

### Apply a theme to a single Clerk component

To apply a theme to a single Clerk component, pass the `appearance` prop to the component. The `appearance` prop accepts the property `theme`, which can be set to a theme.

```tsx {{ filename: 'app/sign-in/[[...sign-in]]/page.tsx', mark: [2, [7, 9]] }}
import { SignIn } from '@clerk/nextjs'
import { dark } from '@clerk/themes'

export default function Page() {
  return (
    <SignIn
      appearance={{
        theme: dark,
      }}
    />
  )
}
```

## Advanced usage

### Apply multiple themes

You can also stack themes by passing an array of themes to the `theme` property of the `appearance` prop. The themes will be applied in the order they are listed. If styles overlap, the last defined theme will take precedence.

In the following example, the "Dark" theme is applied first, then the "Neobrutalism" theme is applied on top of it.

```tsx {{ filename: '/src/app/layout.tsx', mark: [2, [7, 9]] }}
import { ClerkProvider } from '@clerk/nextjs'
import { dark, neobrutalism } from '@clerk/themes'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <ClerkProvider
      appearance={{
        theme: [dark, neobrutalism],
      }}
    >
      <html lang="en">
        <body>{children}</body>
      </html>
    </ClerkProvider>
  )
}
```

### Customize a theme using variables

You can customize a theme by passing an object of variables to the `variables` property of the `appearance` prop. The `variables` property is used to adjust the general styles of the component's base theme, like colors, backgrounds, typography.

In the following example, the primary color of the themes are customized.

> \[!IMPORTANT]
> For a list of all of the variables you can customize, and for more examples on how to use the `variables` property, see the [Variables](/docs/guides/customizing-clerk/appearance-prop/variables) docs.

```tsx {{ filename: '/src/app/layout.tsx', mark: [2, [7, 14]] }}
import { ClerkProvider } from '@clerk/nextjs'
import { dark, neobrutalism, shadesOfPurple } from '@clerk/themes'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <ClerkProvider
      appearance={{
        theme: [dark, neobrutalism],
        variables: { colorPrimary: 'blue' },
        signIn: {
          theme: [shadesOfPurple],
          variables: { colorPrimary: 'green' },
        },
      }}
    >
      <html lang="en">
        <body>{children}</body>
      </html>
    </ClerkProvider>
  )
}
```

## Available themes

Clerk provides six prebuilt themes:

* [The default theme](#default-theme)
* [The "Simple" theme](#simple-theme)
* [The "shadcn" theme](#shadcn-theme)
* [The "Dark" theme](#dark-theme)
* [The "Shades of Purple" theme](#shades-of-purple-theme)
* [The "Neobrutalism" theme](#neobrutalism-theme)

### Default theme

Applied by default when no other theme is provided.

<div style={{padding: "1rem 0", filter: "drop-shadow(rgba(0, 0, 0, 0.16) 0px 12px 24px)"}}>
  ![A sign-in form with a light theme](/docs/images/themes/default.png){{ style: { maxWidth: '400px', width: '100%' } }}
</div>

### "Simple" theme

This theme is a stripped down "Default" theme that removes some more advanced styling techniques, making it easier to apply your own custom styles.

To use the simple theme, set `theme` to `simple`:

```tsx {{ mark: ['simple'] }}
<ClerkProvider
  appearance={{
    theme: 'simple',
  }}
/>
```

<div style={{padding: "1rem 0"}}>
  ![A sign-in form with a simple theme](/docs/images/themes/simple.png){{ style: { maxWidth: '400px', width: '100%' } }}
</div>

### "shadcn" theme

> \[!IMPORTANT]
> This theme is compatible with Tailwind CSS v4 usage. If you need support for Tailwind CSS v3, pass the shadcn variables manually to your `<ClerkProvider />`'s [`variables`](/docs/guides/customizing-clerk/appearance-prop/variables) object.

When using the [shadcn/ui](https://ui.shadcn.com/) library, you can use the `shadcn` theme to apply the shadcn/ui styles to your Clerk components. This will adapt to both light and dark mode automatically.

> \[!IMPORTANT]
> It's recommended to also import the `shadcn.css` file within your `global.css` file. Tailwind scans source files as plain text to detect which classes to generate - classes that only exist in external configurations won't be included in the final CSS.
>
> ```css
> @import 'tailwindcss';
> @import '@clerk/themes/shadcn.css';
> ```

<Tabs items={["Light mode", "Dark mode"]}>
  <div style={{padding: "1rem 0", filter: "drop-shadow(rgba(0, 0, 0, 0.16) 0px 12px 24px)"}}>
    ![A sign-in form with a shadcn theme in light mode](/docs/images/themes/shadcn_light_mode.png){{ style: { maxWidth: '400px', width: '100%' } }}
  </div>

  <div style={{padding: "1rem 0", filter: "drop-shadow(rgba(0, 0, 0, 0.16) 0px 12px 24px)"}}>
    ![A sign-in form with a shadcn theme in dark mode](/docs/images/themes/shadcn_dark_mode.png){{ style: { maxWidth: '400px', width: '100%' } }}
  </div>
</Tabs>

### "Dark" theme

To use the dark theme, set `theme` to `dark`:

```tsx {{ mark: ['dark'] }}
<ClerkProvider
  appearance={{
    theme: 'dark',
  }}
/>
```

<div style={{padding: "1rem 0", filter: "drop-shadow(rgba(0, 0, 0, 0.16) 0px 12px 24px)"}}>
  ![A sign-in form with a dark theme](/docs/images/themes/dark.png){{ style: { maxWidth: '400px', width: '100%' } }}
</div>

### "Shades of purple" theme

To use the shades of purple theme, set `theme` to `shadesOfPurple`:

```tsx {{ mark: ['shadesOfPurple'] }}
<ClerkProvider
  appearance={{
    theme: 'shadesOfPurple',
  }}
/>
```

<div style={{padding: "1rem 0", filter: "drop-shadow(rgba(0, 0, 0, 0.16) 0px 12px 24px)"}}>
  ![A sign-in form with a purple and yellow theme](/docs/images/themes/shades_of_purple.png){{ style: { maxWidth: '400px', width: '100%' } }}
</div>

### "Neobrutalism" theme

To use the neobrutalism theme, set `theme` to `neobrutalism`:

```tsx {{ mark: ['neobrutalism'] }}
<ClerkProvider
  appearance={{
    theme: 'neobrutalism',
  }}
/>
```

<div style={{padding: "1rem 0", filter: "drop-shadow(rgba(0, 0, 0, 0.16) 0px 12px 24px)"}}>
  ![A sign-in form with a neobrutalist red theme](/docs/images/themes/neobrutalism.png){{ style: { maxWidth: '400px', width: '100%' } }}
</div>
