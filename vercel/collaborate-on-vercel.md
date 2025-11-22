# Collaborate on Vercel

Collaboration is key in successful development projects, and Vercel offers robust features to enhance collaboration among developers. From seamless code collaboration to real-time previews with Comments, Vercel empowers your team to work together effortlessly.

## [Make Changes](#make-changes)

Now that your project is publicly available on your domain of choice, it’s time to begin making changes to it. With Vercel's automatic deployments, this won't require any extra effort. By default, when your Vercel project is connected to a Git repository, Vercel will deploy every commit that is pushed to the Git repository, regardless of which branch you're pushing it to.

A Production environment is one built from the `main` or development branch of your Git repository. A preview environment is created when you deploy from any other branch.

Vercel provides a [URL](/docs/deployments/generated-urls#generated-from-git) that reflects the latest pushes to that branch. You can find this either on your dashboard, or in a pull request, which you'll see in the next step

This connection was established for you automatically, so all you have to do is push commits, and you will start receiving links to deployments right on your Git provider.

## [Create a preview deployment](#create-a-preview-deployment)

1. ### [Make your changes](#make-your-changes)

    Create a new branch in your project and make some changes

2. ### [Commit your changes](#commit-your-changes)

    Commit those changes and create a pull request. After a few seconds, Vercel picks up the changes and starts to build and deploy your project. You can see the status of the build through the bot comment made on your PR:

    ![Vercel for GitHub deploying a pull request automatically.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Fgithub-comment-light.png&w=1920&q=75)![Vercel for GitHub deploying a pull request automatically.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Fgithub-comment-dark.png&w=1920&q=75)

    Vercel for GitHub deploying a pull request automatically.

3. ### [Inspect your deployment information](#inspect-your-deployment-information)

    Select Inspect to explore the build within your dashboard. You can see the build is within the preview environment and additional information about the deployment including: [build information](/docs/deployments/builds), a [deployment summary](/docs/deployments#resources-tab-and-deployment-summary), checks, and [domain assignment](/docs/domains). These happen for every deployment

    ![Vercel dashboard showing the preview deployment.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fpreview-dashboard-light.png&w=3840&q=75)![Vercel dashboard showing the preview deployment.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fpreview-dashboard-dark.png&w=3840&q=75)

    Vercel dashboard showing the preview deployment.

4. ### [View your deployment URL](#view-your-deployment-url)

    Return to your pull request. At this point your build should be deployed and you can select Visit Preview. You can now see your changes and share this preview URL with others.

## [Commenting on previews](#commenting-on-previews)

[Comments](/docs/comments) provide a way for your team [or friends](/docs/comments/how-comments-work#sharing) to give direct feedback on [preview deployments](/docs/deployments/environments#preview-environment-pre-production). Share with others by doing the following:

1. ### [Open your deployment](#open-your-deployment)

    Open the preview deployment that you’d like to share by selecting the Domain from the deployment information as shown in step 3 above. Alternatively, you can find it by selecting your project from the [dashboard](/dashboard), and selecting the most recent commit under Active Branches:

    ![Active branch section showing all non-production branches](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Factive-branches-light.png&w=3840&q=75)![Active branch section showing all non-production branches](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Factive-branches-dark.png&w=3840&q=75)

    Active branch section showing all non-production branches

2. ### [Authenticate with your Vercel account](#authenticate-with-your-vercel-account)

    From the Comments toolbar at the bottom of the screen, select Log in to comment and sign in with your Vercel account.

3. ### [Adjust the share settings](#adjust-the-share-settings)

    Select Share in the [Toolbar](/docs/vercel-toolbar) menu. Add the emails of people you would like to share the preview with. If you are previewing a specific commit, you may have the option to share the preview for your branch instead. This option allows you to share a preview that updates with the latest commit to the branch.

    To learn more, including other ways to share, see [Sharing Deployments](/docs/deployments/sharing-deployments).

4. ### [Collaborator needs to sign-in](#collaborator-needs-to-sign-in)

    The person you are sharing the preview with needs to have a Vercel account. To do so, they'll need to select Log in to comment and then enter their email address.

5. ### [Collaborator can comment](#collaborator-can-comment)

    Once the person you are sharing the preview with goes through the security options, they'll be ready to comment. You'll be notified of new comments through email, or when you visit the deployment.

For more information on using Comments, see [Using comments](/docs/comments/using-comments).

[

What's next?

](/docs/getting-started-with-vercel/next-steps)
