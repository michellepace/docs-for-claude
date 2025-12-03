---
title: Users
description: Learn how to manage your users in your Clerk application.
lastUpdated: 2025-12-01T23:27:52.000Z
sdkScoped: "false"
canonical: /docs/guides/users/managing
sourceFile: /docs/guides/users/managing.mdx
---

To get started, it's important to first understand Clerk's <SDKLink href="/docs/reference/javascript/user" sdks={["js-frontend"]} code={true}>User object</SDKLink>.

The `User` object holds all of the information for a single user of your application and provides a set of methods to manage their account. Each `User` has at least one authentication identifier, which might be their email address, phone number, or a username.

A user can be contacted at their primary email address or primary phone number. They can have more than one registered email address, but only one of them will be their primary email address (`User.primaryEmailAddress`). This goes for phone numbers as well; a user can have more than one, but only one phone number will be their primary (`User.primaryPhoneNumber`). At the same time, a user can also have one or more external accounts by connecting to [social providers](/docs/guides/configure/auth-strategies/social-connections/all-providers) such as Google, Apple, Facebook, and many more (`User.externalAccounts`).

Finally, a `User` object holds profile data like the user's name, profile picture, and a set of [metadata](/docs/guides/users/extending) that can be used internally to store arbitrary information. The metadata are split into `publicMetadata` and `privateMetadata`. Both types are set from the [Backend API](/docs/reference/backend-api){{ target: '_blank' }}, but public metadata can also be accessed from the [Frontend API](/docs/reference/frontend-api){{ target: '_blank' }}.

For more information on the `User` object, such as helper methods for retrieving and updating user information and authentication status, see the <SDKLink href="/docs/reference/javascript/user" sdks={["js-frontend"]}>reference docs</SDKLink>. The `User` object is also available in the backend, but it looks slightly different. For more information, see the <SDKLink href="/docs/reference/backend/types/backend-user" sdks={["js-backend"]}>Backend `User` object reference docs</SDKLink>.

## Manage users

