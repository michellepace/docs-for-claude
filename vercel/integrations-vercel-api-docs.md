[Skip to main content](https://vercel.com/docs/rest-api/reference/examples/integrations#content-area)

[Vercel API Docs home page![light logo](https://mintcdn.com/vercel/fxKUJx-Oy_im1Iu0/logo/vercel-logotype-light.svg?fit=max&auto=format&n=fxKUJx-Oy_im1Iu0&q=85&s=e16d6302db6411b67d77ddc3810391e8)![dark logo](https://mintcdn.com/vercel/fxKUJx-Oy_im1Iu0/logo/vercel-logotype-dark.svg?fit=max&auto=format&n=fxKUJx-Oy_im1Iu0&q=85&s=ea47a9bb9db0106e05436a6578c50e9f)](https://vercel.com/docs/rest-api/reference)

Search...

Ctrl K

Search...

Navigation

Examples

Integrations

[Get Started](https://vercel.com/docs/rest-api/reference/welcome) [Endpoints](https://vercel.com/docs/rest-api/reference/endpoints/access-groups/reads-an-access-group)

On this page

- [List integration information](https://vercel.com/docs/rest-api/reference/examples/integrations#list-integration-information)

## [​](https://vercel.com/docs/rest-api/reference/examples/integrations\#list-integration-information)  List integration information

In this example, you list the available integrations in your account.

run.ts

Copy

Ask AI

```
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function listAccountIntegrations() {
  try {
    // List available integrations in the account connected with the Vercel token
    const integrationsResponse = await vercel.integrations.getConfigurations({
      view: 'account',
    });

    integrationsResponse.forEach((config) => {
      console.log(
        `- ${config.slug}: ${
          config.installationType ? `${config.installationType}` : ``
        }integration installed in ${config.projects?.join(' ')}`,
      );
    });
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

listAccountIntegrations();

```

[Environment Variables](https://vercel.com/docs/rest-api/reference/examples/environment-variables) [Logs and Monitoring](https://vercel.com/docs/rest-api/reference/examples/logs-monitoring)

CtrlI

Assistant

Responses are generated using AI and may contain mistakes.