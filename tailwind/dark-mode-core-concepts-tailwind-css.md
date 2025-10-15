[Home](https://tailwindcss.com/) v4.1

`⌘K`  `Ctrl K` [Docs](https://tailwindcss.com/docs) [Blog](https://tailwindcss.com/blog) [Showcase](https://tailwindcss.com/showcase) [Sponsor](https://tailwindcss.com/sponsor) [Plus](https://tailwindcss.com/plus?ref=top) [GitHub repository](https://github.com/tailwindlabs/tailwindcss)

1. Core concepts
2. Dark mode

Core concepts

# Dark mode

Using variants to style your site in dark mode.

## [Overview](https://tailwindcss.com/docs/dark-mode\#overview)

Now that dark mode is a first-class feature of many operating systems, it's becoming more and more common to design a dark version of your website to go along with the default design.

To make this as easy as possible, Tailwind includes a `dark` variant that lets you style your site differently when dark mode is enabled:

Light mode

Writes upside-down

The Zero Gravity Pen can be used to write in any orientation,
including upside-down. It even works in outer space.

Dark mode

Writes upside-down

The Zero Gravity Pen can be used to write in any orientation,
including upside-down. It even works in outer space.

```
<div class="bg-white dark:bg-gray-800 rounded-lg px-6 py-8 ring shadow-xl ring-gray-900/5">  <div>    <span class="inline-flex items-center justify-center rounded-md bg-indigo-500 p-2 shadow-lg">      <svg class="h-6 w-6 stroke-white" ...>        <!-- ... -->      </svg>    </span>  </div>  <h3 class="text-gray-900 dark:text-white mt-5 text-base font-medium tracking-tight ">Writes upside-down</h3>  <p class="text-gray-500 dark:text-gray-400 mt-2 text-sm ">    The Zero Gravity Pen can be used to write in any orientation, including upside-down. It even works in outer space.  </p></div>
```

By default this uses the `prefers-color-scheme` CSS media feature, but you can also build sites that support [toggling dark mode manually](https://tailwindcss.com/docs/dark-mode#toggling-dark-mode-manually) by overriding the dark variant.

## [Toggling dark mode manually](https://tailwindcss.com/docs/dark-mode\#toggling-dark-mode-manually)

If you want your dark theme to be driven by a CSS selector instead of the `prefers-color-scheme` media query, override the `dark` variant to use your custom selector:

app.css

```
@import "tailwindcss";@custom-variant dark (&:where(.dark, .dark *));
```

Now instead of `dark:*` utilities being applied based on `prefers-color-scheme`, they will be applied whenever the `dark` class is present earlier in the HTML tree:

HTML

```
<html class="dark">  <body>    <div class="bg-white dark:bg-black">      <!-- ... -->    </div>  </body></html>
```

How you add the `dark` class to the `html` element is up to you, but a common approach is to use a bit of JavaScript that updates the `class` attribute and syncs that preference to somewhere like `localStorage`.

### [Using a data attribute](https://tailwindcss.com/docs/dark-mode\#using-a-data-attribute)

To use a data attribute instead of a class to activate dark mode, just override the `dark` variant with an attribute selector instead:

app.css

```
@import "tailwindcss";@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));
```

Now dark mode utilities will be applied whenever the `data-theme` attribute is set to `dark` somewhere up the tree:

HTML

```
<html data-theme="dark">  <body>    <div class="bg-white dark:bg-black">      <!-- ... -->    </div>  </body></html>
```

### [With system theme support](https://tailwindcss.com/docs/dark-mode\#with-system-theme-support)

To build three-way theme toggles that support light mode, dark mode, and your system theme, use a custom dark mode selector and the [`window.matchMedia()` API](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia) to detect the system theme and update the `html` element when needed.

Here's a simple example of how you can support light mode, dark mode, as well as respecting the operating system preference:

spaghetti.js

```
// On page load or when changing themes, best to add inline in `head` to avoid FOUCdocument.documentElement.classList.toggle(  "dark",  localStorage.theme === "dark" ||    (!("theme" in localStorage) && window.matchMedia("(prefers-color-scheme: dark)").matches),);// Whenever the user explicitly chooses light modelocalStorage.theme = "light";// Whenever the user explicitly chooses dark modelocalStorage.theme = "dark";// Whenever the user explicitly chooses to respect the OS preferencelocalStorage.removeItem("theme");
```

Again you can manage this however you like, even storing the preference server-side in a database and rendering the class on the server — it's totally up to you.

### On this page

- [Overview](https://tailwindcss.com/docs/dark-mode#overview)
- [Toggling dark mode manually](https://tailwindcss.com/docs/dark-mode#toggling-dark-mode-manually)
  - [Using a data attribute](https://tailwindcss.com/docs/dark-mode#using-a-data-attribute)
  - [With system theme support](https://tailwindcss.com/docs/dark-mode#with-system-theme-support)

![Build UIs that don’t suck — 5-day mini-course](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcourse-promo.a67fd268.jpg&w=384&q=75)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course →](https://tailwindcss.com/build-uis-that-dont-suck)

Copyright © 2025 Tailwind Labs Inc.· [Trademark Policy](https://tailwindcss.com/brand)