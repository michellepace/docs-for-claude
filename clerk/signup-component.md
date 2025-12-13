---
title: "`<SignUp />` component"
description: Clerk's <SignUp /> component renders a UI for signing up users.
sdk: astro, chrome-extension, expo, nextjs, nuxt, react, react-router, remix,
  tanstack-react-start, vue, js-frontend
sdkScoped: "true"
canonical: /docs/:sdk:/reference/components/authentication/sign-up
lastUpdated: 2025-12-12T23:42:35.000Z
availableSdks: astro,chrome-extension,expo,nextjs,nuxt,react,react-router,remix,tanstack-react-start,vue,js-frontend
notAvailableSdks: android,ios,expressjs,fastify,go,ruby,js-backend
activeSdk: nextjs
sourceFile: /docs/reference/components/authentication/sign-up.mdx
---

![The \<SignUp /> component renders a UI for signing up users.](/docs/images/ui-components/sign-up.png){{ style: { maxWidth: '460px' } }}

The `<SignUp />` component renders a UI for signing up users. The functionality of the `<SignUp />` component is controlled by the instance settings you specify in the [Clerk Dashboard](https://dashboard.clerk.com), such as [sign-in and sign-up options](/docs/guides/configure/auth-strategies/sign-up-sign-in-options) and [social connections](/docs/guides/configure/auth-strategies/social-connections/all-providers). You can further customize your `<SignUp />` component by passing additional <SDKLink href="/docs/:sdk:/reference/components/authentication/sign-up#properties" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>properties</SDKLink> at the time of rendering. The `<SignUp />` component also displays any <Tooltip><TooltipTrigger>session tasks</TooltipTrigger><TooltipContent>**Session tasks** are requirements that users must fulfill in order to complete the authentication process, such as choosing an Organization.</TooltipContent></Tooltip> that are required for the user to complete after signing up.

> \[!NOTE]
> The `<SignUp/>` and `<SignIn/>` components cannot render when a user is already signed in, unless the application allows multiple sessions. If a user is already signed in and the application only allows a single session, Clerk will redirect the user to the Home URL instead.

<If sdk={["astro", "chrome-extension", "expo", "nextjs", "nuxt", "react", "react-router", "remix", "tanstack-react-start", "vue"]}>

## Example

  The following example includes basic implementation of the `<SignUp />` component. You can use this as a starting point for your own implementation.

  <If sdk="nextjs">
    If you would like to create a dedicated `/sign-up` page in your Next.js application, there are a few requirements you must follow. See the <SDKLink href="/docs/nextjs/guides/development/custom-sign-up-page" sdks={["nextjs","react-router","remix","tanstack-react-start"]}>dedicated guide</SDKLink> for more information.

    ```tsx {{ filename: 'app/page.tsx' }}
    'use client'

    import { SignUp, useUser } from '@clerk/nextjs'

    export default function Home() {
      const { isSignedIn } = useUser()

      if (!isSignedIn) {
        return <SignUp />
      }

      return <div>Welcome!</div>
    }
    ```
  </If>
</If>

## Properties

All props are optional.

<Properties>
  * `appearance`
  * <code><SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/overview" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby"]}>Appearance</SDKLink> | undefined</code>

  Optional object to style your components. Will only affect <SDKLink href="/docs/:sdk:/reference/components/overview" sdks={["react","nextjs","js-frontend","chrome-extension","expo","expressjs","fastify","react-router","remix","tanstack-react-start","go","astro","nuxt","vue","ruby","js-backend"]}>Clerk components</SDKLink> and not [Account Portal](/docs/guides/account-portal/overview) pages.

  ***

* `fallback`
* `ReactNode`

  An optional element to be rendered while the component is mounting.

  ***

* `fallbackRedirectUrl`
* `string`

  The fallback URL to redirect to after the user signs up, if there's no `redirect_url` in the path already. Defaults to `/`. It's recommended to use [the environment variable](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

  ***

* `forceRedirectUrl`
* `string`

  If provided, this URL will always be used as the redirect destination after the user signs up. It's recommended to use [the environment variable](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

  ***

* `initialValues`
* <SDKLink href="/docs/reference/javascript/types/sign-up-initial-values" sdks={["js-frontend"]} code={true}>SignUpInitialValues</SDKLink>

  The values used to prefill the sign-up fields with.

  ***

* `oauthFlow`
* `"redirect" | "popup" | "auto"`

  Determines how OAuth authentication is performed. Accepts the following properties:

* `"redirect"`: Redirect to the OAuth provider on the current page.
* `"popup"`: Open a popup window.
* `"auto"`: Choose the best method based on whether the current domain typically requires the `"popup"` flow to correctly perform authentication.

  Defaults to `"auto"`.

  ***

* `path`
* `string`

  The path where the component is mounted on when `routing` is set to `path`. It is ignored in hash-based routing. For example: `/sign-up`.

  ***

* `routing`
* `'hash' | 'path'`

  The [routing](/docs/guides/how-clerk-works/routing) strategy for your pages.  Defaults to `'path'` for frameworks that handle routing, such as Next.js and Remix. Defaults to `hash` for all other SDK's, such as React.

  ***

* `signInFallbackRedirectUrl`
* `string`

  The fallback URL to redirect to after the user signs in, if there's no `redirect_url` in the path already. Used for the 'Already have an account? Sign in' link that's rendered.  Defaults to `/`. It's recommended to use [the environment variable](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

  ***

* `signInForceRedirectUrl?`
* `string`

  If provided, this URL will always be redirected to after the user signs in. Used for the 'Already have an account? Sign in' link that's rendered. It's recommended to use [the environment variable](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

  ***

* `signInUrl`
* `string`

  The full URL or path to the sign-in page. Used for the 'Already have an account? Sign in' link that's rendered. It's recommended to use [the environment variable](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

  ***

* `unsafeMetadata`
* <SDKLink href="/docs/reference/javascript/types/metadata#sign-up-unsafe-metadata" sdks={["js-frontend"]} code={true}>SignUpUnsafeMetadata</SDKLink>

  Metadata that can be read and set from the frontend and the backend. Once the sign-up is complete, the value of this field will be automatically copied to the created user's unsafe metadata (`User.unsafeMetadata`). One common use case is to collect custom information about the user during the sign-up process and store it in this property. Read more about [unsafe metadata](/docs/guides/users/extending#unsafe-metadata).
</Properties>

## Customization

To learn about how to customize Clerk components, see the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/overview" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby"]}>customization documentation</SDKLink>.

If Clerk's prebuilt components don't meet your specific needs or if you require more control over the logic, you can rebuild the existing Clerk flows using the Clerk API. For more information, see the [custom flow guides](/docs/guides/development/custom-flows/overview).
