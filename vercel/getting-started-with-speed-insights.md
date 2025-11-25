# Getting started with Speed Insights

This guide will help you get started with using Vercel Speed Insights on your project, showing you how to enable it, add the package to your project, deploy your app to Vercel, and view your data in the dashboard.

Speed Insights is available on [all plans](/docs/plans)

To view instructions on using the Vercel Speed Insights in your project for your framework, use the Choose a framework dropdown on the right (at the bottom in mobile view).

## [Prerequisites](#prerequisites)

* A Vercel account. If you don't have one, you can [sign up for free](https://vercel.com/signup).
* A Vercel project. If you don't have one, you can [create a new project](https://vercel.com/new).
* The Vercel CLI installed. If you don't have it, you can install it using the following command:

    pnpmbunyarnnpm

    ```
    npm i -g vercel
    ```

1. ### [Enable Speed Insights in Vercel](#enable-speed-insights-in-vercel)

    On the [Vercel dashboard](/dashboard), select your Project followed by the Speed Insights tab. You can also select the button below to be taken there. Then, select Enable from the dialog.

    [Go to Speed Insights](/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fspeed-insights&title=Open+Speed+Insights)

    Enabling Speed Insights will add new routes (scoped at`/_vercel/speed-insights/*`) after your next deployment.

2. ### [Add `@vercel/speed-insights` to your project](#add-@vercel/speed-insights-to-your-project)

    Using the package manager of your choice, add the `@vercel/speed-insights` package to your project:

    pnpmbunyarnnpm

    ```
    npm i @vercel/speed-insights
    ```

3. ### [Add the `SpeedInsights` component to your app](#add-the-speedinsights-component-to-your-app)

    The `SpeedInsights` component is a wrapper around the tracking script, offering more seamless integration with Next.js.

    Add the following component to the root layout:

    Next.js v13.5+Older Next.js versions

    Add the following component to your main app file:

    app/layout.tsx

    Next.js (/app)

    Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks

    TypeScript

    TypeScriptJavaScript

    ```
    import { SpeedInsights } from '@vercel/speed-insights/next';
     
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
            <SpeedInsights />
          </body>
        </html>
      );
    }
    ```

    For versions of Next.js older than 13.5, import the `<SpeedInsights>` component from `@vercel/speed-insights/react`.

    Create a dedicated component to avoid opting out from SSR on the layout and pass the pathname of the route to the `SpeedInsights` component:

    app/insights.tsx

    Next.js (/app)

    Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks

    TypeScript

    TypeScriptJavaScript

    ```
    'use client';
     
    import { SpeedInsights } from '@vercel/speed-insights/react';
    import { usePathname } from 'next/navigation';
     
    export function Insights() {
      const pathname = usePathname();
     
      return <SpeedInsights route={pathname} />;
    }
    ```

    Then, import the `Insights` component in your layout:

    app/layout.tsx

    Next.js (/app)

    Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks

    TypeScript

    TypeScriptJavaScript

    ```
    import type { ReactNode } from 'react';
    import { Insights } from './insights';
     
    export default function RootLayout({ children }: { children: ReactNode }) {
      return (
        <html lang="en">
          <head>
            <title>Next.js</title>
          </head>
          <body>
            {children}
            <Insights />
          </body>
        </html>
      );
    }
    ```

4. ### [Deploy your app to Vercel](#deploy-your-app-to-vercel)

    You can deploy your app to Vercel's global [CDN](/docs/cdn) by running the following command from your terminal:

    terminal

    ```
    vercel deploy
    ```

    Alternatively, you can [connect your project's git repository](/docs/git#deploying-a-git-repository), which will enable Vercel to deploy your latest pushes and merges to main.

    Once your app is deployed, it's ready to begin tracking performance metrics.

    If everything is set up correctly, you should be able to find the `/_vercel/speed-insights/script.js` script inside the body tag of your page.

5. ### [View your data in the dashboard](#view-your-data-in-the-dashboard)

    Once your app is deployed, and users have visited your site, you can view the data in the dashboard.

    To do so, go to your [dashboard](/dashboard), select your project, and click the Speed Insights tab.

    After a few days of visitors, you'll be able to start exploring your metrics. For more information on how to use Speed Insights, see [Using Speed Insights](/docs/speed-insights/using-speed-insights).

Learn more about how Vercel supports [privacy and data compliance standards](/docs/speed-insights/privacy-policy) with Vercel Speed Insights.

## [Next steps](#next-steps)

Now that you have Vercel Speed Insights set up, you can explore the following topics to learn more:

* [Learn how to use the `@vercel/speed-insights` package](/docs/speed-insights/package)
* [Learn about metrics](/docs/speed-insights/metrics)
* [Read about privacy and compliance](/docs/speed-insights/privacy-policy)
* [Explore pricing](/docs/speed-insights/limits-and-pricing)
* [Troubleshooting](/docs/speed-insights/troubleshooting)
