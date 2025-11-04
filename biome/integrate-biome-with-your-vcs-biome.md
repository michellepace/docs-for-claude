[Skip to content](https://biomejs.dev/guides/integrate-in-vcs/#_top)

# Integrate Biome with your VCS

The VCS (Version Control System) integration is meant to take advantage of **additional** features that only a VCS can provide.
At the moment, Biome only supports Git.
The integration is **opt-in**.
You have to enable `vcs.enabled` and set `vcs.clientKind` in the Biome configuration file:

```
{

  "vcs": {

    "enabled": true,

    "clientKind": "git"

  }

}
```

This configuration doesn’t do **anything per se**. You need to opt-in the features you want.

### Use the ignore file

[Section titled “Use the ignore file”](https://biomejs.dev/guides/integrate-in-vcs/#use-the-ignore-file)

Enable `vcs.useIgnoreFile`, to allow Biome to ignore all the files and directories listed in the project’s VCS ignore file as well as a `.ignore` file.

```
{

  "vcs": {

    "enabled": true,

    "clientKind": "git",

    "useIgnoreFile": true

  }

}
```

### Process only changed files

[Section titled “Process only changed files”](https://biomejs.dev/guides/integrate-in-vcs/#process-only-changed-files)

This is a feature that is available only via CLI, and allows processing **only** the files that have **changed** from one revision to another.

First, you have to update your configuration file and tell Biome what’s the default branch via the `vcs.defaultBranch` field:

```
{

  "vcs": {

    "enabled": true,

    "clientKind": "git",

    "useIgnoreFile": true,

    "defaultBranch": "main"

  }

}
```

Then, add the `--changed` option to your command, to process only those files that your VCS acknowledged as “changed”. Biome, with the help of the VCS, will determine the changed file from the branch `main` and your current revision:

```
biome check --changed
```

Alternatively, you can use the option `--since` to specify an arbitrary branch. This option **takes precedence** over the option `vcs.defaultBranch`. For example, you might want to check your changes against the `next` branch:

```
biome check --changed --since=next
```

### Process only staged files

[Section titled “Process only staged files”](https://biomejs.dev/guides/integrate-in-vcs/#process-only-staged-files)

Before committing your changes, you may want to check the formatting and lints files that have been added to the _index_, also known as _staged files_.
Add the `--staged` option to your command, to process only those files:

```
biome check --staged
```

The `--staged` option is not available on the `ci` command because you are not expected to commit changes in a CI environment.

Copyright (c) 2023-present Biome Developers and Contributors.
