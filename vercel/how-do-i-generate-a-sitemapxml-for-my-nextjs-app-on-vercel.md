# How do I generate a “sitemap.xml” for my Next.js app on Vercel?

Guidance on how to generate a "sitemap.xml" at build time and runtime.

![Justin VitaleSenior Customer Success Engineer](https://vercel.com/api/www/avatar?s=40&u=justinvitale)

[Guides](https://vercel.com/guides)/Frameworks

1 min read Copy page

Last updated January 12, 2024

In this article, we will show you how to generate a sitemap for your [Next.js application on Vercel](https://vercel.com/docs/frameworks/nextjs).

## [Generating the Sitemap with Next.js](https://vercel.com/guides/how-do-i-generate-a-sitemap-for-my-nextjs-app-on-vercel\#generating-the-sitemap-with-next.js)

The [Next.js App Router](https://nextjs.org/docs/app) has built in support for generating sitemaps. You can use the `sitemap.(js|ts)` file convention to programmatically generate a sitemap by exporting a default function that returns an array of URLs. If using TypeScript, a [`Sitemap`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#returns) type is available.

app/sitemap.ts

```tsx
1import { MetadataRoute } from 'next'

2

3export default function sitemap(): MetadataRoute.Sitemap {

4  return [\
\
5    {\
\
6      url: 'https://acme.com',\
\
7      lastModified: new Date(),\
\
8      changeFrequency: 'yearly',\
\
9      priority: 1,\
\
10    },\
\
11    {\
\
12      url: 'https://acme.com/about',\
\
13      lastModified: new Date(),\
\
14      changeFrequency: 'monthly',\
\
15      priority: 0.8,\
\
16    },\
\
17    {\
\
18      url: 'https://acme.com/blog',\
\
19      lastModified: new Date(),\
\
20      changeFrequency: 'weekly',\
\
21      priority: 0.5,\
\
22    },\
\
23  ]

24}
```

Creating a sitemap with the Next.js App Router

This will generate the following `sitemap.xml` file during `next build`:

sitemap.xml

```html
1<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

2  <url>

3    <loc>https://acme.com</loc>

4    <lastmod>2023-04-06T15:02:24.021Z</lastmod>

5    <changefreq>yearly</changefreq>

6    <priority>1</priority>

7  </url>

8  <url>

9    <loc>https://acme.com/about</loc>

10    <lastmod>2023-04-06T15:02:24.021Z</lastmod>

11    <changefreq>monthly</changefreq>

12    <priority>0.8</priority>

13  </url>

14  <url>

15    <loc>https://acme.com/blog</loc>

16    <lastmod>2023-04-06T15:02:24.021Z</lastmod>

17    <changefreq>weekly</changefreq>

18    <priority>0.5</priority>

19  </url>

20</urlset>
```

The generated sitemap for your Next.js application.

Was this helpful?

supported.

Send
