[Skip to content](https://biomejs.dev/guides/getting-started/#_top)

# Getting Started

Biome is best installed as a development dependency of your projects, but it is
also available as a [standalone executable](https://biomejs.dev/guides/manual-installation) that doesn’t require Node.js.

- [npm](https://biomejs.dev/guides/getting-started/#tab-panel-167)
- [pnpm](https://biomejs.dev/guides/getting-started/#tab-panel-168)
- [bun](https://biomejs.dev/guides/getting-started/#tab-panel-169)
- [deno](https://biomejs.dev/guides/getting-started/#tab-panel-170)
- [yarn](https://biomejs.dev/guides/getting-started/#tab-panel-171)

```
npm i -D -E @biomejs/biome
```

```
pnpm add -D -E @biomejs/biome
```

```
bun add -D -E @biomejs/biome
```

```
deno add -D npm:@biomejs/biome
```

```
yarn add -D -E @biomejs/biome
```

## Configuration

[Section titled “Configuration”](https://biomejs.dev/guides/getting-started/#configuration)

Although Biome can run with zero configuration, you’ll likely want to tweak some
settings to suit your project’s needs, in which case you can run the following
command to generate a `biome.json` configuration file.

- [npm](https://biomejs.dev/guides/getting-started/#tab-panel-172)
- [pnpm](https://biomejs.dev/guides/getting-started/#tab-panel-173)
- [bun](https://biomejs.dev/guides/getting-started/#tab-panel-174)
- [deno](https://biomejs.dev/guides/getting-started/#tab-panel-175)
- [yarn](https://biomejs.dev/guides/getting-started/#tab-panel-176)

```
npx @biomejs/biome init
```

```
pnpm exec biome init
```

```
bunx --bun biome init
```

```
deno run -A npm:@biomejs/biome init
```

```
yarn exec biome init
```

## Usage

[Section titled “Usage”](https://biomejs.dev/guides/getting-started/#usage)

Lets get a quick overview of how to use Biome in your project.

### Command-line interface

[Section titled “Command-line interface”](https://biomejs.dev/guides/getting-started/#command-line-interface)

Biome provides a [command-line interface](https://biomejs.dev/reference/cli) to format, lint, and check your code.

- [npm](https://biomejs.dev/guides/getting-started/#tab-panel-177)
- [pnpm](https://biomejs.dev/guides/getting-started/#tab-panel-178)
- [bun](https://biomejs.dev/guides/getting-started/#tab-panel-179)
- [deno](https://biomejs.dev/guides/getting-started/#tab-panel-180)
- [yarn](https://biomejs.dev/guides/getting-started/#tab-panel-181)

```
# Format all files

npx @biomejs/biome format --write

# Format specific files

npx @biomejs/biome format --write <files>

# Lint files and apply safe fixes to all files

npx @biomejs/biome lint --write

# Lint files and apply safe fixes to specific files

npx @biomejs/biome lint --write <files>

# Format, lint, and organize imports of all files

npx @biomejs/biome check --write

# Format, lint, and organize imports of specific files

npx @biomejs/biome check --write <files>
```

```
# Format all files

pnpm exec biome format --write

# Format specific files

pnpm exec biome format --write <files>

# Lint and apply safe fixes to all files

pnpm exec biome lint --write

# Lint files and apply safe fixes to specific files

pnpm exec biome lint --write <files>

# Format, lint, and organize imports of all files

pnpm exec biome check --write

# Format, lint, and organize imports of specific files

pnpm exec biome check --write <files>
```

```
# Format all files

bunx biome format --write

# Format specific files

bunx biome format --write <files>

# Lint and apply safe fixes to all files

bunx biome lint --write

# Lint files and apply safe fixes to specific files

bunx biome lint --write <files>

# Format, lint, and organize imports of all files

bunx biome check --write

# Format, lint, and organize imports of specific files

bunx biome check --write <files>
```

```
# Format specific files

deno run -A npm:@biomejs/biome format --write <files>

# Format all files

deno run -A npm:@biomejs/biome format --write

# Lint files and apply safe fixes to all files

deno run -A npm:@biomejs/biome lint --write

# Lint files and apply safe fixes to specific files

deno run -A npm:@biomejs/biome lint --write <files>

# Format, lint, and organize imports of all files

deno run -A npm:@biomejs/biome check --write

# Format, lint, and organize imports of specific files

deno run -A npm:@biomejs/biome check --write <files>
```

```
# Format all files

yarn exec biome format --write

# Format specific files

yarn exec biome format --write <files>

# Lint files and apply safe fixes to all files

yarn exec biome lint --write

# Lint files and apply safe fixes to specific files

yarn exec biome lint --write <files>

# Format, lint, and organize imports of all files

yarn exec biome check --write

# Format, lint, and organize imports of specific files

yarn exec biome check --write <files>
```

### Editor integrations

[Section titled “Editor integrations”](https://biomejs.dev/guides/getting-started/#editor-integrations)

Biome is available as a first-party extension in your favorite editors.

- [VS Code](https://biomejs.dev/guides/editors/first-party-extensions#vs-code)
- [IntelliJ](https://biomejs.dev/guides/editors/first-party-extensions#intellij)
- [Zed](https://biomejs.dev/guides/editors/first-party-extensions#zed)

There are also [community extensions](https://biomejs.dev/guides/editors/third-party-extensions)
for other editors, such as **Vim**, **Neovim**, and **Sublime Text**, to name
a few.

### Continuous Integration

[Section titled “Continuous Integration”](https://biomejs.dev/guides/getting-started/#continuous-integration)

Run `biome ci` as part of your CI pipeline to enforce code quality and consistency
across your team. It works just like the `biome check` command, but is optimized for
CI environments.

- [GitHub Actions](https://biomejs.dev/recipes/continuous-integration#github-actions)
- [GitLab CI](https://biomejs.dev/recipes/continuous-integration#gitlab-ci)

See the [Continuous Integration](https://biomejs.dev/recipes/continuous-integration) recipes for more examples.

## Next Steps

[Section titled “Next Steps”](https://biomejs.dev/guides/getting-started/#next-steps)

Success! You’re now ready to use Biome. 🥳

- [Migrate from ESLint and Prettier](https://biomejs.dev/guides/migrate-eslint-prettier)
- Learn more about how to [configure Biome](https://biomejs.dev/guides/configure-biome)
- Learn more about how to use and configure the [formatter](https://biomejs.dev/formatter)
- Learn more about how to use and configure the [linter](https://biomejs.dev/linter)
- Get familiar with the [CLI commands and options](https://biomejs.dev/reference/cli)
- Get familiar with the [configuration options](https://biomejs.dev/reference/configuration)
- Join our [community on Discord](https://biomejs.dev/chat)

Copyright (c) 2023-present Biome Developers and Contributors.
