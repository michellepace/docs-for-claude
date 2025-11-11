# marimo

marimo is an [open-source](https://github.com/marimo-team/marimo) reactive
Python notebook: run a cell or interact with a UI element, and marimo
automatically runs dependent cells (or [marks them as\\
stale](https://docs.marimo.io/guides/reactivity/#configuring-how-marimo-runs-cells)), keeping code
and outputs consistent and preventing bugs before they happen. Every marimo
notebook is stored as pure Python (Git-friendly), executable as a script, and
deployable as an app; while stored as Python, marimo notebooks also have native
support for SQL.

Built from the ground up

marimo was built from the ground up to solve [well-known problems associated with traditional notebooks](https://docs.marimo.io/faq.html#faq-jupyter).

[install with pip](https://docs.marimo.io/#__tabbed_1_1)[install with uv](https://docs.marimo.io/#__tabbed_1_2)[install with conda](https://docs.marimo.io/#__tabbed_1_3)

```bash
pip install marimo && marimo tutorial intro
```

```bash
uv add marimo && uv run marimo tutorial intro
```

```bash
conda install -c conda-forge marimo && marimo tutorial intro
```

Developer experience is core to marimo, with an emphasis on
reproducibility, maintainability, composability, and shareability.

## Highlights [¶](https://docs.marimo.io/\#highlights "Permanent link")

- 🚀 **batteries-included:** replaces `jupyter`, `streamlit`, `jupytext`, `ipywidgets`, `papermill`, and more
- ⚡️ **reactive**: run a cell, and marimo reactively [runs all dependent cells](https://docs.marimo.io/guides/reactivity/) or [marks them as stale](https://docs.marimo.io/#expensive-notebooks)
- 🖐️ **interactive:** [bind sliders, tables, plots, and more](https://docs.marimo.io/guides/interactivity/) to Python — no callbacks required
- 🐍 **git-friendly:** stored as `.py` files
- 🛢️ **designed for data**: query dataframes, databases, warehouses, and lakehouses [with SQL](https://docs.marimo.io/guides/working_with_data/sql/); filter and search [dataframes](https://docs.marimo.io/guides/working_with_data/dataframes/)
- 🤖 **AI-native**: [generate cells with AI](https://docs.marimo.io/guides/generate_with_ai/) tailored for data work
- 🔬 **reproducible:** [no hidden state](https://docs.marimo.io/guides/reactivity/), deterministic execution, [built-in package management](https://docs.marimo.io/guides/editor_features/package_management/)
- 🏃 **executable:** [execute as a Python script](https://docs.marimo.io/guides/scripts/), parameterized by CLI args
- 🛜 **shareable**: [deploy as an interactive web app](https://docs.marimo.io/guides/apps/) or [slides](https://docs.marimo.io/guides/apps/#slides-layout), [run in the browser via WASM](https://docs.marimo.io/guides/wasm/)
- 🧩 **reusable:** [import functions and classes](https://docs.marimo.io/guides/reusing_functions/) from one notebook to another
- 🧪 **testable:** [run pytest](https://docs.marimo.io/guides/testing/) on notebooks
- ⌨️ **a modern editor**: [GitHub Copilot](https://docs.marimo.io/guides/editor_features/ai_completion/#github-copilot), [AI assistants](https://docs.marimo.io/guides/editor_features/ai_completion/), vim keybindings, variable explorer, and [more editor features](https://docs.marimo.io/guides/editor_features/)

## A reactive programming environment [¶](https://docs.marimo.io/\#a-reactive-programming-environment "Permanent link")

marimo guarantees your notebook code, outputs, and program state are consistent. This [solves many problems](https://docs.marimo.io/faq/#faq-problems) associated with traditional notebooks like Jupyter.

**A reactive programming environment.**
Run a cell and marimo _reacts_ by automatically running the cells that
reference its variables, eliminating the error-prone task of manually
re-running cells. Delete a cell and marimo scrubs its variables from program
memory, eliminating hidden state.

**Compatible with expensive notebooks.** marimo lets you [configure the runtime\\
to be\\
lazy](https://docs.marimo.io/guides/configuration/runtime_configuration/),
marking affected cells as stale instead of automatically running them. This
gives you guarantees on program state while preventing accidental execution of
expensive cells.

**Synchronized UI elements.** Interact with [UI\\
elements](https://docs.marimo.io/guides/interactivity/) like [sliders](https://docs.marimo.io/api/inputs/slider/#slider),
[dropdowns](https://docs.marimo.io/api/inputs/dropdown/), [dataframe\\
transformers](https://docs.marimo.io/api/inputs/dataframe/), and [chat\\
interfaces](https://docs.marimo.io/api/inputs/chat/), and the cells that
use them are automatically re-run with their latest values.

**Interactive dataframes.** [Page through, search, filter, and\\
sort](https://docs.marimo.io/guides/working_with_data/dataframes/)
millions of rows blazingly fast, no code required.

**Generate cells with data-aware AI.** [Generate code with an AI\\
assistant](https://docs.marimo.io/guides/editor_features/ai_completion/) that is highly
specialized for working with data, with context about your variables in memory;
[zero-shot entire notebooks](https://docs.marimo.io/guides/generate_with_ai/text_to_notebook/).
Customize the system prompt, bring your own API keys, or use local models.

**Query data with SQL.** Build [SQL](https://docs.marimo.io/guides/working_with_data/sql.html) queries
that depend on Python values and execute them against dataframes, databases, lakehouses,
CSVs, Google Sheets, or anything else using our built-in SQL engine, which
returns the result as a Python dataframe.

![marimo notebook cell showing SQL query that depends on Python values, demonstrating native SQL support within pure Python notebooks](https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/readme-sql-cell.png)

Your notebooks are still pure Python, even if they use SQL.

**Dynamic markdown.** Use markdown parametrized by Python variables to tell
dynamic stories that depend on Python data.

**Built-in package management.** marimo has built-in support for all major
package managers, letting you [install packages on import](https://docs.marimo.io/guides/editor_features/package_management/). marimo can even
[serialize package\\
requirements](https://docs.marimo.io/guides/package_management/inlining_dependencies/)
in notebook files, and auto install them in
isolated venv sandboxes.

**Deterministic execution order.** Notebooks are executed in a deterministic
order, based on variable references instead of cells' positions on the page.
Organize your notebooks to best fit the stories you'd like to tell.

**Performant runtime.** marimo runs only those cells that need to be run by
statically analyzing your code.

**Batteries-included.** marimo comes with GitHub Copilot, AI assistants, Ruff
code formatting, HTML export, fast code completion, a [VS Code\\
extension](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo),
an interactive dataframe viewer, and [many more](https://docs.marimo.io/guides/editor_features/)
quality-of-life features.

## Quickstart [¶](https://docs.marimo.io/\#quickstart "Permanent link")

_The [marimo concepts\_\
_playlist](https://www.youtube.com/watch?v=3N6lInzq5MI&list=PLNJXGo8e1XT9jP7gPbRdm1XwloZVFvLEq)_
_on our [YouTube channel](https://www.youtube.com/@marimo-team) gives an_
_overview of many features._

**Installation.** In a terminal, run

```bash
pip install marimo  # or conda install -c conda-forge marimo
marimo tutorial intro
```

To install with additional dependencies that unlock SQL cells, AI completion, and more,
run

```bash
pip install marimo[recommended]
```

**Create notebooks.**

Create or edit notebooks with

```bash
marimo edit
```

**Run apps.** Run your notebook as a web app, with Python
code hidden and uneditable:

```bash
marimo run your_notebook.py
```

**Execute as scripts.** Execute a notebook as a script at the
command line:

```bash
python your_notebook.py
```

**Automatically convert Jupyter notebooks.** Automatically convert Jupyter
notebooks to marimo notebooks with the CLI

```bash
marimo convert your_notebook.ipynb > your_notebook.py
```

or use our [web interface](https://marimo.io/convert).

**Tutorials.**
List all tutorials:

```bash
marimo tutorial --help
```

**Share cloud-based notebooks.** Use
[molab](https://molab.marimo.io/notebooks), a cloud-based marimo notebook
service similar to Google Colab, to create and share notebook links.

## Questions? [¶](https://docs.marimo.io/\#questions "Permanent link")

See our [FAQ](https://docs.marimo.io/faq/).

## Learn more [¶](https://docs.marimo.io/\#learn-more "Permanent link")

marimo is easy to get started with, with lots of room for power users.
For example, here's an embedding visualizer made in marimo
( [video](https://marimo.io/videos/landing/full.mp4)):

Check out our [guides](https://docs.marimo.io/guides/), [usage examples](https://docs.marimo.io/examples/),
and our [gallery](https://marimo.io/gallery) to learn more.

|     |     |     |     |
| --- | --- | --- | --- |
|  |  |  |  |
| [Tutorial](https://docs.marimo.io/getting_started/key_concepts) | [Inputs](https://docs.marimo.io/api/inputs/) | [Plots](https://docs.marimo.io/guides/working_with_data/plotting) | [Layout](https://docs.marimo.io/api/layouts/) |
| [![shielf logo](https://marimo.io/shield.svg)](https://marimo.app/l/c7h6pz) | [![shielf logo](https://marimo.io/shield.svg)](https://marimo.app/l/0ue871) | [![shielf logo](https://marimo.io/shield.svg)](https://marimo.app/l/lxp1jk) | [![shielf logo](https://marimo.io/shield.svg)](https://marimo.app/l/14ovyr) |

## Contributing [¶](https://docs.marimo.io/\#contributing "Permanent link")

We appreciate all contributions! You don't need to be an expert to help out.
Please see [CONTRIBUTING.md](https://github.com/marimo-team/marimo/blob/main/CONTRIBUTING.md) for more details on how to get
started.

> Questions? Reach out to us [on Discord](https://marimo.io/discord?ref=docs).

## Community [¶](https://docs.marimo.io/\#community "Permanent link")

We're building a community. Come hang out with us!

- 🌟 [Star us on GitHub](https://github.com/marimo-team/marimo)
- 💬 [Chat with us on Discord](https://marimo.io/discord?ref=docs)
- 📧 [Subscribe to our Newsletter](https://marimo.io/newsletter)
- ☁️ [Join our Cloud Waitlist](https://marimo.io/cloud)
- ✏️ [Start a GitHub Discussion](https://github.com/marimo-team/marimo/discussions)
- 💬 [Follow us on Bluesky](https://bsky.app/profile/marimo.io)
- 🐦 [Follow us on Twitter](https://twitter.com/marimo_io)
- 🎥 [Subscribe on YouTube](https://www.youtube.com/@marimo-team)
- 💬 [Follow us on Mastodon](https://mastodon.social/@marimo_io)
- 🕴️ [Follow us on LinkedIn](https://www.linkedin.com/company/marimo-io)

## Inspiration ✨ [¶](https://docs.marimo.io/\#inspiration "Permanent link")

marimo is a **reinvention** of the Python notebook as a reproducible, interactive,
and shareable Python program, instead of an error-prone JSON scratchpad.

We believe that the tools we use shape the way we think — better tools, for
better minds. With marimo, we hope to provide the Python community with a
better programming environment to do research and communicate it; to experiment
with code and share it; to learn computational science and teach it.
