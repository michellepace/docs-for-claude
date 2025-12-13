---
title: "`<ClerkProvider>`"
description: The <ClerkProvider> component provides session and user context to
  Clerk's hooks and components.
sdk: chrome-extension, expo, nextjs, react, react-router, tanstack-react-start
sdkScoped: "true"
canonical: /docs/:sdk:/reference/components/clerk-provider
lastUpdated: 2025-12-11T21:01:08.000Z
availableSdks: chrome-extension,expo,nextjs,react,react-router,tanstack-react-start
notAvailableSdks: js-frontend,android,ios,expressjs,fastify,remix,go,astro,nuxt,vue,ruby,js-backend
activeSdk: nextjs
sourceFile: /docs/reference/components/clerk-provider.mdx
---

The `<ClerkProvider>` component is required to integrate Clerk into your React application, providing session and user context to Clerk's hooks and components.

The recommended approach is to wrap your entire app with `<ClerkProvider>` at the entry point to make authentication globally accessible. If you only need authentication for specific routes or pieces of your application, render `<ClerkProvider>` deeper in the component tree. This allows you to implement Clerk's functionality precisely where required without impacting the rest of your app.

## Example

`app/layout.tsx`:

```tsx
import React from 'react'
import { ClerkProvider } from '@clerk/nextjs'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <ClerkProvider>
      <html lang="en">
        <body>{children}</body>
      </html>
    </ClerkProvider>
  )
}
```

## Properties

