[Skip to content](https://docs.astral.sh/uv/getting-started/features/#features)

# [Features](https://docs.astral.sh/uv/getting-started/features/\#features)

uv provides essential features for Python development — from installing Python and hacking on simple
scripts to working on large projects that support multiple Python versions and platforms.

uv's interface can be broken down into sections, which are usable independently or together.

## [Python versions](https://docs.astral.sh/uv/getting-started/features/\#python-versions)

Installing and managing Python itself.

- `uv python install`: Install Python versions.
- `uv python list`: View available Python versions.
- `uv python find`: Find an installed Python version.
- `uv python pin`: Pin the current project to use a specific Python version.
- `uv python uninstall`: Uninstall a Python version.

See the [guide on installing Python](https://docs.astral.sh/uv/guides/install-python/) to get started.

## [Scripts](https://docs.astral.sh/uv/getting-started/features/\#scripts)

Executing standalone Python scripts, e.g., `example.py`.

- `uv run`: Run a script.
- `uv add --script`: Add a dependency to a script.
- `uv remove --script`: Remove a dependency from a script.

See the [guide on running scripts](https://docs.astral.sh/uv/guides/scripts/) to get started.

## [Projects](https://docs.astral.sh/uv/getting-started/features/\#projects)

Creating and working on Python projects, i.e., with a `pyproject.toml`.

- `uv init`: Create a new Python project.
- `uv add`: Add a dependency to the project.
- `uv remove`: Remove a dependency from the project.
- `uv sync`: Sync the project's dependencies with the environment.
- `uv lock`: Create a lockfile for the project's dependencies.
- `uv run`: Run a command in the project environment.
- `uv tree`: View the dependency tree for the project.
- `uv build`: Build the project into distribution archives.
- `uv publish`: Publish the project to a package index.

See the [guide on projects](https://docs.astral.sh/uv/guides/projects/) to get started.

## [Tools](https://docs.astral.sh/uv/getting-started/features/\#tools)

Running and installing tools published to Python package indexes, e.g., `ruff` or `black`.

- `uvx` / `uv tool run`: Run a tool in a temporary environment.
- `uv tool install`: Install a tool user-wide.
- `uv tool uninstall`: Uninstall a tool.
- `uv tool list`: List installed tools.
- `uv tool update-shell`: Update the shell to include tool executables.

See the [guide on tools](https://docs.astral.sh/uv/guides/tools/) to get started.

## [The pip interface](https://docs.astral.sh/uv/getting-started/features/\#the-pip-interface)

Manually managing environments and packages — intended to be used in legacy workflows or cases where
the high-level commands do not provide enough control.

Creating virtual environments (replacing `venv` and `virtualenv`):

- `uv venv`: Create a new virtual environment.

See the documentation on [using environments](https://docs.astral.sh/uv/pip/environments/) for details.

Managing packages in an environment (replacing [`pip`](https://github.com/pypa/pip) and
[`pipdeptree`](https://github.com/tox-dev/pipdeptree)):

- `uv pip install`: Install packages into the current environment.
- `uv pip show`: Show details about an installed package.
- `uv pip freeze`: List installed packages and their versions.
- `uv pip check`: Check that the current environment has compatible packages.
- `uv pip list`: List installed packages.
- `uv pip uninstall`: Uninstall packages.
- `uv pip tree`: View the dependency tree for the environment.

See the documentation on [managing packages](https://docs.astral.sh/uv/pip/packages/) for details.

Locking packages in an environment (replacing [`pip-tools`](https://github.com/jazzband/pip-tools)):

- `uv pip compile`: Compile requirements into a lockfile.
- `uv pip sync`: Sync an environment with a lockfile.

See the documentation on [locking environments](https://docs.astral.sh/uv/pip/compile/) for details.

Important

These commands do not exactly implement the interfaces and behavior of the tools they are based on. The further you stray from common workflows, the more likely you are to encounter differences. Consult the [pip-compatibility guide](https://docs.astral.sh/uv/pip/compatibility/) for details.

## [Utility](https://docs.astral.sh/uv/getting-started/features/\#utility)

Managing and inspecting uv's state, such as the cache, storage directories, or performing a
self-update:

- `uv cache clean`: Remove cache entries.
- `uv cache prune`: Remove outdated cache entries.
- `uv cache dir`: Show the uv cache directory path.
- `uv tool dir`: Show the uv tool directory path.
- `uv python dir`: Show the uv installed Python versions path.
- `uv self update`: Update uv to the latest version.

## [Next steps](https://docs.astral.sh/uv/getting-started/features/\#next-steps)

Read the [guides](https://docs.astral.sh/uv/guides/) for an introduction to each feature, check out the
[concept](https://docs.astral.sh/uv/concepts/) pages for in-depth details about uv's features, or learn how to
[get help](https://docs.astral.sh/uv/getting-started/help/) if you run into any problems.

Back to top