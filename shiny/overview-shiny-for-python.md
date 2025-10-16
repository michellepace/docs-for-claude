Welcome to the learn Shiny overview! Here we’ll introduce Shiny’s capabilities and link to articles where you can learn more. In the [next article](https://shiny.posit.co/py/docs/user-interfaces.html), we’ll cover more user interface (UI) [components](https://shiny.posit.co/py/docs/overview.html#components) by building this dashboard:

![](https://shiny.posit.co/py/docs/assets/tipping-dashboard.png)

A Shiny dashboard with visuals for exploring restaurant tips (covered in the [next article](https://shiny.posit.co/py/docs/user-interfaces.html)).

Editable examples

Many examples on this site have a code editor for modifying the source code for a Shiny app (which runs entirely in the browser, thanks to [shinylive](https://shiny.posit.co/py/get-started/shinylive.html)). If you’d like to run any examples locally, first [install](https://shiny.posit.co/py/get-started/install.html) Shiny locally, then [create and run](https://shiny.posit.co/py/get-started/create-run.html) by copy/paste relevant code into the `app.py` file (created by `shiny create`).

### Basics [Anchor](https://shiny.posit.co/py/docs/overview.html\#basics)

Shiny apps typically start with [input components](https://shiny.posit.co/py/components/#inputs) to gather information from a user, which are then used to reactively render [output components](https://shiny.posit.co/py/components/#outputs). Here’s a basic example that displays a slider’s value as formatted text.

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

This example demonstrates the basic mechanics behind Shiny apps:

- Inputs are created via `ui.input_*()` functions.

  - The first argument is the input’s `id`, which is used to read the input’s value.
- Outputs are created by decorating a function with `@render.*`.

  - Inside a `render` function, `input` values can be read [reactively](https://shiny.posit.co/py/docs/overview.html#reactivity).
  - When those `input` values change, Shiny knows how to minimally re-render output.
- This example happens to use `shiny.express` which, [compared to core Shiny](https://shiny.posit.co/py/docs/express-vs-core.html), reduces the amount of code required.

### Components [Anchor](https://shiny.posit.co/py/docs/overview.html\#components)

Shiny includes many useful user interface ( `ui`) components for creating inputs, outputs, displaying messages, and more. For brevity sake, we’ll highlight just a few output and layout components here, but for a more comprehensive list, see the [components gallery](https://shiny.posit.co/py/components).

#### Outputs [Anchor](https://shiny.posit.co/py/docs/overview.html\#outputs)

Shiny makes it easy to create dynamic plots, tables, and other interactive widgets. All you need to do is apply a `@render` decorator to a function that returns a suitable object. Shiny includes a wide variety of these decorators in its `render` module, but Shiny [extensions](https://shiny.posit.co/py/docs/custom-component-one-off.html) like `shinywidgets` provide additional decorators for rendering other kinds of outputs, like [Jupyter Widgets](https://shiny.posit.co/py/docs/jupyter-widgets.html).

- Plots
- Tables
- Widgets

To include a plot in an application, apply `@render.plot` to a function that creates a [matplotlib](https://matplotlib.org/) visual. Note that packages like [seaborn](https://seaborn.pydata.org/), [plotnine](https://plotnine.readthedocs.io/en/stable/), [pandas](https://pandas.pydata.org/), etc., are all compatible (as long as they create a matplotlib visual).

app.py×requirements.txt×+

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

16

17

from shiny.express import input, render, ui

ui.input\_selectize(

"var", "Select variable",

choices=\["bill\_length\_mm", "body\_mass\_g"\]

)

@render.plot

defhist():

from matplotlib import pyplot as plt

from palmerpenguins import load\_penguins

df = load\_penguins()

df\[input.var()\].hist(grid=False)

plt.xlabel(input.var())

plt.ylabel("count")

Apply `@render.data_frame` to any code that returns a [pandas](https://pandas.pydata.org/) or [polars](https://pola.rs/) DataFrame for a basic table. For more sophisticated tables, you can use [`render.DataGrid`](https://shiny.posit.co/py/components/outputs/data-grid.html) to add things like filters to your table.

app.py×requirements.txt×+

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

from shiny.express import input, render, ui

ui.input\_selectize(

"var", "Select variable",

choices=\["bill\_length\_mm", "body\_mass\_g"\]

)

@render.data\_frame

defhead():

from palmerpenguins import load\_penguins

df = load\_penguins()

return df\[\["species", input.var()\]\]

See the [Jupyter Widgets article](https://shiny.posit.co/py/docs/jupyter-widgets.html) for more information on rendering Jupyter Widgets in Shiny.

- Altair
- Bokeh
- Plotly
- Pydeck
- Other

app.py×requirements.txt×+

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

16

17

18

from shiny.express import input, ui

from shinywidgets import render\_altair

ui.input\_selectize(

"var", "Select variable",

choices=\["bill\_length\_mm", "body\_mass\_g"\]

)

@render\_altair

defhist():

import altair as alt

from palmerpenguins import load\_penguins

df = load\_penguins()

return (

alt.Chart(df)

.mark\_bar()

.encode(x=alt.X(f"{input.var()}:Q", bin=True), y="count()")

)

app.py×requirements.txt×+

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

16

17

18

19

20

21

22

from shiny.express import input, ui

from shinywidgets import render\_bokeh

ui.input\_selectize(

"var", "Select variable",

choices=\["bill\_length\_mm", "body\_mass\_g"\]

)

@render\_bokeh

defhist():

from bokeh.plotting import figure

from palmerpenguins import load\_penguins

p = figure(x\_axis\_label=input.var(), y\_axis\_label="count")

bins = load\_penguins()\[input.var()\].value\_counts().sort\_index()

p.quad(

top=bins.values,

bottom=0,

left=bins.index - 0.5,

right=bins.index + 0.5,

)

return p

app.py×requirements.txt×+

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

from shiny.express import input, ui

from shinywidgets import render\_plotly

ui.input\_selectize(

"var", "Select variable",

choices=\["bill\_length\_mm", "body\_mass\_g"\]

)

@render\_plotly

defhist():

import plotly.express as px

from palmerpenguins import load\_penguins

df = load\_penguins()

return px.histogram(df, x=input.var())

app.py×requirements.txt×+

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

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

import pydeck as pdk

import shiny.express

from shinywidgets import render\_pydeck

@render\_pydeck

defmap():

UK\_ACCIDENTS\_DATA = "https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv"

layer = pdk.Layer(

"HexagonLayer", \# \`type\` positional argument is here

UK\_ACCIDENTS\_DATA,

get\_position=\["lng", "lat"\],

auto\_highlight=True,

elevation\_scale=50,

pickable=True,

elevation\_range=\[0, 3000\],

extruded=True,

coverage=1,

)

\# Set the viewport location

view\_state = pdk.ViewState(

longitude=-1.415,

latitude=52.2323,

zoom=6,

min\_zoom=5,

max\_zoom=15,

pitch=40.5,

bearing=-27.36,

)

\# Combined all of it and render a viewport

return pdk.Deck(layers=\[layer\], initial\_view\_state=view\_state)

Many [other awesome Python packages](https://github.com/markusschanta/awesome-jupyter#visualization) provide widgets that are compatible with Shiny. In general, you can render them by applying the `@render_widget` decorator.

```sourceCode python
import shiny.express
from shinywidgets import render_widget

@render_widget
def widget():
    # Widget code goes here
    ...
```

#### Layouts [Anchor](https://shiny.posit.co/py/docs/overview.html\#layouts)

Shiny provides a full suite of [layout components](https://shiny.posit.co/py/layouts) which help with arranging multiple inputs and outputs in a variety of ways. As seen below, with `shiny.express`, layout components (e.g., `ui.sidebar()`) can be used as context managers to help with nesting and readability.

- Sidebar
- Multi-page
- Multi-panel
- Multi-column

app.py×requirements.txt×+

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

import plotly.express as px

from shiny.express import input, render, ui

from shinywidgets import render\_widget

ui.page\_opts(title="Sidebar layout", fillable=True)

with ui.sidebar():

ui.input\_select("var", "Select variable", choices=\["total\_bill", "tip"\])

@render\_widget

defhist():

return px.histogram(px.data.tips(), input.var())

app.py×requirements.txt×+

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

16

17

18

19

import plotly.express as px

from shiny.express import input, render, ui

from shinywidgets import render\_widget

ui.page\_opts(title="Multi-page example", fillable=True)

with ui.sidebar():

ui.input\_select("var", "Select variable", choices=\["total\_bill", "tip"\])

with ui.nav\_panel("Plot"):

@render\_widget

defhist():

return px.histogram(px.data.tips(), input.var())

with ui.nav\_panel("Table"):

@render.data\_frame

deftable():

return px.data.tips()

app.py×requirements.txt×+

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

16

17

18

19

20

import plotly.express as px

from shiny.express import input, render, ui

from shinywidgets import render\_widget

ui.page\_opts(title="Multi-tab example", fillable=True)

with ui.sidebar():

ui.input\_select("var", "Select variable", choices=\["total\_bill", "tip"\])

with ui.navset\_card\_underline(title="Penguins"):

with ui.nav\_panel("Plot"):

@render\_widget

defhist():

return px.histogram(px.data.tips(), input.var())

with ui.nav\_panel("Table"):

@render.data\_frame

deftable():

return px.data.tips()

app.py×requirements.txt×+

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

16

17

import plotly.express as px

from shiny.express import input, render, ui

from shinywidgets import render\_widget

ui.page\_opts(title="Multi-column example")

ui.input\_select("var", "Select variable", choices=\["total\_bill", "tip"\])

with ui.layout\_columns(height="300px"):

@render\_widget

defhist():

return px.histogram(px.data.tips(), input.var())

@render.data\_frame

deftable():

return px.data.tips()

Quarto integration

Shiny also integrates well with [Quarto](https://quarto.org/), allowing you to leverage its web-based output formats (e.g., [dashboards](https://quarto.org/docs/dashboards/interactivity/shiny-python/index.html)) in combination with Shiny outputs and reactivity.

### Reactivity [Anchor](https://shiny.posit.co/py/docs/overview.html\#reactivity)

Shiny uses something called [transparent reactivity](https://blog.machinezoo.com/transparent-reactive-programming) to automatically infer relationships between components, and minimally re-render as needed when dependencies change. [1](https://shiny.posit.co/py/docs/overview.html#fn1) As a result, apps naturally retain performance as they grow in size, without workarounds like caching or memoization. All Shiny apps are also built on the same small set of [reactive foundations](https://shiny.posit.co/py/docs/reactive-foundations.html), each of which are simple and easy to learn, but can be combined in novel ways to create seriously sophisticated and performant apps.

To demonstrate how Shiny minimally re-renders, consider the following app which contains two different plots, each of which depends on a different input. When the first input changes, Shiny knows to only re-render the first plot, and vice versa.

app.py×requirements.txt×+

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

16

17

18

19

20

21

22

import plotly.express as px

from shiny.express import input, render, ui

from shinywidgets import render\_plotly

tips = px.data.tips()

with ui.layout\_columns():

@render\_plotly

defplot1():

p = px.histogram(tips, x=input.var1())

p.update\_layout(height=200, xaxis\_title=None)

return p

@render\_plotly

defplot2():

p = px.histogram(tips, x=input.var2())

p.update\_layout(height=200, xaxis\_title=None)

return p

with ui.layout\_columns():

ui.input\_select("var1", None, choices=\["total\_bill", "tip"\], width="100%")

ui.input\_select("var2", None, choices=\["tip", "total\_bill"\], width="100%")

Shiny also knows when outputs are visible or not, and so, will only call `render` functions when needed. For example, in the app below, the `table` function doesn’t get called until the “Table” page is selected.

app.py×requirements.txt×+

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

16

17

18

19

20

21

22

import plotly.express as px

from shiny.express import input, render, ui

from shinywidgets import render\_plotly

tips = px.data.tips()

with ui.sidebar():

ui.input\_selectize("var", "Select variable", choices=\["total\_bill", "tip"\])

ui.nav\_spacer()

with ui.nav\_panel("Plot"):

@render\_plotly

defplot():

p = px.histogram(tips, x=input.var())

p.update\_layout(height=225)

return p

with ui.nav\_panel("Table"):

@render.data\_frame

deftable():

return tips\[\[input.var()\]\]

Learn more

For a more in-depth look at reactivity, check out the [reactivity article](https://shiny.posit.co/py/docs/reactive-foundations.html).

### Starter templates [Anchor](https://shiny.posit.co/py/docs/overview.html\#templates)

Once you’ve [installed](https://shiny.posit.co/py/get-started/install.html) Shiny, the `shiny create` CLI command provides access to a collection of useful starter templates. This command walks you through a series of prompts to help you get started quickly with a helpful example. One great option is the dashboard template, which can be created with:

```sourceCode bash
shiny create --template dashboard
```

![](https://shiny.posit.co/py/docs/assets/dashboard-template.png)

The resulting dashboard generated by the dashboard template

Development workflow

See how to [create and run apps](https://shiny.posit.co/py/get-started/create-run.html) for more information developing Shiny apps locally. Also keep in mind you can develop apps in the browser using the [playground](https://shinylive.io/py/examples/).

### Extensible foundation [Anchor](https://shiny.posit.co/py/docs/overview.html\#extensible)

Shiny is built on a foundation of web standards, allowing you to incrementally adopt custom HTML, CSS, and/or JavaScript as needed. In fact, Shiny UI components themselves are built on a Python representation of HTML/CSS/JavaScript, which you can see by printing them in a Python REPL:

```sourceCode python
>>> from shiny import ui
>>> ui.input_action_button("btn", "Button")
<button class="btn btn-default action-button" id="btn" type="button">Button</button>
```

And, since [UI is HTML](https://shiny.posit.co/py/docs/ui-html.html), you can gently introduce HTML/CSS/JavaScript as needed in your apps to customize without having to learn complicated build tooling and frameworks. However, if you’re versed in web programming, you can also use Shiny to create [custom components](https://shiny.posit.co/py/docs/custom-component-one-off.html) that leverage your favorite JavaScript framework from Python.

### Next steps [Anchor](https://shiny.posit.co/py/docs/overview.html\#next-steps)

Next, we’ll learn more about Shiny components and layouts by making a dashboard.

## Footnotes [Anchor](https://shiny.posit.co/py/docs/overview.html\#footnotes-1)

1. If you’re familiar with JavaScript, you may find a lot of similarities between Shiny and reactivity in modern JS frameworks like [solidjs](https://www.solidjs.com/), [mobx](https://mobx.js.org/computeds.html), and [svelte](https://svelte.dev/blog/runes). [↩︎](https://shiny.posit.co/py/docs/overview.html#fnref1)