# [Installing Python](https://docs.astral.sh/uv/guides/install-python/\#installing-python)

If Python is already installed on your system, uv will
[detect and use](https://docs.astral.sh/uv/guides/install-python/#using-existing-python-versions) it without configuration. However, uv can also
install and manage Python versions. uv [automatically installs](https://docs.astral.sh/uv/guides/install-python/#automatic-python-downloads) missing
Python versions as needed — you don't need to install Python to get started.

## [Getting started](https://docs.astral.sh/uv/guides/install-python/\#getting-started)

To install the latest Python version:

```
$ uv python install

```

Note

Python does not publish official distributable binaries. As such, uv uses distributions from the Astral [`python-build-standalone`](https://github.com/astral-sh/python-build-standalone) project. See the [Python distributions](https://docs.astral.sh/uv/concepts/python-versions/#managed-python-distributions) documentation for more details.

Once Python is installed, it will be used by `uv` commands automatically. uv also adds the installed
version to your `PATH`:

```
$ python3.13

```

uv only installs a _versioned_ executable by default. To install `python` and `python3` executables,
include the experimental `--default` option:

```
$ uv python install --default

```

Tip

See the documentation on [installing Python executables](https://docs.astral.sh/uv/concepts/python-versions/#installing-python-executables)
for more details.

## [Installing a specific version](https://docs.astral.sh/uv/guides/install-python/\#installing-a-specific-version)

To install a specific Python version:

```
$ uv python install 3.12

```

To install multiple Python versions:

```
$ uv python install 3.11 3.12

```

To install an alternative Python implementation, e.g., PyPy:

```
$ uv python install pypy@3.10

```

See the [`python install`](https://docs.astral.sh/uv/concepts/python-versions/#installing-a-python-version) documentation
for more details.

## [Reinstalling Python](https://docs.astral.sh/uv/guides/install-python/\#reinstalling-python)

To reinstall uv-managed Python versions, use `--reinstall`, e.g.:

```
$ uv python install --reinstall

```

This will reinstall all previously installed Python versions. Improvements are constantly being
added to the Python distributions, so reinstalling may resolve bugs even if the Python version does
not change.

## [Viewing Python installations](https://docs.astral.sh/uv/guides/install-python/\#viewing-python-installations)

To view available and installed Python versions:

```
$ uv python list

```

See the [`python list`](https://docs.astral.sh/uv/concepts/python-versions/#viewing-available-python-versions)
documentation for more details.

## [Automatic Python downloads](https://docs.astral.sh/uv/guides/install-python/\#automatic-python-downloads)

Python does not need to be explicitly installed to use uv. By default, uv will automatically
download Python versions when they are required. For example, the following would download Python
3.12 if it was not installed:

```
$ uvx python@3.12 -c "print('hello world')"

```

Even if a specific Python version is not requested, uv will download the latest version on demand.
For example, if there are no Python versions on your system, the following will install Python
before creating a new virtual environment:

```
$ uv venv

```

Tip

Automatic Python downloads can be [easily disabled](https://docs.astral.sh/uv/concepts/python-versions/#disabling-automatic-python-downloads) if you want more control over when Python is downloaded.

## [Using existing Python versions](https://docs.astral.sh/uv/guides/install-python/\#using-existing-python-versions)

uv will use existing Python installations if present on your system. There is no configuration
necessary for this behavior: uv will use the system Python if it satisfies the requirements of the
command invocation. See the
[Python discovery](https://docs.astral.sh/uv/concepts/python-versions/#discovery-of-python-versions) documentation for
details.

To force uv to use the system Python, provide the `--no-managed-python` flag. See the
[Python version preference](https://docs.astral.sh/uv/concepts/python-versions/#requiring-or-disabling-managed-python-versions)
documentation for more details.

## [Upgrading Python versions](https://docs.astral.sh/uv/guides/install-python/\#upgrading-python-versions)

Important

Support for upgrading Python patch versions is in _preview_. This means the behavior is
experimental and subject to change.

To upgrade a Python version to the latest supported patch release:

```
$ uv python upgrade 3.12

```

To upgrade all uv-managed Python versions:

```
$ uv python upgrade

```

See the [`python upgrade`](https://docs.astral.sh/uv/concepts/python-versions/#upgrading-python-versions) documentation
for more details.

## [Next steps](https://docs.astral.sh/uv/guides/install-python/\#next-steps)

To learn more about `uv python`, see the [Python version concept](https://docs.astral.sh/uv/concepts/python-versions/)
page and the [command reference](https://docs.astral.sh/uv/reference/cli/#uv-python).

Or, read on to learn how to [run scripts](https://docs.astral.sh/uv/guides/scripts/) and invoke Python with uv.
