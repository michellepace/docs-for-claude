[Skip to content](https://docs.marimo.io/getting_started/quickstart/#quickstart)

# Quickstart [¶](https://docs.marimo.io/getting_started/quickstart/\#quickstart "Permanent link")

Installing marimo gets you the `marimo` command-line interface (CLI), the entry
point to all things marimo.

## Run tutorials [¶](https://docs.marimo.io/getting_started/quickstart/\#run-tutorials "Permanent link")

`marimo tutorial intro` opens the intro tutorial. List all tutorials with

```bash
marimo tutorial --help
```

See marimo in action on YouTube

The [marimo concepts playlist](https://www.youtube.com/watch?v=3N6lInzq5MI&list=PLNJXGo8e1XT9jP7gPbRdm1XwloZVFvLEq) on our [YouTube channel](https://www.youtube.com/@marimo-team) gives an overview of many features.

## Edit notebooks [¶](https://docs.marimo.io/getting_started/quickstart/\#edit-notebooks "Permanent link")

Create and edit notebooks with `marimo edit`.

- launch the notebook server to create new notebooks,
and start or stop existing ones:

```bash
marimo edit
```

- create or edit a single notebook with

```bash
marimo edit your_notebook.py
```

(If `your_notebook.py` doesn't exist, marimo will create a blank notebook
named `your_notebook.py`.)

## Deploy as apps [¶](https://docs.marimo.io/getting_started/quickstart/\#deploy-as-apps "Permanent link")

Use `marimo run` to [serve your notebook as an app](https://docs.marimo.io/guides/apps/), with
Python code hidden and uneditable.

```bash
marimo run your_notebook.py
```

## Run as scripts [¶](https://docs.marimo.io/getting_started/quickstart/\#run-as-scripts "Permanent link")

Run your notebook as a script with

```bash
python your_notebook.py
```

You can also [pass CLI args](https://docs.marimo.io/guides/scripts/) to your notebook.

## Convert Jupyter notebooks and Python scripts to marimo [¶](https://docs.marimo.io/getting_started/quickstart/\#convert-jupyter-notebooks-and-python-scripts-to-marimo "Permanent link")

Automatically convert Jupyter notebooks and Python scripts to marimo notebooks with `marimo convert`:

```bash
# From Jupyter notebook
marimo convert your_notebook.ipynb -o your_notebook.py

# From Python script or jupytext py:percent format
marimo convert your_script.py -o your_notebook.py
```

Then open the notebook with `marimo edit your_notebook.py`

Disable autorun on startup

marimo automatically runs notebooks when they are opened. If this
is a problem for you (not all Jupyter notebooks are designed to be run on
startup), you can disable autorun on startup via [user configuration](https://docs.marimo.io/guides/configuration/runtime_configuration/).

1. Type `marimo config show` to get the location of your config file.
2. If no config file exists, create it at `$XDG_CONFIG_HOME/marimo/marimo.toml`.
3. Update your config to include the following:

marimo.toml

```toml
[runtime]
auto_instantiate = false
```

## Export marimo notebooks to other file formats [¶](https://docs.marimo.io/getting_started/quickstart/\#export-marimo-notebooks-to-other-file-formats "Permanent link")

Use

```bash
marimo export
```

to [export marimo notebooks](https://docs.marimo.io/guides/exporting/) to other file formats,
including HTML, IPYNB, and markdown.

## Install optional dependencies for more features [¶](https://docs.marimo.io/getting_started/quickstart/\#install-optional-dependencies-for-more-features "Permanent link")

Some features require additional dependencies, which are not installed by default. This includes:

- [SQL cells](https://docs.marimo.io/guides/working_with_data/sql/)
- Charts in the datasource viewer
- [AI features](https://docs.marimo.io/guides/editor_features/ai_completion/)
- Format on save

To install the optional dependencies, run:

[install with pip](https://docs.marimo.io/getting_started/quickstart/#__tabbed_1_1)[install with uv](https://docs.marimo.io/getting_started/quickstart/#__tabbed_1_2)[install with conda](https://docs.marimo.io/getting_started/quickstart/#__tabbed_1_3)

```bash
pip install "marimo[recommended]"
```

```bash
uv add "marimo[recommended]"
```

```bash
conda install -c conda-forge marimo duckdb altair polars openai ruff
```

This will install: `duckdb`, `altair`, `polars`, `openai`, and `ruff`.

## Enable GitHub Copilot and AI Assistant [¶](https://docs.marimo.io/getting_started/quickstart/\#enable-github-copilot-and-ai-assistant "Permanent link")

The marimo editor natively supports [GitHub Copilot](https://copilot.github.com/),
an AI pair programmer, similar to VS Code.

_Get started with Copilot_:

1. Install [Node.js](https://nodejs.org/en/download).
2. Enable Copilot via the settings menu in the marimo editor.

_Note_: Copilot is not yet available in our conda distribution; please install
marimo from `PyPI` if you need Copilot.

marimo also comes with support for [other copilots](https://docs.marimo.io/guides/editor_features/ai_completion/#custom-copilots),
and a built-in [AI assistant](https://docs.marimo.io/guides/editor_features/ai_completion/) that helps you write code.

## Share links to cloud notebooks [¶](https://docs.marimo.io/getting_started/quickstart/\#share-links-to-cloud-notebooks "Permanent link")

Use [molab](https://molab.marimo.io/notebooks), a cloud-based marimo notebook
service similar to Google Colab, to create and share notebook links
( [docs](https://docs.marimo.io/guides/molab/)).

## Coming from VS Code? [¶](https://docs.marimo.io/getting_started/quickstart/\#coming-from-vs-code "Permanent link")

The best way to use marimo is through the CLI. While we do have a VS Code extension,
we are actively rewriting it to provide a more native and robust experience, similar
to what you may be used to for Jupyter notebooks. In the meantime, we recommend using
the CLI. You can try our [existing extension](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo), but please
be aware that you may run into issues, and that a revamped extension is coming soon.

Back to top

![Project Logo](https://marimo.io/logo.png)

Ask

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)
