---
title: "`<UserButton />` component"
description: Clerk's <UserButton /> component is used to render the familiar
  user button UI popularized by Google.
search:
  rank: 1
sdk: astro, chrome-extension, expo, nextjs, nuxt, react, react-router, remix,
  tanstack-react-start, vue, js-frontend
sdkScoped: "true"
canonical: /docs/:sdk:/reference/components/user/user-button
lastUpdated: 2025-12-11T21:25:35.000Z
availableSdks: astro,chrome-extension,expo,nextjs,nuxt,react,react-router,remix,tanstack-react-start,vue,js-frontend
notAvailableSdks: android,ios,expressjs,fastify,go,ruby,js-backend
activeSdk: nextjs
sourceFile: /docs/reference/components/user/user-button.mdx
---

![The \<UserButton /> component renders the familiar user button UI popularized by Google.](/docs/images/ui-components/user-button.png){{ style: { maxWidth: '436px' } }}

The `<UserButton />` component renders the familiar user button UI popularized by Google. When selected, it opens a dropdown menu with options to manage account settings and sign out. The "Manage account" option launches the <SDKLink href="/docs/:sdk:/reference/components/user/user-profile" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<UserProfile /></SDKLink> component, providing access to profile and security settings.

For users that have [multi-session](/docs/guides/secure/session-options#multi-session-applications) enabled, the `<UserButton />` also allows users to sign into multiple accounts at once and instantly switch between them without the need for a full page reload. Learn more [here](/docs/guides/secure/session-options#multi-session-applications).

<If sdk={["astro", "chrome-extension", "expo", "nextjs", "nuxt", "react", "react-router", "remix", "tanstack-react-start", "vue"]}>

## Example

  In the following example, `<UserButton />` is mounted inside a header component, which is a common pattern on many websites and applications. When the user is signed in, they will see their avatar and be able to open the popup menu.

  <If sdk="nextjs">
    <CodeBlockTabs options={["App Router", "Pages Router"]}>
      ```tsx {{ filename: 'layout.tsx', mark: [8] }}
      import { ClerkProvider, SignedIn, SignedOut, SignInButton, UserButton } from '@clerk/nextjs'

      function Header() {
        return (
          <header style={{ display: 'flex', justifyContent: 'space-between', padding: 20 }}>
            <h1>My App</h1>
            <SignedIn>
              <UserButton />
            </SignedIn>
            <SignedOut>
              <SignInButton />
            </SignedOut>
          </header>
        )
      }

      export default function RootLayout({ children }: { children: React.ReactNode }) {
        return (
          <html lang="en">
            <ClerkProvider>
              <Header />
              {children}
            </ClerkProvider>
          </html>
        )
      }
      ```

      ```tsx {{ filename: 'pages/_app.tsx', mark: [9] }}
      import { ClerkProvider, SignedIn, SignedOut, SignInButton, UserButton } from '@clerk/nextjs'
      import type { AppProps } from 'next/app'

      function Header() {
        return (
          <header style={{ display: 'flex', justifyContent: 'space-between', padding: 20 }}>
            <h1>My App</h1>
            <SignedIn>
              <UserButton />
            </SignedIn>
            <SignedOut>
              <SignInButton />
            </SignedOut>
          </header>
        )
      }

      function MyApp({ pageProps, Component }: AppProps) {
        return (
          <ClerkProvider {...pageProps}>
            <Header />
            <Component {...pageProps} />
          </ClerkProvider>
        )
      }

      export default MyApp
      ```
    </CodeBlockTabs>
  </If>
</If>

## Properties

The `<UserButton />` component accepts the following properties, all of which are **optional**:

<Properties>
  * `afterMultiSessionSingleSignOutUrl` (deprecated)
  * `string`

  **Deprecated. Move `afterMultiSessionSingleSignOutUrl` to <SDKLink href="/docs/:sdk:/reference/components/clerk-provider" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>\<ClerkProvider /></SDKLink>.** The full URL or path to navigate to after signing out from a currently active account in a multi-session app.

  ***

* `afterSignOutUrl` (deprecated)
* `string`

  **Deprecated. Move `afterSignOutUrl` to <SDKLink href="/docs/:sdk:/reference/components/clerk-provider" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>\<ClerkProvider /></SDKLink>.** The full URL or path to navigate to after a successful sign-out.

  ***

* `afterSwitchSessionUrl`
* `string`

  The full URL or path to navigate to after a successful account change in a multi-session app.

  ***

* `appearance`
* <code><SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/overview" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby"]}>Appearance</SDKLink> | undefined</code>

  Optional object to style your components. Will only affect <SDKLink href="/docs/:sdk:/reference/components/overview" sdks={["react","nextjs","js-frontend","chrome-extension","expo","expressjs","fastify","react-router","remix","tanstack-react-start","go","astro","nuxt","vue","ruby","js-backend"]}>Clerk components</SDKLink> and not [Account Portal](/docs/guides/account-portal/overview) pages.

  ***

* `defaultOpen`
* `boolean`

  Controls whether the `<UserButton />` should open by default during the first render.

  ***

* `showName`
* `boolean`

  Controls if the user name is displayed next to the user image button.

  ***

* `signInUrl`
* `string`

  The full URL or path to navigate to when the **Add another account** button is clicked. It's recommended to use [the environment variable](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

  ***

* `userProfileMode`
* `'modal' | 'navigation'`

  Controls whether selecting the **Manage your account** button will cause the <SDKLink href="/docs/:sdk:/reference/components/user/user-profile" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<UserProfile /></SDKLink> component to open as a modal, or if the browser will navigate to the `userProfileUrl` where `<UserProfile />` is mounted as a page. Defaults to: `'modal'`.

  ***

* `userProfileProps`
* `object`

  Specify options for the underlying <SDKLink href="/docs/:sdk:/reference/components/user/user-profile" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<UserProfile /></SDKLink> component. For example: `{additionalOAuthScopes: {google: ['foo', 'bar'], github: ['qux']}}`.

  ***

* `userProfileUrl`
* `string`

  The full URL or path leading to the user management interface.

  ***

* `fallback?`
* `ReactNode`

  An optional element to be rendered while the component is mounting.
</Properties>

## Customization

To learn about how to customize Clerk components, see the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/appearance-prop/overview" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend","fastify","expressjs","js-backend","go","ruby"]}>customization documentation</SDKLink>.

You can also <SDKLink href="/docs/:sdk:/guides/customizing-clerk/adding-items/user-button" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>add custom actions and links to the `<UserButton />` menu</SDKLink>.
