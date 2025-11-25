# Advanced Web Analytics Config with @vercel/analytics

## [Getting started](#getting-started)

To get started with analytics, follow our [Quickstart](/docs/analytics/quickstart) guide which will walk you through the process of setting up analytics for your project.

## [`mode`](#mode)

Override the automatic environment detection.

This option allows you to force a specific environment for the package. If not defined, it will use `auto` which tries to set the `development` or `production` mode based on available environment variables such as `NODE_ENV`.

If your used framework does not expose these environment variables, the automatic detection won't work correctly. In this case, you're able to provide the correct `mode` manually or by other helpers that your framework exposes.

If you're using the `<Analytics />` component, you can pass the `mode` prop to force a specific environment:

app/layout.tsx

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
import { Analytics } from '@vercel/analytics/next';
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>Next.js</title>
      </head>
      <body>
        {children}
        <Analytics mode="production" />;
      </body>
    </html>
  );
}
```

## [`debug`](#debug)

You'll see all analytics events in the browser's console with the debug mode. This option is automatically enabled if the `NODE_ENV` environment variable is available and either `development` or `test`.

You can manually disable it to prevent debug messages in your browsers console.

To disable the debug mode for server-side events, you need to set the `VERCEL_WEB_ANALYTICS_DISABLE_LOGS` environment variable to `true`.

app/layout.tsx

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
import { Analytics } from '@vercel/analytics/next';
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>Next.js</title>
      </head>
      <body>
        {children}
        <Analytics debug />
      </body>
    </html>
  );
}
```

## [`beforeSend`](#beforesend)

With the `beforeSend` option, you can modify the event data before it's sent to Vercel. Below, you will see an example that ignores all events that have a `/private` inside the URL.

Returning `null` will ignore the event and no data will be sent. You can also modify the URL and check our docs about [redacting sensitive data](/docs/analytics/redacting-sensitive-data).

app/layout.tsx

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
import { Analytics, type BeforeSendEvent } from '@vercel/analytics/next';
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>Next.js</title>
      </head>
      <body>
        {children}
        <Analytics
          beforeSend={(event: BeforeSendEvent) => {
            if (event.url.includes('/private')) {
              return null;
            }
            return event;
          }}
        />
      </body>
    </html>
  );
}
```

## [`endpoint`](#endpoint)

The `endpoint` option allows you to report the collected analytics to a different url than the default: `https://yourdomain.com/_vercel/insights`.

This is useful when deploying several projects under the same domain, as it allows you to keep each application isolated.

For example, when `yourdomain.com` is managed outside of Vercel:

1. "alice-app" is deployed under `yourdomain.com/alice/*`, vercel alias is `alice-app.vercel.sh`
2. "bob-app" is deployed under `yourdomain.com/bob/*`, vercel alias is `bob-app.vercel.sh`
3. `yourdomain.com/_vercel/*` is routed to `alice-app.vercel.sh`

Both applications are sending their analytics to `alice-app.vercel.sh`. To restore the isolation, "bob-app" should use:

```
<Analytics endpoint="https://bob-app.vercel.sh/_vercel/insights" />
```

## [`scriptSrc`](#scriptsrc)

The `scriptSrc` option allows you to load the Web Analytics script from a different URL than the default one.

```
<Analytics scriptSrc="https://bob-app.vercel.sh/_vercel/insights/script.js" />
```
