---
title: "`captcha` prop"
description: Utilize Clerk's `captcha` prop in order to change the appearance of
  the CAPTCHA widget.
sdk: astro, chrome-extension, expo, nextjs, nuxt, react, react-router, remix,
  tanstack-react-start, vue, js-frontend, fastify, expressjs, js-backend, go,
  ruby, android
sdkScoped: "true"
canonical: /docs/:sdk:/guides/customizing-clerk/appearance-prop/captcha
lastUpdated: 2025-12-03T22:33:41.000Z
availableSdks: astro,chrome-extension,expo,nextjs,nuxt,react,react-router,remix,tanstack-react-start,vue,js-frontend,fastify,expressjs,js-backend,go,ruby,android
notAvailableSdks: ios
activeSdk: nextjs
sourceFile: /docs/guides/customizing-clerk/appearance-prop/captcha.mdx
---

{/*JS file: <https://github.com/clerk/javascript/blob/main/packages/types/src/appearance.ts#L538>*/}

The `captcha` property can be used to change the appearance of the CAPTCHA widget.

## Properties

<Properties>
  * `theme`
  * `'auto' | 'light' | 'dark'`

  The CAPTCHA widget theme. Defaults to `auto`.

  ***

* `size`
* `'normal' | 'flexible' | 'compact'`

  The CAPTCHA widget size. Defaults to `normal`.

  ***

* `language`
* `string`

  The CAPTCHA widget language/locale. When setting the language for CAPTCHA, this is how localization is prioritized:

* `appearance.captcha.language`: Set by this `language` property.
* `localization.locale`: Set by the [`localization` prop on `<ClerkProvider>`](/docs/guides/customizing-clerk/localization). Some languages are [supported by Clerk](/docs/guides/customizing-clerk/localization) but not by Cloudflare Turnstile, which is used for the CAPTCHA widget. See [Cloudflare Turnstile's supported languages](https://developers.cloudflare.com/turnstile/reference/supported-languages).
* `en-US`: Clerk's default language.
</Properties>

## Usage

<If notSdk={["astro", "js-frontend", "vue", "nuxt", "fastify"]}>
  To customize the CAPTCHA widget, pass the `appearance` prop to the <SDKLink href="/docs/:sdk:/reference/components/clerk-provider" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>\<ClerkProvider></SDKLink> component. The `appearance` prop accepts the property `captcha`, which can be used to apply different changes to the widget.

  In the following example, the CAPTCHA is customized to use the dark theme, a flexible size, and Spanish as the display language.

  ```tsx {{ mark: [[3, 7]] }}
  <ClerkProvider
    appearance={{
      captcha: {
        theme: 'dark',
        size: 'flexible',
        language: 'es-ES',
      },
    }}
  >
    {/* ... */}
  </ClerkProvider>
  ```

</If>
