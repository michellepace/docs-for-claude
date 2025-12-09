---
title: Add custom pages and links to the `<OrganizationProfile />` component
description: Learn how to add custom pages and include external links within the
  navigation sidenav of the <OrganizationProfile /> component.
sdk: astro, chrome-extension, expo, nextjs, nuxt, react, react-router, remix,
  tanstack-react-start, vue, js-frontend
sdkScoped: "true"
canonical: /docs/:sdk:/guides/customizing-clerk/adding-items/organization-profile
lastUpdated: 2025-12-03T22:33:41.000Z
availableSdks: astro,chrome-extension,expo,nextjs,nuxt,react,react-router,remix,tanstack-react-start,vue,js-frontend
notAvailableSdks: android,ios,expressjs,fastify,go,ruby,js-backend
activeSdk: nextjs
sourceFile: /docs/guides/customizing-clerk/adding-items/organization-profile.mdx
---

The <SDKLink href="/docs/:sdk:/reference/components/organization/organization-profile" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<OrganizationProfile /></SDKLink> component supports the addition of custom pages and external links to the component's sidenav. It only accepts the following components as children:

* `<OrganizationSwitcher.OrganizationProfilePage />` or `<OrganizationProfile.Page />` to add a <SDKLink href="/docs/:sdk:/guides/customizing-clerk/adding-items/organization-profile#add-a-custom-page" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>custom page</SDKLink>.
* `<OrganizationSwitcher.OrganizationProfileLink />` or `<OrganizationProfile.Link />` to add a <SDKLink href="/docs/:sdk:/guides/customizing-clerk/adding-items/organization-profile#add-a-custom-link" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>custom link</SDKLink>.

You can also <SDKLink href="/docs/:sdk:/guides/customizing-clerk/adding-items/organization-profile#reorder-default-routes" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>reorder default routes</SDKLink>.

## Before you start

Before you start, it's important to understand how the `<OrganizationProfile />` can be accessed:

* As a modal: When a user selects the <SDKLink href="/docs/:sdk:/reference/components/organization/organization-switcher" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]} code={true}>\<OrganizationSwitcher /></SDKLink> component and then selects the **Manage Organization** option, the `<OrganizationProfile />` will open as a modal by default.
* As a dedicated page: You can embed the `<OrganizationProfile />` component itself in a dedicated page.

This guide includes examples for both use cases. On the code examples, you can select one of the following two tabs to see the implementation for your preferred use case:

* `<OrganizationSwitcher />` tab: By default, the `<OrganizationSwitcher />` sets `organizationProfileMode='modal'`. If you are using the default settings, then you should select this tab.
* `Dedicated page` tab: If you do not want the `<OrganizationProfile />` to open as a modal, then you should select this tab. For these examples, on the `<OrganizationSwitcher />` component, you need to set `organizationProfileMode='navigation'` and `organizationProfileUrl='/organization-profile'`.

## Add a custom page

To add a custom page to the `<OrganizationProfile />` component, you will need to use one of the following components, depending on the use case mentioned in the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/adding-items/organization-profile#before-you-start" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>Before you start</SDKLink> section.

| Use case | Component to use |
| - | - |
| `<OrganizationSwitcher />` component | `<OrganizationSwitcher.OrganizationProfilePage />` |
| Dedicated page with the `<OrganizationProfile />` component | `<OrganizationProfile.Page />` |

### Props

`<OrganizationSwitcher.OrganizationProfilePage />` and `<OrganizationProfile.Page />` accept the following props, all of which are **required**:

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

  The path segment that will be used to navigate to the custom page. For example, if the `<OrganizationProfile />` component is rendered at `/organization`, then the custom page will be accessed at `/organization/{url}` when using [path routing](/docs/guides/how-clerk-works/routing).

  ***

* `children`
* `React.ReactElement`

  The content to be rendered inside the custom page.
</Properties>

### Example

