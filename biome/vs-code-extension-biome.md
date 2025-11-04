[Skip to content](https://biomejs.dev/reference/vscode/#_top)

# VS Code extension

Biome comes with an official [VS Code extension](https://marketplace.visualstudio.com/items?itemName=biomejs.biome) that tightly integrates with
your code editor, providing formatting, linting, and code refactoring features to your
development workflow.

This reference document provides an overview of the extension’s features, how to install
it, and how to configure it for your projects.

## Installing the extension

[Section titled “Installing the extension”](https://biomejs.dev/reference/vscode/#installing-the-extension)

The recommended way to install the extension is through the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=biomejs.biome)
for VS Code users, or the [Open VSX registry](https://open-vsx.org/extension/biomejs/biome) for VSCodium and other derivatives such as Cursor.

- [![](https://img.shields.io/badge/Install%20Biome-in%20VS%20Code-007ACC?style=flat&logo=biome)](vscode:extension/biomejs.biome)
- [![](https://img.shields.io/badge/Install%20Biome-in%20VSCodium-007ACC?style=flat&logo=biome)](vscodium:extension/biomejs.biome)

## Common use cases

[Section titled “Common use cases”](https://biomejs.dev/reference/vscode/#common-use-cases)

### Single-root workspaces

[Section titled “Single-root workspaces”](https://biomejs.dev/reference/vscode/#single-root-workspaces)

A single-root workspace is your typical VS Code workspace, where there is only one workspace folder.

- Directorysrc/

- main.ts

- biome.json
- package.json

### Multi-root workspaces

[Section titled “Multi-root workspaces”](https://biomejs.dev/reference/vscode/#multi-root-workspaces)

A multi-root workspace is a workspace where there are multiple workspace folders. In this case, the extension will automatically create
a Biome instance per workspace folder.

- Directoryapi/(workspace folder)

- biome.json
- Directorysrc/

- main.ts

- Directoryapp/(workspace folder)

- biome.json
- Directorysrc/

- main.ts

- my.code-workspace

## Features

[Section titled “Features”](https://biomejs.dev/reference/vscode/#features)

### Formatting

[Section titled “Formatting”](https://biomejs.dev/reference/vscode/#formatting)

The Biome extension registers itself as a formatter for [supported file types](https://biomejs.dev/internals/language-support), and supports formatting a whole file, or a selection of code.

Run either one of the following commands from the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette):

- To format a whole file, run the `Format Document` command.
- To format a selection of code, select the code and run the `Format Selection` command.

#### Formatting on save

[Section titled “Formatting on save”](https://biomejs.dev/reference/vscode/#formatting-on-save)

To enable formatting on save, set VS Code’s [`editor.formatOnSave`](vscode://settings/editor.formatOnSave) setting to `true`.

### Code fixing

[Section titled “Code fixing”](https://biomejs.dev/reference/vscode/#code-fixing)

The Biome extension registers itself as a code action provider for [supported file types](https://biomejs.dev/internals/language-support), and provides code fixes for diagnostics
that have safe fixes.

#### Fix on save

[Section titled “Fix on save”](https://biomejs.dev/reference/vscode/#fix-on-save)

To enable **Fix on Save**, update VS Code’s [`editor.codeActionsOnSave`](vscode://settings/editor.codeActionsOnSave) setting to include the following. This will apply only [the safe fixes](https://biomejs.dev/linter/#safe-fixes):

```
{

  "editor.codeActionsOnSave": {

    "source.fixAll.biome": "explicit"

  }

}
```

If you want to apply [unsafe fixes](https://biomejs.dev/linter/#unsafe-fixes) on save, you must make the [code fix of the rule safe](https://biomejs.dev/linter/#configure-the-code-fix).

#### Manual quick fixes

[Section titled “Manual quick fixes”](https://biomejs.dev/reference/vscode/#manual-quick-fixes)

To manually apply a quick fix, select the diagnostic and click the `Quick Fix` button.

### Import sorting

[Section titled “Import sorting”](https://biomejs.dev/reference/vscode/#import-sorting)

The extension is able to sort imports on save for [supported file types](https://biomejs.dev/internals/language-support). To enable this feature, set VS Code’s [`editor.codeActionsOnSave`](vscode://settings/editor.codeActionsOnSave) setting to include the following:

```
{

  "editor.codeActionsOnSave": {

    "source.organizeImports.biome": "explicit"

  }

}
```

## Settings reference

[Section titled “Settings reference”](https://biomejs.dev/reference/vscode/#settings-reference)

The following settings are available for the extension.

### `biome.enabled`

[Section titled “biome.enabled”](https://biomejs.dev/reference/vscode/#biomeenabled)

**Default:**`true` \| **Scopes:**`global`, `workspace`, `workspace folder`

This setting controls whether the extension will create LSP session for a workspace folder. When set globally, it applies to all workspace folders, unless they themselves override the setting.

### `biome.configurationPath`

[Section titled “biome.configurationPath”](https://biomejs.dev/reference/vscode/#biomeconfigurationpath)

**Default:**`null` \| **Scopes:**`global`, `workspace`, `workspace folder`

This setting allows you to specify the path to a custom configuration file. If left unspecified, the default configuration file will be used.

### `biome.requireConfiguration`

[Section titled “biome.requireConfiguration”](https://biomejs.dev/reference/vscode/#biomerequireconfiguration)

**Default:**`false` \| **Scopes:**`global`, `workspace`, `workspace folder`

This setting controls whether Biome will register itself as a formatter and diagnostics provider.

When set to `true`, the extension will only register itself as a formatter and diagnostics provider if a `biome.json` file is present in the workspace folder.

### `biome.lsp.bin`

[Section titled “biome.lsp.bin”](https://biomejs.dev/reference/vscode/#biomelspbin)

**Default:**`undefined` \| **Scopes:**`global`, `workspace`, `workspace folder`

This setting allows you to override the path to the `biome` binary. This is useful if you want to use a different version of Biome,
or if you want to use a binary that’s not on your `PATH`. In can be either a path to a binary, or an object that maps a platform to a path.

- [string](https://biomejs.dev/reference/vscode/#tab-panel-238)
- [object](https://biomejs.dev/reference/vscode/#tab-panel-239)

```
{

  "biome.lsp.bin": "/path/to/biome"

}
```

When using an object, the key is the platform identifier, constructed from the `<process.os>-<process.arch>` value, and the value is the path to the binary.

```
{

  "biome.lsp.bin": {

    "darwin-arm64": "/path/to/biome",

    "win32-x64": "/path/to/biome.exe"

  }

}
```

You should be aware of that `@biomejs/biome` doesn’t ship any binaries. The file `@biomejs/biome/bin` is just a tiny
wrapper that delegates the operation to the real binary. The binary installed on your machine depends on the architecture of your OS and architecture.

The binaries are packages that start with `@biomejs/cli-*`, and can be found in [this list](https://www.npmjs.com/search?q=%40biomejs%2Fcli-*).
So, if you’re pointing to the binary installed via `npm`, the configuration will look like this:

- [string](https://biomejs.dev/reference/vscode/#tab-panel-240)
- [object](https://biomejs.dev/reference/vscode/#tab-panel-241)

```
{

  "biome.lsp.bin": "./node_modules/@biomejs/cli-linux-x64/bin"

}
```

When using an object, the key is the platform identifier, constructed from the `<process.os>-<process.arch>` value, and the value is the path to the binary.

```
{

  "biome.lsp.bin": {

    "darwin-arm64": "./node_modules/@biomejs/cli-darwin-arm64/bin",

    "win32-x64": "./node_modules/@biomejs/cli-win32-x64/bin"

  }

}
```

### `biome.runFromTemporaryLocation`

[Section titled “biome.runFromTemporaryLocation”](https://biomejs.dev/reference/vscode/#biomerunfromtemporarylocation)

**Default:**`true (windows), false (others)` \| **Scopes:**`global`, `workspace`, `workspace folder`

Whether to copy the Biome binary and run it from a temporary location.

On Windows, disabling this setting will prevent you from updating Biome in your node modules while an active
LSP session is running, because the OS locks the binary while it’s running. You’ll need to close VS Code before updating Biome.

### `biome.suggestInstallingGlobally`

[Section titled “biome.suggestInstallingGlobally”](https://biomejs.dev/reference/vscode/#biomesuggestinstallingglobally)

**Default:**`true` \| **Scopes:**`global`, `workspace`, `workspace folder`

When a global installation of Biome is required but not found in the `PATH`, the extension will suggest installing it.

This setting controls whether that suggestion popup is shown.

### `biome.lsp.trace.server`

[Section titled “biome.lsp.trace.server”](https://biomejs.dev/reference/vscode/#biomelsptraceserver)

**Default:**`off` \| **Scopes:**`global`

This setting allows to set the logging level of the Biome LSP trace. The possible values are `off`, `messages`, `verbose`.
You may want to set this setting to `verbose` when you encounter issues with the extension, and you’d like to share the logs with us.

## Troubleshooting

[Section titled “Troubleshooting”](https://biomejs.dev/reference/vscode/#troubleshooting)

There may be times when you encounter unexpected issues with the extension. Here a a couple tip to help you troubleshoot
the most common issues, and reset the extension’s state.

### Accessing the LSP trace

[Section titled “Accessing the LSP trace”](https://biomejs.dev/reference/vscode/#accessing-the-lsp-trace)

If you encounter issues with the extension, we may ask you to share the LSP trace with us. You can do so by setting the [`biome.lsp.trace.server`](https://biomejs.dev/reference/vscode/#biomelsptrace_server) setting to `verbose`,
and re-running the action that caused the issue. The trace will be made available the [output](vscode://workbrench/panel) panel, under the `Biome LSP trace (xxx)` select option.

## Migrating from the `2.x` extension

[Section titled “Migrating from the 2.x extension”](https://biomejs.dev/reference/vscode/#migrating-from-the-2x-extension)

If you are migrating from the `2.x` extension, we recommend the following steps, in this exact order:

1. Update the extension
2. Close the editor completely.
3. Open your task manager, and make sure to kill all processes named `biome`.
4. Open your editor.

This will destroy possible old Daemon connections that are still connected to the editor, but can’t be shutdown gracefully by the extension, which caused
some incorrect formatting when a file was saved.

### Changes

[Section titled “Changes”](https://biomejs.dev/reference/vscode/#changes)

- The `biome.lspBin` setting has been deprecated in favor of `biome.lsp.bin`. It will still work for now, but we recommend updating your settings to use the new name.
- The `biome.requireConfigFile` has been renamed to `biome.requireConfiguration`. You should migrate the setting now as **the old is no longer supported**.

Copyright (c) 2023-present Biome Developers and Contributors.
