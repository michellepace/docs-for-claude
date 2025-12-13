---
title: "`<UserProfile />` component"
description: Clerk's <UserProfile /> component is used to render a beautiful,
  full-featured account management UI that allows users to manage their profile
  and security settings.
sdk: astro, chrome-extension, expo, nextjs, nuxt, react, react-router, remix,
  tanstack-react-start, vue, js-frontend
sdkScoped: "true"
canonical: /docs/:sdk:/reference/components/user/user-profile
lastUpdated: 2025-12-11T21:25:35.000Z
availableSdks: astro,chrome-extension,expo,nextjs,nuxt,react,react-router,remix,tanstack-react-start,vue,js-frontend
notAvailableSdks: android,ios,expressjs,fastify,go,ruby,js-backend
activeSdk: nextjs
sourceFile: /docs/reference/components/user/user-profile.mdx
---

![The \<UserProfile /> component renders a full-featured account management UI that allows users to manage their profile and security settings.](/docs/images/ui-components/user-profile.png){{ style: { maxWidth: '100%' } }}

The `<UserProfile />` component is used to render a beautiful, full-featured account management UI that allows users to manage their profile, security, and billing settings.

<If sdk={["astro", "chrome-extension", "expo", "nextjs", "nuxt", "react", "react-router", "remix", "tanstack-react-start", "vue"]}>

## Example

  <If sdk="nextjs">
    The `<UserProfile />` component must be embedded using the [Next.js optional catch-all route](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#optional-catch-all-routes) in order for the routing to work.

    ```jsx {{ filename: 'app/user-profile/[[...user-profile]]/page.tsx' }}
    import { UserProfile } from '@clerk/nextjs'

    const UserProfilePage = () => <UserProfile />

    export default UserProfilePage
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

* `routing`
* `'hash' | 'path'`

  The [routing](/docs/guides/how-clerk-works/routing) strategy for your pages. Defaults to `'path'` for frameworks that handle routing, such as Next.js and Remix. Defaults to `hash` for all other SDK's, such as React.

  ***

* `path`
* `string`

  The path where the component is mounted on when `routing` is set to `path`. It is ignored in hash-based routing. For example: `/user-profile`.

  ***

* `additionalOAuthScopes`
* `object`

  Specify additional scopes per OAuth provider that your users would like to provide if not already approved.  For example: `{google: ['foo', 'bar'], github: ['qux']}`.

  ***

* `customPages`
* <code><SDKLink href="/docs/reference/javascript/types/custom-page" sdks={["js-frontend"]}>CustomPage</SDKLink>\[]</code>

  An array of custom pages to add to the user profile. Only available for the <SDKLink href="/docs/reference/javascript/overview" sdks={["js-frontend"]}>JavaScript SDK</SDKLink>. To add custom pages with React-based SDK's, see the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/adding-items/user-profile" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>dedicated guide</SDKLink>.

  ***

* `fallback?`
* `ReactNode`

  An optional element to be rendered while the component is mounting.
</Properties>

## Customization

To learn about how to customize Clerk components, see the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/overview" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby"]}>customization documentation</SDKLink>.

In addition, you also can add custom pages and links to the `<UserProfile />` navigation sidenav. For more information, refer to the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/adding-items/user-profile" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>Custom Pages documentation</SDKLink>.
