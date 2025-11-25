# Protection Bypass for Automation

Protection Bypass for Automation is available on [all plans](/docs/plans)

The Protection Bypass for Automation feature lets you bypass Vercel Deployment Protection ([Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection), [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication), and [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips)) for automated tooling (e.g. E2E testing).

The generated secret can be used to bypass deployment protection on all deployments in a project until it is revoked. This value will also be automatically added to your deployments as a [system environment variable](/docs/environment-variables/system-environment-variables#VERCEL_AUTOMATION_BYPASS_SECRET) `VERCEL_AUTOMATION_BYPASS_SECRET`.

The environment variable value is set when a deployment is built, so regenerating the secret in the project settings will invalidate previous deployments. You will need to redeploy your app if you update the secret in order to use the new value.

![Protection Bypass for Automation option](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fenable-bypass-protection-light.png&w=1920&q=75)![Protection Bypass for Automation option](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fenable-bypass-protection-dark.png&w=1920&q=75)

Protection Bypass for Automation option

## [Who can manage protection bypass for automation?](#who-can-manage-protection-bypass-for-automation)

* [Team members](/docs/rbac/access-roles#team-level-roles) with at least the [member](/docs/rbac/access-roles#member-role) role
* [Project members](/docs/rbac/access-roles#project-level-roles) with the [Project Administrator](/docs/rbac/access-roles#project-administrators) role

## [Using Protection Bypass for Automation](#using-protection-bypass-for-automation)

To use Protection Bypass for Automation, set an HTTP header (or query parameter) named `x-vercel-protection-bypass` with the value of the generated secret for the project.

Using a header is strongly recommended, however in cases where your automation tool is unable to specify a header, it is also possible to set the same name and value as a query parameter.

```
x-vercel-protection-bypass: your-generated-secret (required)
```

### [Advanced Configuration](#advanced-configuration)

To bypass authorization on follow-up requests (e.g. for in-browser testing) you can set an additional header or query parameter named `x-vercel-set-bypass-cookie` with the value `true`.

This will set the authorization bypass as a cookie using a redirect with a `Set-Cookie` header.

```
x-vercel-set-bypass-cookie: true
```

If you are accessing the deployment through a non-direct way (e.g. in an `iframe`) then you may need to further configure `x-vercel-set-bypass-cookie` by setting the value to `samesitenone`.

This will set `SameSite` to `None` on the `Set-Cookie` header, by default `SameSite` is set to `Lax`.

```
x-vercel-set-bypass-cookie: samesitenone
```

### [Examples](#examples)

#### [Playwright](#playwright)

playwright.config.ts

```ts
const config: PlaywrightTestConfig = {
  use: {
    extraHTTPHeaders: {
      'x-vercel-protection-bypass': process.env.VERCEL_AUTOMATION_BYPASS_SECRET,
      'x-vercel-set-bypass-cookie': true | 'samesitenone' (optional)
    }
  }
}
```
