# [Creating projects](https://docs.astral.sh/uv/concepts/projects/init/\#creating-projects)

uv supports creating a project with `uv init`.

When creating projects, uv supports two basic templates: [**applications**](https://docs.astral.sh/uv/concepts/projects/init/#applications) and
[**libraries**](https://docs.astral.sh/uv/concepts/projects/init/#libraries). By default, uv will create a project for an application. The `--lib`
flag can be used to create a project for a library instead.

## [Target directory](https://docs.astral.sh/uv/concepts/projects/init/\#target-directory)

uv will create a project in the working directory, or, in a target directory by providing a name,
e.g., `uv init foo`. If there's already a project in the target directory, i.e., if there's a
`pyproject.toml`, uv will exit with an error.

## [Applications](https://docs.astral.sh/uv/concepts/projects/init/\#applications)

Application projects are suitable for web servers, scripts, and command-line interfaces.

Applications are the default target for `uv init`, but can also be specified with the `--app` flag.

```
$ uv init example-app

```

The project includes a `pyproject.toml`, a sample file ( `main.py`), a readme, and a Python version
pin file ( `.python-version`).

```
$ tree example-app
example-app
├── .python-version
├── README.md
├── main.py
└── pyproject.toml

```

Note

Prior to v0.6.0, uv created a file named `hello.py` instead of `main.py`.

The `pyproject.toml` includes basic metadata. It does not include a build system, it is not a
[package](https://docs.astral.sh/uv/concepts/projects/config/#project-packaging) and will not be installed into the environment:

pyproject.toml

```
[project]
name = "example-app"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

```

The sample file defines a `main` function with some standard boilerplate:

main.py

```
def main():
    print("Hello from example-app!")

if __name__ == "__main__":
    main()

```

Python files can be executed with `uv run`:

```
$ cd example-app
$ uv run main.py
Hello from example-project!

```

## [Packaged applications](https://docs.astral.sh/uv/concepts/projects/init/\#packaged-applications)

Many use-cases require a [package](https://docs.astral.sh/uv/concepts/projects/config/#project-packaging). For example, if you are creating
a command-line interface that will be published to PyPI or if you want to define tests in a
dedicated directory.

The `--package` flag can be used to create a packaged application:

```
$ uv init --package example-pkg

```

The source code is moved into a `src` directory with a module directory and an `__init__.py` file:

```
$ tree example-pkg
example-pkg
├── .python-version
├── README.md
├── pyproject.toml
└── src
    └── example_pkg
        └── __init__.py

```

A [build system](https://docs.astral.sh/uv/concepts/projects/config/#build-systems) is defined, so the project will be installed into the
environment:

pyproject.toml

```
[project]
name = "example-pkg"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[project.scripts]
example-pkg = "example_pkg:main"

[build-system]
requires = ["uv_build>=0.8.4,<0.9.0"]
build-backend = "uv_build"

```

Tip

The `--build-backend` option can be used to request an alternative build system.

A [command](https://docs.astral.sh/uv/concepts/projects/config/#entry-points) definition is included:

pyproject.toml

```
[project]
name = "example-pkg"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[project.scripts]
example-pkg = "example_pkg:main"

[build-system]
requires = ["uv_build>=0.8.4,<0.9.0"]
build-backend = "uv_build"

```

The command can be executed with `uv run`:

```
$ cd example-pkg
$ uv run example-pkg
Hello from example-pkg!

```

## [Libraries](https://docs.astral.sh/uv/concepts/projects/init/\#libraries)

A library provides functions and objects for other projects to consume. Libraries are intended to be
built and distributed, e.g., by uploading them to PyPI.

Libraries can be created by using the `--lib` flag:

```
$ uv init --lib example-lib

```

Note

Using `--lib` implies `--package`. Libraries always require a packaged project.

As with a [packaged application](https://docs.astral.sh/uv/concepts/projects/init/#packaged-applications), a `src` layout is used. A `py.typed`
marker is included to indicate to consumers that types can be read from the library:

```
$ tree example-lib
example-lib
├── .python-version
├── README.md
├── pyproject.toml
└── src
    └── example_lib
        ├── py.typed
        └── __init__.py

```

Note

A `src` layout is particularly valuable when developing libraries. It ensures that the library is
isolated from any `python` invocations in the project root and that distributed library code is
well separated from the rest of the project source.

A [build system](https://docs.astral.sh/uv/concepts/projects/config/#build-systems) is defined, so the project will be installed into the
environment:

pyproject.toml

```
[project]
name = "example-lib"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[build-system]
requires = ["uv_build>=0.8.4,<0.9.0"]
build-backend = "uv_build"

```

Tip

You can select a different build backend template by using `--build-backend` with `hatchling`,
`uv_build`, `flit-core`, `pdm-backend`, `setuptools`, `maturin`, or `scikit-build-core`. An
alternative backend is required if you want to create a [library with extension modules](https://docs.astral.sh/uv/concepts/projects/init/#projects-with-extension-modules).

The created module defines a simple API function:

\_\_init\_\_.py

```
def hello() -> str:
    return "Hello from example-lib!"

```

And you can import and execute it using `uv run`:

```
$ cd example-lib
$ uv run python -c "import example_lib; print(example_lib.hello())"
Hello from example-lib!

```

## [Projects with extension modules](https://docs.astral.sh/uv/concepts/projects/init/\#projects-with-extension-modules)

Most Python projects are "pure Python", meaning they do not define modules in other languages like
C, C++, FORTRAN, or Rust. However, projects with extension modules are often used for performance
sensitive code.

Creating a project with an extension module requires choosing an alternative build system. uv
supports creating projects with the following build systems that support building extension modules:

- [`maturin`](https://www.maturin.rs/) for projects with Rust
- [`scikit-build-core`](https://github.com/scikit-build/scikit-build-core) for projects with C, C++,
FORTRAN, Cython

Specify the build system with the `--build-backend` flag:

```
$ uv init --build-backend maturin example-ext

```

Note

Using `--build-backend` implies `--package`.

The project contains a `Cargo.toml` and a `lib.rs` file in addition to the typical Python project
files:

```
$ tree example-ext
example-ext
├── .python-version
├── Cargo.toml
├── README.md
├── pyproject.toml
└── src
    ├── lib.rs
    └── example_ext
        ├── __init__.py
        └── _core.pyi

```

Note

If using `scikit-build-core`, you'll see CMake configuration and a `main.cpp` file instead.

The Rust library defines a simple function:

src/lib.rs

```
use pyo3::prelude::*;

#[pyfunction]
fn hello_from_bin() -> String {
    "Hello from example-ext!".to_string()
}

#[pymodule]
fn _core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hello_from_bin, m)?)?;
    Ok(())
}

```

And the Python module imports it:

src/example\_ext/\_\_init\_\_.py

```
from example_ext._core import hello_from_bin

def main() -> None:
    print(hello_from_bin())

```

The command can be executed with `uv run`:

```
$ cd example-ext
$ uv run example-ext
Hello from example-ext!

```

Important

Changes to the extension code in `lib.rs` or `main.cpp` will require running `--reinstall` to
rebuild them.

## [Creating a minimal project](https://docs.astral.sh/uv/concepts/projects/init/\#creating-a-minimal-project)

If you only want to create a `pyproject.toml`, use the `--bare` option:

```
$ uv init example --bare

```

uv will skip creating a Python version pin file, a README, and any source directories or files.
Additionally, uv will not initialize a version control system (i.e., `git`).

```
$ tree example-bare
example-bare
└── pyproject.toml

```

uv will also not add extra metadata to the `pyproject.toml`, such as the `description` or `authors`.

```
[project]
name = "example"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []

```

The `--bare` option can be used with other options like `--lib` or `--build-backend` — in these
cases uv will still configure a build system but will not create the expected file structure.

When `--bare` is used, additional features can still be used opt-in:

```
$ uv init example --bare --description "Hello world" --author-from git --vcs git --python-pin

```
