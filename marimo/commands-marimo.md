[Skip to content](https://docs.marimo.io/cli/#marimo)

# marimo [¶](https://docs.marimo.io/cli/\#marimo "Permanent link")

Welcome to marimo!
Getting started:

- marimo tutorial intro

Example usage:

- marimo edit create or edit notebooks
- marimo edit notebook.py create or edit a notebook called notebook.py
- marimo run notebook.py run a notebook as a read-only app
- marimo tutorial --help list tutorials

**Usage:**

```bash
marimo [OPTIONS] COMMAND [ARGS]...
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `--version` | boolean | Show the version and exit. | `False` |
| `-l`, `--log-level` | choice (`DEBUG` \| `INFO` \| `WARN` \| `ERROR` \| `CRITICAL`) | Choose logging level. | `WARN` |
| `-q`, `--quiet` | boolean | Suppress standard out. | `False` |
| `-y`, `--yes` | boolean | Automatic yes to prompts, running non-interactively. | `False` |
| `-d`, `--development-mode` | boolean | Run in development mode; enables debug logs and server autoreload. | `False` |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

## marimo check [¶](https://docs.marimo.io/cli/\#marimo-check "Permanent link")

Check and format marimo files.

**Usage:**

```bash
marimo check [OPTIONS] [FILES]...
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `--fix` | boolean | Whether to in place update files. | `False` |
| `--strict` | boolean | Whether warnings return a non-zero exit code. | `False` |
| `-v`, `--verbose` / `-q`, `--quiet` | boolean | Whether to print detailed messages. | `True` |
| `--unsafe-fixes` | boolean | Enable fixes that may change code behavior (e.g., removing empty cells). | `False` |
| `--ignore-scripts` | boolean | Ignore files that are not recognizable as marimo notebooks. | `False` |
| `--format` | choice (`full` \| `json`) | Output format for diagnostics. | `full` |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

## marimo config [¶](https://docs.marimo.io/cli/\#marimo-config "Permanent link")

Various commands for the marimo config.

**Usage:**

```bash
marimo config [OPTIONS] COMMAND [ARGS]...
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

### marimo config describe [¶](https://docs.marimo.io/cli/\#marimo-config-describe "Permanent link")

Describe the marimo config.

**Usage:**

```bash
marimo config describe [OPTIONS]
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

### marimo config show [¶](https://docs.marimo.io/cli/\#marimo-config-show "Permanent link")

Show the marimo config.

**Usage:**

```bash
marimo config show [OPTIONS]
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

## marimo convert [¶](https://docs.marimo.io/cli/\#marimo-convert "Permanent link")

Convert a Jupyter notebook, Markdown file, or Python script to a marimo notebook.

Supported input formats:
\- `.ipynb` (local or GitHub-hosted)
\- `.md` files with `{python}` code fences
\- `.py` scripts in py:percent format

Behavior:
\- Jupyter notebooks: outputs are stripped.

- Markdown files: only `{python}` fenced code blocks are converted.

Example:

```python
x = 1 + 2
print(x)
```

\- Python scripts:
\- If already a valid marimo notebook, no conversion is performed.
\- Otherwise, marimo attempts to convert using py:percent formatting,
preserving top-level comments and docstrings.

Example usage:

```bash
marimo convert your_nb.ipynb -o your_nb.py
```

or

```bash
marimo convert your_nb.md -o your_nb.py
```

or

```bash
marimo convert script.py -o your_nb.py
```

After conversion:

```bash
marimo edit your_nb.py
```

Note:
Since marimo's reactive execution differs from traditional notebooks,
you may need to refactor code that mutates variables across cells
(e.g., modifying a dataframe in multiple cells), which can lead to
unexpected behavior.

**Usage:**

```bash
marimo convert [OPTIONS] FILENAME
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `-o`, `--output` | path | Output file to save the converted notebook to. If not provided, the converted notebook will be printed to stdout. | None |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

## marimo edit [¶](https://docs.marimo.io/cli/\#marimo-edit "Permanent link")

Create or edit notebooks.

- marimo edit Start the marimo notebook server
- marimo edit notebook.py Create or edit notebook.py

**Usage:**

```bash
marimo edit [OPTIONS] [NAME] [ARGS]...
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `-p`, `--port` | integer | Port to attach to. | None |
| `--host` | text | Host to attach to. | `127.0.0.1` |
| `--proxy` | text | Address of reverse proxy. | None |
| `--headless` | boolean | Don't launch a browser. | `False` |
| `--token` / `--no-token` | boolean | Use a token for authentication. This enables session-based authentication. A random token will be generated if --token-password is not set. If --no-token is set, session-based authentication will not be used. | `True` |
| `--token-password` | text | Use a specific token for authentication. This enables session-based authentication. A random token will be generated if not set. | None |
| `--token-password-file` | text | Path to file containing token password, or '-' for stdin. Mutually exclusive with --token-password. | None |
| `--base-url` | text | Base URL for the server. Should start with a /. | \`\` |
| `--allow-origins` | text | Allowed origins for CORS. Can be repeated. Use \* for all origins. | None |
| `--skip-update-check` | boolean | Don't check if a new version of marimo is available for download. | `False` |
| `--sandbox` / `--no-sandbox` | boolean | Run the notebook in an isolated environment, with dependencies tracked via PEP 723 inline metadata. If already declared, dependencies will install automatically. Requires uv. | None |
| `--watch` | boolean | Watch the file for changes and reload the code when saved in another editor. | `False` |
| `--skew-protection` / `--no-skew-protection` | boolean | Enable skew protection middleware to prevent version mismatch issues. | `True` |
| `--timeout` | float | Enable a global timeout to shut down the server after specified number of minutes of no connection | None |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

## marimo env [¶](https://docs.marimo.io/cli/\#marimo-env "Permanent link")

Print out environment information for debugging purposes.

**Usage:**

```bash
marimo env [OPTIONS]
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

## marimo export [¶](https://docs.marimo.io/cli/\#marimo-export "Permanent link")

Export a notebook to various formats.

**Usage:**

```bash
marimo export [OPTIONS] COMMAND [ARGS]...
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

### marimo export html [¶](https://docs.marimo.io/cli/\#marimo-export-html "Permanent link")

Run a notebook and export it as an HTML file.

Example:

```bash
marimo export html notebook.py -o notebook.html
```

Optionally pass CLI args to the notebook:

```bash
marimo export html notebook.py -o notebook.html -- -arg1 foo -arg2 bar
```

**Usage:**

```bash
marimo export html [OPTIONS] NAME [ARGS]...
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `--include-code` / `--no-include-code` | boolean | Include notebook code in the exported HTML file. | `True` |
| `--watch` / `--no-watch` | boolean | Watch notebook for changes and regenerate the output on modification. If watchdog is installed, it will be used to watch the file. Otherwise, file watcher will poll the file every 1s. | `False` |
| `-o`, `--output` | path | Output file to save the HTML to. If not provided, the HTML will be printed to stdout. | None |
| `--sandbox` / `--no-sandbox` | boolean | Run the command in an isolated virtual environment using `uv run --isolated`. Requires `uv`. | None |
| `-f`, `--force` | boolean | Force overwrite of the output file if it already exists. | `False` |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

### marimo export html-wasm [¶](https://docs.marimo.io/cli/\#marimo-export-html-wasm "Permanent link")

Export a notebook as a WASM-powered standalone HTML file.

Example:

```bash
marimo export html-wasm notebook.py -o notebook.wasm.html
```

The exported HTML file will run the notebook using WebAssembly, making it
completely self-contained and executable in the browser. This lets you
share interactive notebooks on the web without setting up
infrastructure to run Python code.

The exported notebook runs using Pyodide, which supports most
but not all Python packages. To learn more, see the Pyodide
documentation.

In order for this file to be able to run, it must be served over HTTP,
and cannot be opened directly from the file system (e.g. file://).

**Usage:**

```bash
marimo export html-wasm [OPTIONS] NAME
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `-o`, `--output` | path | Output directory to save the HTML to. | `Sentinel.UNSET` |
| `--mode` | choice (`edit` \| `run`) | Whether the notebook code should be editable or readonly. | `run` |
| `--watch` / `--no-watch` | boolean | Whether to watch the original file and export upon change | `False` |
| `--show-code` / `--no-show-code` | boolean | Whether to show code by default in the exported HTML file; only relevant for run mode. | `False` |
| `--include-cloudflare` / `--no-include-cloudflare` | boolean | Whether to include Cloudflare Worker configuration files (index.js and wrangler.jsonc) for easy deployment. | `False` |
| `--sandbox` / `--no-sandbox` | boolean | Run the command in an isolated virtual environment using `uv run --isolated`. Requires `uv`. | None |
| `-f`, `--force` | boolean | Force overwrite of the output file if it already exists. | `False` |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

### marimo export ipynb [¶](https://docs.marimo.io/cli/\#marimo-export-ipynb "Permanent link")

Export a marimo notebook as a Jupyter notebook in topological order.

Example:

```bash
marimo export ipynb notebook.py -o notebook.ipynb
```

Watch for changes and regenerate the script on modification:

```bash
marimo export ipynb notebook.py -o notebook.ipynb --watch
```

Requires nbformat to be installed.

**Usage:**

```bash
marimo export ipynb [OPTIONS] NAME
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `--sort` | choice (`top-down` \| `topological`) | Sort cells top-down or in topological order. | `topological` |
| `--watch` / `--no-watch` | boolean | Watch notebook for changes and regenerate the output on modification. If watchdog is installed, it will be used to watch the file. Otherwise, file watcher will poll the file every 1s. | `False` |
| `-o`, `--output` | path | Output file to save the ipynb file to. If not provided, the ipynb contents will be printed to stdout. | None |
| `--include-outputs` / `--no-include-outputs` | boolean | Run the notebook and include outputs in the exported ipynb file. | `False` |
| `--sandbox` / `--no-sandbox` | boolean | Run the command in an isolated virtual environment using `uv run --isolated`. Requires `uv`. | None |
| `-f`, `--force` | boolean | Force overwrite of the output file if it already exists. | `False` |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

### marimo export md [¶](https://docs.marimo.io/cli/\#marimo-export-md "Permanent link")

Export a marimo notebook as a code fenced Markdown file.

Example:

```bash
marimo export md notebook.py -o notebook.md
```

Watch for changes and regenerate the script on modification:

```bash
marimo export md notebook.py -o notebook.md --watch
```

**Usage:**

```bash
marimo export md [OPTIONS] NAME
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `--watch` / `--no-watch` | boolean | Watch notebook for changes and regenerate the output on modification. If watchdog is installed, it will be used to watch the file. Otherwise, file watcher will poll the file every 1s. | `False` |
| `-o`, `--output` | path | Output file to save the markdown to. If not provided, markdown will be printed to stdout. | None |
| `--sandbox` / `--no-sandbox` | boolean | Run the command in an isolated virtual environment using `uv run --isolated`. Requires `uv`. | None |
| `-f`, `--force` | boolean | Force overwrite of the output file if it already exists. | `False` |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

### marimo export script [¶](https://docs.marimo.io/cli/\#marimo-export-script "Permanent link")

Export a marimo notebook as a flat script, in topological order.

Example:

```bash
marimo export script notebook.py -o notebook.script.py
```

Watch for changes and regenerate the script on modification:

```bash
marimo export script notebook.py -o notebook.script.py --watch
```

**Usage:**

```bash
marimo export script [OPTIONS] NAME
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `--watch` / `--no-watch` | boolean | Watch notebook for changes and regenerate the output on modification. If watchdog is installed, it will be used to watch the file. Otherwise, file watcher will poll the file every 1s. | `False` |
| `-o`, `--output` | path | Output file to save the script to. If not provided, the script will be printed to stdout. | None |
| `--sandbox` / `--no-sandbox` | boolean | Run the command in an isolated virtual environment using `uv run --isolated`. Requires `uv`. | None |
| `-f`, `--force` | boolean | Force overwrite of the output file if it already exists. | `False` |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

## marimo new [¶](https://docs.marimo.io/cli/\#marimo-new "Permanent link")

Create an empty notebook, or generate from a prompt with AI

- marimo new Create an empty notebook
- marimo new "Plot an interactive 3D surface with matplotlib." Generate a notebook from a prompt.
- marimo new prompt.txt Generate a notebook from a file containing a prompt.

Visit [https://marimo.app/ai](https://marimo.app/ai) for more prompt examples.

**Usage:**

```bash
marimo new [OPTIONS] [PROMPT]
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `-p`, `--port` | integer | Port to attach to. | None |
| `--host` | text | Host to attach to. | `127.0.0.1` |
| `--proxy` | text | Address of reverse proxy. | None |
| `--headless` | boolean | Don't launch a browser. | `False` |
| `--token` / `--no-token` | boolean | Use a token for authentication. This enables session-based authentication. A random token will be generated if --token-password is not set. If --no-token is set, session-based authentication will not be used. | `True` |
| `--token-password` | text | Use a specific token for authentication. This enables session-based authentication. A random token will be generated if not set. | None |
| `--token-password-file` | text | Path to file containing token password, or '-' for stdin. Mutually exclusive with --token-password. | None |
| `--base-url` | text | Base URL for the server. Should start with a /. | \`\` |
| `--sandbox` / `--no-sandbox` | boolean | Run the notebook in an isolated environment, with dependencies tracked via PEP 723 inline metadata. If already declared, dependencies will install automatically. Requires uv. | None |
| `--skew-protection` / `--no-skew-protection` | boolean | Enable skew protection middleware to prevent version mismatch issues. | `True` |
| `--timeout` | float | Enable a global timeout to shut down the server after specified number of minutes of no connection | None |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

## marimo recover [¶](https://docs.marimo.io/cli/\#marimo-recover "Permanent link")

Recover a marimo notebook from JSON.

**Usage:**

```bash
marimo recover [OPTIONS] NAME
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

## marimo run [¶](https://docs.marimo.io/cli/\#marimo-run "Permanent link")

Run a notebook as an app in read-only mode.

If NAME is a url, the notebook will be downloaded to a temporary file.

Example:

```bash
marimo run notebook.py
```

**Usage:**

```bash
marimo run [OPTIONS] NAME [ARGS]...
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `-p`, `--port` | integer | Port to attach to. | None |
| `--host` | text | Host to attach to. | `127.0.0.1` |
| `--proxy` | text | Address of reverse proxy. | None |
| `--headless` | boolean | Don't launch a browser. | `False` |
| `--token` / `--no-token` | boolean | Use a token for authentication. This enables session-based authentication. A random token will be generated if --token-password is not set. If --no-token is set, session-based authentication will not be used. | `False` |
| `--token-password` | text | Use a specific token for authentication. This enables session-based authentication. A random token will be generated if not set. | None |
| `--token-password-file` | text | Path to file containing token password, or '-' for stdin. Mutually exclusive with --token-password. | None |
| `--include-code` | boolean | Include notebook code in the app. | `False` |
| `--session-ttl` | integer | Seconds to wait before closing a session on websocket disconnect. | `120` |
| `--watch` | boolean | Watch the file for changes and reload the app. If watchdog is installed, it will be used to watch the file. Otherwise, file watcher will poll the file every 1s. | `False` |
| `--skew-protection` / `--no-skew-protection` | boolean | Enable skew protection middleware to prevent version mismatch issues. | `True` |
| `--base-url` | text | Base URL for the server. Should start with a /. | \`\` |
| `--allow-origins` | text | Allowed origins for CORS. Can be repeated. | None |
| `--redirect-console-to-browser` | boolean | Redirect console logs to the browser console. | `False` |
| `--sandbox` / `--no-sandbox` | boolean | Run the notebook in an isolated environment, with dependencies tracked via PEP 723 inline metadata. If already declared, dependencies will install automatically. Requires uv. | None |
| `--check` / `--no-check` | boolean | Disable a static check of the notebook before running. | `True` |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

## marimo shell-completion [¶](https://docs.marimo.io/cli/\#marimo-shell-completion "Permanent link")

Install shell completions for marimo. Supports bash, zsh, and fish.

**Usage:**

```bash
marimo shell-completion [OPTIONS]
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |

## marimo tutorial [¶](https://docs.marimo.io/cli/\#marimo-tutorial "Permanent link")

Open a tutorial.

marimo is a powerful library for making reactive notebooks
and apps. To get the most out of marimo, get started with a few
tutorials, starting with the intro:

```bash
marimo tutorial intro
```

Recommended sequence:

- intro
- dataflow
- ui
- markdown
- plots
- sql
- layout
- fileformat
- markdown-format
- for-jupyter-users

**Usage:**

```bash
marimo tutorial [OPTIONS] {intro|dataflow|ui|markdown|plots|sql|layout|filefor
                mat|markdown-format|for-jupyter-users}
```

**Options:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `-p`, `--port` | integer | Port to attach to. | None |
| `--host` | text | Host to attach to. | `127.0.0.1` |
| `--proxy` | text | Address of reverse proxy. | None |
| `--headless` | boolean | Don't launch a browser. | `False` |
| `--token` / `--no-token` | boolean | Use a token for authentication. This enables session-based authentication. A random token will be generated if --token-password is not set. If --no-token is set, session-based authentication will not be used. | `True` |
| `--token-password` | text | Use a specific token for authentication. This enables session-based authentication. A random token will be generated if not set. | None |
| `--token-password-file` | text | Path to file containing token password, or '-' for stdin. Mutually exclusive with --token-password. | None |
| `--skew-protection` / `--no-skew-protection` | boolean | Enable skew protection middleware to prevent version mismatch issues. | `True` |
| `--help`, `-h` | boolean | Show this message and exit. | `False` |
