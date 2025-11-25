Deployment Protection

Deployment Protection

# Deployment Protection on Vercel

Copy page

Ask AI about this page

Last updatedSeptember 24, 2025

Deployment Protection safeguards both your preview and production URLs across various environments. Configured at the project level through your settings, Deployment Protection provides detailed access control for different deployment types.

Vercel offers the following Deployment Protection features:

- [Vercel Authentication](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication): Restricts access to your deployments to only Vercel users with suitable access rights. Vercel Authentication is available on all plans
- [Password Protection](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/password-protection): Restricts access to your deployments to only users with the correct password. Password Protection is available on the Enterprise plan, or as a paid add-on for Pro plans
- [Trusted IPs](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips): Restricts access to your deployments to only users with the correct IP address. Trusted IPs is available on the Enterprise plan

Deployment protection requires authentication for all requests, including
those to Middleware.

## [Configuring Deployment Protection](https://vercel.com/docs/deployment-protection\#configuring-deployment-protection)

Deployment Protection is managed through your project settings. To configure Deployment Protection:

1. From the [dashboard](https://vercel.com/dashboard), select the project you wish to set Deployment Protection on
2. Once selected, navigate to the Settings tab
3. From the list, select the Deployment Protection tab

## [Understanding Deployment Protection by environment](https://vercel.com/docs/deployment-protection\#understanding-deployment-protection-by-environment)

You can configure the type of Deployment Protection for each environment in your project depending on your projects security needs. When choosing your protection method, you can select from three options:

- [Standard Protection](https://vercel.com/docs/deployment-protection#standard-protection): This option protects all domains except [Production Custom Domains](https://vercel.com/docs/domains/working-with-domains/add-a-domain). Standard Protection is available on all plans
- [All Deployments](https://vercel.com/docs/deployment-protection#all-deployments): Protects all URLs. Protecting all deployments is available on Pro and Enterprise plans
- [(Legacy) Standard Protection](https://vercel.com/docs/deployment-protection#legacy-standard-protection): This option protects all preview URLs and [deployment URLs](https://vercel.com/docs/deployments/generated-urls). All [up to date production URLs](https://vercel.com/docs/deployments/generated-urls) are unprotected.
- [(Legacy) Only Preview Deployments](https://vercel.com/docs/deployment-protection#legacy-only-preview-deployments): This option protects only preview URLs. This does not protect past production deployments.

To protect [only production URLs](https://vercel.com/docs/deployment-protection#only-production-deployments), you can use [Trusted IPs](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips). Note that this option is only available on the Enterprise plan.

### [Standard Protection](https://vercel.com/docs/deployment-protection\#standard-protection)

Standard Protectionis availableon [all plans](https://vercel.com/docs/plans)

Standard Protection is the recommended way to secure your deployments, as it protects all domains except [Production Custom Domains](https://vercel.com/docs/domains/working-with-domains/add-a-domain).

![Selecting Standard Protection in the Vercel Dashboard.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fcontentful%2Fimage%2Fe5382hct74si%2F7LHNvuRkcDlKMWswY7c8xd%2F858a8627a82bcec2c456bcd42618b3f5%2FScreenshot_2025-07-09_at_5.05.58%25C3%25A2__pm.png&w=1920&q=75)![Selecting Standard Protection in the Vercel Dashboard.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fcontentful%2Fimage%2Fe5382hct74si%2F7LHNvuRkcDlKMWswY7c8xd%2F858a8627a82bcec2c456bcd42618b3f5%2FScreenshot_2025-07-09_at_5.05.58%25C3%25A2__pm.png&w=1920&q=75)Selecting Standard Protection in the Vercel Dashboard.

Standard Protection can be configured with the following Deployment Protection features:

- [Vercel Authentication](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication)
- [Password Protection](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/password-protection)
- [Trusted IPs](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips)

#### [Migrating to Standard Protection](https://vercel.com/docs/deployment-protection\#migrating-to-standard-protection)

Enabling Standard Protection restricts public access to the production [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). This affects `VERCEL_URL` and `VERCEL_BRANCH_URL` from [System Environment Variables](https://vercel.com/docs/environment-variables/system-environment-variables#system-environment-variables), making them unsuitable for fetch requests.

If you are using `VERCEL_URL` or `VERCEL_BRANCH_URL` to make fetch requests, you will need to update your requests to target the same domain the user has requested.

The Framework Environment Variable `VERCEL_URL` is prefixed with the name of
the framework. For example, `VERCEL_URL` for Next.js is
`NEXT_PUBLIC_VERCEL_URL`, and `VERCEL_URL` for Nuxt is `NUXT_ENV_VERCEL_URL`.
See the [Framework Environment\\
Variables](https://vercel.com/docs/environment-variables/framework-environment-variables)
documentation for more information.

For client-side requests, use relative paths in the fetch call to target the current domain, automatically including the user's authentication cookie for protected URLs.

```
// Before
fetch(`${process.env.VERCEL_URL}/some/path`);

// After
fetch('/some/path');
// Note: For operations requiring fully qualified URLs, such as generating OG images,
// replace '/some/path' with the actual domain (e.g. 'https://yourdomain.com/some/path').
```

For server-side requests, use the origin from the incoming request and manually add request cookies to pass the user's authentication cookie.

```
const headers = { cookie: <incoming request header cookies> };
fetch('<incoming request origin>/some/path', { headers });
```

Bypassing protection using [Protection Bypass for Automation](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation) is an option but not required for requests targeting the same domain.

### [All deployments](https://vercel.com/docs/deployment-protection\#all-deployments)

Protecting all deploymentsis availableon [Enterprise plans](https://vercel.com/docs/plans/enterprise)or with the [Advanced Deployment Protection](https://vercel.com/docs/security/deployment-protection#advanced-deployment-protection) add-on for [Pro plans](https://vercel.com/docs/plans/pro)

Selecting All Deployments secures all deployments, both preview and production, restricting public access entirely.

With this configuration, all URLs, including your production domain `example.com` and [generated URLs](https://vercel.com/docs/deployments/generated-urls) like `my-project-1234.vercel.app`, are protected.

![Selecting All Deployments in the Vercel Dashboard.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fall-deployments-light.png&w=1920&q=75)![Selecting All Deployments in the Vercel Dashboard.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fall-deployments-dark.png&w=1920&q=75)Selecting All Deployments in the Vercel Dashboard.

Protecting all deployments can be configured with the following Deployment Protection features:

- [Vercel Authentication](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication)
- [Password Protection](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/password-protection)
- [Trusted IPs](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips)

### [Only production deployments](https://vercel.com/docs/deployment-protection\#only-production-deployments)

Protecting production deploymentsis availableon [Enterprise plans](https://vercel.com/docs/plans/enterprise)

Restrict access to protected deployments to a list of [Trusted IPs](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/trusted-ips).

Preview deployment URLs remain publicly accessible. This feature is only available on the Enterprise plan.

Want to talk to our team?

This feature is available on the Enterprise plan.

Schedule Call

![Selecting All Deployments in the Vercel Dashboard.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fprod-deployments-light.png&w=1920&q=75)![Selecting All Deployments in the Vercel Dashboard.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fprod-deployments-dark.png&w=1920&q=75)Selecting All Deployments in the Vercel Dashboard.

### [(Legacy) Standard Protection](https://vercel.com/docs/deployment-protection\#legacy-standard-protection)

(Legacy) Standard Protection is a legacy feature that protects all preview URLs and [deployment URLs](https://vercel.com/docs/deployments/generated-urls). All [up to date production URLs](https://vercel.com/docs/deployments/generated-urls) are unprotected.

### [(Legacy) Only Preview Deployments](https://vercel.com/docs/deployment-protection\#legacy-only-preview-deployments)

Selecting (Legacy) Only Preview Deployments protects preview URLs, while the production environment remains publicly accessible.

For example, Vercel generates a preview URL such as `my-preview-5678.vercel.app`, which will be protected. In contrast, all production URLs, including any past or current generated production branch URLs like `*-main.vercel.app`, remain accessible.

## [Advanced Deployment Protection](https://vercel.com/docs/deployment-protection\#advanced-deployment-protection)

Advanced Deployment Protection features are available to Enterprise customers by default. Customers on the Pro plan can access these features for an additional $150 per month, including:

- [Password Protection](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/password-protection)
- [Private Production Deployments](https://vercel.com/docs/security/deployment-protection#configuring-deployment-protection)
- [Deployment Protection Exceptions](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/deployment-protection-exceptions)

### [Enabling Advanced Deployment Protection](https://vercel.com/docs/deployment-protection\#enabling-advanced-deployment-protection)

To opt-into Advanced Deployment Protection while on a Pro plan:

1. Navigate to your Project Settings and select the Deployment Protection tab
2. Then choose one of the above protection features
3. You will then be prompted to upgrade to the Advanced Deployment Protection add-on through an Enable and Pay button before you can use the feature

When you enable Advanced Deployment Protection, you will be charged $150 per month for the add-on, and will have access to _all_ Advanced Deployment Protection features.

### [Disabling Advanced Deployment Protection](https://vercel.com/docs/deployment-protection\#disabling-advanced-deployment-protection)

To opt out of Advanced Deployment Protection:

1. Navigate to your Team Settings, then the Billing page
2. Press Edit on the feature you want to disable and follow the instructions to disable the add-on

In order to disable Advanced Deployment Protection, you must have been using the feature for a minimum of thirty days. After this time, once cancelled, all Advanced Deployment Protection features will be disabled.

## [More resources](https://vercel.com/docs/deployment-protection\#more-resources)

- [Methods to protect deployments](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments)
- [Methods to bypass deployment protection](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection)

* * *

[Previous\\
\\
Activity Log](https://vercel.com/docs/activity-log)

[Next\\
\\
Bypass Deployment Protection](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection)

Was this helpful?

supported.

Send