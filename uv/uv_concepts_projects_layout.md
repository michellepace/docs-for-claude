# [Project structure and files](https://docs.astral.sh/uv/concepts/projects/layout/\#project-structure-and-files)

## [The `pyproject.toml`](https://docs.astral.sh/uv/concepts/projects/layout/\#the-pyprojecttoml)

Python project metadata is defined in a
[`pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) file. uv
requires this file to identify the root directory of a project.

Tip

`uv init` can be used to create a new project. See [Creating projects](https://docs.astral.sh/uv/concepts/projects/init/) for
details.

A minimal project definition includes a name and version:

pyproject.toml

```
[project]
name = "example"
version = "0.1.0"

```

Additional project metadata and configuration includes:

- [Python version requirement](https://docs.astral.sh/uv/concepts/projects/config/#python-version-requirement)
- [Dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/)
- [Build system](https://docs.astral.sh/uv/concepts/projects/config/#build-systems)
- [Entry points (commands)](https://docs.astral.sh/uv/concepts/projects/config/#entry-points)

## [The project environment](https://docs.astral.sh/uv/concepts/projects/layout/\#the-project-environment)

When working on a project with uv, uv will create a virtual environment as needed. While some uv
commands will create a temporary environment (e.g., `uv run --isolated`), uv also manages a
persistent environment with the project and its dependencies in a `.venv` directory next to the
`pyproject.toml`. It is stored inside the project to make it easy for editors to find — they need
the environment to give code completions and type hints. It is not recommended to include the
`.venv` directory in version control; it is automatically excluded from `git` with an internal
`.gitignore` file.

To run a command in the project environment, use `uv run`. Alternatively the project environment can
be activated as normal for a virtual environment.

When `uv run` is invoked, it will create the project environment if it does not exist yet or ensure
it is up-to-date if it exists. The project environment can also be explicitly created with
`uv sync`. See the [locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/) documentation for details.

It is _not_ recommended to modify the project environment manually, e.g., with `uv pip install`. For
project dependencies, use `uv add` to add a package to the environment. For one-off requirements,
use [`uvx`](https://docs.astral.sh/uv/guides/tools/) or
[`uv run --with`](https://docs.astral.sh/uv/concepts/projects/run/#requesting-additional-dependencies).

Tip

If you don't want uv to manage the project environment, set [`managed = false`](https://docs.astral.sh/uv/reference/settings/#managed)
to disable automatic locking and syncing of the project. For example:

pyproject.toml

```
[tool.uv]
managed = false

```

## [The lockfile](https://docs.astral.sh/uv/concepts/projects/layout/\#the-lockfile)

uv creates a `uv.lock` file next to the `pyproject.toml`.

`uv.lock` is a _universal_ or _cross-platform_ lockfile that captures the packages that would be
installed across all possible Python markers such as operating system, architecture, and Python
version.

Unlike the `pyproject.toml`, which is used to specify the broad requirements of your project, the
lockfile contains the exact resolved versions that are installed in the project environment. This
file should be checked into version control, allowing for consistent and reproducible installations
across machines.

A lockfile ensures that developers working on the project are using a consistent set of package
versions. Additionally, it ensures when deploying the project as an application that the exact set
of used package versions is known.

The lockfile is [automatically created and updated](https://docs.astral.sh/uv/concepts/projects/sync/#automatic-lock-and-sync) during uv
invocations that use the project environment, i.e., `uv sync` and `uv run`. The lockfile may also be
explicitly updated using `uv lock`.

`uv.lock` is a human-readable TOML file but is managed by uv and should not be edited manually. The
`uv.lock` format is specific to uv and not usable by other tools.

### [`pylock.toml`](https://docs.astral.sh/uv/concepts/projects/layout/\#pylocktoml)

In [PEP 751](https://peps.python.org/pep-0751/), Python standardized a new resolution file format,
`pylock.toml`.

`pylock.toml` is a resolution output format intended to replace `requirements.txt` (e.g., in the
context of `uv pip compile`, whereby a "locked" `requirements.txt` file is generated from a set of
input requirements). `pylock.toml` is standardized and tool-agnostic, such that in the future,
`pylock.toml` files generated by uv could be installed by other tools, and vice versa.

Some of uv's functionality cannot be expressed in the `pylock.toml` format; as such, uv will
continue to use the `uv.lock` format within the project interface.

However, uv supports `pylock.toml` as an export target and in the `uv pip` CLI. For example:

- To export a `uv.lock` to the `pylock.toml` format, run: `uv export -o pylock.toml`
- To generate a `pylock.toml` file from a set of requirements, run:
`uv pip compile -o pylock.toml -r requirements.in`
- To install from a `pylock.toml` file, run: `uv pip sync pylock.toml` or
`uv pip install -r pylock.toml`
