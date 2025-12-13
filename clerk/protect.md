---
title: "`<Protect>`"
description: The Protect component protects content or even entire routes based
  on authentication, and optionally, authorization. It only renders its children
  when the current user is signed-in, and if performing authorization checks, if
  the user has been granted a specific type of access control (Role, Permission,
  Feature, or Plan).
sdk: astro, chrome-extension, expo, nextjs, nuxt, react, react-router, remix,
  tanstack-react-start, vue
sdkScoped: "true"
canonical: /docs/:sdk:/reference/components/control/protect
lastUpdated: 2025-12-11T21:01:08.000Z
availableSdks: astro,chrome-extension,expo,nextjs,nuxt,react,react-router,remix,tanstack-react-start,vue
notAvailableSdks: js-frontend,android,ios,expressjs,fastify,go,ruby,js-backend
activeSdk: nextjs
sourceFile: /docs/reference/components/control/protect.mdx
---

The <SDKLink href="/docs/:sdk:/reference/components/control/protect" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<Protect /></SDKLink> component protects content or even entire routes based on:

* authentication: whether the user is signed-in or not.
* authorization: whether the user has been granted a specific type of access control (Role, Permission, Feature, or Plan)

`<Protect />` **always** performs authentication checks. To perform <Tooltip><TooltipTrigger>authorization checks</TooltipTrigger><TooltipContent>Authorization checks are checks you perform in your code to determine the access rights and privileges of a user, ensuring they have the necessary permissions to perform specific actions or access certain content. Learn more about [authorization checks](/docs/guides/secure/authorization-checks).</TooltipContent></Tooltip>, you can pass different props, like `role`, `permission`, `feature`, or `plan`.

`<Protect />` accepts a `fallback` prop that will be rendered if the user fails the authentication or authorization checks.

`<Protect />` can be used both client-side and server-side (in Server Components).

> \[!CAUTION]
> This component only **visually hides** its children when the current user is not authorized. The contents of its children remain accessible via the browser's source code even if the user fails the authorization check. Do not use this component to hide sensitive information that should be completely inaccessible to unauthorized users. For truly sensitive data, perform <Tooltip><TooltipTrigger>authorization checks</TooltipTrigger><TooltipContent>Authorization checks are checks you perform in your code to determine the access rights and privileges of a user, ensuring they have the necessary permissions to perform specific actions or access certain content. Learn more about [authorization checks](/docs/guides/secure/authorization-checks).</TooltipContent></Tooltip> on the server before sending the data to the client.

## Usage

### Authentication checks

`<Protect />` always performs authentication checks. It will render its children if the user is signed-in, and its `fallback` prop if the user is signed-out.

<If sdk="nextjs">
  ```tsx {{ filename: 'app/dashboard/page.tsx' }}
  import { Protect } from '@clerk/nextjs'

  export default function Page() {
    return (
      <Protect fallback={<p>Users that are signed-out can see this.</p>}>
        <p>Users that are signed-in can see this.</p>
      </Protect>
    )
  }

  ```
</If>

### Authorization checks

To limit who is able to see the content that `<Protect>` renders, you can pass **one** of the access control props: `permission`, `role`, `feature`, or `plan`. It's recommended to use **Permission-based** authorization over **Role-based** authorization, and **Feature-based** authorization over **Plan-based** authorization, as they are more flexible, easier to manage, and more secure.

If you do not pass any of the access control props, `<Protect>` will render its children if the user is signed in, regardless of their Role or its Permissions.

For more complex authorization logic, <SDKLink href="/docs/:sdk:/reference/components/control/protect#render-content-conditionally" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]}>pass conditional logic to the `condition` prop</SDKLink>.

### Render content by Permissions

The following example demonstrates how to use the `<Protect />` component to protect content by checking if the user has the `org:invoices:create` Permission.

