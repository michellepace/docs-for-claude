---
title: Themes
description: Clerk currently offers six prebuilt themes for you to customize the
  overall appearance of your Clerk app.
sdk: astro, chrome-extension, expo, nextjs, nuxt, react, react-router, remix,
  tanstack-react-start, vue, js-frontend, fastify, expressjs, js-backend, go,
  ruby, android
sdkScoped: "true"
canonical: /docs/:sdk:/guides/customizing-clerk/appearance-prop/themes
lastUpdated: 2025-12-03T22:33:41.000Z
availableSdks: astro,chrome-extension,expo,nextjs,nuxt,react,react-router,remix,tanstack-react-start,vue,js-frontend,fastify,expressjs,js-backend,go,ruby,android
notAvailableSdks: ios
activeSdk: nextjs
sourceFile: /docs/guides/customizing-clerk/appearance-prop/themes.mdx
---

Clerk currently offers <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/themes#available-themes" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>six prebuilt themes</SDKLink> for you to customize the overall appearance of your Clerk application.

## Installation

1. To get started, install the `@clerk/themes` package.

   ```npm
   npm install @clerk/themes
   ```

2. To use a theme, import it from `@clerk/themes` and apply it using the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/overview" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]} code={true}>appearance prop</SDKLink>.

## Usage

You can apply themes at **different levels** depending on your needs:

* Across all Clerk components
* All instances of a Clerk component
* A single Clerk component

For more customization options, refer to the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/themes#advanced-usage" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Advanced usage</SDKLink> section.

### Apply a theme to all Clerk components

<If notSdk={["astro", "js-frontend", "vue", "nuxt", "fastify"]}>
  To apply a theme to all Clerk components, pass the `appearance` prop to the <SDKLink href="/docs/:sdk:/reference/components/clerk-provider" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>\<ClerkProvider></SDKLink> component. The `appearance` prop accepts the property `theme`, which can be set to a theme.

  In the following example, the "Dark" theme is applied to all Clerk components.

  ```tsx {{ prettier: false, mark: [1, [4, 6]] }}
   import { dark } from '@clerk/themes'

   <ClerkProvider
    appearance={{
       theme: dark,
     }}
   >
     {/* ... */}
   </ClerkProvider>
  ```

</If>

### Apply a theme to all instances of a Clerk component

To apply a theme to all instances of a Clerk component, you can pass the name of the Clerk component itself to the `appearance` prop.

In the following example, the "Neobrutalism" theme is applied to all instances of the <SDKLink href="/docs/:sdk:/reference/components/authentication/sign-in" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<SignIn /></SDKLink> component.

<If notSdk={["astro", "js-frontend", "vue", "nuxt", "fastify"]}>

  ```tsx {{ prettier: false, mark: [1, [4, 7]] }}
  import { dark, neobrutalism } from '@clerk/themes'

  <ClerkProvider
    appearance={{
      theme: dark,
      signIn: { theme: neobrutalism },
    }}
  >
    {/* ... */}
  </ClerkProvider>
  ```

</If>

### Apply a theme to a single Clerk component

To apply a theme to a single Clerk component, pass the `theme` property to the `appearance` prop of the Clerk component.

In the following example, the "Dark" theme is applied to the <SDKLink href="/docs/:sdk:/reference/components/authentication/sign-in" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<SignIn /></SDKLink> component.

<If notSdk={["vue", "nuxt"]}>

  ```tsx {{ mark: [[2, 4]] }}
  <SignIn
    appearance={{
      theme: dark,
    }}
  />
  ```

</If>

## Advanced usage

### Apply multiple themes

You can also stack themes by passing an array of themes to the `theme` property of the `appearance` prop. The themes will be applied in the order they are listed. If styles overlap, the last defined theme will take precedence.

In the following example, the "Dark" theme is applied first, then the "Neobrutalism" theme is applied on top of it.

<If notSdk={["astro", "js-frontend", "vue", "nuxt", "fastify"]}>

  ```tsx {{ prettier: false, mark: [1, [4, 6]] }}
   import { dark, neobrutalism } from '@clerk/themes'

   <ClerkProvider
     appearance={{
       theme: [dark, neobrutalism],
     }}
   >
     {/* ... */}
   </ClerkProvider>
  ```

</If>

### Customize a theme using variables

You can customize a theme by passing an object of variables to the `variables` property of the `appearance` prop. The `variables` property is used to adjust the general styles of the component's base theme, like colors, backgrounds, typography.

> \[!IMPORTANT]
> For a list of all of the variables you can customize, and for more examples on how to use the `variables` property, see the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/variables" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Variables</SDKLink> docs.

In the following example, the primary color of the themes are customized.

<If notSdk={["astro", "js-frontend", "vue", "nuxt", "fastify"]}>

  ```tsx {{ prettier: false, mark: [1, [4, 11]] }}
  import { dark, neobrutalism, shadesOfPurple } from '@clerk/themes'

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
    {/* ... */}
  </ClerkProvider>
  ```

</If>

## Available themes

Clerk provides six prebuilt themes:

* <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/themes#default-theme" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>The default theme</SDKLink>
* <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/themes#simple-theme" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>The "Simple" theme</SDKLink>
* <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/themes#shadcn-theme" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>The "shadcn" theme</SDKLink>
* <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/themes#dark-theme" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>The "Dark" theme</SDKLink>
* <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/themes#shades-of-purple-theme" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>The "Shades of Purple" theme</SDKLink>
* <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/themes#neobrutalism-theme" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>The "Neobrutalism" theme</SDKLink>

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
> This theme is compatible with Tailwind CSS v4 usage. If you need support for Tailwind CSS v3, pass the shadcn variables manually to your `<ClerkProvider />`'s <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/variables" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]} code={true}>variables</SDKLink> object.

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
