# Use a template

### Using CLI?

Clone the template to your local machine and use the following snippet to deploy the template with Vercel CLI:

terminal

```
vercel --cwd [path-to-project]
```

Accelerate your development on Vercel with [Templates](/templates). This guide will show you how to use templates to fast-track project setup, leverage popular frontend frameworks, and maximize Vercel's features.

1. ### [Find a template](#find-a-template)

    From [https://vercel.com/templates](/templates), select the template you’d like to deploy. You can use the filters to select a template based on use case, framework, and other requirements.

    Not sure which one to use? How about [exploring Next.js](https://vercel.com/templates/next.js/nextjs-boilerplate).

    ![Viewing the templates marketplace](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Ftemplates-light.png&w=3840&q=75)![Viewing the templates marketplace](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Ftemplates-dark.png&w=3840&q=75)

    Viewing the templates marketplace

2. ### [Deploy the template to Vercel](#deploy-the-template-to-vercel)

    Once you've selected a template, Click Deploy on the template page to start the process.

    ![Deploying your chosen template](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fdeploying-template-light.png&w=1080&q=75)![Deploying your chosen template](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fdeploying-template-dark.png&w=1080&q=75)

    Deploying your chosen template

3. ### [Connect your Git provider](#connect-your-git-provider)

    To ensure you can easily update your project after deploying it, Vercel will create a new repository with your chosen [Git provider](/docs/git). Every push to that Git repository will be deployed automatically.

    First, select the Git provider that you'd like to connect to. Once you’ve signed in, you’ll need to set the scope and repository name. At this point, Vercel will clone a copy of the source code into your Git account.

    ![Connecting your Git provider and creating a new repository](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fgit-provider-light.png&w=1920&q=75)![Connecting your Git provider and creating a new repository](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fgit-provider-dark.png&w=1920&q=75)

    Connecting your Git provider and creating a new repository

4. ### [Project deployment](#project-deployment)

    Once the project has been cloned to your git provider, Vercel will automatically start deploying the project. This starts with [building your project](/docs/deployments/builds), then [assigning the domain](/docs/deployments/generated-urls), and finally celebrating your deployed project with confetti.

    ![Deploying a template](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fdeploy-template-light.png&w=1920&q=75)![Deploying a template](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fdeploy-template-dark.png&w=1920&q=75)

    Deploying a template

5. ### [View your dashboard](#view-your-dashboard)

    At this point, you’ve created a production deployment, with its very own domain assigned. If you continue to your [dashboard](/dashboard), you can click on the domain to preview a live, accessible URL that is instantly available on the internet.

    ![Viewing your deployment information](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fprod-view-light.png%3Flightbox&w=3840&q=75)![Viewing your deployment information](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fprod-view-dark.png%3Flightbox&w=3840&q=75)

    Viewing your deployment information

    Zoom Image

    ![Viewing your deployment information](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fprod-view-light.png%3Flightbox&w=3840&q=75)![Viewing your deployment information](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fprod-view-dark.png%3Flightbox&w=3840&q=75)

    Viewing your deployment information

6. ### [Clone the project to your machine](#clone-the-project-to-your-machine)

    Finally, you'll want to clone the source files to your local machine so that you can make some changes later. To do this from your dashboard, select the Git repository button and clone the repository.

Because you used a template, we’ve automatically included any additional environment set up as part of the template. You can customize your project by configuring environment variables and build options.

Environment Variables are key-value pairs that can be defined in your project settings for each [Environment](/docs/environment-variables#environments). Teams can also use [shared environment variables](/docs/environment-variables/shared-environment-variables) that are linked between multiple projects.

Vercel automatically configures builds settings based on your framework, but you can [customize the build](/docs/deployments/configure-a-build) in your project settings or within a [vercel.json](/docs/project-configuration) file.

## [Next Steps](#next-steps)

Next, learn how to assign a domain to your new deployment.

[

Add a domain

](/docs/getting-started-with-vercel/domains)
