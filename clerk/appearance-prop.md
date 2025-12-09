---
title: "`Appearance` prop"
description: Utilize Clerk's appearance property in order to share styles across
  every component or individually to any of the Clerk components.
sdk: astro, chrome-extension, expo, nextjs, nuxt, react, react-router, remix,
  tanstack-react-start, vue, js-frontend, fastify, expressjs, js-backend, go,
  ruby, android
sdkScoped: "true"
canonical: /docs/:sdk:/guides/customizing-clerk/appearance-prop/overview
lastUpdated: 2025-12-03T22:33:41.000Z
availableSdks: astro,chrome-extension,expo,nextjs,nuxt,react,react-router,remix,tanstack-react-start,vue,js-frontend,fastify,expressjs,js-backend,go,ruby,android
notAvailableSdks: ios
activeSdk: nextjs
sourceFile: /docs/guides/customizing-clerk/appearance-prop/overview.mdx
---

{/*JS file: <https://github.com/clerk/javascript/blob/main/packages/types/src/appearance.ts#L619>*/}

Customizing the appearance of Clerk components is a powerful way to make your application look and feel unique. Clerk provides a way to customize the appearance of its components using the `appearance` prop.

The `appearance` prop can be used to share styles across every component, or applied individually to any of the Clerk components. When using it for global styling, the prop is available wherever you initialize the Clerk integration. For most SDKs, this means applying it to the <SDKLink href="/docs/:sdk:/reference/components/clerk-provider" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>\<ClerkProvider></SDKLink> component, while in others, it's configured through the SDK's Clerk integration or plugin.

This applies to all of the React-based packages, like <SDKLink href="/docs/nextjs/getting-started/quickstart" sdks={["nextjs","react","js-frontend","chrome-extension","expo","android","ios","expressjs","fastify","react-router","remix","tanstack-react-start","go","astro","nuxt","vue","ruby","js-backend"]}>Next.js</SDKLink>, as well as <SDKLink href="/docs/reference/javascript/overview" sdks={["js-frontend"]}>the pure JavaScript ClerkJS package</SDKLink>.

## Properties

The `appearance` prop accepts the following properties:

<Properties>
  * `theme?`
  * `BaseTheme | BaseTheme[]`

  A theme used as the base theme for the components. For more information, see <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/themes" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Themes</SDKLink>.

  ***

* `layout?`
* `Layout`

  Configuration options that affect the layout of the components, allowing customizations that are hard to implement with just CSS. For more information, see <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/layout" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Layout</SDKLink>.

  ***

* `variables?`
* `Variables`

  General theme overrides. This styles will be merged with our base theme. Can override global styles like colors, fonts, etc. For more information, see <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/variables" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Variables</SDKLink>.

  ***

* `elements?`
* `Elements`

  Fine-grained theme overrides. Useful when you want to style specific elements or elements that are under a specific state. For more information, see the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/overview#customize-elements-of-a-clerk-component" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Customize elements of a Clerk component</SDKLink> section.

  ***

* `captcha?`
* `Captcha`

  Configuration options that affect the appearance of the CAPTCHA widget. For more information, see the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/captcha" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>dedicated guide</SDKLink>.

  ***

* `cssLayerName?`
* `string`

  The name of the CSS layer for Clerk component styles. This is useful for advanced CSS customization, allowing you to control the cascade and prevent style conflicts by isolating Clerk's styles within a specific layer. For more information on CSS layers, see the [MDN documentation on @layer](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer).
</Properties>

## Using a prebuilt theme

Clerk offers a set of prebuilt themes that can be used to quickly style Clerk components. See the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/themes" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Themes</SDKLink> docs for more information.

## Customize the layout

The `layout` property is used to adjust the layout of the <SDKLink href="/docs/:sdk:/reference/components/authentication/sign-in" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<SignIn/></SDKLink> and <SDKLink href="/docs/:sdk:/reference/components/authentication/sign-up" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<SignUp/></SDKLink> components, as well as set important links to your support, terms, and privacy pages. See the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/layout" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Layout</SDKLink> docs for more information.

## Customize the base theme

The `variables` property is used to adjust the general styles of a component's base theme, like colors, backgrounds, and typography. See the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/variables" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Variables</SDKLink> docs for more information.

## Customize elements of a Clerk component

If you want full control over the appearance of a Clerk component, you can target the underlying elements by using their CSS classes and then apply your own styles.

First, you need to identify the underlying element of the Clerk component you want to style. You can do this by **inspecting** the HTML of the component.

For example, if you want to style the primary button in a Clerk component, you can right-click on the primary button and select "Inspect" from the menu. This will open the browser's developer tools and highlight the element in the HTML, as shown in the following image:

![The inspect element tab opened with an element selected. It shows a list of classes and a lock icon in between human-readable classnames and randomly generated ones](/docs/images/customization/identifying_elements.png)

When you select an element that is part of a Clerk component, you'll notice a list of classes like so:

```html
cl-formButtonPrimary cl-button 🔒️ cl-internal-1ta0xpz
```

Any of the classes listed before the lock icon (🔒️) are safe to rely on, such as `cl-formButtonPrimary` or `cl-button` from the previous example. You'll use these classes to target the necessary elements of the Clerk component.

> \[!NOTE]
> Anything after the lock icon (🔒️) are internal classes used for Clerk's internal styling and should not be modified.

Once you have identified the classes of the element you want to target, there are many ways to apply your custom styles depending on your preference:

