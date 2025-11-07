[Supported Frameworks](https://vercel.com/docs/frameworks)

[Full-stack](https://vercel.com/docs/frameworks/full-stack)

Next.js

Next.js (/app)

Choose a framework to optimize documentation to:

- Next.js (/app)
- Next.js (/pages)

[Supported Frameworks](https://vercel.com/docs/frameworks)

[Full-stack](https://vercel.com/docs/frameworks/full-stack)

Next.js

# Next.js on Vercel

Copy page

Ask AI about this page

Last updated October 9, 2025

[Next.js](https://nextjs.org/) is a fullstack React framework for the web, maintained by Vercel.

While Next.js works when self-hosting, deploying to Vercel is zero-configuration and provides additional enhancements for scalability, availability, and performance globally.

## [Getting started](https://vercel.com/docs/frameworks/full-stack/nextjs\#getting-started)

To get started with Next.js on Vercel:

- If you already have a project with Next.js, install [Vercel CLI](https://vercel.com/docs/cli) and run the `vercel` command from your project's root directory
- Clone one of our Next.js example repos to your favorite git provider and deploy it on Vercel with the button below:

[![Deploy our Next.js template, or view a live example.](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/next.svg)](https://vercel.com/templates/next.js/nextjs-boilerplate)

[Deploy](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fnextjs&template=nextjs) [Live Example](https://nextjs-template.vercel.app/)

- Or, choose a template from Vercel's marketplace:

Get started in minutes

## Deploy a new Next.js project with a template

[View All Templates](https://vercel.com/templates/next.js)

[![Next.js App Router Playground](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2Fk9BYNIi5HwkHop568SjEI%2Fcfb7e8215a11667d32265b34c43b4b5b%2FCleanShot_2022-10-25_at_14.38.59_2x.png&w=3840&q=75)\\
\\
Next.js App Router Playground\\
\\
Examples of many Next.js App Router features.](https://vercel.com/templates/next.js/app-directory) [![Image Gallery Starter](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F3PkqiHFN4mAmCpexoBvb2B%2Fe52a778e2b4320220665c73a3b8a498a%2FCleanShot_2022-12-02_at_10.42.14_2x.png&w=3840&q=75)\\
\\
Image Gallery Starter\\
\\
An image gallery built on Next.js and Cloudinary.](https://vercel.com/templates/next.js/image-gallery-starter) [![Next.js Boilerplate](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F1aHobcZ8H6WY48u5CMXlOe%2F0f0efe6bd469985b692555fbcad1cc01%2Fnextjs-template.png&w=3840&q=75)\\
\\
Next.js Boilerplate\\
\\
Get started with Next.js and React in seconds.](https://vercel.com/templates/next.js/nextjs-boilerplate)

[View All Templates](https://vercel.com/templates/next.js)

Vercel deployments can [integrate with your git provider](https://vercel.com/docs/git) to [generate preview URLs](https://vercel.com/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your Next.js project.

## [Incremental Static Regeneration](https://vercel.com/docs/frameworks/full-stack/nextjs\#incremental-static-regeneration)

[Incremental Static Regeneration (ISR)](https://vercel.com/docs/incremental-static-regeneration) allows you to create or update content _without_ redeploying your site. ISR has three main benefits for developers: better performance, improved security, and faster build times.

When self-hosting, (ISR) is limited to a single region workload. Statically generated pages are not distributed closer to visitors by default, without additional configuration or vendoring of a CDN. By default, self-hosted ISR does _not_ persist generated pages to durable storage. Instead, these files are located in the Next.js cache (which expires).

To enable ISR with Next.js in the `app` router, add an options object with a `revalidate` property to your `fetch` requests:

Next.js (/app)Next.js (/pages)

apps/example/page.tsx

TypeScript

TypeScriptJavaScript

```
export default async function Page() {
  const res = await fetch('https://api.vercel.app/blog', {
    next: { revalidate: 10 }, // Seconds
  });

  const data = await res.json();

  return (
    <main>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  );
}
```

To summarize, using ISR with Next.js on Vercel:

- Better performance with our global [CDN](https://vercel.com/docs/cdn)
- Zero-downtime rollouts to previously statically generated pages
- Framework-aware infrastructure enables global content updates in 300ms
- Generated pages are both cached and persisted to durable storage

[Learn more about Incremental Static Regeneration (ISR)](https://vercel.com/docs/incremental-static-regeneration)

## [Server-Side Rendering (SSR)](https://vercel.com/docs/frameworks/full-stack/nextjs\#server-side-rendering-ssr)

Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, checking authentication or looking at the location of an incoming request.

On Vercel, you can server-render Next.js applications through [Vercel Functions](https://vercel.com/docs/functions).

To summarize, SSR with Next.js on Vercel:

- Scales to zero when not in use
- Scales automatically with traffic increases
- Has zero-configuration support for [`Cache-Control` headers](https://vercel.com/docs/edge-cache), including `stale-while-revalidate`
- Framework-aware infrastructure enables automatic creation of Functions for SSR

[Learn more about SSR](https://nextjs.org/docs/app/building-your-application/rendering#static-and-dynamic-rendering-on-the-server)

## [Streaming](https://vercel.com/docs/frameworks/full-stack/nextjs\#streaming)

Vercel supports streaming in Next.js projects with any of the following:

- [Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/router-handlers)
- [Vercel Functions](https://vercel.com/docs/functions/streaming-functions)
- React Server Components

Streaming data allows you to fetch information in chunks rather than all at once, speeding up Function responses. You can use streams to improve your app's user experience and prevent your functions from failing when fetching large files.

[Streaming with `loading` and `Suspense`](https://vercel.com/docs/frameworks/full-stack/nextjs\#streaming-with-loading-and-suspense)

In the Next.js App Router, you can use the `loading` file convention or a `Suspense` component to show an instant loading state from the server while the content of a route segment loads.

The `loading` file provides a way to show a loading state for a whole route or route-segment, instead of just particular sections of a page. This file affects all its child elements, including layouts and pages. It continues to display its contents until the data fetching process in the route segment completes.

The following example demonstrates a basic `loading` file:

loading.tsx

TypeScript

TypeScriptJavaScript

```
export default function Loading() {
  return <p>Loading...</p>;
}
```

Learn more about loading in the [Next.js docs](https://nextjs.org/docs/app/building-your-application/routing/loading-ui-and-streaming).

The `Suspense` component, introduced in React 18, enables you to display a fallback until components nested within it have finished loading. Using `Suspense` is more granular than showing a loading state for an entire route, and is useful when only sections of your UI need a loading state.

You can specify a component to show during the loading state with the `fallback` prop on the `Suspense` component as shown below:

app/dashboard/page.tsx

TypeScript

TypeScriptJavaScript

```
import { Suspense } from 'react';
import { PostFeed, Weather } from './components';

export default function Posts() {
  return (
    <section>
      <Suspense fallback={<p>Loading feed...</p>}>
        <PostFeed />
      </Suspense>
      <Suspense fallback={<p>Loading weather...</p>}>
        <Weather />
      </Suspense>
    </section>
  );
}
```

To summarize, using Streaming with Next.js on Vercel:

- Speeds up Function response times, improving your app's user experience
- Display initial loading UI with incremental updates from the server as new data becomes available

Learn more about [Streaming](https://vercel.com/docs/functions/streaming-functions) with Vercel Functions.

## [Partial Prerendering](https://vercel.com/docs/frameworks/full-stack/nextjs\#partial-prerendering)

Partial Prerendering as an experimental feature. It is currently
**not suitable for production** environments.

Partial Prerendering (PPR) is an experimental feature in Next.js that allows the static portions of a page to be pre-generated and served from the cache, while the dynamic portions are streamed in a single HTTP request.

When a user visits a route:

- A static route _shell_ is served immediately, this makes the initial load fast.
- The shell leaves _holes_ where dynamic content will be streamed in to minimize the perceived overall page load time.
- The async holes are loaded in parallel, reducing the overall load time of the page.

This approach is useful for pages like dashboards, where unique, per-request data coexists with static elements such as sidebars or layouts. This is different from how your application behaves today, where entire routes are either fully static or dynamic.

See the [Partial Prerendering docs](https://nextjs.org/docs/app/api-reference/next-config-js/partial-prerendering) to learn more.

## [Image Optimization](https://vercel.com/docs/frameworks/full-stack/nextjs\#image-optimization)

[Image Optimization](https://vercel.com/docs/image-optimization) helps you achieve faster page loads by reducing the size of images and using modern image formats.

When deploying to Vercel, images are automatically optimized on demand, keeping your build times fast while improving your page load performance and [Core Web Vitals](https://vercel.com/docs/speed-insights).

When self-hosting, Image Optimization uses the default Next.js server for optimization. This server manages the rendering of pages and serving of static files.

To use Image Optimization with Next.js on Vercel, import the `next/image` component into the component you'd like to add an image to, as shown in the following example:

Next.js (/app)Next.js (/pages)

components/ExampleComponent.tsx

TypeScript

TypeScriptJavaScript

```
import Image from 'next/image';

interface ExampleProps {
  name: string;
}

const ExampleComponent = ({ name }: ExampleProps) => {
  return (
    <>
      <Image
        src="example.png"
        alt="Example picture"
        width={500}
        height={500}
      />
      <span>{name}</span>
    </>
  );
};

export default ExampleComponent;
```

To summarize, using Image Optimization with Next.js on Vercel:

- Zero-configuration Image Optimization when using `next/image`
- Helps your team ensure great performance by default
- Keeps your builds fast by optimizing images on-demand
- Requires No additional services needed to procure or set up

[Learn more about Image Optimization](https://vercel.com/docs/image-optimization)

## [Font Optimization](https://vercel.com/docs/frameworks/full-stack/nextjs\#font-optimization)

[`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) enables built-in automatic self-hosting for any font file. This means you can optimally load web fonts with zero [layout shift](https://vercel.com/docs/speed-insights/metrics#cumulative-layout-shift-cls), thanks to the underlying CSS [`size-adjust`](https://developer.mozilla.org/docs/Web/CSS/@font-face/size-adjust) property.

This also allows you to use all [Google Fonts](https://fonts.google.com/) with performance and privacy in mind. CSS and font files are downloaded at build time and self-hosted with the rest of your static files. No requests are sent to Google by the browser.

Next.js (/app)Next.js (/pages)

app/layout.tsx

TypeScript

TypeScriptJavaScript

```
import { Inter } from 'next/font/google';

// If loading a variable font, you don't need to specify the font weight
const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
});

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  );
}
```

To summarize, using Font Optimization with Next.js on Vercel:

- Enables built-in, automatic self-hosting for font files
- Loads web fonts with zero layout shift
- Allows for CSS and font files to be downloaded at build time and self-hosted with the rest of your static files
- Ensures that no requests are sent to Google by the browser

[Learn more about Font Optimization](https://nextjs.org/docs/app/building-your-application/optimizing/fonts)

## [Open Graph Images](https://vercel.com/docs/frameworks/full-stack/nextjs\#open-graph-images)

Dynamic social card images (using the [Open Graph protocol](https://vercel.com/docs/og-image-generation)) allow you to create a unique image for every page of your site. This is useful when sharing links on the web through social platforms or through text message.

The [Vercel OG](https://vercel.com/docs/og-image-generation) image generation library allows you generate fast, dynamic social card images using Next.js API Routes.

The following example demonstrates using OG image generation in both the Next.js Pages and App Router:

Next.js (/app)Next.js (/pages)

app/api/og/route.tsx

TypeScript

TypeScriptJavaScript

```
import { ImageResponse } from 'next/og';
// App router includes @vercel/og.
// No need to install it.

export async function GET(request: Request) {
  return new ImageResponse(
    (
      <div
        style={{
          fontSize: 128,
          background: 'white',
          width: '100%',
          height: '100%',
          display: 'flex',
          textAlign: 'center',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        Hello world!
      </div>
    ),
    {
      width: 1200,
      height: 600,
    },
  );
}
```

To see your generated image, run `npm run dev` in your terminal and visit the `/api/og` route in your browser (most likely `http://localhost:3000/api/og`).

To summarize, the benefits of using Vercel OG with Next.js include:

- Instant, dynamic social card images without needing headless browsers
- Generated images are automatically cached on the Vercel CDN
- Image generation is co-located with the rest of your frontend codebase

[Learn more about OG Image Generation](https://vercel.com/docs/og-image-generation)

## [Middleware](https://vercel.com/docs/frameworks/full-stack/nextjs\#middleware)

[Middleware](https://vercel.com/docs/routing-middleware) is code that executes before a request is processed. Because Middleware runs before the cache, it's an effective way of providing personalization to statically generated content.

When deploying middleware with Next.js on Vercel, you get access to built-in helpers that expose each request's geolocation information. You also get access to the `NextRequest` and `NextResponse` objects, which enable rewrites, continuing the middleware chain, and more.

See [the Middleware API docs](https://vercel.com/docs/routing-middleware/api) for more information.

To summarize, Middleware with Next.js on Vercel:

- Runs using [Middleware](https://vercel.com/docs/routing-middleware) which are deployed globally
- Replaces needing additional services for customizable routing rules
- Helps you achieve the best performance for serving content globally

[Learn more about Middleware](https://vercel.com/docs/routing-middleware)

## [Draft Mode](https://vercel.com/docs/frameworks/full-stack/nextjs\#draft-mode)

[Draft Mode](https://vercel.com/docs/draft-mode) enables you to view draft content from your [Headless CMS](https://vercel.com/docs/solutions/cms) immediately, while still statically generating pages in production.

See [our Draft Mode docs](https://vercel.com/docs/draft-mode#getting-started) to learn how to use it with Next.js.

### [Self-hosting Draft Mode](https://vercel.com/docs/frameworks/full-stack/nextjs\#self-hosting-draft-mode)

When self-hosting, every request using Draft Mode hits the Next.js server, potentially incurring extra load or cost. Further, by spoofing the cookie, malicious users could attempt to gain access to your underlying Next.js server.

### [Draft Mode security](https://vercel.com/docs/frameworks/full-stack/nextjs\#draft-mode-security)

Deployments on Vercel automatically secure Draft Mode behind the same authentication used for Preview Comments. In order to enable or disable Draft Mode, the viewer must be logged in as a member of the [Team](https://vercel.com/docs/teams-and-accounts). Once enabled, Vercel's CDN will bypass the ISR cache automatically and invoke the underlying [Vercel Function](https://vercel.com/docs/functions).

### [Enabling Draft Mode in Preview Deployments](https://vercel.com/docs/frameworks/full-stack/nextjs\#enabling-draft-mode-in-preview-deployments)

You and your team members can toggle Draft Mode in the Vercel Toolbar in [production](https://vercel.com/docs/vercel-toolbar/in-production-and-localhost/add-to-production), [localhost](https://vercel.com/docs/vercel-toolbar/in-production-and-localhost/add-to-localhost), and [Preview Deployments](https://vercel.com/docs/deployments/environments#preview-environment-pre-production#comments). When you do so, the toolbar will become purple to indicate Draft Mode is active.

![The Vercel toolbar when Draft Mode is enabled.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Fdraft-mode%2Fdraft-toolbar1-light.png&w=828&q=75)![The Vercel toolbar when Draft Mode is enabled.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Fdraft-mode%2Fdraft-toolbar1-dark.png&w=828&q=75)The Vercel toolbar when Draft Mode is enabled.

Users outside your Vercel team cannot toggle Draft Mode.

To summarize, the benefits of using Draft Mode with Next.js on Vercel include:

- Easily server-render previews of static pages
- Adds additional security measures to prevent malicious usage
- Integrates with any headless provider of your choice
- You can enable and disable Draft Mode in [the comments toolbar](https://vercel.com/docs/comments/how-comments-work) on Preview Deployments

[Learn more about Draft Mode](https://vercel.com/docs/draft-mode)

## [Web Analytics](https://vercel.com/docs/frameworks/full-stack/nextjs\#web-analytics)

Vercel's Web Analytics features enable you to visualize and monitor your application's performance over time. The Analytics tab in your project's dashboard offers detailed insights into your website's visitors, with metrics like top pages, top referrers, and user demographics.

To use Web Analytics, navigate to the Analytics tab of your project dashboard on Vercel and select Enable in the modal that appears.

To track visitors and page views, we recommend first installing our `@vercel/analytics` package by running the terminal command below in the root directory of your Next.js project:

pnpmyarnnpmbun

```
pnpm i @vercel/analytics
```

Then, follow the instructions below to add the `Analytics` component to your app either using the `pages` directory or the `app` directory.

The `Analytics` component is a wrapper around the tracking script, offering more seamless integration with Next.js, including route support.

Add the following code to the root layout:

Next.js (/app)Next.js (/pages)

app/layout.tsx

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
        <Analytics />
      </body>
    </html>
  );
}
```

To summarize, Web Analytics with Next.js on Vercel:

- Enables you to track traffic and see your top-performing pages
- Offers you detailed breakdowns of visitor demographics, including their OS, browser, geolocation, and more

[Learn more about Web Analytics](https://vercel.com/docs/analytics)

## [Speed Insights](https://vercel.com/docs/frameworks/full-stack/nextjs\#speed-insights)

You can see data about your project's [Core Web Vitals](https://vercel.com/docs/speed-insights/metrics#core-web-vitals-explained) performance in your dashboard on Vercel. Doing so will allow you to track your web application's loading speed, responsiveness, and visual stability so you can improve the overall user experience.

On Vercel, you can track your Next.js app's Core Web Vitals in your project's dashboard.

### [reportWebVitals](https://vercel.com/docs/frameworks/full-stack/nextjs\#reportwebvitals)

If you're self-hosting your app, you can use the [`useWebVitals`](https://nextjs.org/docs/advanced-features/measuring-performance#build-your-own) hook to send metrics to any analytics provider. The following example demonstrates a custom `WebVitals` component that you can use in your app's root `layout` file:

app/\_components/web-vitals.tsx

TypeScript

TypeScriptJavaScript

```
'use client';

import { useReportWebVitals } from 'next/web-vitals';

export function WebVitals() {
  useReportWebVitals((metric) => {
    console.log(metric);
  });
}
```

You could then reference your custom `WebVitals` component like this:

app/layout.ts

TypeScript

TypeScriptJavaScript

```
import { WebVitals } from './_components/web-vitals';

export default function Layout({ children }) {
  return (
    <html>
      <body>
        <WebVitals />
        {children}
      </body>
    </html>
  );
}
```

Next.js uses [Google's `web-vitals` library](https://github.com/GoogleChrome/web-vitals#web-vitals) to measure the Web Vitals metrics available in `reportWebVitals`.

To summarize, tracking Web Vitals with Next.js on Vercel:

- Enables you to track traffic performance metrics, such as [First Contentful Paint](https://vercel.com/docs/speed-insights/metrics#first-contentful-paint-fcp), or [First Input Delay](https://vercel.com/docs/speed-insights/metrics#first-input-delay-fid)
- Enables you to view performance analytics by page name and URL for more granular analysis
- Shows you [a score for your app's performance](https://vercel.com/docs/speed-insights/metrics#how-the-scores-are-determined) on each recorded metric, which you can use to track improvements or regressions

[Learn more about Speed Insights](https://vercel.com/docs/speed-insights)

## [Service integrations](https://vercel.com/docs/frameworks/full-stack/nextjs\#service-integrations)

Vercel has partnered with popular service providers, such as MongoDB and Sanity, to create integrations that make using those services with Next.js easier. There are many integrations across multiple categories, such as [Commerce](https://vercel.com/integrations#commerce), [Databases](https://vercel.com/integrations#databases), and [Logging](https://vercel.com/integrations#logging).

To summarize, Integrations on Vercel:

- Simplify the process of connecting your preferred services to a Vercel project
- Help you achieve the optimal setup for a Vercel project using your preferred service
- Configure your environment variables for you

[Learn more about Integrations](https://vercel.com/integrations)

## [More benefits](https://vercel.com/docs/frameworks/full-stack/nextjs\#more-benefits)

See [our Frameworks documentation page](https://vercel.com/docs/frameworks) to learn about the benefits available to all frameworks when you deploy on Vercel.

## [More resources](https://vercel.com/docs/frameworks/full-stack/nextjs\#more-resources)

Learn more about deploying Next.js projects on Vercel with the following resources:

- [Build a fullstack Next.js app](https://vercel.com/guides/nextjs-prisma-postgres)
- [Build a multi-tenant app](https://vercel.com/docs/multi-tenant)
- [Next.js with Contenful](https://vercel.com/guides/integrating-next-js-and-contentful-for-your-headless-cms)
- [Next.js with Stripe Checkout and Typescript](https://vercel.com/guides/getting-started-with-nextjs-typescript-stripe)
- [Next.js with Magic.link](https://vercel.com/guides/add-auth-to-nextjs-with-magic)
- [Generate a sitemap with Next.js](https://vercel.com/guides/how-do-i-generate-a-sitemap-for-my-nextjs-app-on-vercel)
- [Next.js ecommerce with Shopify](https://vercel.com/guides/deploying-locally-built-nextjs)
- [Deploy a locally built Next.js app](https://vercel.com/guides/deploying-locally-built-nextjs)
- [Deploying Next.js to Vercel](https://www.youtube.com/watch?v=AiiGjB2AxqA)
- [Learn about combining static and dynamic rendering on the same page in Next.js 14](https://www.youtube.com/watch?v=wv7w_Zx-FMU)
- [Learn about suspense boundaries and streaming when loading your UI](https://nextjs.org/docs/app/building-your-application/routing/loading-ui-and-streaming)

* * *

[Previous\\
\\
Full-stack](https://vercel.com/docs/frameworks/full-stack)

[Next\\
\\
SvelteKit](https://vercel.com/docs/frameworks/full-stack/sveltekit)

Was this helpful?

supported.

Send