| Property | Type | Description |
| -------- | ---- | ----------- |
| `afterMultiSessionSingleSignOutUrl?` | `null \| string` | The full URL or path to navigate to after signing out the current user is complete. This option applies to [multi-session applications](/docs/guides/secure/session-options#multi-session-applications). |
| ~~`afterSignInUrl?`~~ | `null \| string` | **Deprecated.** Use `signInFallbackRedirectUrl` or `signInForceRedirectUrl` instead. |
| `afterSignOutUrl?` | `null \| string` | Full URL or path to navigate to after successful sign out. |
| ~~`afterSignUpUrl?`~~ | `null \| string` | **Deprecated.** Use `signUpFallbackRedirectUrl` or `signUpForceRedirectUrl` instead. |
| `allowedRedirectOrigins?` | `(string \| RegExp)[]` | An optional array of domains to validate user-provided redirect URLs against. If no match is made, the redirect is considered unsafe and the default redirect will be used with a warning logged in the console. |
| `allowedRedirectProtocols?` | `string[]` | An optional array of protocols to validate user-provided redirect URLs against. If no match is made, the redirect is considered unsafe and the default redirect will be used with a warning logged in the console. |
| `appearance?` | `Appearance<Theme>` | Optional object to style your components. Will only affect Clerk Components and not [Account Portal](/docs/guides/account-portal/overview) pages. |
| `clerkJSUrl?` | `string` | The URL that `@clerk/clerk-js` should be hot-loaded from. |
| `clerkJSVariant?` | `"" \| "headless"` | If your web application only uses Control Components, you can set this value to `'headless'` and load a minimal ClerkJS bundle for optimal page performance. |
| `clerkJSVersion?` | `string` | The npm version for `@clerk/clerk-js`. |
| `domain?` | `string \| (url: URL) => string` | **Required if your application is a satellite application**. Sets the domain of the satellite application. |
| `experimental?` | `{ commerce?: boolean; persistClient?: boolean; rethrowOfflineNetworkErrors?: boolean }` | Enable experimental flags to gain access to new features. These flags are not guaranteed to be stable and may change drastically in between patch or minor versions. |
| `initialState?` | `{ actor?: { sub: string; [key: string]: unknown }; factorVerificationAge?: [number, number]; organization?: OrganizationResource; orgId?: string; orgPermissions?: string[]; orgRole?: string; orgSlug?: string; session?: SessionResource; sessionClaims?: JwtPayload; sessionId?: string; sessionStatus?: SessionStatusClaim; user?: UserResource; userId?: string }` | Provide an initial state of the Clerk client during server-side rendering. You don't need to set this value yourself unless you're [developing an SDK](/docs/guides/development/sdk-development/overview). |
| `isSatellite?` | `boolean \| (url: URL) => boolean` | A boolean that indicates whether the application is a satellite application. |
| `localization?` | [`LocalizationResource`](/docs/guides/customizing-clerk/localization) | Optional object to localize your components. Will only affect Clerk Components and not [Account Portal](/docs/guides/account-portal/overview) pages. |
| `newSubscriptionRedirectUrl?` | `null \| string` | The URL to navigate to after the user completes the checkout and clicks the "Continue" button. |
| `nonce?` | `string` | This nonce value will be passed through to the `@clerk/clerk-js` script tag. Use it to implement a [strict-dynamic CSP](/docs/guides/secure/best-practices/csp-headers#implementing-a-strict-dynamic-csp). Requires the `dynamic` prop to also be set. |
| `proxyUrl?` | `string \| (url: URL) => string` | **Required for applications that run behind a reverse proxy**. The URL that Clerk will proxy requests to. Can be either a relative path (`/__clerk`) or a full URL (`https://<your-domain>/__clerk`). |
| `publishableKey` | `string` | The Clerk Publishable Key for your instance. This can be found on the [API keys](https://dashboard.clerk.com/last-active?path=api-keys) page in the Clerk Dashboard. |
| ~~`redirectUrl?`~~ | `null \| string` | **Deprecated.** Use `signInFallbackRedirectUrl`, `signInForceRedirectUrl`, `signUpFallbackRedirectUrl`, or `signUpForceRedirectUrl` instead. |
| `routerPush?` | `(to: string, metadata?: { windowNavigate: (to: string \| URL) => void }) => unknown` | A function which takes the destination path as an argument and performs a "push" navigation. |
| `routerReplace?` | `(to: string, metadata?: { windowNavigate: (to: string \| URL) => void }) => unknown` | A function which takes the destination path as an argument and performs a "replace" navigation. |
| `sdkMetadata?` | `{ environment?: string; name: string; version: string }` | Contains information about the SDK that the host application is using. You don't need to set this value yourself unless you're [developing an SDK](/docs/guides/development/sdk-development/overview). |
| `sdkMetadata.environment?` | `string` | Typically this will be the `NODE_ENV` that the SDK is currently running in. |
| `sdkMetadata.name` | `string` | The npm package name of the SDK. |
| `sdkMetadata.version` | `string` | The npm package version of the SDK. |
| `selectInitialSession?` | `(client: ClientResource) => null \| SignedInSessionResource` | By default, the last signed-in session is used during client initialisation. This option allows you to override that behaviour, e.g. by selecting a specific session. |
| `signInFallbackRedirectUrl?` | `null \| string` | The fallback URL to redirect to after the user signs in, if there's no `redirect_url` in the path already. It's recommended to use the [environment variable](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead. Defaults to `'/'`. |
| `signInForceRedirectUrl?` | `null \| string` | This URL will always be redirected to after the user signs in. It's recommended to use the [environment variable](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead. |
| `signInUrl?` | `string` | This URL will be used for any redirects that might happen and needs to point to your primary application on the client-side. This option is optional for production instances. **It is required to be set for a satellite application in a development instance**. It's recommended to use [the environment variable](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead. |
| `signUpFallbackRedirectUrl?` | `null \| string` | The fallback URL to redirect to after the user signs up, if there's no `redirect_url` in the path already. It's recommended to use the [environment variable](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead. Defaults to `'/'`. |
| `signUpForceRedirectUrl?` | `null \| string` | This URL will always be redirected to after the user signs up. It's recommended to use the [environment variable](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead. |
| `signUpUrl?` | `string` | This URL will be used for any redirects that might happen and needs to point to your primary application on the client-side. This option is optional for production instances but **must be set for a satellite application in a development instance**. It's recommended to use [the environment variable](/docs/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead. |
| `standardBrowser?` | `boolean` | By default, ClerkJS is loaded with the assumption that cookies can be set (browser setup). On native platforms this value must be set to `false`. |
| `supportEmail?` | `string` | Optional support email for display in authentication screens. Will only affect Clerk Components and not [Account Portal](/docs/guides/account-portal/overview) pages. |
| `taskUrls?` | `Partial<Record<"choose-organization" \| "reset-password", string>>` | Customise the URL paths users are redirected to after sign-in or sign-up when specific session tasks need to be completed. When `undefined`, it uses Clerk's default task flow URLs. Defaults to `undefined`. |
| `telemetry?` | `false \| { debug?: boolean; disabled?: boolean; perEventSampling?: boolean }` | Controls whether or not Clerk will collect [telemetry data](/docs/guides/how-clerk-works/security/clerk-telemetry). If set to `debug`, telemetry events are only logged to the console and not sent to Clerk. |
| `touchSession?` | `boolean` | By default, the [Clerk Frontend API `touch` endpoint](/docs/reference/frontend-api/tag/Sessions#operation/touchSession) is called during page focus to keep the last active session alive. This option allows you to disable this behaviour. |
| `waitlistUrl?` | `string` | The full URL or path to the waitlist page. If `undefined`, will redirect to the [Account Portal waitlist page](/docs/guides/account-portal/overview#waitlist). |

## SDK-specific properties

### Next.js

| Property | Type | Description |
| -------- | ---- | ----------- |
| `dynamic` | `boolean` | Indicates whether or not Clerk should make dynamic auth data available based on the current request. Defaults to `false`. Opts the application into dynamic rendering when `true`. For more information, see [Next.js rendering modes and Clerk](/docs/guides/development/rendering-modes). |

### Chrome Extension

| Property | Type | Description |
| -------- | ---- | ----------- |
| `syncHost` | `string` | To enable, pass the URL of the web application that the extension will sync the authentication state from. See the dedicated guide for more information. |
