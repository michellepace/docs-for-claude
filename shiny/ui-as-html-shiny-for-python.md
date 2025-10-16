Under the hood, Shiny UI stands on a foundation of HTML, CSS, and JavaScript. In fact, if you print a UI component in a Python REPL, you’ll see its HTML representation:

from shiny import ui

ui.input\_action\_button("btn", "Button")

```output-content

```

## Creating HTML [Anchor](https://shiny.posit.co/py/docs/ui-html.html\#creating-html)

Shiny provides some convenience for creating HTML, like `ui.markdown()`:

from shiny import ui

ui.markdown("Hello \*\*world\*\*!")

```output-content

```

Also, `ui.HTML()` for raw HTML:

from shiny import ui

ui.HTML("<p>Hello <strong>world</strong>!</p>")

```output-content

```

As well as common HTML tags like `ui.div()`, `ui.span()`, `ui.p()`, `ui.h2()`, etc.

from shiny import ui

ui.div("Hello", ui.span("world"), "!")

```output-content

```

Also, less common tags are available under `ui.tags`:

from shiny import ui

ui.tags.video(src="video.mp4")

```output-content

```

## HTML tag objects [Anchor](https://shiny.posit.co/py/docs/ui-html.html\#html-tag-objects)

One benefit working with formal `Tag` object (e.g., `ui.div()`) is that you can use its methods and attributes to:

1. Add/remove HTML attributes like `class` and `style`.
2. Add/remove child tags.
3. `show()` to view the HTML in a browser:

from shiny import ui

x = ui.div("Hello")

x.add\_style("color:red;")

\# x.show()

```output-content

```

That said, you can also provide HTML attributes when creating the `Tag` (via either named arguments or a dictionary):

from shiny import ui

\# Both of these are equivalent:

ui.a("Help", href="help.html")

ui.a({"href": "help.html"}, "Help")

```output-content

```

Reserved keywords like class

In Python, there are some reserved keywords which can’t be used as argument names, such as `class`. To get around this, you can either use a dictionary as above, or append an underscore to the argument. If there’s a trailing `_`, it will be stripped off when creating the tag object.

from shiny import ui

\# Two ways of doing the same thing

ui.a({"href": "help.html", "class": "help-link"}, "Help")

ui.a("Help", href="help.html", class\_="help-link")

<a href="help.html">Help</a>

```output-content

```

## `<head>` content [Anchor](https://shiny.posit.co/py/docs/ui-html.html\#head-content)

The `<head>` of an HTML document is a special place where you can load CSS, JavaScript, and add other “meta” content that should only be loaded once. `head_content()` provides an easy easy way to add to the `<head>`, and can be placed anywhere in the UI. For example, to add a [`robots` meta tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag):

```sourceCode python
from shiny import ui

ui.head_content(
    ui.tags.meta(name="robots", content="noindex")
)
```

If `head_content()` wants to import local files, see [here](https://shiny.posit.co/py/docs/ui-customize.html#serve-local-files) to learn how to serve local files. If you find yourself using `ui.head_content()` to import CSS and JavaScript, you may instead want to use `ui.include_css()` and `ui.include_js()`, which are covered [here](https://shiny.posit.co/py/docs/ui-customize.html#css-file). Lastly, if you’re loading files for a framework like Bootstrap, Svelte, etc. consider using `HTMLDependency()` instead (see below).

## HTML Dependencies [Anchor](https://shiny.posit.co/py/docs/ui-html.html\#html-dependencies)

`HTMLDependency()` provides a useful way to include CSS, JavaScript, other files which should _only ever be loaded once_. Most Shiny apps don’t need to worry about this problem, but if you’re creating UI components that you expect other people to use, then it’s important to be aware of `HTMLDependency()`. It’s typically used to load frameworks like Bootstrap or Svelte, and can also be included as a child of any `Tag`/ `TagList` object, so may see it used in the wild like this:

```sourceCode python
from shiny import ui

def my_ui(x):
    return ui.TagList(
        x,
        ui.HTMLDependency(
            name="my-ui",
            version="0.1.0",
            source={"subdir": ...},
            stylesheet=[{"href": "my-ui.css"}],
            script=[{"src": "my-ui.js"}],
        )
    )
```

Resolving dependencies

If multiple `HTMLDependency()` objects with the same `name` are included in the UI, then only the latest version is loaded.

Custom bindings

Learn more about HTMLDependencies in the [custom component guide](https://shiny.posit.co/py/docs/custom-component-one-off.html).

## List fragments [Anchor](https://shiny.posit.co/py/docs/ui-html.html\#list-fragments)

When you need a collaction of HTML tags, you can usually just use a Python list or tuple. However, in some more advanced situations, it’s helpful to use a `TagList`, which has some additional attributes and methods (e.g., `.render()`, `.get_dependencies()`, etc).

from shiny import ui

ui.TagList(

ui.div("Hello"),

ui.span("World"),

"!"

)

```output-content

```

## HTML-like objects [Anchor](https://shiny.posit.co/py/docs/ui-html.html\#html-like-objects)

If you’ve created a custom Python object that you’d like to be able to render as a Shiny UI object, you can either create a full-blown [Shiny binding](https://shiny.posit.co/py/docs/custom-component-one-off.html) and/or implement a [`_repr_html_` method](https://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display). The former approach is recommended if it’s important to access the object’s state from Python, while the latter is recommended if the object is just a simple container for HTML (plus, it should also work in Jupyter notebooks).