<If notSdk="js-frontend">
  <If notSdk={["astro", "vue", "nuxt"]}>
    The following example demonstrates two ways that you can render content in a custom page: **as a component** or **as a direct child**.

    <CodeBlockTabs options={["<OrganizationSwitcher />", "Dedicated page"]}>
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
          <OrganizationSwitcher>
            {/* You can pass the content as a component */}
            <OrganizationSwitcher.OrganizationProfilePage
              label="Custom Page"
              url="custom"
              labelIcon={<DotIcon />}
            >
              <CustomPage />
            </OrganizationSwitcher.OrganizationProfilePage>

            {/* You can also pass the content as direct children */}
            <OrganizationSwitcher.OrganizationProfilePage
              label="Terms"
              labelIcon={<DotIcon />}
              url="terms"
            >
              <div>
                <h1>Custom Terms Page</h1>
                <p>This is the content of the custom terms page.</p>
              </div>
            </OrganizationSwitcher.OrganizationProfilePage>
          </OrganizationSwitcher>
        </header>
      )

      export default Header
      ```

      ```tsx {{ filename: 'organization-profile/page.tsx', collapsible: true }}
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

      const OrganizationProfilePage = () => (
        <OrganizationProfile path="/organization-profile" routing="path">
          {/* You can pass the content as a component */}
          <OrganizationProfile.Page label="Custom Page" labelIcon={<DotIcon />} url="custom-page">
            <CustomPage />
          </OrganizationProfile.Page>

          {/* You can also pass the content as direct children */}
          <OrganizationProfile.Page label="Terms" labelIcon={<DotIcon />} url="terms">
            <div>
              <h1>Custom Terms Page</h1>
              <p>This is the content of the custom terms page.</p>
            </div>
          </OrganizationProfile.Page>
        </OrganizationProfile>
      )

      export default OrganizationProfilePage
      ```
    </CodeBlockTabs>
  </If>
</If>

## Add a custom link

<If notSdk="js-frontend">
  To add a custom link to the `<OrganizationProfile />` navigation sidenav, you will need to use one of the following components, depending on the use case mentioned in the <SDKLink href="/docs/:sdk:/guides/customizing-clerk/adding-items/organization-profile#before-you-start" sdks={["astro","chrome-extension","expo","nextjs","nuxt","react","react-router","remix","tanstack-react-start","vue","js-frontend"]}>Before you start</SDKLink> section.

  | Use case | Component to use |
  | - | - |
  | `<OrganizationSwitcher />` component | `<OrganizationSwitcher.OrganizationProfileLink />` |
  | Dedicated page with the `<OrganizationProfile />` component | `<OrganizationProfile.Link />` |

### Props

  `<OrganizationSwitcher.OrganizationProfileLink />` and `<OrganizationProfile.Link />` accept the following props, all of which are **required**:

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

    The full URL or path that will be used to navigate to the external link. For path segments, if the `<OrganizationProfile />` component is rendered at `/organization`, then the external link will be accessed at `/organization/{url}` when using [path routing](/docs/guides/how-clerk-works/routing).
  </Properties>

### Example

  The following example adds a custom link to the `<OrganizationProfile />` sidenav that navigates to the homepage.

  <If notSdk={["astro", "vue", "nuxt"]}>
    <CodeBlockTabs options={["<OrganizationSwitcher />", "Dedicated page"]}>
      ```tsx {{ filename: 'components/Header.tsx' }}
      const DotIcon = () => {
        return (
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
          </svg>
        )
      }

      const Header = () => (
        <header>
          <OrganizationSwitcher>
            <OrganizationSwitcher.OrganizationProfileLink
              label="Homepage"
              url="/"
              labelIcon={<DotIcon />}
            />
          </OrganizationSwitcher>
        </header>
      )

      export default Header
      ```

      ```tsx {{ filename: 'organization-profile/page.tsx' }}
      const DotIcon = () => {
        return (
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
          </svg>
        )
      }

      const OrganizationProfilePage = () => (
        <OrganizationProfile path="/organization-profile" routing="path">
          <OrganizationProfile.Link label="Homepage" labelIcon={<DotIcon />} url="/" />
        </OrganizationProfile>
      )

      export default OrganizationProfilePage
      ```
    </CodeBlockTabs>
  </If>
</If>

## Reorder default routes

The `<OrganizationProfile />` component includes two default menu items: `Members` and `General`, in that order. You can reorder these default items by setting the `label` prop to `'members'` or `'general'`. This will target the existing default item and allow you to rearrange it.

Note that when reordering default routes, the first item in the navigation sidenav cannot be a custom link.

### Example

The following example adds a custom page as the first item in the sidenav, followed by a custom link to the homepage, and then the default `Members` and `General` pages.

<If notSdk={["astro", "js-frontend", "vue", "nuxt"]}>
  <CodeBlockTabs options={["<OrganizationSwitcher />", "Dedicated Page"]}>
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
        <OrganizationSwitcher>
          <OrganizationSwitcher.OrganizationProfilePage
            label="Custom Page"
            url="custom"
            labelIcon={<DotIcon />}
          >
            <CustomPage />
          </OrganizationSwitcher.OrganizationProfilePage>
          <OrganizationSwitcher.OrganizationProfileLink
            label="Homepage"
            url="/"
            labelIcon={<DotIcon />}
          />
          <OrganizationSwitcher.OrganizationProfilePage label="members" />
          <OrganizationSwitcher.OrganizationProfilePage label="general" />
        </OrganizationSwitcher>
      </header>
    )

    export default Header
    ```

    ```tsx {{ filename: 'organization-profile/page.tsx', collapsible: true }}
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

    const OrganizationProfilePage = () => (
      <OrganizationProfile>
        <OrganizationProfile.Page label="Custom Page" url="custom" labelIcon={<DotIcon />}>
          <CustomPage />
        </OrganizationProfile.Page>
        <OrganizationProfile.Link label="Homepage" url="/" labelIcon={<DotIcon />} />
        <OrganizationProfile.Page label="members" />
        <OrganizationProfile.Page label="general" />
      </OrganizationProfile>
    )

    export default OrganizationProfilePage
    ```
  </CodeBlockTabs>
</If>
