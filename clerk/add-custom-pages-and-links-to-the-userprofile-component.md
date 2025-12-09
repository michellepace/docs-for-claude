---
title: Add custom pages and links to the `<UserProfile />` component
description: Learn how to add custom pages and include external links within the
  navigation sidenav of the <UserProfile /> component.
sdk: astro, chrome-extension, expo, nextjs, nuxt, react, react-router, remix,
  tanstack-react-start, vue, js-frontend
sdkScoped: "true"
canonical: /docs/:sdk:/guides/customizing-clerk/adding-items/user-profile
lastUpdated: 2025-12-03T22:33:41.000Z
availableSdks: astro,chrome-extension,expo,nextjs,nuxt,react,react-router,remix,tanstack-react-start,vue,js-frontend
notAvailableSdks: android,ios,expressjs,fastify,go,ruby,js-backend
activeSdk: nextjs
sourceFile: /docs/guides/customizing-clerk/adding-items/user-profile.mdx
---

The <SDKLink href="/docs/:sdk:/reference/components/user/user-profile" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<UserProfile /></SDKLink> component supports the addition of custom pages and external links to the component's sidenav. It only accepts the following components as children:

* `<UserButton.UserProfilePage />` or `<UserProfile.Page />` to add a <SDKLink href="/docs/:sdk:/guides/customizing-clerk/adding-items/user-profile#add-a-custom-page" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>custom page</SDKLink>.
* `<UserButton.UserProfileLink />` or `<UserProfile.Link />` to add a <SDKLink href="/docs/:sdk:/guides/customizing-clerk/adding-items/user-profile#add-a-custom-link" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>custom link</SDKLink>.

You can also <SDKLink href="/docs/:sdk:/guides/customizing-clerk/adding-items/user-profile#reorder-default-routes" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>reorder default routes</SDKLink>.

## Before you start

Before you start, it's important to understand how the `<UserProfile />` can be accessed:

* As a modal: When a user selects the <SDKLink href="/docs/:sdk:/reference/components/user/user-button" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<UserButton /></SDKLink> component and then selects the **Manage account** menu item, the `<UserProfile />` will open as a modal by default.
* As a dedicated page: You can embed the `<UserProfile />` component itself in a dedicated page.

This guide includes examples for both use cases. On the code examples, you can select one of the following two tabs to see the implementation for your preferred use case:

* `<UserButton />` tab: By default, the `<UserButton />` sets `userProfileMode='modal'`. If you are using the default settings, then you should select this tab.
* `Dedicated page` tab: If you do not want the `<UserProfile />` to open as a modal, then you should select this tab. For these examples, on the `<UserButton />` component, you need to set `userProfileMode='navigation'` and `userProfileUrl='/user-profile'`.

## Add a custom page

To add a custom page to the `<UserProfile />` component, you will need to use one of the following components, depending on the use case mentioned in the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/adding-items/user-profile#before-you-start" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>Before you start</SDKLink> section.

| Use case | Component to use |
| - | - |
| `<UserButton />` component | `<UserButton.UserProfilePage />` |
| Dedicated page with the `<UserProfile />` component | `<UserProfile.Page />` |

### Props

`<UserButton.UserProfilePage />` and `<UserProfile.Page />` accept the following props, all of which are **required**:

<Properties>
  * `label`
  * `string`

  The name that will be displayed in the navigation sidenav for the custom page.

  ***

* `labelIcon`
* `React.ReactElement`

  An icon displayed next to the label in the navigation sidenav.

  ***

* `url`
* `string`

  The path segment that will be used to navigate to the custom page. For example, if the `<UserProfile />` component is rendered at `/user`, then the custom page will be accessed at `/user/{url}` when using [path routing](/docs/guides/how-clerk-works/routing).

  ***

* `children`
* `React.ReactElement`

  The content to be rendered inside the custom page.
</Properties>

### Example

<If notSdk="js-frontend">
  <If notSdk={["astro", "vue", "nuxt"]}>
    The following example demonstrates two ways that you can render content in a custom page: **as a component** or **as a direct child**.

    <CodeBlockTabs options={["<UserButton />", "Dedicated page"]}>
      ```tsx {{ filename: 'components/Header.tsx', collapsible: true }}
      const DotIcon = () => {
        return (
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
          </svg>
        )
      }

      const CustomPage = () => {
        return (
          <div>
            <h1>Custom page</h1>
            <p>This is the content of the custom page.</p>
          </div>
        )
      }

      const Header = () => (
        <header>
          <UserButton>
            {/* You can pass the content as a component */}
            <UserButton.UserProfilePage label="Custom Page" url="custom" labelIcon={<DotIcon />}>
              <CustomPage />
            </UserButton.UserProfilePage>

            {/* You can also pass the content as direct children */}
            <UserButton.UserProfilePage label="Terms" labelIcon={<DotIcon />} url="terms">
              <div>
                <h1>Custom Terms Page</h1>
                <p>This is the content of the custom terms page.</p>
              </div>
            </UserButton.UserProfilePage>
          </UserButton>
        </header>
      )

      export default Header
      ```

      ```tsx {{ filename: 'user-profile/page.tsx', collapsible: true }}
      const DotIcon = () => {
        return (
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
          </svg>
        )
      }

      const CustomPage = () => {
        return (
          <div>
            <h1>Custom page</h1>
            <p>This is the content of the custom page.</p>
          </div>
        )
      }

      const UserProfilePage = () => (
        <UserProfile path="/user-profile" routing="path">
          {/* You can pass the content as a component */}
          <UserProfile.Page label="Custom Page" labelIcon={<DotIcon />} url="custom-page">
            <CustomPage />
          </UserProfile.Page>

          {/* You can also pass the content as direct children */}
          <UserProfile.Page label="Terms" labelIcon={<DotIcon />} url="terms">
            <div>
              <h1>Custom Terms Page</h1>
              <p>This is the content of the custom terms page.</p>
            </div>
          </UserProfile.Page>
        </UserProfile>
      )

      export default UserProfilePage
      ```
    </CodeBlockTabs>
  </If>
