# Metadata Files API Reference

@doc-version: 16.0.3

This section of the docs covers **Metadata file conventions**. File-based metadata can be defined by adding special metadata files to route segments.

Each file convention can be defined using a static file (e.g. `opengraph-image.jpg`), or a dynamic variant that uses code to generate the file (e.g. `opengraph-image.js`).

Once a file is defined, Next.js will automatically serve the file (with hashes in production for caching) and update the relevant head elements with the correct metadata, such as the asset's URL, file type, and image size.

> **Good to know**:
>
> * Special Route Handlers like [`sitemap.ts`](/docs/app/api-reference/file-conventions/metadata/sitemap.md), [`opengraph-image.tsx`](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md), and [`icon.tsx`](/docs/app/api-reference/file-conventions/metadata/app-icons.md), and other [metadata files](/docs/app/api-reference/file-conventions/metadata.md) are cached by default.
> * If using along with [`proxy.ts`](/docs/app/api-reference/file-conventions/proxy.md), [configure the matcher](/docs/app/api-reference/file-conventions/proxy.md#matcher) to exclude the metadata files.

* [favicon, icon, and apple-icon](/docs/app/api-reference/file-conventions/metadata/app-icons.md)
  * API Reference for the Favicon, Icon and Apple Icon file conventions.
* [manifest.json](/docs/app/api-reference/file-conventions/metadata/manifest.md)
  * API Reference for manifest.json file.
* [opengraph-image and twitter-image](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md)
  * API Reference for the Open Graph Image and Twitter Image file conventions.
* [robots.txt](/docs/app/api-reference/file-conventions/metadata/robots.md)
  * API Reference for robots.txt file.
* [sitemap.xml](/docs/app/api-reference/file-conventions/metadata/sitemap.md)
  * API Reference for the sitemap.xml file.
