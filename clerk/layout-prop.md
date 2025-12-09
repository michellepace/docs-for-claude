---
title: "`Layout` prop"
description: Utilize Clerk's layout prop in order to change the layout of the
  <SignIn /> and <SignUp /> components, as well as set important links to your
  support, terms and privacy pages.
sdk: astro, chrome-extension, expo, nextjs, nuxt, react, react-router, remix,
  tanstack-react-start, vue, js-frontend, fastify, expressjs, js-backend, go,
  ruby, android
sdkScoped: "true"
canonical: /docs/:sdk:/guides/customizing-clerk/appearance-prop/layout
lastUpdated: 2025-12-03T22:33:41.000Z
availableSdks: astro,chrome-extension,expo,nextjs,nuxt,react,react-router,remix,tanstack-react-start,vue,js-frontend,fastify,expressjs,js-backend,go,ruby,android
notAvailableSdks: ios
activeSdk: nextjs
sourceFile: /docs/guides/customizing-clerk/appearance-prop/layout.mdx
---

{/*JS file: <https://github.com/clerk/javascript/blob/main/packages/types/src/appearance.ts#L538>*/}

The `layout` property can be used to change the layout of the <SDKLink href="/docs/:sdk:/reference/components/authentication/sign-in" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<SignIn/></SDKLink> and <SDKLink href="/docs/:sdk:/reference/components/authentication/sign-up" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<SignUp/></SDKLink> components, as well as set important links to your support, terms, and privacy pages.

## Properties

<Properties>
  * `animations`
  * `boolean`

  Whether to enable animations inside the components. Defaults to `true`.

  ***

* `helpPageUrl`
* `string`

  The URL to your help page.

  ***

* `logoImageUrl`
* `string`

  The URL to your logo image. By default, the components will use the logo you've set in the Clerk Dashboard. This option is helpful when you need to display different logos for different themes, for example: white logo on dark themes, black logo on light themes.

  ***

* `logoLinkUrl`
* `string`

  Controls where the browser will redirect to after the user clicks the application logo. If a URL is provided, it will be used as the `href` of the link. If a value is not passed in, the components will use the Home URL as set in the Clerk Dashboard. Defaults to `undefined`.

  ***

* `logoPlacement`
* `'inside' | 'outside'`

  The placement of your logo. Defaults to `'inside'`.

  ***

* `privacyPageUrl`
* `string`

  The URL to your privacy page.

  ***

* `shimmer`
* `boolean`

  This option enables the shimmer animation for the avatars of `<UserButton />` and `<OrganizationSwitcher />`. Defaults to `true`.

  ***

* `showOptionalFields`
* `boolean`

  Whether to show optional fields on the sign in and sign up forms. Defaults to `true`.

  ***

* `socialButtonsPlacement`
* `'bottom' | 'top'`

  The placement of your social buttons. Defaults to `'top'`.

  ***

* `socialButtonsVariant`
* `'blockButton' | 'iconButton' | 'auto'`

  The variant of your social buttons. By default, the components will use `blockButton` if you have less than 3 social providers enabled, otherwise `iconButton` will be used.

  ***

* `termsPageUrl`
* `string`

  The URL to your terms page.

  ***

* `unsafe_disableDevelopmentModeWarnings`
* `boolean`

  Whether development warnings show up in development mode. **Only enable this if you want to preview how the components will look in production.**
</Properties>

## Usage

<If notSdk={["astro", "js-frontend", "vue", "nuxt", "fastify"]}>
  To make changes to the layout, pass the `appearance` prop to the <SDKLink href="/docs/:sdk:/reference/components/clerk-provider" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>\<ClerkProvider></SDKLink> component. The `appearance` prop accepts the property `layout`, which can be used to apply different changes to the widget.

  In the following example, the layout is customized so that social buttons appear at the bottom, use the icon style, and the terms page directs to a custom URL.

  ```tsx {{ mark: [[3, 7]] }}
  <ClerkProvider
    appearance={{
      layout: {
        socialButtonsPlacement: 'bottom',
        socialButtonsVariant: 'iconButton',
        termsPageUrl: 'https://clerk.com/terms',
      },
    }}
  >
    {/* ... */}
  </ClerkProvider>
  ```

</If>
