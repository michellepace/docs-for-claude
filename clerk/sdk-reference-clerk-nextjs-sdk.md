---
title: Clerk Next.js SDK
description: The Clerk Next.js SDK gives you access to prebuilt components,
  React hooks, and helpers to make user authentication easier.
sdk: nextjs
sdkScoped: "true"
canonical: /docs/reference/nextjs/overview
lastUpdated: 2025-12-01T23:27:52.000Z
availableSdks: nextjs
notAvailableSdks: react,js-frontend,chrome-extension,expo,android,ios,expressjs,fastify,react-router,remix,tanstack-react-start,go,astro,nuxt,vue,ruby,js-backend
activeSdk: nextjs
sourceFile: /docs/reference/nextjs/overview.mdx
---

The Clerk Next.js SDK gives you access to prebuilt components, React hooks, and helpers to make user authentication easier. Refer to the <SDKLink href="/docs/nextjs/getting-started/quickstart" sdks={["nextjs","react","js-frontend","chrome-extension","expo","android","ios","expressjs","fastify","react-router","remix","tanstack-react-start","go","astro","nuxt","vue","ruby","js-backend"]}>quickstart guide</SDKLink> to get started.

## `clerkMiddleware()`

The `clerkMiddleware()` helper integrates Clerk authentication into your Next.js application through middleware. It allows you to integrate authorization into both the client and server of your application. You can [learn more here](/docs/reference/nextjs/clerk-middleware).

## Client-side helpers

Because the Next.js SDK is built on top of the Clerk React SDK, you can use the hooks that the React SDK provides. These hooks include access to the <SDKLink href="/docs/reference/javascript/clerk" sdks={["js-frontend"]} code={true}>Clerk</SDKLink> object, <SDKLink href="/docs/reference/javascript/user" sdks={["js-frontend"]} code={true}>User object</SDKLink>, <SDKLink href="/docs/reference/javascript/organization" sdks={["js-frontend"]} code={true}>Organization object</SDKLink>, and a set of useful helper methods for signing in and signing up.

* <SDKLink href="/docs/:sdk:/reference/hooks/use-user" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>useUser()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-clerk" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>useClerk()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-auth" sdks={["astro","chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>useAuth()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-sign-in" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>useSignIn()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-sign-up" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>useSignUp()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-session" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>useSession()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-session-list" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>useSessionList()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-organization" sdks={["chrome-extension","expo","nextjs","react","react-router","remix","tanstack-react-start"]} code={true}>useOrganization()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-organization-list" sdks={["chrome-extension","expo","nextjs","react","react-router","remix","tanstack-react-start"]} code={true}>useOrganizationList()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-reverification" sdks={["chrome-extension","expo","nextjs","react","react-router","remix","tanstack-react-start"]} code={true}>useReverification()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-checkout" sdks={["nextjs","react"]} code={true}>useCheckout()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-payment-element" sdks={["nextjs","react"]} code={true}>usePaymentElement()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-payment-methods" sdks={["nextjs","react"]} code={true}>usePaymentMethods()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-plans" sdks={["nextjs","react"]} code={true}>usePlans()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-subscription" sdks={["nextjs","react"]} code={true}>useSubscription()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-statements" sdks={["nextjs","react"]} code={true}>useStatements()</SDKLink>
* <SDKLink href="/docs/:sdk:/reference/hooks/use-payment-attempts" sdks={["nextjs","react"]} code={true}>usePaymentAttempts()</SDKLink>

## Server-side helpers

### App router

Clerk provides first-class support for the [Next.js App Router](https://nextjs.org/docs/app). The following references show how to integrate Clerk features into apps using the latest App Router and React Server Components features.

* [`auth()`](/docs/reference/nextjs/app-router/auth)
* [`currentUser()`](/docs/reference/nextjs/app-router/current-user)
* [Route Handlers](/docs/reference/nextjs/app-router/route-handlers)
* [Server Actions](/docs/reference/nextjs/app-router/server-actions)

### Pages router

Clerk continues to provide drop-in support for the Next.js Pages Router. In addition to the main Clerk integration, the following references are available for apps using Pages Router.

* [`getAuth()`](/docs/reference/nextjs/pages-router/get-auth)
* [`buildClerkProps()`](/docs/reference/nextjs/pages-router/build-clerk-props)

## `clerkClient`

<SDKLink href="/docs/js-backend/getting-started/quickstart" sdks={["js-backend"]}>Clerk's JS Backend SDK</SDKLink> provides access to Backend API resources and low-level authentication utilities for JavaScript environments. For example, to retrieve a list of all users in your application, you can use the `users.getUserList()` method from the JS Backend SDK instead of manually making a fetch request to the [https://api.clerk.com/v1/users](https://clerk.com/docs/reference/backend-api/tag/users/get/users) endpoint.

All resource operations are mounted as sub-APIs on the `clerkClient` object. See the <SDKLink href="/docs/js-backend/getting-started/quickstart#usage" sdks={["js-backend"]}>reference documentation</SDKLink> for more information.

## `Auth` object

Both `auth()` (App Router) and `getAuth()` (Pages Router) return an `Auth` object. This JavaScript object contains important information like the current user's session ID, user ID, and Organization ID. Learn more about the <SDKLink href="/docs/reference/backend/types/auth-object" sdks={["js-backend"]} code={true}>Auth object</SDKLink>{{ target: '_blank' }}.

## Demo repositories

For examples of Clerk's features, such as user and Organization management, integrated into a single application, see the Next.js demo repositories:

* [Clerk + Next.js App Router Demo](https://github.com/clerk/clerk-nextjs-demo-app-router)
* [Clerk + Next.js Pages Router Demo](https://github.com/clerk/clerk-nextjs-demo-pages-router)
