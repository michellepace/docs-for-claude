[Deployment Protection](https://vercel.com/docs/deployment-protection)

[Protect Deployments](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments)

Vercel Authentication

[Deployment Protection](https://vercel.com/docs/deployment-protection)

[Protect Deployments](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments)

Vercel Authentication

# Vercel Authentication

Copy page

Ask AI about this page

Last updatedSeptember 15, 2025

Vercel Authenticationis availableon [all plans](https://vercel.com/docs/plans)

Those with the[owner](https://vercel.com/docs/rbac/access-roles#owner-role), [member](https://vercel.com/docs/rbac/access-roles#member-role) and [admin](https://vercel.com/docs/rbac/access-roles#admin-role)rolescan manage Vercel Authentication

Vercel Authentication lets you restrict access to your public and non-public deployments. It is the recommended approach to protecting your deployments, and available on all plans. When enabled, it allows only users with deployment access to view and comment on your site.

Users attempting to access the deployment will encounter a Vercel login redirect. If already logged into Vercel, Vercel will authenticate them automatically.

After login, users are redirected and a cookie is set in the browser if they have view access. If the user does not have access to view the deployment, they will be redirected to [request access](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/vercel-authentication#access-requests).

## [Who can access protected deployments?](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/vercel-authentication\#who-can-access-protected-deployments)

- Logged in [team members](https://vercel.com/docs/rbac/access-roles#team-level-roles) with at least a viewer role ( [Viewer Pro](https://vercel.com/docs/rbac/access-roles#viewer-pro-role) or [Viewer Enterprise](https://vercel.com/docs/rbac/access-roles#viewer-enterprise-role))
- Logged in [project members](https://vercel.com/docs/rbac/access-roles#project-level-roles) with at least the [project Viewer](https://vercel.com/docs/rbac/access-roles#project-viewer) role
- Logged in members of an [access group](https://vercel.com/docs/rbac/access-groups) that has access to the project the deployment belongs to
- Logged in Vercel users who have been [granted access](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/vercel-authentication#access-requests)
- Anyone who has been given a [Shareable Link](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links) to the deployment
- Tools using the [protection bypass for automation](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation) header

## [Access requests](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/vercel-authentication\#access-requests)

Access requestsare availableon [all plans](https://vercel.com/docs/plans)

Those with the[owner](https://vercel.com/docs/rbac/access-roles#owner-role), [member](https://vercel.com/docs/rbac/access-roles#member-role), [admin](https://vercel.com/docs/rbac/access-roles#admin-role) and [developer](https://vercel.com/docs/rbac/access-roles#developer-role)rolescan accept or reject access requests

When a Vercel user visits your protected deployment, but they do not have permission to access it, they have the option to request access for their Vercel account.
This request triggers an email and Vercel notification to the branch authors.

![External users can request access to protected deployments.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Frequest-access.png&w=640&q=75)![External users can request access to protected deployments.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Frequest-access-dark.png&w=640&q=75)External users can request access to protected deployments.

The access request can be approved or declined. Additionally, granted access can be revoked for a user at any time.

Users granted access can view the latest deployment from a specific branch when logged in with their Vercel account.
They can also leave preview [Comments](https://vercel.com/docs/comments) if these are enabled on your team.

Those on the Hobby plan can only have one external user per account. If you need more, you can upgrade to a [Pro plan](https://vercel.com/docs/plans/pro-plan/trials).

You can manage access requests in the following way

1. From your [dashboard](https://vercel.com/dashboard) go to the Settings tab
2. Select Deployment Protection and then choose the Requests tab to see pending requests
3. Choose Access to manage existing access

![Access requests can be approved and declined on the Dashboard > Settings > Deployment Protection > Requests section.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fmanage-requests.png&w=1920&q=75)![Access requests can be approved and declined on the Dashboard > Settings > Deployment Protection > Requests section.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fmanage-requests-dark.png&w=1920&q=75)Access requests can be approved and declined on the Dashboard > Settings > Deployment Protection > Requests section.![Granted access requests can be managed on the Dashboard > Settings > Deployment Protection > Access section.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fgranted-access-list.png&w=1920&q=75)![Granted access requests can be managed on the Dashboard > Settings > Deployment Protection > Access section.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fgranted-access-list-dark.png&w=1920&q=75)Granted access requests can be managed on the Dashboard > Settings > Deployment Protection > Access section.

Access requests can also be managed using the share modal on the deployment page

![Access requests can be approved, declined and revoked in the deployment share modal.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fmanage-access-v2-light.png&w=828&q=75)![Access requests can be approved, declined and revoked in the deployment share modal.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fmanage-access-v2-dark.png&w=828&q=75)Access requests can be approved, declined and revoked in the deployment share modal.

## [Vercel Authentication security considerations](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/vercel-authentication\#vercel-authentication-security-considerations)

You can configure Vercel Authentication for different environments, as outlined in [Understanding Deployment Protection by environment](https://vercel.com/docs/security/deployment-protection#understanding-deployment-protection-by-environment). This feature works alongside other security measures like [Password Protection](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/password-protection) and [Trusted IPs](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips). For specific use-cases, you can bypass Vercel Authentication with methods like [Shareable Links](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links) or [Protection bypass for Automation](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation).

Disabling Vercel Authentication renders all existing deployments unprotected. However, re-enabling it allows previously authenticated users to maintain access without a new login provided they have already authenticated to the specific deployment and have a cookie set in their browser. The authentication token sent as a cookie is restricted to one URL and isn't transferable, even between URLs pointing to the same deployment.

| Consideration | Description |
| --- | --- |
| Environment Configuration | Can be enabled for different environments. See [Understanding Deployment Protection by environment](https://vercel.com/docs/security/deployment-protection#understanding-deployment-protection-by-environment) |
| Compatibility | Compatible with [Password Protection](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/password-protection) and [Trusted IPs](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips) |
| Bypass Methods | Can be bypassed using [Shareable Links](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links) and [Protection bypass for Automation](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation) |
| Disabling | All existing deployments become unprotected when Vercel Authentication is disabled |
| Re-enabling | Users who have logged in previously will still have access without re-authenticating |
| Token Scope | Tokens are valid for a single URL and are not reusable across different URLs |

## [Managing Vercel Authentication](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/vercel-authentication\#managing-vercel-authentication)

Admins and members can enable or disable Vercel Authentication for their team. Hobby teams can also enable or disable for their own projects. Vercel Authentication is managed on a per-project basis.

You can manage Vercel Authentication through the dashboard, API, or Terraform:

### [Manage using the dashboard](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/vercel-authentication\#manage-using-the-dashboard)

1. ### [Go to Project Deployment Protection Settings](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/vercel-authentication\#go-to-project-deployment-protection-settings)



From your Vercel [dashboard](https://vercel.com/dashboard):

1. Select the project that you wish to enable Password Protection for
2. Go to Settings then Deployment Protection
2. ### [Manage Vercel Authentication](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/vercel-authentication\#manage-vercel-authentication)



From the Vercel Authentication section:


1. Use the toggle to enable the feature
2. Select the [deployment environment](https://vercel.com/docs/deployments/environments) you want to protect
3. Finally, Select Save

All your existing and future deployments will be protected with Vercel Authentication for the project. Next time when you access a deployment, you will be asked to log in with Vercel if you aren't already logged in, you will be redirected to the deployment URL and a cookie will be set in your browser for that deployment URL.
![Enabling Vercel Authentication.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fsso-protection-light.png&w=1920&q=75)![Enabling Vercel Authentication.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fsso-protection-dark.png&w=1920&q=75)Enabling Vercel Authentication.

### [Manage using the API](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/vercel-authentication\#manage-using-the-api)

You can manage Vercel Authentication using the Vercel API endpoint to [update an existing project](https://vercel.com/docs/rest-api/reference/endpoints/projects/update-an-existing-project) with the following body

- `prod_deployment_urls_and_all_previews`: Standard Protection
- `all`: All Deployments
- `preview`: Only Preview Deployments

```
// enable / update Vercel Authentication
{
  "ssoProtection": {
    "deploymentType": "prod_deployment_urls_and_all_previews" | "all" | "preview"
  }
}

// disable Vercel Authentication
{
  "ssoProtection": null
}
```

### [Manage using Terraform](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/vercel-authentication\#manage-using-terraform)

You can configure Vercel Authentication using `vercel_authentication` in the `vercel_project` data source in the [Vercel Terraform Provider](https://registry.terraform.io/providers/vercel/vercel/latest/docs/data-sources/project).

* * *

[Previous\\
\\
Trusted IPs](https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/trusted-ips)

[Next\\
\\
Directory Sync](https://vercel.com/docs/directory-sync)

Was this helpful?

supported.

Send