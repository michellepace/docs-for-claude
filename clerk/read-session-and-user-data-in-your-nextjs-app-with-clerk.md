---
title: Protect content and read user data
description: Learn how to use Clerk's hooks and helpers to protect content and
  read user data in your Next.js application.
metadata:
  title: Read session and user data in your Next.js app with Clerk
sdk: nextjs, expo, react-router, remix, tanstack-react-start, astro, nuxt
sdkScoped: "true"
canonical: /docs/:sdk:/guides/users/reading
lastUpdated: 2025-12-01T23:27:52.000Z
availableSdks: nextjs,expo,react-router,remix,tanstack-react-start,astro,nuxt
notAvailableSdks: react,js-frontend,chrome-extension,android,ios,expressjs,fastify,go,vue,ruby,js-backend
activeSdk: nextjs
sourceFile: /docs/guides/users/reading.mdx
---

Clerk provides a set of [hooks and helpers](/docs/reference/nextjs/overview#client-side-helpers) that you can use to protect content and read user data in your Next.js application. Here are examples of how to use these helpers in both the client and server-side to get you started.

## Server-side

### App Router

[`auth()`](/docs/reference/nextjs/app-router/auth) and [`currentUser()`](/docs/reference/nextjs/app-router/current-user) are App Router-specific helpers that you can use inside of your Route Handlers, Middleware, Server Components, and Server Actions.

* The `auth()` helper will return the <SDKLink href="/docs/reference/backend/types/auth-object" sdks={["js-backend"]} code={true}>Auth</SDKLink> object of the currently active user.
* The `currentUser()` helper will return the <SDKLink href="/docs/reference/backend/types/backend-user" sdks={["js-backend"]} code={true}>Backend User</SDKLink> object of the currently active user, which includes helpful information like the user's name or email address. **It does count towards the [Backend API request rate limit](/docs/guides/how-clerk-works/system-limits)** so it's recommended to use the <SDKLink href="/docs/:sdk:/reference/hooks/use-user" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>useUser()</SDKLink> hook on the client side when possible and only use `currentUser()` when you specifically need user data in a server context. For more information on this helper, see the [`currentUser()`](/docs/reference/nextjs/app-router/current-user) reference.

The following example uses the [`auth()`](/docs/reference/nextjs/app-router/auth) helper to validate an authenticated user and the `currentUser()` helper to access the `Backend User` object for the authenticated user.

> \[!TIP]
> Any requests from a Client Component to a Route Handler will read the session from cookies and will not need the token sent as a Bearer token.

<Tabs items={["Server components and actions", "Route Handler"]}>
  <Tab>
    ```tsx {{ filename: 'app/page.tsx' }}
    import { auth, currentUser } from '@clerk/nextjs/server'

    export default async function Page() {
      // Use `auth()` to access `isAuthenticated` - if false, the user is not signed in
      const { isAuthenticated } = await auth()

      // Protect the route by checking if the user is signed in
      if (!isAuthenticated) {
        return <div>Sign in to view this page</div>
      }

      // Get the Backend User object when you need access to the user's information
      const user = await currentUser()

      // Use `user` to render user details or create UI elements
      return <div>Welcome, {user.firstName}!</div>
    }
    ```
  </Tab>

  <Tab>
    > \[!WARNING]
    > The <SDKLink href="/docs/reference/backend/types/backend-user" sdks={["js-backend"]} code={true}>Backend User</SDKLink> object includes a `privateMetadata` field that should not be exposed to the frontend. Avoid passing the full user object returned by `currentUser()` to the frontend. Instead, pass only the specified fields you need.

    ```tsx {{ filename: 'app/api/user/route.ts' }}
    import { NextResponse } from 'next/server'
    import { currentUser, auth } from '@clerk/nextjs/server'

    export async function GET() {
      // Use `auth()` to access `isAuthenticated` - if false, the user is not signed in
      const { isAuthenticated } = await auth()

      // Protect the route by checking if the user is signed in
      if (!isAuthenticated) {
        return new NextResponse('Unauthorized', { status: 401 })
      }

      // Use `currentUser()` to get the Backend User object
      const user = await currentUser()

      // Add your Route Handler's logic with the returned `user` object

      return NextResponse.json(
        { userId: user.id, email: user.emailAddresses[0].emailAddress },
        { status: 200 },
      )
    }
    ```
  </Tab>
</Tabs>

### Pages Router

For Next.js applications using the Pages Router, the [`getAuth()`](/docs/reference/nextjs/pages-router/get-auth) helper will return the <SDKLink href="/docs/reference/backend/types/auth-object" sdks={["js-backend"]} code={true}>Auth</SDKLink> object of the currently active user, which contains important information like the current user's session ID, user ID, and Organization ID, as well as the `isAuthenticated` property which can be used to protect your API routes.

In some cases, you may need the full <SDKLink href="/docs/reference/backend/types/backend-user" sdks={["js-backend"]} code={true}>Backend User</SDKLink> object of the currently active user. This is helpful if you want to render information, like their first and last name, directly from the server.

The `clerkClient()` helper returns an instance of the <SDKLink href="/docs/js-backend/getting-started/quickstart" sdks={["js-backend"]}>JS Backend SDK</SDKLink>, which exposes Clerk's Backend API resources through methods such as the <SDKLink href="/docs/reference/backend/user/get-user" sdks={["js-backend"]} code={true}>getUser()</SDKLink>{{ target: '_blank' }} method. This method returns the full `Backend User` object. **It does count towards the [Backend API request rate limit](/docs/guides/how-clerk-works/system-limits)** so it's recommended to use the <SDKLink href="/docs/:sdk:/reference/hooks/use-user" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>useUser()</SDKLink> hook on the client side when possible and only use `getUser()` when you specifically need user data in a server context.

In the following example, the `userId` is passed to the JS Backend SDK's `getUser()` method to get the user's full `Backend User` object.

<Tabs items={["API Route", "getServerSideProps"]}>
  <Tab>
    ```tsx {{ filename: 'pages/api/auth.ts' }}
    import { getAuth, clerkClient } from '@clerk/nextjs/server'
    import type { NextApiRequest, NextApiResponse } from 'next'

    export default async function handler(req: NextApiRequest, res: NextApiResponse) {
      // Use `getAuth()` to access `isAuthenticated` and the user's ID
      const { isAuthenticated, userId } = getAuth(req)

      // Protect the route by checking if the user is signed in
      if (!isAuthenticated) {
        return res.status(401).json({ error: 'Unauthorized' })
      }

      // Initialize the JS Backend SDK
      const client = await clerkClient()

      // Get the user's full Backend User object
      const user = await client.users.getUser(userId)

      return res.status(200).json({ user })
    }
    ```
  </Tab>

  <Tab>
    The `buildClerkProps()` function is used in your Next.js application's `getServerSideProps` to pass authentication state from the server to the client. It returns props that get spread into the `<ClerkProvider>` component. This enables Clerk's client-side helpers, such as `useAuth()`, to correctly determine the user's authentication status during server-side rendering.

    ```tsx {{ filename: 'pages/example.tsx' }}
    import { getAuth, buildClerkProps } from '@clerk/nextjs/server'
    import { GetServerSideProps } from 'next'

    export const getServerSideProps: GetServerSideProps = async (ctx) => {
      // Use `getAuth()` to access `isAuthenticated` and the user's ID
      const { isAuthenticated, userId } = getAuth(ctx.req)

      // Protect the route by checking if the user is signed in
      if (!isAuthenticated) {
        return {
          redirect: {
            destination: '/sign-in',
            permanent: false,
          },
        }
      }

      // Initialize the JS Backend SDK
      const client = await clerkClient()

      // Get the user's full `Backend User` object
      const user = await client.users.getUser(userId)

      // Pass the `user` object to buildClerkProps()
      return { props: { ...buildClerkProps(ctx.req, { user }) } }
    }
    ```
  </Tab>
</Tabs>

## Client-side

### `useAuth()`

{/*TODO: Keep in sync with /tanstack-react-start/read-session-data and /expo/read-session-user-data*/}

The following example uses the <SDKLink href="/docs/:sdk:/reference/hooks/use-auth" sdks={["astro","chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>useAuth()</SDKLink> hook to access the current auth state, as well as helper methods to manage the current session.

```tsx {{ filename: 'example.tsx' }}
export default function Example() {
  const { isLoaded, isSignedIn, userId, sessionId, getToken } = useAuth()

  const fetchExternalData = async () => {
    // Use `getToken()` to get the current user's session token
    const token = await getToken()

    // Use `token` to fetch data from an external API
    const response = await fetch('https://api.example.com/data', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })

    return response.json()
  }

  // Use `isLoaded` to check if Clerk is loaded
  if (!isLoaded) {
    return <div>Loading...</div>
  }

  // Use `isSignedIn` to check if the user is signed in
  if (!isSignedIn) {
    // You could also add a redirect to the sign-in page here
    return <div>Sign in to view this page</div>
  }

  return (
    <div>
      Hello, {userId}! Your current active session is {sessionId}.
    </div>
  )
}
```

### `useUser()`

{/*TODO: Keep in sync with /reference/tanstack-react-start/read-session-data and /reference/expo/read-session-user-data*/}

The following example uses the <SDKLink href="/docs/:sdk:/reference/hooks/use-user" sdks={["chrome-extension","expo","nextjs","react","react-router","tanstack-react-start"]} code={true}>useUser()</SDKLink> hook to access the <SDKLink href="/docs/reference/javascript/user" sdks={["js-frontend"]} code={true}>User</SDKLink> object, which contains the current user's data such as their full name. The following example demonstrates how to use `useUser()` to check if the user is signed in and display their first name.

```tsx {{ filename: 'src/Example.tsx' }}
export default function Example() {
  const { isSignedIn, user, isLoaded } = useUser()

  // Use `isLoaded` to check if Clerk is loaded
  if (!isLoaded) {
    return <div>Loading...</div>
  }

  // Use `isSignedIn` to protect the content
  if (!isSignedIn) {
    return <div>Sign in to view this page</div>
  }

  // Use `user` to access the current user's data
  return <div>Hello {user.firstName}!</div>
}
```
