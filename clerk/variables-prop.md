---
title: "`Variables` prop"
description: Utilize Clerk's variables property in order to adjust the general
  styles of the component's base theme, like colors, backgrounds, typography.
sdk: astro, chrome-extension, expo, nextjs, nuxt, react, react-router, remix,
  tanstack-react-start, vue, js-frontend, fastify, expressjs, js-backend, go,
  ruby, android
sdkScoped: "true"
canonical: /docs/:sdk:/guides/customizing-clerk/appearance-prop/variables
lastUpdated: 2025-12-03T22:33:41.000Z
availableSdks: astro,chrome-extension,expo,nextjs,nuxt,react,react-router,remix,tanstack-react-start,vue,js-frontend,fastify,expressjs,js-backend,go,ruby,android
notAvailableSdks: ios
activeSdk: nextjs
sourceFile: /docs/guides/customizing-clerk/appearance-prop/variables.mdx
---

{/*JS file: <https://github.com/clerk/javascript/blob/main/packages/types/src/appearance.ts#L399>*/}

The `variables` property is used to adjust the general styles of the component's base theme, like colors, backgrounds, and typography.

## Properties

<Properties>
  * `colorPrimary`
  * `string`

  The primary color used throughout the components.

  CSS variable: `--clerk-color-primary`

  ***

* `colorDanger`
* `string`

  The color used for error states.

  CSS variable: `--clerk-color-danger`

  ***

* `colorSuccess`
* `string`

  The color used for success states.

  CSS variable: `--clerk-color-success`

  ***

* `colorWarning`
* `string`

  The color used for warning states.

  CSS variable: `--clerk-color-warning`

  ***

* `colorNeutral`
* `string`

  The color that will be used for all to generate the neutral shades the components use. This option applies to borders, backgrounds for hovered elements, hovered dropdown options.

  CSS variable: `--clerk-color-neutral`

  ***

* `colorForeground`
* `string`

  The color used for text.

  CSS variable: `--clerk-color-foreground`

  ***

* `colorPrimaryForeground`
* `string`

  The color used for text on the primary background.

  CSS variable: `--clerk-color-primary-foreground`

  ***

* `colorMutedForeground`
* `string`

  The color used for secondary text.

  CSS variable: `--clerk-color-muted-foreground`

  ***

* `colorMuted`
* `string`

  The color used for muted backgrounds.

  CSS variable: `--clerk-color-muted`

  ***

* `colorBackground`
* `string`

  The background color for the card container.

  CSS variable: `--clerk-color-background`

  ***

* `colorInputForeground`
* `string`

  The color used for text in input fields.

  CSS variable: `--clerk-color-input-foreground`

  ***

* `colorInput`
* `string`

  The background color used for input fields.

  CSS variable: `--clerk-color-input`

  ***

* `colorShimmer`
* `string`

  The color of the avatar shimmer.

  CSS variable: `--clerk-color-shimmer`

  ***

* `colorRing`
* `string`

  The color of the ring when an interactive element is focused.

  CSS variable: `--clerk-color-ring`

  ***

* `colorShadow`
* `string`

  The base shadow color used in the components.

  CSS variable: `--clerk-color-shadow`

  ***

* `colorBorder`
* `string`

  The base border color used in the components.

  CSS variable: `--clerk-color-border`

  ***

* `colorModalBackdrop`
* `string`

  The background color of the modal backdrop.

  CSS variable: `--clerk-color-modal-backdrop`

  ***

* `fontFamily`
* `string`

  The font family used throughout the components. By default, it is set to `inherit`.

  CSS variable: `--clerk-font-family`

  ***

* `fontFamilyButtons`
* `string`

  The font family used for buttons. By default, it is set to `inherit`.

  CSS variable: `--clerk-font-family-buttons`

  ***

* `fontSize`
* `string` | `{xs: string, sm: string, md: string, lg: string, xl: string}`

  The font size used throughout the components. By default, this is set to `0.8125rem`.

  CSS variable: `--clerk-font-size`

  ***

* `fontWeight`
* `{normal: number, medium: number, semibold: number, bold: number}`

  The font weight used throughout the components. By default, this is set to `{normal: 400, medium: 500, semibold: 600, bold: 700}`.

  CSS variable: `--clerk-font-weight`

  ***

* `borderRadius`
* `string`

  The border radius used throughout the components. By default, this is set to `0.375rem`.

  CSS variable: `--clerk-border-radius`

  ***

* `spacing`
* `string`

  The spacing unit used throughout the components. By default, this is set to `1rem`.

  CSS variable: `--clerk-spacing`
</Properties>

### Deprecated properties  {{ toc: false }}

The following properties are deprecated as of 2025-07-15 and will be removed in the next major version of Clerk.

* `colorText` (use `colorForeground` instead)
* `colorTextOnPrimaryBackground` (use `colorPrimaryForeground` instead)
* `colorTextSecondary` (use `colorMutedForeground` instead)
* `spacingUnit` (use `spacing` instead)
* `colorInputText` (use `colorInputForeground` instead)
* `colorInputBackground` (use `colorInput` instead)

