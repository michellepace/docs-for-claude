# Next.js 16.1

Next.js 16.1 focuses on faster development workflows and improved stability, with major updates to Turbopack and tooling.

- [**Turbopack File System Caching for `next dev` (stable)**](https://nextjs.org/blog/next-16-1#turbopack-file-system-caching-for-next-dev): Improved compile times for `next dev` by default.
- [**Next.js Bundle Analyzer (experimental)**](https://nextjs.org/blog/next-16-1#nextjs-bundle-analyzer-experimental): Optimize your code with our new interactive tool.
- [**Easier debugging**](https://nextjs.org/blog/next-16-1#easier-debugging-with-next-dev---inspect): Debug your Next.js app with `next dev --inspect`.
- [**Transitive external dependencies**](https://nextjs.org/blog/next-16-1#improved-handling-of-serverexternalpackages): Turbopack can automatically handle transitive external dependencies with no warnings.

## Upgrade Today

```bash
# Use the automated upgrade CLI
npx @next/codemod@canary upgrade latest

# ...or upgrade manually
npm install next@latest react@latest react-dom@latest

# ...or start a new project
npx create-next-app@latest
```

## Turbopack File System Caching for `next dev`

Turbopack file system caching for `next dev` is now stable and on by default. Compiler artifacts are stored on disk, leading to significantly faster compile times when restarting your development server, especially in large projects.

**First route compile time benchmarks:**

| Project | Cold Start | Cached | Improvement |
| ------- | ---------- | ------ | ----------- |
| react.dev | 3.7s | 380ms | ~10× faster |
| nextjs.org | 3.5s | 700ms | ~5× faster |
| Large internal Vercel app | 15s | 1.1s | ~14× faster |

Internal applications at Vercel have been dogfooding this for the past year. To learn more about how we built file system caching for Turbopack, watch [Luke Sandberg's talk at Next.js Conf](https://nextjs.org/conf/session/are-we-turbo-yet).

Following this release, we'll be stabilizing file system caching for `next build`. See our [documentation](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache) for more information, and share your [feedback](https://github.com/vercel/next.js/discussions/87283) on the dedicated GitHub discussion.

## Next.js Bundle Analyzer (experimental)

Next.js 16.1 includes a new experimental [Bundle Analyzer](https://nextjs.org/docs/app/guides/package-bundling#nextjs-bundle-analyzer-experimental) that works with Turbopack. It makes it easier to optimize bundle sizes for both server and client code—helping improve Core Web Vitals, reduce lambda cold start times, and identify bloated dependencies.

```bash
next experimental-analyze
```

Running the command launches an interactive UI to inspect production bundles, identify large modules, and see why they're included.

![Bundle Analyzer treemap with TopNav.tsx selected](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fstatic%2Fblog%2Fnext-16-1%2Fbundle_analyzer_dark.png&w=3840&q=75)

<!--
IMAGE DESCRIPTION: The Bundle Analyzer UI shows:
- Left: Treemap where rectangle size = module byte size. Hierarchy displays [project]/node_modules/ and src/ directories
- Right: "Import chain" panel showing WHY a module is bundled, tracing from component → parent → route entry point
- Top: Route filter dropdown, Client/Server/JS/CSS/JSON/Asset tabs
- Selected module shows: output size (e.g. 34.62 KB), output chunks paths

USE CASES:
- Bloated dependencies: large rectangles in node_modules indicate heavy imports
- Import chain debugging: understand why something is bundled (e.g. single component pulling massive library)
- Server/client split issues: toggle views to spot code that shouldn't be in client bundles
- Tree-shaking failures: "(local declarations only)" annotation means only specific exports used
-->

> **Try it yourself:** [Open the interactive Bundle Analyzer demo](https://turbopack-bundle-analyzer-demo.vercel.sh/) to explore the module graph.

The Bundle Analyzer is deeply integrated into Next.js, allowing you to:

- Filter bundles by route
- View the full import chain showing why a module is included
- Trace imports across server-to-client component boundaries and dynamic imports
- View CSS and other imported asset sizes
- Switch between client and server views

## Easier Debugging with `next dev --inspect`

You can now enable the [Node.js debugger](https://nodejs.org/en/learn/getting-started/debugging) by passing `--inspect` to `next dev`. Previously this required passing `NODE_OPTIONS=--inspect` and would attach the inspector to all processes spawned by Next.js instead of only to the process running your code.

## Improved Handling of `serverExternalPackages`

Next.js allows you to keep dependencies unbundled using [`serverExternalPackages`](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages). Previously, this only worked reliably for direct dependencies. If you used a library that internally depends on something like `sqlite`, and needed to externalize `sqlite`, you'd have to add it to your own `package.json`—even though it's not your direct dependency. This workaround leaked internal implementation details, created maintenance burden, and could lead to impossible version conflicts when multiple packages required different versions of the same dependency.

Next.js 16.1 fixes this for Turbopack, which now correctly resolves and externalizes transitive dependencies in `serverExternalPackages` without additional configuration.

## Other Updates

- **20MB smaller installs**: Next.js installs are about 20MB smaller thanks to simplifications in the Turbopack file system caching layer.
- **New `next upgrade` command**: A new [`next upgrade`](https://nextjs.org/docs/app/getting-started/upgrading#latest-version) command makes upgrading easier. Going forward, you can just run this to upgrade Next.js versions.
- **MCP `get_routes` tool**: The [Next.js DevTools MCP server](https://nextjs.org/docs/app/guides/mcp) now has a `get_routes` tool to get the full list of routes in your application.
- **`generateStaticParams` timing**: Time spent on [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params) is now logged as part of the timings shown for requests in development.
- **Build worker logging**: `next build` "Collecting page data" and "Generating static pages" now log the number of worker threads used.
- **Improved async import bundling**: Turbopack has improved bundling of async imports in dev to reduce the number of chunks produced, avoiding certain pathological but real-world cases.
- **Relative source map paths**: Turbopack now produces source maps with relative file paths for server-side code, improving compatibility with Node.js and other ecosystem tools.
