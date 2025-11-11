# Marimo

A python visual notebook that works like I imagined scientific notebooks should

**Assumed audience:** People interactively developing code on annoying remote clusters

[marimo](https://marimo.io/) is a Python-specific computational notebook that mostly just works. In particular, it solves many pain points of [Jupyter](https://danmackinlay.name/notebook/jupyter.html) (HT [Jean-Michel Perraud](https://au.linkedin.com/in/jean-michel-perraud-ba916078)). I think Jupyter is an ongoing disaster — a tarpit filled with problems that are each individually poisonous and on fire.

## 1 Value proposition [Anchor](https://danmackinlay.name/notebook/marimo.html\#value-proposition)

The [FAQ](https://docs.marimo.io/faq.html#faq-jupyter) explains it well, but I can summarise: **tl;dr**: Marimo is a different, imperfect compromise between the needs for reproducibility and reliability. Its abstractions are less likely to spill on my trousers than Jupyter’s are, while being more interactive than a pure Python script.

> marimo solves problems in reproducibility, maintainability, interactivity, reusability, and shareability of notebooks.
>
> **Reproducibility.** In Jupyter notebooks, the code you see doesn’t necessarily match the outputs on the page or the program state. If you delete a cell, its variables stay in memory, which other cells may still reference; users can execute cells in arbitrary order. This leads to widespread reproducibility issues. [One study](https://blog.jetbrains.com/datalore/2020/12/17/we-downloaded-10-000-000-jupyter-notebooks-from-github-this-is-what-we-learned/#consistency-of-notebooks) analysed 10 million Jupyter notebooks and found that 36% of them weren’t reproducible.
>
> In contrast, marimo guarantees that your code, outputs, and program state are consistent, eliminating hidden state and making your notebook reproducible. marimo achieves this by intelligently analysing your code and understanding the relationships between cells and automatically re-running cells as needed.
>
> **Maintainability.** marimo notebooks are stored as pure Python programs (`.py` files). This lets you version them with git; in contrast, Jupyter notebooks are stored as JSON and require [extra steps to version](https://danmackinlay.name/notebook/jupyter_file_format.html).
>
> **Interactivity.** marimo notebooks come with [UI elements](https://docs.marimo.io/faq.html#/guides/interacivity) that are automatically synchronised with Python (like sliders, dropdowns); _e.g._, scrub a slider and all cells that reference it are automatically re-run with the new value. This is [difficult to get working in Jupyter notebooks](https://danmackinlay.name/notebook/jupyter_ui.html).
>
> **Reusability.** marimo notebooks can be executed as Python scripts from the command line (since they’re stored as `.py` files). In contrast, this requires extra steps to do for Jupyter, such as copying and pasting the code out or using external frameworks. In the future, we’ll also let you import symbols (functions, classes) defined in a marimo notebook into other Python programs/notebooks, something you can’t easily do with Jupyter.
>
> **Shareability.** Every marimo notebook can double as an interactive web app, complete with UI elements, which you can serve using the `marimo run` command. This isn’t possible in Jupyter without substantial extra effort.

The prices we pay:

1. Marimo is less widely supported. Jupyter is everywhere.
2. Unlike Jupyter, Marimo does not store the output of cells, so we can’t see the output of a cell without running it (unless we introduce our own explicit caching). This is a loss, true, but that supposed “feature” of Jupyter has caused me more pain than joy, so I do not miss it. \[traumatic flashback to purging a gigabyte-sized notebook from my team git repo\]. Caching should be explicit, not impossible to avoid.
3. The “topological” execution order of cells can be confusing because it is not what Python traditionally does, although it is the only way to keep a notebook consistent. Note that notebook cells can appear in any order on the page, but they may execute in a totally different and sometimes surprising order (for example, if we made a typo and defined a variable somewhere foolish).
4. The browser UI is pretty good (better than Jupyter), but not quite as polished as my [VS Code](https://danmackinlay.name/notebook/vs_code_python.html) setup. The [VS Code integration](https://danmackinlay.name/notebook/vs_code_python.html) is a bit janky — not quite as good as the native browser version (with all due respect to the developer!).
5. Marimo has a [VS Code integration](https://danmackinlay.name/notebook/vs_code_python.html), not quite as fancy as the Jupyter integration; [make sure you use their recommended settings](https://github.com/marimo-team/vscode-marimo#python-configuration)
6. To keep execution order deterministic and names consistent, we can’t change the referent of a variable between cells. That would be fine in a functional language but is kind of tedious in Python, whose programming patterns depend on changing variable referents; this results in lots of awkwardly named things like `experiment1`, `experiment2`, etc. There are [patterns to work around it](https://docs.marimo.io/guides/coming_from/jupyter/?h=stop#adapting-to-marimos-restriction-on-redefining-variables) but they are not idiomatic in Python.
7. … Not sure yet. I’ll note problems as I discover them.

Places where marimo’s trade-offs are likely to be worthwhile for me:

1. Development of code on [HPC clusters](https://danmackinlay.name/notebook/hpc_hell.html) where we want interactivity and persistence.
2. Sharing code in a literate/exploratory way, i.e. with colleagues or students.
3. Maybe building dashboards?

Places where I might prefer Jupyter:

1. If I were working on some system that uses Jupyter but bans Marimo. This might arise in situations like Google Colab, where Jupyter is the primary interface, or in other turnkey data-science systems. A lot of people drank the Jupyter Kool-Aid.

Places where I would use neither:

1. When I am working inside VS Code on my local machine and have my IDE set up just how I like it, and have no need to share with others. Then I’ll use that and plot using the local GUI infrastructure and the local [AI coding assistants](https://danmackinlay.name/notebook/automatic_coding.html).

Note that this leaves not much of a niche for Jupyter in my life.

## 2 Installation [Anchor](https://danmackinlay.name/notebook/marimo.html\#installation)

```bash
pip install marimo
```

See [Getting Started with marimo](https://docs.marimo.io/getting_started/index.html#github-copilot) for other options.

## 3 IDE integration [Anchor](https://danmackinlay.name/notebook/marimo.html\#ide-integration)

IDE integration has been marimo’s weak suit for me so far. I use [VS Code for Python](https://danmackinlay.name/notebook/vs_code_python.html) — the marimo extension exists, but it’s somewhat janky.

I don’t tend to use it; I run marimo notebooks in the browser.

According to [this GitHub issue](https://github.com/marimo-team/vscode-marimo/issues/58), I needed the following config for VS Code to find the marimo interpreter and stop it from beachballing forever:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "marimo.marimoPath": "${workspaceFolder}/.venv/bin/marimo",
  "marimo.debug": true
}
```

If we have our local Python environment somewhere else, we need to change that too.

It seems incompatible with [ruff auto-linting](https://danmackinlay.name/notebook/vs_code_python.html#linting).

## 4 Markdown [Anchor](https://danmackinlay.name/notebook/marimo.html\#markdown)

We’ve got rich Markdown support. Nice. It might not behave as expected; Markdown is generated by Python code, so markdown cells aren’t rendered until we _execute_ them, which is different from classic notebooks such as Mathematica or Jupyter. On the other hand, it has upsides, like we can add Python code to our

I could not see it documented, but for markdown to work, the first cell in the notebook should say

```python
import marimo as mo
```

Symptoms of not doing this: the error `NameError('name 'mo' is not defined')`.

## 5 Remote access [Anchor](https://danmackinlay.name/notebook/marimo.html\#remote-access)

Marimo runs a web app we can access remotely. We can forward connections manually. Pro tip: it will automatically set up a tunnel if we run it using a [VS Code Remote](https://danmackinlay.name/notebook/vs_code_networked.html) connection.

## 6 Debugging [Anchor](https://danmackinlay.name/notebook/marimo.html\#debugging)

Interactive debuggers are supported, though this is only documented in an [image on LinkedIn](https://www.linkedin.com/posts/marimo-io_marimo-already-has-a-built-in-variable-explorer-activity-7155264683057270784-tbna/).

```python
pdb.set_trace()
breakpoint()
```

## 7 With coding assistants [Anchor](https://danmackinlay.name/notebook/marimo.html\#with-coding-assistants)

Let’s say I am using a [coding agent](https://danmackinlay.name/notebook/automatic_coding.html). Can we generate a marimo notebook?

First, note that marimo has [in-built LLM support](https://docs.marimo.io/guides/editor_features/ai_completion). I don’t use this workflow much because I am usually generating a very large codebase, and the notebook context is insufficient. Although maybe I am using it wrong?

So, consider a more general agent. The syntactic constraints of `marimo` notebooks can work sometimes, but can also be taxing. In principle, generating marimo notebooks from a coding agent is highly efficient because marimo notebooks are pure Python files. In practice there is some friction.

I’ve tested this with Claude. Claude works best when pointed to an [example marimo notebook for reference](https://danmackinlay.name/notebook/marimo.html#example-notebook). Show Claude a simple template like that and request new content or edits based on this example, rather than asking it to generate an entire notebook from scratch.

Here is a minimal prompt that might get an assistant generating `marimo` notebooks OK (it’s worked for me for a while):

- Marimo notebooks are just `.py` files with clear internal structure and marked cells.
- Each cell in marimo begins with Python code, optionally using marimo’s API (`import marimo as mo`).
- Variables cannot be redeclared across cells, and each cell forms part of a directed acyclic graph.
- Test any candidate change for syntactic validity using one of the [export commands](https://danmackinlay.name/notebook/marimo.html#export-import), e.g. `python notebook.py`.

Here is a maximal prompt: [koaning’s Claude.md file for marimo](https://gist.github.com/koaning/ce4786b532f1e0477bc89bd804907e40)

It might help to auto-run the notebook with watch mode: `marimo edit --watch notebook.py`?

## 8 Exporting/importing [Anchor](https://danmackinlay.name/notebook/marimo.html\#export-import)

Convert marimo notebooks to other formats (Markdown, Jupyter) using built-in commands:

- To markdown:

```bash
marimo export md notebook.py -o notebook.md
```

- To Jupyter:

```bash
marimo export ipynb notebook.py -o notebook.ipynb
```

- Convert markdown back to marimo:

```bash
marimo convert notebook.md > notebook.py
```

- To simply run it — use the fact it's still a Python script:

```bash
python notebook.py
```

## 9 Distributing marimo notebooks [Anchor](https://danmackinlay.name/notebook/marimo.html\#distributing-marimo-notebooks)

### 9.1 In Python packages [Anchor](https://danmackinlay.name/notebook/marimo.html\#in-python-packages)

We already know how to do this via [setuptools](https://danmackinlay.name/notebook/python_packaging.html).

### 9.2 As environments with self-contained requirements [Anchor](https://danmackinlay.name/notebook/marimo.html\#as-environments-with-self-contained-requirements)

Nifty! See the following intros

- [Serializing package requirements in marimo notebooks](https://simonwillison.net/2024/Sep/17/serializing-package-requirements-in-marimo-notebooks/)
- [Serializing package requirements in marimo notebooks \| marimo](https://marimo.io/blog/sandboxed-notebooks)

> This takes advantage of the PEP 723 inline metadata mechanism, where a code comment at the top of a Python file can list package dependencies (and their versions).
>
> I tried this out by installing marimo using uv:
>
> ```bash
> uv tool install --python=3.12 marimo
> ```
>
> Then grabbing one of their example notebooks:
>
> ```bash
> wget 'https://raw.githubusercontent.com/marimo-team/spotlights/main/001-anywidget/tldraw_colorpicker.py'
> ```
>
> And running it in a fresh dependency sandbox like this:
>
> ```bash
> marimo run --sandbox tldraw_colorpicker.py
> ```

### 9.3 In the browser [Anchor](https://danmackinlay.name/notebook/marimo.html\#in-the-browser)

[It can run (purely) in the browser without installing Python](https://blog.pyodide.org/posts/marimo/).

## 10 Tips [Anchor](https://danmackinlay.name/notebook/marimo.html\#tips)

### 10.1 Dotenv [Anchor](https://danmackinlay.name/notebook/marimo.html\#dotenv)

[dotenv](https://danmackinlay.name/notebook/dotenv.html) is [weird in marimo](https://docs.marimo.io/faq.html#how-do-i-use-dotenv):

```python
dotenv.load_dotenv(dotenv.find_dotenv(usecwd=True))
```

### 10.2 Caching some outputs [Anchor](https://danmackinlay.name/notebook/marimo.html\#caching-some-outputs)

[There is a native cache](https://docs.marimo.io/api/caching.html#marimo.cache) that caches the output of a cell when we want it to.

### 10.3 Extra UI widgets [Anchor](https://danmackinlay.name/notebook/marimo.html\#extra-ui-widgets)

Extra UI widgets? [koaning/wigglystuff: A collection of creative AnyWidgets for Python notebook environments](https://github.com/koaning/wigglystuff).

### 10.4 Quarto integration [Anchor](https://danmackinlay.name/notebook/marimo.html\#quarto-integration)

Prototype [Quarto](https://danmackinlay.name/notebook/quarto.html) integration: [marimo-quarto](https://dmadisetti.github.io/quarto-marimo/).

### 10.5 Execution order [Anchor](https://danmackinlay.name/notebook/marimo.html\#execution-order)

Execution order is worth [reading about](https://docs.marimo.io/getting_started/key_concepts.html): marimo ensures that cells are executed in a consistent order to maintain reproducibility. If we modify a cell, marimo automatically reruns any dependent cells to keep the notebook’s state consistent. That means cells are _not_ executed in the order we see them on the page, so _e.g._ we can put boilerplate imports at the end of the notebook. I would not do that because why introduce weirdness?

## 11 File format [Anchor](https://danmackinlay.name/notebook/marimo.html\#file-format)

The file format of marimo is clever. It uses _Python code_ to encode Python code. That might not sound revolutionary, but Jupyter used JSON to encode Python code, which has created [an ongoing quagmire](https://danmackinlay.name/notebook/jupyter_file_format.html).

In marimo, there are Jupyter-like cells, but they get their functionality via decorators. They also execute like normal Python code when needed. Here is an example of what a marimo notebook looks like on the inside:

```python
import marimo

__generated_with = "0.9.32"
app = marimo.App(width="medium")

@app.cell
def __():
    import marimo as mo
    return (mo,)

@app.cell
def __():
    print("Hello world")
    return

@app.cell
def __(mo):
    mo.md(
        r"""
        ## Markdown is supported

        You can write in **bold**.
        """
    )
    return

if __name__ == "__main__":
    app.run()
```

Most notebooks can be exported as plain Python scripts using the `marimo export script` command.

```bash
marimo export script your_notebook.py -o your_notebook_script.py
```

NB: This doesn’t work if [crazy asynchronous stuff](https://danmackinlay.name/notebook/python_async.html) is going on.

## 12 Example notebook [Anchor](https://danmackinlay.name/notebook/marimo.html\#example-notebook)

For priming our coding assistant, or general interest, here’s what we expect our notebooks to look like on the inside. They look much nicer when we run them in `marimo edit` mode.

```python
import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")

@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # example notebook

    this is a markdown cell
    """
    )
    return

@app.cell
def _():
    a = "bar"
    c = "foo"
    d = "baz"
    def example_function(*args):
        return f"return: `args` {args} and local `a` {a}"
    return a, c, d, example_function

@app.cell
def _(c, d, example_function):
    b = example_function(d, c)
    print(b)
    # Expected response
    # return: `args` ('baz', 'foo') and local `a` bar
    return

@app.cell
def _(a, c, d):
    print(a, c, d)
    # Expected response
    # bar foo baz
    return

if __name__ == "__main__":
    app.run()
```
