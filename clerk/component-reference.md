---
title: Component Reference
description: A list of Clerk's comprehensive suite of components designed to
  seamlessly integrate authentication and multi-tenancy into your application.
sdk: react, nextjs, js-frontend, chrome-extension, expo, android, expressjs,
  fastify, react-router, remix, tanstack-react-start, go, astro, nuxt, vue,
  ruby, js-backend
sdkScoped: "true"
canonical: /docs/:sdk:/reference/components/overview
lastUpdated: 2025-12-01T23:27:52.000Z
availableSdks: react,nextjs,js-frontend,chrome-extension,expo,android,expressjs,fastify,react-router,remix,tanstack-react-start,go,astro,nuxt,vue,ruby,js-backend
notAvailableSdks: ios
activeSdk: nextjs
sourceFile: /docs/reference/components/overview.mdx
---

Clerk offers a comprehensive suite of components designed to seamlessly integrate authentication and multi-tenancy into your application. With Clerk components, you can easily customize the appearance of authentication components and pages, manage the entire authentication flow to suit your specific needs, and even build robust SaaS applications.

## Authentication components

* <SDKLink href="/docs/:sdk:/reference/components/authentication/sign-in" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<SignIn /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/authentication/sign-up" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<SignUp /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/authentication/google-one-tap" sdks={["astro","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<GoogleOneTap /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/authentication/task-choose-organization" sdks={["js-frontend","nextjs","react","react-router","remix","tanstack-react-start"]} code={true}>\<TaskChooseOrganization /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/authentication/waitlist" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<Waitlist /></SDKLink>

## User components

* <SDKLink href="/docs/:sdk:/reference/components/user/user-avatar" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<UserAvatar /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/user/user-button" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<UserButton /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/user/user-profile" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<UserProfile /></SDKLink>

## Organization components

* <SDKLink href="/docs/:sdk:/reference/components/organization/create-organization" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<CreateOrganization /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/organization/organization-profile" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<OrganizationProfile /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/organization/organization-switcher" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<OrganizationSwitcher /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/organization/organization-list" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<OrganizationList /></SDKLink>

## Billing components

* <SDKLink href="/docs/:sdk:/reference/components/billing/pricing-table" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<PricingTable /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/billing/checkout-button" sdks={["react","nextjs","vue"]} code={true}>\<CheckoutButton /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/billing/plan-details-button" sdks={["react","nextjs","vue"]} code={true}>\<PlanDetailsButton /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/billing/subscription-details-button" sdks={["react","nextjs","vue"]} code={true}>\<SubscriptionDetailsButton /></SDKLink>

## Control components

Control components manage authentication-related behaviors in your application. They handle tasks such as controlling content visibility based on user authentication status, managing loading states during authentication processes, and redirecting users to appropriate pages. Control components render at `<Loading />` and `<Loaded />` states for assertions on the <SDKLink href="/docs/reference/javascript/clerk" sdks={["js-frontend"]} code={true}>Clerk object</SDKLink>. A common example is the <SDKLink href="/docs/:sdk:/reference/components/control/signed-in" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<SignedIn></SDKLink> component, which allows you to conditionally render content only when a user is authenticated.

* <SDKLink href="/docs/:sdk:/reference/components/control/authenticate-with-redirect-callback" sdks={["astro","chrome-extension","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<AuthenticateWithRedirectCallback /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/control/clerk-loaded" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<ClerkLoaded /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/control/clerk-loading" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<ClerkLoading /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/control/clerk-degraded" sdks={["nextjs","react","react-router","chrome-extension","remix","tanstack-react-start"]} code={true}>\<ClerkDegraded /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/control/clerk-failed" sdks={["nextjs","react","react-router","chrome-extension","remix","tanstack-react-start"]} code={true}>\<ClerkFailed /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/control/protect" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<Protect /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/control/redirect-to-sign-in" sdks={["chrome-extension","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<RedirectToSignIn /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/control/redirect-to-sign-up" sdks={["chrome-extension","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<RedirectToSignUp /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/control/redirect-to-tasks" sdks={["chrome-extension","nextjs","nuxt","react","react-router","tanstack-react-start","vue"]} code={true}>\<RedirectToTasks /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/control/redirect-to-user-profile" sdks={["nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<RedirectToUserProfile /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/control/redirect-to-organization-profile" sdks={["nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<RedirectToOrganizationProfile /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/control/redirect-to-create-organization" sdks={["nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<RedirectToCreateOrganization /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/control/signed-in" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<SignedIn /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/control/signed-out" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<SignedOut /></SDKLink>

## Unstyled components

* <SDKLink href="/docs/:sdk:/reference/components/unstyled/sign-in-button" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<SignInButton /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/unstyled/sign-in-with-metamask" sdks={["expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<SignInWithMetamaskButton /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/unstyled/sign-up-button" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<SignUpButton /></SDKLink>
* <SDKLink href="/docs/:sdk:/reference/components/unstyled/sign-out-button" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue"]} code={true}>\<SignOutButton /></SDKLink>

## Customization guides

* [Customize components with the `appearance` prop](/docs/guides/customizing-clerk/appearance-prop/overview)
* [Localize components with the `localization` prop (experimental)](/docs/guides/customizing-clerk/localization)
* [Add pages to the `<UserProfile />` component](/docs/guides/customizing-clerk/adding-items/user-profile)
* [Add pages to the `<OrganizationProfile />` component](/docs/guides/customizing-clerk/adding-items/organization-profile)

### Secured by Clerk branding

> \[!WARNING]
> This feature requires a [paid plan](/pricing){{ target: '_blank' }} for production use, but all features are free to use in development mode so that you can try out what works for you. See the [pricing](/pricing){{ target: '_blank' }} page for more information.

By default, Clerk displays a **Secured by Clerk** badge on Clerk components. You can remove this branding by following these steps:

1. In the Clerk Dashboard, navigate to your application's [**Settings**](https://dashboard.clerk.com/~/settings).
2. Under **Branding**, toggle on the **Remove "Secured by Clerk" branding** option.
