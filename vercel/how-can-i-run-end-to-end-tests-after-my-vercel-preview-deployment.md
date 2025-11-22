# How can I run end-to-end tests after my Vercel Preview Deployment?

Learn how to use the Vercel CLI in combination with your CI/CD provider to run end-to-end tests for every code change.

Last updated June 30, 2025

You can run an end-to-end test suite after your Vercel deployment has finished with the following methods:

- [Using GitHub Actions' repository\_dispatch events](https://vercel.com/guides/how-can-i-run-end-to-end-tests-after-my-vercel-preview-deployment#using-github-actions'-repository_dispatch-events)
- [Using webhooks with other CI providers](https://vercel.com/guides/how-can-i-run-end-to-end-tests-after-my-vercel-preview-deployment#using-webhooks-for-other-ci-providers)

If your project has [Deployment Protection](https://vercel.com/docs/deployment-protection) enabled, ensure you use [Protection Bypass for Automation](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation) so your test environments can reach your deployments.

## [Using GitHub Actions' `repository_dispatch` events](https://vercel.com/guides/how-can-i-run-end-to-end-tests-after-my-vercel-preview-deployment\#using-github-actions'-repository_dispatch-events)

1. Connect your Git repository to your project. For new projects, you can [follow these docs](https://vercel.com/docs/concepts/git#deploying-a-git-repository). For existing projects, visit your Git configuration in the Settings tab of your project dashboard.
2. Create a GitHub workflow in `.github/workflows` with the following:

```yml
name: Playwright Tests

on:
  repository_dispatch:
    types:
      - 'vercel.deployment.success'
jobs:
  run-e2es:
    if: github.event_name == 'repository_dispatch'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.client_payload.git.sha }}
      - name: Install dependencies
        run: npm ci && npx playwright install --with-deps
      - name: Run tests
        run: npx playwright test
        env:
          BASE_URL: ${{ github.event.client_payload.url }}
```

A GitHub Action that runs an end-to-end test suite using repository\_dispatch events.

## [Using webhooks for other CI providers](https://vercel.com/guides/how-can-i-run-end-to-end-tests-after-my-vercel-preview-deployment\#using-webhooks-for-other-ci-providers)

1. [Configure a webhook](https://vercel.com/docs/webhooks?__vercel_draft=1#configure-a-webhook) for the `deployment.succeeded` event.
2. Listen for the webhook to trigger your CI workflow.
3. Run end-to-end test suites.

Was this helpful?

supported.

Send
