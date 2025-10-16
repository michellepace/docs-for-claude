This article digs into the syntax differences translation _Express_ and _Core_ apps as well as a [translation guide](https://shiny.posit.co/py/docs/express-to-core.html#translation-guide) to help you move from Express to Core.

The quickest way to tell whether an app is an Express app is the presence of `shiny.express` in the import statements. Common Express imports like `from shiny.express import ui, input` highlight the main difference from Core: expression of user interfaces ( `ui`) and where `input` values come from. You’ll also commonly see Core imports like `from shiny import reactive` in Express apps, highlighting the fact that things like reactivity work the same way in both modes.

To dig into more specifics, consider the following app that just displays a slider value, and notice the following:

- Core requires an `App()` object, which in turn requires a UI definition and server function.
- Core UI starts with a `ui.page_*()` call to create a page layout. It also requires output containers (i.e., `ui.output_*()`) in the UI with ids that match the corresponding `render` function.

  - In Express, these page and output containers are implicit. [1](https://shiny.posit.co/py/docs/express-to-core.html#fn1)

- Core
- Express

app.py+

99

1

2

3

4

5

6

7

8

9

10

11

12

13

from shiny import App, render, ui

app\_ui = ui.page\_fixed(

ui.input\_slider("val", "Slider label", min=0, max=100, value=50),

ui.output\_text\_verbatim("slider\_val")

)

defserver(input, output, session):

@render.text

defslider\_val():

returnf"Slider value: {input.val()}"

app = App(app\_ui, server)

app.py+

9

1

2

3

4

5

6

7

from shiny.express import input, render, ui

ui.input\_slider("val", "Slider label", min=0, max=100, value=50)

@render.text

defslider\_val():

returnf"Slider value: {input.val()}"

What's this?

Now, suppose we add a UI component that takes other components as children, like `ui.layout_columns()`. In Core, this is done by nesting [pure function](https://en.wikipedia.org/wiki/Pure_function) calls. However, in Express, UI components that take other UI components as children are context managers, so we use `with` statements instead.

- Core
- Express

app.py+

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

from shiny import App, render, ui

app\_ui = ui.page\_fixed(

ui.layout\_columns(

ui.input\_slider("val", "Slider label", min=0, max=100, value=50),

ui.output\_text\_verbatim("slider\_val")

)

)

defserver(input, output, session):

@render.text

defslider\_val():

returnf"Slider value: {input.val()}"

app = App(app\_ui, server)

app.py+

9

1

2

3

4

5

6

7

8

from shiny.express import input, render, ui

with ui.layout\_columns():

ui.input\_slider("val", "Slider label", min=0, max=100, value=50)

@render.text

defslider\_val():

returnf"Slider value: {input.val()}"

What's this?

Terminal UI

Terminal UI components (e.g. `ui.input_slider()`); that is, components that usually don’t take other UI components as children, are not context managers in Express.

HTML tags

In Express, [HTML tags](https://shiny.posit.co/py/docs/ui-html.html) can be used as both context managers and/or pure functions. For example, `ui.div(ui.h1("Hello world!"))` is also equivalent to `with ui.div(): ui.h1("Hello world!")`.

### Translation guide [Anchor](https://shiny.posit.co/py/docs/express-to-core.html\#translation-guide)

When translating an Express app to Core, the following steps are recommended:

1. Replace Express imports with Core imports (e.g., `from shiny.express import ui` -\> `from shiny import ui`).
2. Add `from shiny import App`.
3. Add the following just below the imports:

```sourceCode python
app_ui = ui.page_fixed(
    # static UI here
)

def server(input, output, session):
    # render/reactive logic here
    ...

app = App(app_ui, server)
```

4. Then, start moving the “top-level” Express logic into the UI/server:

- Identify `@render` and `@reactive` functions and move them inside `server` function.
- Add `ui.output_*()` containers to `app_ui` for each `@render` function.
- Move `ui` components (i.e., inputs and layout) and move them inside the `app_ui`.

  - Remember that, in Core, layout components like `ui.layout_columns()` are pure functions, not context managers.
- If your Express app has top-level `ui.sidebar()` and/or `ui.nav_panel()` components, you’ll need to also change `ui.page_fixed()` to `ui.page_sidebar()`/ `ui.page_navbar()`.

## Footnotes [Anchor](https://shiny.posit.co/py/docs/express-to-core.html\#footnotes-1)

1. In Express, page layout options can be controlled via `ui.page_opts()` and (at least some, for now) output containers can be controlled through their respective `@render.*()` decorators. [↩︎](https://shiny.posit.co/py/docs/express-to-core.html#fnref1)