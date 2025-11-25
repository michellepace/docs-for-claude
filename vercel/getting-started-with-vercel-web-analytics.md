# Getting started with Vercel Web Analytics

This guide will help you get started with using Vercel Web Analytics on your project, showing you how to enable it, add the package to your project, deploy your app to Vercel, and view your data in the dashboard.

Select your framework to view instructions on using the Vercel Web Analytics in your project.

## [Prerequisites](#prerequisites)

* A Vercel account. If you don't have one, you can [sign up for free](https://vercel.com/signup).
* A Vercel project. If you don't have one, you can [create a new project](https://vercel.com/new).
* The Vercel CLI installed. If you don't have it, you can install it using the following command:

    pnpmbunyarnnpm

    ```
    pnpm i -g vercel
    ```

1. ### [Enable Web Analytics in Vercel](#enable-web-analytics-in-vercel)

    On the [Vercel dashboard](/dashboard), select your Project and then click the Analytics tab and click Enable from the dialog.

    [Go to Web Analytics](/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fanalytics&title=Open+Web+Analytics)

    Enabling Web Analytics will add new routes (scoped at `/_vercel/insights/*`) after your next deployment.

* ### [Add `@vercel/analytics` to your project](#add-@vercel/analytics-to-your-project)

    Using the package manager of your choice, add the `@vercel/analytics` package to your project:

    pnpmbunyarnnpm

    ```
    pnpm i @vercel/analytics
    ```

  3. ### [Add the `Analytics` component to your app](#add-the-analytics-component-to-your-app)

    The `Analytics` component is a wrapper around the tracking script, offering more seamless integration with Next.js, including route support.

    Add the following code to the root layout:

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
            <Analytics />
          </body>
        </html>
      );
    }
    ```

4. ### [Deploy your app to Vercel](#deploy-your-app-to-vercel)

    Deploy your app using the following command:

    terminal

    ```
    vercel deploy
    ```

    If you haven't already, we also recommend [connecting your project's Git repository](/docs/git#deploying-a-git-repository), which will enable Vercel to deploy your latest commits to main without terminal commands.

    Once your app is deployed, it will start tracking visitors and page views.

    If everything is set up properly, you should be able to see a Fetch/XHR request in your browser's Network tab from `/_vercel/insights/view` when you visit any page.

5. ### [View your data in the dashboard](#view-your-data-in-the-dashboard)

    Once your app is deployed, and users have visited your site, you can view your data in the dashboard.

    To do so, go to your [dashboard](/dashboard), select your project, and click the Analytics tab.

    After a few days of visitors, you'll be able to start exploring your data by viewing and [filtering](/docs/analytics/filtering) the panels.

    Users on Pro and Enterprise plans can also add [custom events](/docs/analytics/custom-events) to their data to track user interactions such as button clicks, form submissions, or purchases.

Learn more about how Vercel supports [privacy and data compliance standards](/docs/analytics/privacy-policy) with Vercel Web Analytics.

## [Next steps](#next-steps)

Now that you have Vercel Web Analytics set up, you can explore the following topics to learn more:

* [Learn how to use the `@vercel/analytics` package](/docs/analytics/package)
* [Learn how to set update custom events](/docs/analytics/custom-events)
* [Learn about filtering data](/docs/analytics/filtering)
* [Read about privacy and compliance](/docs/analytics/privacy-policy)
* [Explore pricing](/docs/analytics/limits-and-pricing)
* [Troubleshooting](/docs/analytics/troubleshooting)