<If sdk="nextjs">
  ```jsx {{ filename: 'app/protected/invoices/page.tsx' }}
  import { Protect } from '@clerk/nextjs'

  export default function Page() {
    return (
      <Protect
        permission="org:invoices:create"
        fallback={<p>You do not have the Permissions to create an invoice.</p>}
      >
        <p>Users with Permission org:invoices:create can see this.</p>
      </Protect>
    )
  }
  ```

</If>

### Render content by Role

While authorization by `permission` is **recommended**, for convenience, `<Protect>` allows a `role` prop to be passed.

The following example demonstrates how to use the `<Protect />` component to protect content by checking if the user has the `org:billing` Role.

<If sdk="nextjs">
  ```jsx {{ filename: 'app/protected/billing/page.tsx' }}
  import { Protect } from '@clerk/nextjs'

  export default function ProtectPage() {
    return (
      <Protect
        role="org:billing"
        fallback={<p>Only a member of the Billing department can access this content.</p>}
      >
        <p>Users with Role org:billing can see this.</p>
      </Protect>
    )
  }

  ```
</If>

### Render content by Plan

The following example demonstrates how to use `<Protect />` to protect content by checking if the user has a Plan.

<If sdk="nextjs">
  ```tsx {{ filename: 'app/protected/bronze/page.tsx' }}
  import { Protect } from '@clerk/nextjs'

  export default function ProtectPage() {
    return (
      <Protect
        plan="bronze"
        fallback={<p>Sorry, only subscribers to the Bronze plan can access this content.</p>}
      >
        <p>Welcome, Bronze subscriber!</p>
      </Protect>
    )
  }
  ```

</If>

### Render content by Feature

The following example demonstrates how to use `<Protect />` to protect content by checking if the user has a Feature.

<If sdk="nextjs">
  ```tsx {{ filename: 'app/protected/premium-access/page.tsx' }}
  import { Protect } from '@clerk/nextjs'

  export default function Page() {
    return (
      <Protect
        feature="premium_access"
        fallback={
          <p>Sorry, only subscribers with the Premium Access feature can access this content.</p>
        }
      >
        <p>Congratulations! You have access to the Premium Access feature.</p>
      </Protect>
    )
  }

  ```
</If>

### Render content conditionally

The following example uses `<Protect>`'s `condition` prop to conditionally render its children if the user has the correct Role.

<If sdk="nextjs">
  ```tsx {{ filename: 'app/dashboard/settings/page.tsx' }}
  import type { PropsWithChildren } from 'react'
  import { Protect } from '@clerk/nextjs'

  export default function Page() {
    return (
      <Protect
        condition={(has) => has({ role: 'org:admin' }) || has({ role: 'org:billing_manager' })}
        fallback={<p>Only an Admin or Billing Manager can access this content.</p>}
      >
        <p>The settings page.</p>
      </Protect>
    )
  }
  ```

</If>

## Properties

<Properties>
  * `condition?`
  * `has => boolean`

  Optional conditional logic that renders the children if it returns `true`.

  ***

* `fallback?`
* `JSX`

  Optional UI to show when a user doesn't have the correct type of access control to access the protected content.

  ***

* `feature?`
* `string`

  Optional string corresponding to a [Feature](/docs/guides/billing/overview).

  ***

* `plan?`
* `string`

  Optional string corresponding to a [Plan](/docs/guides/billing/overview).

  ***

* `permission?`
* `string`

  Optional string corresponding to a [Permission](/docs/guides/organizations/control-access/roles-and-permissions) in the format `org:<feature>:<permission>`

  ***

* `role?`
* `string`

  Optional string corresponding to a [Role](/docs/guides/organizations/control-access/roles-and-permissions) in the format `org:<role>`

  ***

* `treatPendingAsSignedOut?`
* `boolean`

  A boolean that indicates whether to treat <SDKLink href="/docs/reference/javascript/types/session-status#properties" sdks={["js-frontend"]}>pending sessions</SDKLink> as signed out. Defaults to `true`.
</Properties>