</If>

## Add a custom link

<If notSdk="js-frontend">
  To add a custom link to the `<UserProfile />` component, you will need to use one of the following components, depending on the use case mentioned in the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/adding-items/user-profile#before-you-start" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>Before you start</SDKLink> section.

  | Use case | Component to use |
  | - | - |
  | `<UserButton />` component | `<UserButton.UserProfileLink />` |
  | Dedicated page with the `<UserProfile />` component | `<UserProfile.Link />` |

### Props

  `<UserButton.UserProfileLink />` and `<UserProfile.Link />` accept the following props, all of which are **required**:

  <Properties>
    * `label`
    * `string`

    The name that will be displayed in the navigation sidenav for the link.

    ***

    * `labelIcon`
    * `React.ReactElement`

    An icon displayed next to the label in the navigation sidenav.

    ***

    * `url`
    * `string`

    The path segment that will be used to navigate to the custom page. For example, if the `<UserProfile />` component is rendered at `/user`, then the custom link will be navigate to `/user/{url}` when using [path routing](/docs/guides/how-clerk-works/routing).
  </Properties>

### Example

  The following example adds a custom link to the `<UserProfile />` sidenav that navigates to the homepage.

  <If notSdk={["astro", "vue", "nuxt"]}>
    <CodeBlockTabs options={["<UserButton />", "Dedicated page"]}>
      ```tsx {{ filename: 'components/Header.tsx', collapsible: true }}
      const DotIcon = () => {
        return (
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
          </svg>
        )
      }

      const Header = () => (
        <header>
          <UserButton>
            <UserButton.UserProfileLink label="Homepage" url="/" labelIcon={<DotIcon />} />
          </UserButton>
        </header>
      )

      export default Header
      ```

      ```tsx {{ filename: 'user-profile/page.tsx' }}
      const DotIcon = () => {
        return (
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
          </svg>
        )
      }

      const UserProfilePage = () => (
        <UserProfile path="/user-profile" routing="path">
          <UserProfile.Link label="Homepage" labelIcon={<DotIcon />} url="/" />
        </UserProfile>
      )

      export default UserProfilePage
      ```
    </CodeBlockTabs>
  </If>
</If>

## Reorder default routes

The `<UserProfile />` component includes two default menu items: `Account` and `Security`, in that order. You can reorder these default items by setting the `label` prop to `'account'` or `'security'`. This will target the existing default item and allow you to rearrange it.

Note that when reordering default routes, the first item in the navigation sidenav cannot be a custom link.

### Example

The following example adds a custom page as the first item in the sidenav, followed by a custom link to the homepage, and then the default `Account` and `Security` pages.

<If notSdk={["astro", "js-frontend", "vue", "nuxt"]}>
  <CodeBlockTabs options={["<UserButton />", "Dedicated page"]}>
    ```tsx {{ filename: 'components/Header.tsx', collapsible: true }}
    const DotIcon = () => {
      return (
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
          <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
        </svg>
      )
    }

    const CustomPage = () => {
      return (
        <div>
          <h1>Custom page</h1>
          <p>This is the content of the custom page.</p>
        </div>
      )
    }

    const Header = () => (
      <header>
        <UserButton>
          <UserButton.UserProfilePage label="Custom Page" url="custom" labelIcon={<DotIcon />}>
            <CustomPage />
          </UserButton.UserProfilePage>
          <UserButton.UserProfileLink label="Homepage" url="/" labelIcon={<DotIcon />} />
          <UserButton.UserProfilePage label="account" />
          <UserButton.UserProfilePage label="security" />
        </UserButton>
      </header>
    )

    export default Header
    ```

    ```tsx {{ filename: 'user-profile/page.tsx', collapsible: true }}
    const DotIcon = () => {
      return (
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
          <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
        </svg>
      )
    }

    const CustomPage = () => {
      return (
        <div>
          <h1>Custom page</h1>
          <p>This is the content of the custom page.</p>
        </div>
      )
    }

    const UserProfilePage = () => (
      <UserProfile>
        <UserProfile.Page label="Custom Page" url="custom" labelIcon={<DotIcon />}>
          <CustomPage />
        </UserProfile.Page>
        <UserProfile.Link label="Homepage" url="/" labelIcon={<DotIcon />} />
        <UserProfile.Page label="account" />
        <UserProfile.Page label="security" />
      </UserProfile>
    )

    export default UserProfilePage
    ```
  </CodeBlockTabs>
</If>
