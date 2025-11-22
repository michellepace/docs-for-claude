# Integrations

> Learn how to use the Vercel SDK through real-life examples.

## List integration information

In this example, you list the available integrations in your account.

```ts run.ts theme={"system"}
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