1. <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/overview#use-global-css-to-style-clerk-components" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Use global CSS styling</SDKLink>
2. <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/overview#use-custom-css-classes-to-style-clerk-components" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Pass custom CSS classes</SDKLink>
   * <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/overview#use-tailwind-classes-to-style-clerk-components" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Using Tailwind</SDKLink>
   * <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/overview#use-css-modules-to-style-clerk-components" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Using CSS modules</SDKLink>
3. <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/overview#use-inline-css-objects-to-style-clerk-components" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby","android"]}>Pass inline CSS to your Clerk options</SDKLink>

### Use global CSS to style Clerk components

You can style the elements of a Clerk component with global CSS.

For this example, say you want to style the primary button in a Clerk component. You inspect the primary button to find the classes that you can use to target the element:

```html
cl-formButtonPrimary cl-button 🔒️ cl-internal-1ta0xpz
```

You can then create a global CSS file, use the classes you identified to target the primary button, and apply your custom styles. In this case, `cl-formButtonPrimary` is the class you want to use because it's specific to the primary button:

```css {{ filename: 'styles/global.css' }}
.cl-formButtonPrimary {
  font-size: 14px;
  text-transform: none;
  background-color: #611bbd;
}

.cl-formButtonPrimary:hover,
.cl-formButtonPrimary:focus,
.cl-formButtonPrimary:active {
  background-color: #49247a;
}
```

### Use custom CSS classes to style Clerk components

You can pass additional classes to Clerk component elements by using the `elements` property on the `appearance` prop.

For example, an element in a Clerk component will have classes that look something like this:

```html
cl-formButtonPrimary cl-button 🔒️ cl-internal-1ta0xpz
```

Remove the `cl-` prefix from a class and use it as the key for a new object in the `elements` property. The value of this object should be the string of classes you want to apply to the element.

The following example shows how to style the primary button in a `<SignIn />` component with custom CSS classes:

<If notSdk={["vue", "nuxt"]}>

  ```tsx {{ mark: [4] }}
  <SignIn
    appearance={{
      elements: {
        formButtonPrimary: 'your-org-button org-red-button',
      },
    }}
  />
  ```

</If>

#### Use Tailwind classes to style Clerk components

To use Tailwind CSS v4, you must set the `cssLayerName` property to ensure that Tailwind's utility styles are applied after Clerk's styles.

<If notSdk={["astro", "js-frontend", "vue", "nuxt"]}>
  It's recommended to add this to the <SDKLink href="/docs/:sdk:/reference/components/clerk-provider" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>\<ClerkProvider></SDKLink> that wraps your app so that it's applied to all Clerk components, as shown in the following example. The example names the layer `clerk` but you can name it anything you want.

  Use the following tabs to view the code necessary for each file.

  <CodeBlockTabs options={["layout.tsx", "global.css"]}>
    ```tsx {{ mark: ["cssLayerName: 'clerk'"] }}
    <ClerkProvider
      appearance={{
        cssLayerName: 'clerk',
      }}
    >
      {/* ... */}
    </ClerkProvider>
    ```

    ```css {{ mark: ['clerk'] }}
    @layer theme, base, clerk, components, utilities;
    @import 'tailwindcss';
    ```
  </CodeBlockTabs>
</If>

Then, you can use Tailwind's classes to style the elements of the Clerk component. The following example shows how to use Tailwind classes to style the primary button in a `<SignIn />` component:

<If notSdk={["vue", "nuxt"]}>

  ```tsx {{ mark: [4] }}
  <SignIn
    appearance={{
      elements: {
        formButtonPrimary: 'bg-slate-500 hover:bg-slate-400 text-sm',
      },
    }}
  />
  ```

</If>

#### Use CSS modules to style Clerk components

CSS modules are a great way to scope your CSS to a specific component.

Create your module file and add the CSS you want to apply, as shown in the following example for the `<SignIn />` component:

```css {{ filename: 'styles/SignIn.module.css' }}
.primaryColor {
  background-color: bisque;
  color: black;
}
```

Then you can apply this by importing the file and using the classes whenever required:

<If notSdk={["vue", "nuxt"]}>

  ```tsx {{ mark: [1, 8] }}
  import styles from '../styles/SignIn.module.css'

  export default function CustomSignIn() {
    return (
      <SignIn
        appearance={{
          elements: {
            formButtonPrimary: styles.primaryColor,
          },
        }}
      />
    )
  }
  ```

</If>

### Use inline CSS objects to style Clerk components

You can style the elements of a Clerk component with inline CSS objects.

The following example shows how to style the primary button in a `<SignIn />` component with an inline CSS object:

<If notSdk={["vue", "nuxt"]}>

  ```tsx {{ mark: [[4, 11]] }}
  <SignIn
    appearance={{
      elements: {
        formButtonPrimary: {
          fontSize: 14,
          textTransform: 'none',
          backgroundColor: '#611BBD',
          '&:hover, &:focus, &:active': {
            backgroundColor: '#49247A',
          },
        },
      },
    }}
  />
  ```

</If>

## Next steps

Here are a few resources you can utilize to customize your Clerk components further:

<Cards>
  * [Localization](/docs/guides/customizing-clerk/localization)
  * Learn how to localize your Clerk components.

  ***

* [Prebuilt themes](/docs/guides/customizing-clerk/appearance-prop/themes)
* Explore the prebuilt themes that you can use to quickly style your Clerk components.

  ***

* [Customize layouts](/docs/guides/customizing-clerk/appearance-prop/layout)
* Learn how to change the layout and links of your Clerk components.
</Cards>