You can manage your users [in the Clerk Dashboard](#in-the-clerk-dashboard), or [programmatically](#programmatically).

### In the Clerk Dashboard

To manage users in the Clerk Dashboard, navigate to the [**Users**](https://dashboard.clerk.com/~/users) page.

### Programmatically

You can manage users programmatically through the [frontend](#in-the-frontend) or [backend](#in-the-backend).

#### In the frontend

Depending on the level of abstraction you need, you can manage users in the frontend using Clerk's prebuilt components, React hooks, or lower-level JavaScript methods.

* Prebuilt components: Clerk provides the prebuilt components <SDKLink href="/docs/:sdk:/reference/components/user/user-button" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<UserButton /></SDKLink> and <SDKLink href="/docs/:sdk:/reference/components/user/user-profile" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<UserProfile /></SDKLink> to help your users manage their profile data.
* Hooks: Because Clerk's React-based SDKs are built on top of the Clerk React SDK, you can use the <SDKLink href="/docs/reference/react/overview#custom-hooks" sdks={["react"]}>hooks</SDKLink> that the React SDK provides. These hooks include access to the `User` object and helpful methods for managing user authentication and profile data.
* JavaScript methods: If Clerk's prebuilt components don't meet your specific needs or if you require more control over the logic, you can rebuild the existing Clerk flows using the Clerk API. For more information, see the [custom flow guides](/docs/guides/development/custom-flows/overview).

#### In the backend

The <SDKLink href="/docs/js-backend/getting-started/quickstart" sdks={["js-backend"]}>JS Backend SDK</SDKLink> is a wrapper around the [Backend API](/docs/reference/backend-api){{ target: '_blank' }} that makes it easier to interact with the API. It includes many methods for managing users, such as `getUser()`, `createUser()`, and `deleteUser()`. For more information, see the <SDKLink href="/docs/js-backend/getting-started/quickstart" sdks={["js-backend"]}>JS Backend SDK reference docs</SDKLink>.

## Create users

You can create users either [in the Clerk Dashboard](#in-the-clerk-dashboard-2) or [programmatically](#programmatically-2).

### In the Clerk Dashboard

To create a user in the Clerk Dashboard, navigate to the [**Users**](https://dashboard.clerk.com/~/users) page and select **Create user**.

### Programmatically

To create a user programmatically, you can either <SDKLink href="/docs/reference/backend/user/create-user#backend-api-bapi-endpoint" sdks={["js-backend"]}>make a request directly to Clerk's Backend API</SDKLink> or use the <SDKLink href="/docs/reference/backend/user/create-user" sdks={["js-backend"]} code={true}>createUser()</SDKLink> method as shown in the following example.

<Tabs items={["Next.js", "Astro", "Express", "React Router", "Tanstack React Start"]}>
  <Tab>
    ```ts {{ filename: 'app/api/example/route.ts' }}
    import { auth, clerkClient } from '@clerk/nextjs/server'
    import { NextResponse } from 'next/server'

    export async function POST() {
      const client = await clerkClient()
      const user = await client.users.createUser({
        emailAddress: ['test@example.com'],
        password: 'password',
      })

      return NextResponse.json({ message: 'User created', user })
    }
    ```
  </Tab>

  <Tab>
    ```tsx {{ filename: 'src/api/example.ts' }}
    import type { APIRoute } from 'astro'
    import { clerkClient } from '@clerk/astro/server'

    export const POST: APIRoute = async (context) => {
      await clerkClient(context).users.createUser({
        emailAddress: ['test@example.com'],
        password: 'password',
      })

      return new Response(JSON.stringify({ success: true }), { status: 200 })
    }
    ```
  </Tab>

  <Tab>
    ```ts {{ filename: 'public.ts' }}
    import { getAuth, clerkClient } from '@clerk/express'

    app.post('/createUser', async (req, res) => {
      await clerkClient.users.createUser({
        emailAddress: ['test@example.com'],
        password: 'password',
      })

      res.status(200).json({ success: true })
    })
    ```
  </Tab>

  <Tab>
    ```tsx {{ filename: 'app/routes/example.tsx' }}
    import { clerkClient } from '@clerk/react-router/server'
    import type { Route } from './+types/example'
    import { json } from 'react-router-dom'

    export async function action({ request }: Route.ActionArgs) {
      const formData = await request.formData()
      const emailAddress = formData.get('emailAddress')
      const password = formData.get('password')

      await clerkClient.users.createUser({
        emailAddress: [emailAddress],
        password: password,
      })

      return json({ success: true })
    }
    ```
  </Tab>

  <Tab>
    ```tsx {{ filename: 'app/routes/api/example.tsx' }}
    import { json } from '@tanstack/react-start'
    import { createFileRoute } from '@tanstack/react-router'
    import { clerkClient } from '@clerk/tanstack-react-start/server'

    export const ServerRoute = createFileRoute('/api/example')({
      server: {
        handlers: {
          POST: async () => {
            await clerkClient().users.createUser({
              emailAddress: ['test@example.com'],
              password: 'my-secure-password',
            })

            return json({ success: true })
          },
        },
      },
    })
    ```
  </Tab>
</Tabs>

## Delete users

You can delete users either in the Clerk Dashboard](#in-the-clerk-dashboard-3) or [programmatically](#programmatically).

> \[!IMPORTANT]
> Bulk deletion of users cannot currently be done through the Clerk Dashboard or programmatically. If you need to bulk delete users, please [contact support](/contact/support){{ target: '_blank' }}.

### In the Clerk Dashboard

To delete a user in the Clerk Dashboard, navigate to the [**Users**](https://dashboard.clerk.com/~/users) page. You can either select the user and then in the side navigation menu, select **Delete user**, or select the menu icon on the right side of the user's row and select **Delete user**.

### Programmatically

To delete a user programmatically, you can either <SDKLink href="/docs/reference/backend/user/delete-user#backend-api-bapi-endpoint" sdks={["js-backend"]}>make a request directly to Clerk's Backend API</SDKLink> or use the <SDKLink href="/docs/reference/backend/user/delete-user" sdks={["js-backend"]} code={true}>deleteUser()</SDKLink> method as shown in the following example.

<Tabs items={["Next.js", "Astro", "Express", "React Router", "Tanstack React Start"]}>
  <Tab>
    ```ts {{ filename: 'app/api/example/route.ts' }}
    import { clerkClient } from '@clerk/nextjs/server'
    import { NextResponse } from 'next/server'

    export async function POST() {
      await clerkClient.users.deleteUser('user_123')

      return NextResponse.json({ success: true })
    }
    ```
  </Tab>

  <Tab>
    ```tsx {{ filename: 'src/api/example.ts' }}
    import type { APIRoute } from 'astro'
    import { clerkClient } from '@clerk/astro/server'

    export const POST: APIRoute = async (context) => {
      await clerkClient(context).users.deleteUser('user_123')

      return new Response(JSON.stringify({ success: true }), { status: 200 })
    }
    ```
  </Tab>

  <Tab>
    ```ts {{ filename: 'public.ts' }}
    import { clerkClient } from '@clerk/express'

    app.post('/deleteUser', async (req, res) => {
      await clerkClient.users.deleteUser('user_123')

      res.status(200).json({ success: true })
    })
    ```
  </Tab>

  <Tab>
    ```tsx {{ filename: 'app/routes/example.tsx' }}
    import { clerkClient } from '@clerk/react-router/server'
    import type { Route } from './+types/example'
    import { json, redirect } from 'react-router-dom'

    export async function action({ request }: Route.ActionArgs) {
      const formData = await request.formData()
      const userId = formData.get('userId')

      await clerkClient.users.deleteUser(userId)

      return json({ success: true })
    }
    ```
  </Tab>

  <Tab>
    ```tsx {{ filename: 'app/routes/api/example.tsx' }}
    import { json } from '@tanstack/react-start'
    import { createFileRoute } from '@tanstack/react-router'
    import { auth, clerkClient } from '@clerk/tanstack-react-start/server'

    export const ServerRoute = createFileRoute('/api/example')({
      server: {
        handlers: {
          POST: async () => {
            await clerkClient().users.deleteUser('user_123')

            return json({ success: true })
          },
        },
      },
    })
    ```
  </Tab>
</Tabs>
