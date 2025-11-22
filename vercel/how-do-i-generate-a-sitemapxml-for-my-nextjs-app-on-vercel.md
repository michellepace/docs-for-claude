# How do I generate a “sitemap.xml” for my Next.js app on Vercel?

Guidance on how to generate a "sitemap.xml" at build time and runtime.

![Avatar for justinvitale](/api/www/avatar?s=40&u=justinvitale "Avatar for justinvitale")Justin VitaleSenior Customer Success Engineer

[Guides](/guides)/Frameworks

1 min read Copy page

Last updated January 13, 2024

In this article, we will show you how to generate a sitemap for your [Next.js application on Vercel](https://vercel.com/docs/frameworks/nextjs).

## [Generating the Sitemap with Next.js](#generating-the-sitemap-with-next.js)

The [Next.js App Router](https://nextjs.org/docs/app) has built in support for generating sitemaps. You can use the `sitemap.(js|ts)` file convention to programmatically generate a sitemap by exporting a default function that returns an array of URLs. If using TypeScript, a [`Sitemap`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#returns) type is available.

app/sitemap.ts

```ts
import { MetadataRoute } from 'next'
 
export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: 'https://acme.com',
      lastModified: new Date(),
      changeFrequency: 'yearly',
      priority: 1,
    },
    {
      url: 'https://acme.com/about',
      lastModified: new Date(),
      changeFrequency: 'monthly',
      priority: 0.8,
    },
    {
      url: 'https://acme.com/blog',
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 0.5,
    },
  ]
}
```

Creating a sitemap with the Next.js App Router

This will generate the following `sitemap.xml` file during `next build`:

sitemap.xml

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://acme.com</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>yearly</changefreq>
    <priority>1</priority>
  </url>
  <url>
    <loc>https://acme.com/about</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://acme.com/blog</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
```

The generated sitemap for your Next.js application.
