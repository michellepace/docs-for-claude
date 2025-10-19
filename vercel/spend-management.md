Your Privacy

This site uses tracking technologies. You may opt in or opt out of the use of these technologies.

Essential
On

Essential cookies and services are used to enable core website features, such as ensuring the security of the website.

* * *

Marketing
Off

Marketing cookies and services are used to deliver personalized advertisements, promotions, and offers. These technologies enable targeted advertising and marketing campaigns by collecting information about users' interests, preferences, and online activities.

* * *

Analytics
Off

Analytics cookies and services are used for collecting statistical information about how visitors interact with a website. These technologies provide insights into website usage, visitor behavior, and site performance to understand and improve the site and enhance user experience.

* * *

Functional
Off

Functional cookies and services are used to offer enhanced and personalized functionalities. These technologies provide additional features and improved user experiences, such as remembering your language preferences, font sizes, region selections, and customized layouts. Opting out of these cookies may render certain services or functionality of the website unavailable.

SaveDenyAccept all

[Privacy Policy](https://vercel.com/legal/privacy-policy)

Your Privacy

This site uses tracking technologies. You may opt in or opt out of the use of these technologies.

DenyAccept all

Consent Settings

[Privacy Policy](https://vercel.com/legal/privacy-policy)

Choose a framework to optimize documentation to:

Copy page

# Spend Management

Spend Managementis availableon [Pro plans](https://vercel.com/docs/plans/pro)

Those with the[owner](https://vercel.com/docs/rbac/access-roles#owner-role) and [billing](https://vercel.com/docs/rbac/access-roles#billing-role)rolescan access this feature

Spend management is a way for you to notify or to automatically take action on your account when your team hits a [set spend amount](https://vercel.com/docs/spend-management#what-does-spend-management-include). The actions you can take are:

- [Receive a notification](https://vercel.com/docs/spend-management#managing-alert-threshold-notifications)
- [Trigger a webhook](https://vercel.com/docs/spend-management#configuring-a-webhook)
- [Pause the production deployment of all your projects](https://vercel.com/docs/spend-management#pausing-projects)

Setting a spend amount does not automatically stop usage. If you want to pause
all your projects at a certain amount, you must [enable the\\
option](https://vercel.com/docs/spend-management#pausing-projects).

The spend amount is set per billing cycle.

Setting the amount halfway through a billing cycle considers your current spend. You can increase or decrease your spend amount as needed. If you configure it below the current monthly spend, Spend Management will trigger any configured actions (including pausing all projects).

## [What does Spend Management include?](https://vercel.com/docs/spend-management\#what-does-spend-management-include)

The spend amount that you set covers [metered resources](https://vercel.com/docs/limits#additional-resources) that go beyond your Pro plan [credits and usage allocation](https://vercel.com/docs/plans/pro-plan#credit-and-usage-allocation) for all projects on your team.

It does not include seats, integrations (such as Marketplace), or separate [add-ons](https://vercel.com/docs/pricing#pro-plan-add-ons), which Vercel charges on a monthly basis.

### [How Vercel checks your spend amount](https://vercel.com/docs/spend-management\#how-vercel-checks-your-spend-amount)

Vercel checks your metered resource usage often to determine if you are approaching or have exceeded your spend amount. This check happens every few minutes.

## [Managing your spend amount](https://vercel.com/docs/spend-management\#managing-your-spend-amount)

1. To enable spend management, you must have an [Owner](https://vercel.com/docs/rbac/access-roles#owner-role) or [Billing](https://vercel.com/docs/rbac/access-roles#billing-role) role on your [Pro](https://vercel.com/docs/plans/pro-plan) team
2. From your team's [dashboard](https://vercel.com/dashboard), select the Settings tab
3. Select Billing from the list
4. Under Spend Management, toggle the switch to enabled:![Spend Management section with toggle enabled.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fspend-manage-light.png&w=1920&q=75)![Spend Management section with toggle enabled.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fspend-manage-dark.png&w=1920&q=75)Spend Management section with toggle enabled.
5. Set the amount in USD at which you would like to receive a notification or trigger an action
6. Select the action(s) to happen when your spend amount is reached: [pause all your projects](https://vercel.com/docs/spend-management#pausing-projects), [send notifications](https://vercel.com/docs/spend-management#managing-alert-threshold-notifications), or [trigger a webhook URL](https://vercel.com/docs/spend-management#configuring-a-webhook)

## [Managing alert threshold notifications](https://vercel.com/docs/spend-management\#managing-alert-threshold-notifications)

When you set a spend amount, Vercel automatically enables web and email notifications for your team. These get triggered when spending on your team reaches 50%, 75%, and 100% of the spend amount. You can also receive [SMS notifications](https://vercel.com/docs/spend-management#sms-notifications) when your team reaches 100% of the spend amount. To manage your notifications:

1. You must have an [Owner](https://vercel.com/docs/rbac/access-roles#owner-role) or [Billing](https://vercel.com/docs/rbac/access-roles#billing-role) role on your [Pro](https://vercel.com/docs/plans/pro-plan) team
2. From your team's [dashboard](https://vercel.com/dashboard), select the Settings tab
3. Select My Notifications from the list
4. Under Team, ensure that Spend Management is selected
5. Select the  icon and select the thresholds for which you would like to receive web and email notification, as described in [Notifications](https://vercel.com/docs/notifications)
6. Repeat the previous step for the Web, Email, and SMS notification sections

Following these steps only configures **your** notifications. Team members
with the Owner or Billing role can configure their own preferences

### [SMS notifications](https://vercel.com/docs/spend-management\#sms-notifications)

In addition to web and email notifications, you can enable SMS notifications for Spend Management. They are only triggered when you reach 100% of your spend amount.

To enable SMS notifications:

1. You must have an [Owner](https://vercel.com/docs/rbac/access-roles#owner-role) or [Billing](https://vercel.com/docs/rbac/access-roles#billing-role) role on your [Pro](https://vercel.com/docs/plans/pro-plan) team. Note that following these steps only configures your SMS notifications. Each member with an Owner or Billing role can configure their own SMS notifications for Spend Management
2. Set your [spend amount](https://vercel.com/docs/spend-management#managing-your-spend-amount)
3. From your team's [dashboard](https://vercel.com/dashboard), select the Settings tab
4. Select My Notifications from the list, scroll to SMS at the bottom of the page and toggle the switch to Enabled. If your personal profile has a phone number associated with it, SMS notifications will be enabled by default
5. Under Team, ensure that Spend Management is selected
6. Enter your phone number and follow the steps to verify it

## [Pausing projects](https://vercel.com/docs/spend-management\#pausing-projects)

Vercel provides an option to automatically pause the production deployment for all of your projects when your spend amount is reached.

1. In the Spend Management section of your team's settings, enable and set your [spend amount](https://vercel.com/docs/spend-management#managing-your-spend-amount)
2. Ensure the Pause production deployment switch is Enabled
3. Confirm the action by entering the team name and select Continue. Your changes save automatically
4. When your team reaches the spend amount, Vercel automatically pauses the production deployment for all projects on your team

When visitors access your production deployment while it is paused, they will see a [503 DEPLOYMENT\_PAUSED error](https://vercel.com/docs/errors/DEPLOYMENT_PAUSED).

### [Unpausing projects](https://vercel.com/docs/spend-management\#unpausing-projects)

Projects need to be resumed on an individual basis, either [through the dashboard](https://vercel.com/docs/projects/overview#resuming-a-project) or the [Vercel REST API](https://vercel.com/docs/rest-api/reference/endpoints/projects/unpause-a-project).

Projects won't automatically unpause if you increase the spend amount, you must resume each project manually.

## [Configuring a webhook](https://vercel.com/docs/spend-management\#configuring-a-webhook)

You can configure a webhook URL to trigger events such as serving a static version of your site, [pausing a project](https://vercel.com/docs/projects/overview#pausing-a-project), or sending a Slack notification.

Vercel will send a [HTTPS POST request](https://vercel.com/docs/spend-management#webhook-payload) to the URL that you provide when the following events happen:

- [When a spend amount reaches 100%](https://vercel.com/docs/spend-management#spend-amount)
- [At the end of your billing cycle](https://vercel.com/docs/spend-management#end-of-billing-cycle)

To configure a webhook for spend management:

1. In the Spend Management section of your team's settings, set your [spend amount](https://vercel.com/docs/spend-management#managing-your-spend-amount)
2. Enter the webhook URL for the endpoint that will receive a POST request. In order to be accessible, make sure your endpoints are public
3. Secure your webhooks by comparing the [`x-vercel-signature`](https://vercel.com/docs/headers/request-headers#x-vercel-signature) request header to the SHA that is generated when you save your webhook. To learn more, see the [securing webhooks](https://vercel.com/docs/webhooks/webhooks-api#securing-webhooks) documentation

### [Webhook payload](https://vercel.com/docs/spend-management\#webhook-payload)

The webhook URL receives an HTTP POST request with the following JSON payload for each event:

#### [Spend amount](https://vercel.com/docs/spend-management\#spend-amount)

Sent when the team hits 50%, 75%, and 100% of their spend amount. For budgets created before September 2025, this is only sent at 100%.

| Parameters | Type | Description |
| --- | --- | --- |
| `budgetAmount` | int | The [spend amount](https://vercel.com/docs/spend-management#managing-your-spend-amount) that you have set |
| `currentSpend` | int | The [total cost](https://vercel.com/docs/spend-management#managing-your-spend-amount) that your team [has accrued](https://vercel.com/docs/spend-management#what-does-spend-management-include) during the current billing cycle. |
| `teamId` | string | Your Vercel Team ID |
| `thresholdPercent` | int | The percentage of the total budget amount for the threshold that triggered this alert |

webhook-payload.json

```grid text-[var(--ds-gray-1000)] text-left whitespace-pre break-normal !text-[13px] leading-[20px] font-mono hyphens-none
{
  "budgetAmount": 500,
  "currentSpend": 500,
  "teamId": "team_jkT8yZ3oE1u6xLo8h6dxfNc3",
  "thresholdPercent": 100
}
```

### [End of billing cycle](https://vercel.com/docs/spend-management\#end-of-billing-cycle)

Sent when the billing cycle ends. You can use this event to resume paused projects.

| Parameters | Type | Description |
| --- | --- | --- |
| `teamId` | string | Your Vercel Team ID |
| `type` | string | The type of event |

webhook-payload.json

```grid text-[var(--ds-gray-1000)] text-left whitespace-pre break-normal !text-[13px] leading-[20px] font-mono hyphens-none
{
  "teamId": "team_jkT8yZ3oE1u6xLo8h6dxfNc3",
  "type": "endOfBillingCycle"
}
```

## [Spend Management activity](https://vercel.com/docs/spend-management\#spend-management-activity)

Vercel displays all spend management activity in the Activity tab of your [team's dashboard](https://vercel.com/docs/observability/activity-log). This includes spend amount creation and updates, and project pausing and unpausing.

## [More resources](https://vercel.com/docs/spend-management\#more-resources)

For more information on Vercel's pricing, guidance on optimizing consumption, and invoices, see the following resources:

- [How are resources used on Vercel?](https://vercel.com/docs/pricing/how-does-vercel-calculate-usage-of-resources)
- [Manage and optimize usage](https://vercel.com/docs/pricing/manage-and-optimize-usage)
- [Understanding my invoice](https://vercel.com/docs/pricing/understanding-my-invoice)
- [Spend limits for Vercel](https://youtu.be/-_vpoayWTps?si=Jv6b8szx68lVHGYz)

* * *

[Previous\\
\\
Pricing](https://vercel.com/docs/pricing)

[Next\\
\\
Security / Overview](https://vercel.com/docs/security)

Was this helpful?

supported.

Send