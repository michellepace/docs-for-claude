---
title: Legal compliance
description: Learn how to configure your legal compliance settings in the Clerk Dashboard.
lastUpdated: 2025-12-03T22:33:41.000Z
sdkScoped: "false"
canonical: /docs/guides/secure/legal-compliance
sourceFile: /docs/guides/secure/legal-compliance.mdx
---

Clerk provides a legal compliance setting that allows you to require users to agree to your terms of service or privacy policy before they can sign up to your application. After enabling the setting, there will be a checkbox to accept the terms in your <SDKLink href="/docs/:sdk:/reference/components/authentication/sign-up" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<SignUp /> component</SDKLink> or [Account Portal sign-up page](/docs/guides/customizing-clerk/account-portal#sign-up).

To configure the setting:

1. In the Clerk Dashboard, navigate to the [**Legal**](https://dashboard.clerk.com/~/compliance/legal) page.
2. Enable or disable **Require express consent to legal documents**.
