---
title: Customize your redirect URLs
description: Customize where your users are redirected to after they sign in or sign up.
lastUpdated: 2025-12-01T23:27:52.000Z
sdkScoped: "false"
canonical: /docs/guides/development/customize-redirect-urls
sourceFile: /docs/guides/development/customize-redirect-urls.mdx
---

When a user navigates to a Clerk sign-up or sign-in page via a link or button, like <SDKLink href="/docs/:sdk:/reference/components/unstyled/sign-in-button" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<SignInButton /></SDKLink>, Clerk will:

1. Persist the previous page's URL in a `redirect_url` query string.
2. Navigate back to that page after the sign-up or sign-in is completed.

For example, a user selecting a sign-in button on `example.com/foo` is navigated to `example.com/sign-in?redirect_url=example.com/foo`. Once the sign-in process is completed, Clerk will then use the `redirect_url` query string to redirect the user back to `example.com/foo`.

However, you can customize this behavior to redirect users to a specific page by using the following methods:

* [Environment variables (recommended)](#environment-variables)
* [Props on Clerk components](#redirect-url-props)

## Environment variables

The following environment variables are available for customizing your redirect URLs.

For the `FORCE` and `FALLBACK` variables, it's recommended to define both sign-up and sign-in variables, as some users may choose to sign up instead after attempting to sign in, and vice versa.

<Tabs items={["General", "Next.js"]}>
  <Tab>
    | Variable | Description | Example |
    | - | - | - |
    | `CLERK_SIGN_IN_URL` | The full URL or path to your sign-in page. Needs to point to your primary application on the client-side. **Required for a satellite application in a development instance.** | `/sign-in` |
    | `CLERK_SIGN_UP_URL` | The full URL or path to your sign-up page. Needs to point to your primary application on the client-side. **Required for a satellite application in a development instance.** | `/sign-up` |
    | `CLERK_SIGN_IN_FORCE_REDIRECT_URL` | If provided, this URL will always be redirected to after the user signs in. | `/dashboard` |
    | `CLERK_SIGN_UP_FORCE_REDIRECT_URL` | If provided, this URL will always be redirected to after the user signs up. | `/dashboard` |
    | `CLERK_SIGN_IN_FALLBACK_REDIRECT_URL` | The fallback URL to redirect to after the user signs in, if there's no `redirect_url` in the path already. Defaults to `/`. | `/dashboard` |
    | `CLERK_SIGN_UP_FALLBACK_REDIRECT_URL` | The fallback URL to redirect to after the user signs up, if there's no `redirect_url` in the path already. Defaults to `/`. | `/dashboard` |
  </Tab>

  <Tab>
    | Variable | Description | Example |
    | - | - | - |
    | `NEXT_PUBLIC_CLERK_SIGN_IN_URL` | The full URL or path to your sign-in page. Needs to point to your primary application on the client-side. **Required for a satellite application in a development instance.** | `/sign-in` |
    | `NEXT_PUBLIC_CLERK_SIGN_UP_URL` | The full URL or path to your sign-up page. Needs to point to your primary application on the client-side. **Required for a satellite application in a development instance.** | `/sign-up` |
    | `NEXT_PUBLIC_CLERK_SIGN_IN_FORCE_REDIRECT_URL` | If provided, this URL will always be redirected to after the user signs in. | `/dashboard` |
    | `NEXT_PUBLIC_CLERK_SIGN_UP_FORCE_REDIRECT_URL` | If provided, this URL will always be redirected to after the user signs up. | `/dashboard` |
    | `NEXT_PUBLIC_CLERK_SIGN_IN_FALLBACK_REDIRECT_URL` | The fallback URL to redirect to after the user signs in, if there's no `redirect_url` in the path already. Defaults to `/`. | `/dashboard` |
    | `NEXT_PUBLIC_CLERK_SIGN_UP_FALLBACK_REDIRECT_URL` | The fallback URL to redirect to after the user signs up, if there's no `redirect_url` in the path already. Defaults to `/`. | `/dashboard` |
  </Tab>
</Tabs>

## Redirect URL props

This section describes the properties available for customizing your redirect URLs on Clerk components. In general, **it's recommended to use [environment variables](#environment-variables) instead.**

> \[!WARNING]
> The `afterSignIn`, `afterSignUp`, and `redirectUrl` props are deprecated. If you're still using them, the props described in this section will override them.

### Fallback redirect URL props

The "fallback redirect URL" props will only be used if there is no `redirect_url` value. This can happen if the user has navigated directly to the sign up or sign in page.

* `fallbackRedirectUrl` - Used by sign-in and sign-up related components.
* `signInFallbackRedirectUrl` - Used for the 'Already have an account? Sign in' link that's rendered on sign-up components, such as `<SignUp />` and `<SignUpButton>`.
* `signUpFallbackRedirectUrl` - Used for the 'Don't have an account? Sign up' link that's rendered on sign-in components, such as `<SignIn />` and `<SignInButton>`.

### Force redirect URL props

The "force redirect URL" props will *always* redirect to the provided URL after sign up or sign in, regardless of what page the user was on before, and will override the `redirect_url` value if present.

* `forceRedirectUrl` - Used by sign-in and sign-up related components.
* `signInForceRedirectUrl` - Used for the 'Already have an account? Sign in' link that's rendered on sign-up components, such as `<SignUp />` and `<SignUpButton>`.
* `signUpForceRedirectUrl` - Used for the 'Don't have an account? Sign up' link that's rendered on sign-in components, such as `<SignIn />` and `<SignInButton>`.

### Set the props

It is recommended to define both sign-up and sign-in variables, as some users may choose to sign up instead after attempting to sign in, and vice versa. For example, if you define `signInFallbackRedirectUrl`, you should also define `signUpFallbackRedirectUrl`.

The following components accept the redirect URL props:

* [`<RedirectToSignIn />`](https://clerk.com/docs/nextjs/reference/components/control/redirect-to-sign-in)
* [`<RedirectToSignUp />`](https://clerk.com/docs/nextjs/reference/components/control/redirect-to-sign-up)
* [`<ClerkProvider>`](https://clerk.com/docs/nextjs/reference/components/clerk-provider)
* [`<SignInButton>`](https://clerk.com/docs/nextjs/reference/components/unstyled/sign-in-button)
* [`<SignUpButton>`](https://clerk.com/docs/nextjs/reference/components/unstyled/sign-up-button)
* [`<SignIn>`](https://clerk.com/docs/nextjs/reference/components/authentication/sign-in)
* [`<SignUp>`](https://clerk.com/docs/nextjs/reference/components/authentication/sign-up)

See the appropriate reference documentation for each component, as linked above, for more information on what specific props are available.

> \[!NOTE]
> `<RedirectToSignIn />` or `<RedirectToSignUp />` child components will always take precedence over `<ClerkProvider>`.
