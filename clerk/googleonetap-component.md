---
title: "`<GoogleOneTap />` component"
description: Clerk's <GoogleOneTap /> component renders a UI for authenticating
  users with Google's One Tap API.
sdk: astro, expo, nextjs, nuxt, react, react-router, remix,
  tanstack-react-start, vue, js-frontend
sdkScoped: "true"
canonical: /docs/:sdk:/reference/components/authentication/google-one-tap
lastUpdated: 2025-12-11T21:01:08.000Z
availableSdks: astro,expo,nextjs,nuxt,react,react-router,remix,tanstack-react-start,vue,js-frontend
notAvailableSdks: chrome-extension,android,ios,expressjs,fastify,go,ruby,js-backend
activeSdk: nextjs
sourceFile: /docs/reference/components/authentication/google-one-tap.mdx
---

> \[!IMPORTANT]
> To use Google One Tap with Clerk, you must [enable Google as a social connection in the Clerk Dashboard](/docs/guides/configure/auth-strategies/social-connections/google#configure-for-your-production-instance) and make sure to use custom credentials.

The `<GoogleOneTap />` component renders the [Google One Tap](https://developers.google.com/identity/gsi/web/guides/features) UI so that users can use a single button to sign-up or sign-in to your Clerk application with their Google accounts.

By default, this component will redirect users back to the page where the authentication flow started. However, you can override this with <SDKLink href="/docs/:sdk:/reference/components/authentication/google-one-tap#properties" sdks={["astro","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>force redirect URL props</SDKLink> or [force redirect URL environment variables](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects).

> \[!TIP]
> `<GoogleOneTap>` does not render if the user is already signed into your Clerk application, so there's no need to manually check if a user is signed in yourself before rendering it.

<If sdk={["astro", "expo", "nextjs", "nuxt", "react", "react-router", "remix", "tanstack-react-start", "vue"]}>

## Example

  The following example includes basic implementation of the `<GoogleOneTap />` component. You can use this as a starting point for your own implementation.

  <If sdk="nextjs">
    ```tsx {{ filename: 'app/sign-in/[[...sign-in]]/page.tsx' }}
    import { GoogleOneTap } from '@clerk/nextjs'

    export default function Page() {
      return <GoogleOneTap />
    }
    ```
  </If>
</If>

## Properties

<Properties>
  * `cancelOnTapOutside?`
  * `boolean`

  If `true`, the One Tap prompt closes automatically if the user clicks outside of the prompt. Defaults to `true`.

  ***

* `itpSupport?`
* `boolean`

  If `true`, enables the [ITP-specific UX](https://developers.google.com/identity/gsi/web/guides/itp) when One Tap is rendered on ITP browsers such as Chrome on iOS, Safari, and FireFox. Defaults to `true`.

  ***

* `fedCmSupport?`
* `boolean`

  If `true`, enables Google One Tap to use [the FedCM API](https://developers.google.com/privacy-sandbox/3pcd/fedcm) to sign users in. See Google's docs on [best practices when disabling FedCM support](https://developers.google.com/identity/gsi/web/guides/display-google-one-tap#do_not_cover_google_one_tap). Defaults to `true`

  ***

* `signInForceRedirectUrl?`
* `string`

  Useful if you want to redirect to a path specific to Google One Tap users. If provided, this URL will **always** be redirected to after the user signs in, overriding any <SDKLink href="/docs/:sdk:/reference/components/clerk-provider#properties" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>\<ClerkProvider> redirect URL props</SDKLink> or [redirect URL environment variables](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects).

  ***

* `signUpForceRedirectUrl?`
* `string`

  Useful if you want to redirect to a path specific to Google One Tap users. If provided, this URL will **always** be redirected to after the user signs up, overriding any <SDKLink href="/docs/:sdk:/reference/components/clerk-provider#properties" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>\<ClerkProvider> redirect URL props</SDKLink> or [redirect URL environment variables](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects).
</Properties>

## Limitations

* If your application will use the Google API on behalf of your users, the `<GoogleOneTap>` component is not recommended, as Google does not provide Clerk with an access or refresh token that you can use.
* Users with the 1Password browser extension may not be able to render the Google One Tap UI. They must disable this extension.
* When testing in development, if you select the `X` button to close the Google One Tap UI, you may encounter [a cooldown](https://developers.google.com/identity/gsi/web/guides/features#exponential_cooldown) that prevents you from rendering it again for a period of time. To bypass the cooldown, remove the `g_state` cookie.
