Shiny Express has a simple syntax that makes it easy to get started. But achieving this outer simplicity requires some inner complexity. As your usage of Shiny Express becomes more advanced, you may start to encounter some of this complexity.

(In comparison, Shiny Core requires slightly more effort to learn and to write, but is more predictable and easier to reason about.)

This article peels back the curtain on Shiny Express, and reveals some of the hurdles you may run into as your apps grow. Where possible, we’ve added utilities and techniques to deal with these issues.

It’s our hope that after reading this article, you’ll have a far more complete mental model of how Shiny Express works, and be able to write more advanced apps with less friction. That being said, if you spend a lot of time using these advanced Express features, you may want to consider switching to Shiny Core.

The following information is organized into two broad topics: [Programming UI](https://shiny.posit.co/py/docs/express-in-depth.html#programming-ui) and [Shared objects](https://shiny.posit.co/py/docs/express-in-depth.html#shared-objects).

## Programming UI [Anchor](https://shiny.posit.co/py/docs/express-in-depth.html\#programming-ui)

Let’s start with an unremarkable bit of Shiny Express UI code: one card container, with a heading tag and a string inside.

app.py+

9

1

2

3

4

5

from shiny.express import ui

with ui.card(class\_="mt-3"):

ui.h3("Socrates")

"470-399 BC"

Now let’s say we want to add a second card.

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

9

from shiny.express import ui

with ui.card(class\_="mt-3"):

ui.h3("Socrates")

"470-399 BC"

with ui.card(class\_="mt-3"):

ui.h3("Immanuel Kant")

"1724-1804"

That works. But as good programmers, we don’t like to repeat ourselves. So we’ll follow programming best practices and refactor that UI logic into a function:

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

9

from shiny.express import ui

defperson(name, years):

with ui.card(class\_="mt-3"):

ui.h3(name)

years

person("Socrates", "470-399 BC")

person("Immanuel Kant", "1724-1804")

Uh oh, that doesn’t look right. Such a simple and obviously correct refactor, yet the cards are now empty!

### Interactive mode vs script mode [Anchor](https://shiny.posit.co/py/docs/express-in-depth.html\#interactive-mode-vs-script-mode)

To understand why, you first need to know that the Python interpreter has two different ways of executing code: _interactive_ mode and _script_ mode.

If you’ve been using Python for a while, you intuitively understand these modes, even if you’ve never stopped to think about it. If you run `python` and type `"hello"` into the prompt, you’ll see `hello` printed back to you. But if you create a `script.py` file containing `"hello"` and run `python script.py`, you won’t see anything printed.

In interactive mode, the Python interpreter automatically prints the result of each expression; in script mode, `print()` must be called explicitly.

Shiny Express executes your `app.py` file in interactive mode, not script mode. Even though you’re not at an interactive prompt, it still “prints” the result of each expression. Now, it doesn’t literally use the `print()` function—that would just print text to the console—but a lower-level function in Python called [`sys.displayhook`](https://docs.python.org/3/library/sys.html#sys.displayhook) that is designed to be overridden by frameworks like Shiny (and Jupyter, incidentally).

This is so important that we’ll repeat it: **Shiny Express executes your `app.py` file in interactive mode, which automatically calls `sys.displayhook()` on each expression.**

That’s why, in our simple examples above, a bare string like `"470-399 BC"` gets printed to the screen. If Shiny Express was executed in script mode (like Shiny Core is, by the way), you’d have to rewrite it as:

```sourceCode python
sys.displayhook("470-399 BC")
```

to get the string to appear in the UI. Gross.

### Functions in interactive mode [Anchor](https://shiny.posit.co/py/docs/express-in-depth.html\#functions-in-interactive-mode)

One important aspect of interactive mode is that only top-level expressions are printed. If you define a function in interactive mode, the expressions that make it up are not automatically printed.

```sourceCode python
>>> def foo():
...     "470-399 BC"
...
>>> foo()
>>>
```

Now that you understand that Shiny Express executes in interactive mode, you can see why our `person()` function doesn’t work. The UI code in the body of the `person()` function isn’t automatically printed because it’s not at the top level.

You could fix this by calling `sys.displayhook` on each UI element.

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

import sys

from shiny.express import ui

defperson(name, years):

with ui.card(class\_="mt-3"):

sys.displayhook(ui.h3(name))

sys.displayhook(years)

person("Socrates", "470-399 BC")

person("Immanuel Kant", "1724-1804")

OK, it works, but that’s pretty gross. Is there a better way to fix this problem?

The answer is yes, but before we get to that, let’s take a step back and restate what we’ve learned so far.

- You can call `sys.displayhook()` to tell Shiny Express to display something.
- Shiny Express executes `app.py` in interactive mode, not script mode.
- In interactive mode, only top-level expressions are displayed, not expressions in function bodies.

Now let’s see where this approach causes problems, and how we can solve them. We’ll start with the `person()` function we just tried to write.

### Problem: Writing UI generating functions [Anchor](https://shiny.posit.co/py/docs/express-in-depth.html\#problem-writing-ui-generating-functions)

We want to write functions that generate UI, and we don’t want to have to call `sys.displayhook()` by hand.

#### Solution: `@expressify` decorator [Anchor](https://shiny.posit.co/py/docs/express-in-depth.html\#solution-expressify-decorator)

Apply the `@expressify` decorator to a function to tell Shiny Express that the function body should be executed in interactive mode. Think of it as rewriting the function body so that `sys.displayhook()` wraps every expression.

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

from shiny.express import expressify, ui

@expressify

defperson(name, years):

with ui.card(class\_="mt-3"):

ui.h3(name)

years

person("Socrates", "470-399 BC")

person("Immanuel Kant", "1724-1804")

Shiny Core perspective

Shiny Core doesn’t need an `@expressify` decorator because it does not rely on interactive mode and never calls `sys.displayhook` anyway. Instead, UI functions are just normal functions that happen to return UI objects.

### Problem: Collect UI code into a variable [Anchor](https://shiny.posit.co/py/docs/express-in-depth.html\#problem-collect-ui-code-into-a-variable)

Sometimes we have a need to generate UI for some purpose other than directly displaying it. For example, we might want to save it to be displayed later, or multiple times.

This works OK for simple objects like strings (naturally) and even non-container UI elements—you can simply store them as variables, and that works. But in the examples above, we’re using `with ui.card():`, and you can’t store a `with` statement in a variable.

```sourceCode python
>>> x = with ui.card():
  File "<stdin>", line 1
    x = with ui.card():
        ^^^^
SyntaxError: invalid syntax
```

You also cannot use `with ui.card() as x:` syntax, because UI context managers like `ui.card()` don’t yield anything, for reasons we’ll get to in a moment.

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

9

from shiny.express import expressify, ui

with ui.card(class\_="mt-3") as x:

ui.h3("Socrates")

"470-399 BC"

x

x

x

It looks for a moment like it worked, but no, it didn’t; instead of displaying the card three times, it displayed it once. That’s because leaving the `with ui.card():` context immediately displays the entire card, and then the `x` is just assigned a `None` value, which doesn’t display anything.

#### Solution: `ui.hold()` context manager [Anchor](https://shiny.posit.co/py/docs/express-in-depth.html\#solution-ui.hold-context-manager)

The `ui.hold()` context manager allows you to collect UI code into a variable.

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

from shiny.express import expressify, ui

with ui.hold() as x:

with ui.card(class\_="mt-3"):

ui.h3("Socrates")

"470-399 BC"

x

x

x

In this case, it’s just a single card, but there’s no limit to how much or how little UI you can nest under `ui.hold()`.

Shiny Core perspective

In Shiny Core, UI objects are just normal objects, so you can assign them to variables no differently than you would an integer or a list.

### Problem: Reactively rendering UI [Anchor](https://shiny.posit.co/py/docs/express-in-depth.html\#problem-reactively-rendering-ui)

So far, all of the UI we’ve generated has been “static”—it’s generated once, when the page loads, and never changes. It’s pretty common in Shiny to want to generate UI in response to user input or server events.

We can do this in Shiny Express by using the `@render.ui` decorator, which expects a function that returns a UI object. We can combine `@expressify` and `ui.hold()` to make this work. (Spoiler alert: we’re just setting up a strawman solution here, we’ll get to the “right” way in a moment.)

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

from shiny.express import expressify, input, render, ui

ui.input\_text("name", "Name", "Socrates")

ui.input\_text("years", "Years", "470-399 BC")

@render.ui

@expressify

defperson():

with ui.hold() as result:

with ui.card(class\_="mt-3"):

ui.h3(input.name())

input.years()

return result

That does work; change the name or year inputs, and the card updates. But it’s way more boilerplate than we’d like.

#### Solution: `@render.express` decorator [Anchor](https://shiny.posit.co/py/docs/express-in-depth.html\#solution-render.express-decorator)

The `@render.express` decorator is a shorthand for that combination of `@render.ui` \+ `@expressify` \+ `ui.hold`. You can just think of it as “reactively render a chunk of Express code”.

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

from shiny.express import expressify, input, render, ui

ui.input\_text("name", "Name", "Socrates")

ui.input\_text("years", "Years", "470-399 BC")

@render.express

defperson():

with ui.card(class\_="mt-3"):

ui.h3(input.name())

input.years()

It’s almost anticlimactically simple to use, considering how much explaining we had to do to get here.

Shiny Core perspective

In Shiny Core, you should use `@render.ui` and skip `@expressify` or `ui.hold()`—they’re not needed. Instead, your render function would return a UI object directly.

### Problem: Display causes a TypeError [Anchor](https://shiny.posit.co/py/docs/express-in-depth.html\#problem-display-causes-a-typeerror)

When Express currently raises an error when attempting to display an object that is not a valid UI object. This can surface in suprising ways, for example, when calling a function to perform a side-effect (like logging) which returns an unknown class of object.

```sourceCode python
from shiny.express import session

session.on_ended(lambda: "Session ended!")
```

```sourceCode python
TypeError: Invalid tag item type: <class 'function'>. Consider calling str() on this value before treating it as a tag item.
```

### Solution: Assign to a variable [Anchor](https://shiny.posit.co/py/docs/express-in-depth.html\#solution-assign-to-a-variable)

In Express, you can assign the result of a function call to a variable to prevent displaying it, so you can use it to work around this issue.

```sourceCode python
from shiny.express import session

_ = session.on_ended(lambda: "Session ended!")
```

### Summary [Anchor](https://shiny.posit.co/py/docs/express-in-depth.html\#summary)

- When writing a function that contains Shiny Express UI code, always decorate it with `@expressify`. This tells Python to execute the function body in interactive mode, which is necessary for the UI to be displayed.
- If you want to collect UI into a variable instead of displaying it, wrap it in a `with ui.hold() as var_name:` block.
- If you want to reactively render UI, decorate the function with `@render.express`.

## Shared objects [Anchor](https://shiny.posit.co/py/docs/express-in-depth.html\#shared-objects)

For better performance, it’s often useful to have some code run _once_ when the app initializes, not every time a new connection (i.e., session) is made. All of the code in a Shiny Express `app.py` file is re-executed every time a new connection is made, so it’s not a good place to do expensive work that only needs to be done once.

Fortunately, if you move expensive code to a separate module, it will only be executed once (and objects can then be shared across sessions).

app.py×shared.py×data.csv×+

9

1

2

3

4

5

6

7

from shiny.express import render

import shared

\# Runs once per session

@render.data\_frame

defdf():

return shared.df

Shiny Core perspective

In Shiny Core, code outside of the `server` function scope runs once per startup (not per user session). See the code below for the equivalent Shiny Core app.

Show code

```sourceCode python
from shiny import App, render, ui
import pandas as pd
from pathlib import Path

df = pd.read_csv(Path(__file__).parent / "data.csv") # Read in once

app_ui = ui.page_fixed(ui.output_data_frame("dat"))

def server(input, output, session):
    @render.data_frame
    def dat():
        # Returned to each session
        return df

app = App(app_ui, server)
```

Shared reactive objects

It’s also possible to share reactive objects across sessions. This can be potentially dangerous since one users activity could impact another’s, but also quite useful in combination [`reactive.file_reader`](https://shiny.posit.co/py/api/express/reactive.file_reader.html) and [`reactive.poll`](https://shiny.posit.co/py/api/express/reactive.poll.html) to create a reactive data source that’s only polled once, no matter how many users are connected.

### Sessions [Anchor](https://shiny.posit.co/py/docs/express-in-depth.html\#sessions)

Shiny apps have an object that represent a particular user’s [session](https://shiny.posit.co/py/api/Session.html). This object is useful for a variety of more advanced tasks like [sending messages to the client](https://shiny.posit.co/py/api/Session.html#shiny.Session.send_custom_message) and [serving up session-specific data](https://shiny.posit.co/py/api/Session.html#shiny.Session.dynamic_route). In Express, you’ll need to import `session` from `shiny.express` and only use it inside a reactive function, like a `@reactive.effect`:

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

from shiny import reactive

from shiny.express import session, ui

@reactive.effect

asyncdef\_():

x = {"message": "Hello from Python!"}

await session.send\_custom\_message("send\_alert", x)

ui.tags.script(

"""

Shiny.addCustomMessageHandler("send\_alert", function(x) {

document.body.innerHTML = x.message;

});

"""

)

Shiny Core sessions

In Shiny Core, the session object is available through `server` function, and can be used anywhere in the server function scope.