## Usage

You can customize Clerk components by passing an object of variables to the `variables` property of the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/overview" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]} code={true}>appearance</SDKLink> prop.

> \[!NOTE browser-compatibility-considerations]
> **Browser Compatibility Considerations**
>
> Clerk's theming system uses modern CSS features like [`color-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color-mix) and [relative color syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_colors/Relative_colors) to automatically generate color variations from your base colors. These features require:
>
> * **`color-mix()`**: Chrome 111+, Firefox 113+, Safari 16.2+
> * **Relative color syntax**: Chrome 119+, Firefox 120+, Safari 16.4+
>
> For broader browser support, when using the `variables` prop, **use direct color values** (e.g. `colorPrimary: '#6c47ff'`) instead of CSS variables or modern color functions.

### Apply `variables` to all Clerk components

<If notSdk={["astro", "js-frontend", "vue", "nuxt", "fastify"]}>
  To apply `variables` to all Clerk components, pass the `appearance` prop to the <SDKLink href="/docs/:sdk:/reference/components/clerk-provider" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>\<ClerkProvider></SDKLink> component. The `appearance` prop accepts the property `variables`.

  In the following example, the primary color is set to blue and the text color is set to black. Since these styles are applied to the SDK's Clerk integration, which wraps the entire application, they will be applied to all Clerk components that use the primary or text color.

  ```tsx {{ mark: [[3, 6]] }}
  <ClerkProvider
    appearance={{
      variables: {
        colorPrimary: '#0000ff', // blue
        colorForeground: '#000000', // black
      },
    }}
  >
    {/* ... */}
  </ClerkProvider>
  ```

</If>

### Apply `variables` to all instances of a Clerk component

To customize all instances of a Clerk component, you can pass the name of the Clerk component itself to the `appearance` prop.

In the following example, the primary color is set to blue and the text color is set to black for all instances of the <SDKLink href="/docs/:sdk:/reference/components/authentication/sign-in" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<SignIn /></SDKLink> component.

<If notSdk={["astro", "js-frontend", "vue", "nuxt", "fastify"]}>

  ```tsx {{ mark: [[3, 8]] }}
  <ClerkProvider
    appearance={{
      signIn: {
        variables: {
          colorPrimary: '#0000ff', // blue
          colorForeground: '#000000', // black
        },
      },
    }}
  >
    {/* ... */}
  </ClerkProvider>
  ```

</If>

### Apply `variables` to a single Clerk component

To customize a single Clerk component, pass the `variables` property to the `appearance` prop of the Clerk component.

The following example shows how to customize the <SDKLink href="/docs/:sdk:/reference/components/authentication/sign-in" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<SignIn /></SDKLink> component by setting the primary color to blue and the text color to black.

<If notSdk={["vue", "nuxt"]}>

  ```tsx {{ mark: [[3, 6]] }}
  <SignIn
    appearance={{
      variables: {
        colorPrimary: '#0000ff', // blue
        colorForeground: '#000000', // black
      },
    }}
  />
  ```

</If>

### Using CSS variables

> \[!WARNING]
> Please consider this approach with browser compatibility in mind, as it may not work in older browsers. See <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/variables#browser-compatibility-considerations" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Browser Compatibility Considerations</SDKLink> for details.

You can also use CSS variables to customize the appearance of Clerk components. This approach is particularly useful when:

* You have a pre-defined design system with CSS custom properties
* You want to support automatic dark/light mode switching
* You need to dynamically update colors based on user preferences
* You're integrating Clerk into an existing application with established CSS variables

The following example demonstrates how to use CSS variables to customize the appearance of Clerk components, but for maximum browser compatibility, it's recommended to use direct color values instead.

Use the following tabs to view the code necessary for each file.

<If notSdk={["astro", "js-frontend", "vue", "nuxt"]}>
  <CodeBlockTabs options={["layout.tsx", "global.css"]}>
    ```tsx {{ mark: [4] }}
    <ClerkProvider
      appearance={{
        variables: {
          colorPrimary: 'var(--brand-primary)',
        },
      }}
    >
      {/* ... */}
    </ClerkProvider>
    ```

    ```css
    :root {
      --brand-primary: oklch(49.1% 0.27 292.581);
    }

    @media (prefers-color-scheme: dark) {
      :root {
        --brand-primary: oklch(54.1% 0.281 293.009);
      }
    }
    ```
  </CodeBlockTabs>
</If>

### Clerk CSS variables

Clerk exposes native CSS variables if you would prefer to define variables directly in your application's stylesheet. All variables exposed through the `appearance` object are also exposed as CSS variables; see the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/variables#properties" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>properties</SDKLink> section for a list of the available variables.

The Clerk CSS variables are prefixed with `clerk-` and are in kebab-case:

```css
:root {
  --clerk-color-primary: #0000ff; /* colorPrimary */
  --clerk-color-foreground: #000000; /* colorForeground */
}
```
