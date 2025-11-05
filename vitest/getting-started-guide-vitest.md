[Skip to content](https://vitest.dev/guide/#VPContent)

On this page

# Getting Started [​](https://vitest.dev/guide/\#getting-started)

## Overview [​](https://vitest.dev/guide/\#overview)

Vitest (pronounced as _"veetest"_) is a next generation testing framework powered by Vite.

You can learn more about the rationale behind the project in the [Why Vitest](https://vitest.dev/guide/why) section.

## Trying Vitest Online [​](https://vitest.dev/guide/\#trying-vitest-online)

You can try Vitest online on [StackBlitz](https://vitest.new/). It runs Vitest directly in the browser, and it is almost identical to the local setup but doesn't require installing anything on your machine.

## Adding Vitest to Your Project [​](https://vitest.dev/guide/\#adding-vitest-to-your-project)

[Learn how to install by Video](https://vueschool.io/lessons/how-to-install-vitest?friend=vueuse)

npmyarnpnpmbun

bash

```
npm install -D vitest
```

bash

```
yarn add -D vitest
```

bash

```
pnpm add -D vitest
```

bash

```
bun add -D vitest
```

TIP

Vitest requires Vite >=v6.0.0 and Node >=v20.0.0

It is recommended that you install a copy of `vitest` in your `package.json`, using one of the methods listed above. However, if you would prefer to run `vitest` directly, you can use `npx vitest` (the `npx` tool comes with npm and Node.js).

The `npx` tool will execute the specified command. By default, `npx` will first check if the command exists in the local project's binaries. If it is not found there, `npx` will look in the system's `$PATH` and execute it if found. If the command is not found in either location, `npx` will install it in a temporary location prior to execution.

## Writing Tests [​](https://vitest.dev/guide/\#writing-tests)

As an example, we will write a simple test that verifies the output of a function that adds two numbers.

sum.js

js

```
export function sum(a, b) {
  return a + b
}
```

sum.test.js

js

```
import { expect, test } from 'vitest'
import { sum } from './sum.js'

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3)
})
```

TIP

By default, tests must contain `.test.` or `.spec.` in their file name.

Next, in order to execute the test, add the following section to your `package.json`:

package.json

json

```
{
  "scripts": {
    "test": "vitest"
  }
}
```

Finally, run `npm run test`, `yarn test` or `pnpm test`, depending on your package manager, and Vitest will print this message:

txt

```
✓ sum.test.js (1)
  ✓ adds 1 + 2 to equal 3

Test Files  1 passed (1)
     Tests  1 passed (1)
  Start at  02:15:44
  Duration  311ms
```

WARNING

If you are using Bun as your package manager, make sure to use `bun run test` command instead of `bun test`, otherwise Bun will run its own test runner.

Learn more about the usage of Vitest, see the [API](https://vitest.dev/api/) section.

## Configuring Vitest [​](https://vitest.dev/guide/\#configuring-vitest)

One of the main advantages of Vitest is its unified configuration with Vite. If present, `vitest` will read your root `vite.config.ts` to match with the plugins and setup as your Vite app. For example, your Vite [resolve.alias](https://vitejs.dev/config/shared-options.html#resolve-alias) and [plugins](https://vitejs.dev/guide/using-plugins) configuration will work out-of-the-box. If you want a different configuration during testing, you can:

- Create `vitest.config.ts`, which will have the higher priority
- Pass `--config` option to CLI, e.g. `vitest --config ./path/to/vitest.config.ts`
- Use `process.env.VITEST` or `mode` property on `defineConfig` (will be set to `test` if not overridden) to conditionally apply different configuration in `vite.config.ts`. Note that like any other environment variable, `VITEST` is also exposed on `import.meta.env` in your tests

Vitest supports the same extensions for your configuration file as Vite does: `.js`, `.mjs`, `.cjs`, `.ts`, `.cts`, `.mts`. Vitest does not support `.json` extension.

If you are not using Vite as your build tool, you can configure Vitest using the `test` property in your config file:

vitest.config.ts

ts

```
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    // ...
  },
})
```

TIP

Even if you do not use Vite yourself, Vitest relies heavily on it for its transformation pipeline. For that reason, you can also configure any property described in [Vite documentation](https://vitejs.dev/config/).

If you are already using Vite, add `test` property in your Vite config. You'll also need to add a reference to Vitest types using a [triple slash directive](https://www.typescriptlang.org/docs/handbook/triple-slash-directives.html#-reference-types-) at the top of your config file.

vite.config.ts

ts

```
/// <reference types="vitest/config" />
import { defineConfig } from 'vite'

export default defineConfig({
  test: {
    // ...
  },
})
```

See the list of config options in the [Config Reference](https://vitest.dev/config/)

WARNING

If you decide to have two separate config files for Vite and Vitest, make sure to define the same Vite options in your Vitest config file since it will override your Vite file, not extend it. You can also use `mergeConfig` method from `vite` or `vitest/config` entries to merge Vite config with Vitest config:

vitest.config.mjsvite.config.mjs

ts

```
import { defineConfig, mergeConfig } from 'vitest/config'
import viteConfig from './vite.config.mjs'

export default mergeConfig(viteConfig, defineConfig({
  test: {
    // ...
  },
}))
```

ts

```
import { defineConfig } from 'vite'
import Vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [Vue()],
})
```

However, we recommend using the same file for both Vite and Vitest, instead of creating two separate files.

## Projects Support [​](https://vitest.dev/guide/\#projects-support)

Run different project configurations inside the same project with [Test Projects](https://vitest.dev/guide/projects). You can define a list of files and folders that define your projects in `vitest.config` file.

vitest.config.ts

ts

```
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    projects: [\
      // you can use a list of glob patterns to define your projects\
      // Vitest expects a list of config files\
      // or directories where there is a config file\
      'packages/*',\
      'tests/*/vitest.config.{e2e,unit}.ts',\
      // you can even run the same tests,\
      // but with different configs in the same "vitest" process\
      {\
        test: {\
          name: 'happy-dom',\
          root: './shared_tests',\
          environment: 'happy-dom',\
          setupFiles: ['./setup.happy-dom.ts'],\
        },\
      },\
      {\
        test: {\
          name: 'node',\
          root: './shared_tests',\
          environment: 'node',\
          setupFiles: ['./setup.node.ts'],\
        },\
      },\
    ],
  },
})
```

## Command Line Interface [​](https://vitest.dev/guide/\#command-line-interface)

In a project where Vitest is installed, you can use the `vitest` binary in your npm scripts, or run it directly with `npx vitest`. Here are the default npm scripts in a scaffolded Vitest project:

package.json

json

```
{
  "scripts": {
    "test": "vitest",
    "coverage": "vitest run --coverage"
  }
}
```

To run tests once without watching for file changes, use `vitest run`. You can specify additional CLI options like `--port` or `--https`. For a full list of CLI options, run `npx vitest --help` in your project.

Learn more about the [Command Line Interface](https://vitest.dev/guide/cli)

## Automatic Dependency Installation [​](https://vitest.dev/guide/\#automatic-dependency-installation)

Vitest will prompt you to install certain dependencies if they are not already installed. You can disable this behavior by setting the `VITEST_SKIP_INSTALL_CHECKS=1` environment variable.

## IDE Integrations [​](https://vitest.dev/guide/\#ide-integrations)

We also provided an official extension for Visual Studio Code to enhance your testing experience with Vitest.

[Install from VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=vitest.explorer)

Learn more about [IDE Integrations](https://vitest.dev/guide/ide)

## Examples [​](https://vitest.dev/guide/\#examples)

| Example | Source | Playground |
| --- | --- | --- |
| `basic` | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/basic) | [Play Online](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/basic?initialPath=__vitest__/) |
| `fastify` | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/fastify) | [Play Online](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/fastify?initialPath=__vitest__/) |
| `in-source-test` | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/in-source-test) | [Play Online](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/in-source-test?initialPath=__vitest__/) |
| `lit` | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/lit) | [Play Online](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/lit?initialPath=__vitest__/) |
| `vue` | [GitHub](https://github.com/vitest-tests/browser-examples/tree/main/examples/vue) | [Play Online](https://stackblitz.com/fork/github/vitest-tests/browser-examples/tree/main/examples/vue?initialPath=__vitest__/) |
| `marko` | [GitHub](https://github.com/marko-js/examples/tree/master/examples/library-ts) | [Play Online](https://stackblitz.com/fork/github/marko-js/examples/tree/master/examples/library-ts/) |
| `preact` | [GitHub](https://github.com/vitest-tests/browser-examples/tree/main/examples/preact) | [Play Online](https://stackblitz.com/fork/github/vitest-tests/browser-examples/tree/main/examples/preact?initialPath=__vitest__/) |
| `react` | [GitHub](https://github.com/vitest-tests/browser-examples/tree/main/examples/react) | [Play Online](https://stackblitz.com/fork/github/vitest-tests/browser-examples/tree/main/examples/react?initialPath=__vitest__/) |
| `solid` | [GitHub](https://github.com/vitest-tests/browser-examples/tree/main/examples/solid) | [Play Online](https://stackblitz.com/fork/github/vitest-tests/browser-examples/tree/main/examples/solid?initialPath=__vitest__/) |
| `svelte` | [GitHub](https://github.com/vitest-tests/browser-examples/tree/main/examples/svelte) | [Play Online](https://stackblitz.com/fork/github/vitest-tests/browser-examples/tree/main/examples/svelte?initialPath=__vitest__/) |
| `sveltekit` | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/sveltekit) | [Play Online](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/sveltekit?initialPath=__vitest__/) |
| `profiling` | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/profiling) | Not Available |
| `typecheck` | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/typecheck) | [Play Online](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/typecheck?initialPath=__vitest__/) |
| `projects` | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/projects) | [Play Online](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/projects?initialPath=__vitest__/) |

## Projects using Vitest [​](https://vitest.dev/guide/\#projects-using-vitest)

- [unocss](https://github.com/unocss/unocss)
- [unplugin-auto-import](https://github.com/antfu/unplugin-auto-import)
- [unplugin-vue-components](https://github.com/antfu/unplugin-vue-components)
- [vue](https://github.com/vuejs/core)
- [vite](https://github.com/vitejs/vite)
- [vitesse](https://github.com/antfu/vitesse)
- [vitesse-lite](https://github.com/antfu/vitesse-lite)
- [fluent-vue](https://github.com/demivan/fluent-vue)
- [vueuse](https://github.com/vueuse/vueuse)
- [milkdown](https://github.com/Saul-Mirone/milkdown)
- [gridjs-svelte](https://github.com/iamyuu/gridjs-svelte)
- [spring-easing](https://github.com/okikio/spring-easing)
- [bytemd](https://github.com/bytedance/bytemd)
- [faker](https://github.com/faker-js/faker)
- [million](https://github.com/aidenybai/million)
- [Vitamin](https://github.com/wtchnm/Vitamin)
- [neodrag](https://github.com/PuruVJ/neodrag)
- [svelte-multiselect](https://github.com/janosh/svelte-multiselect)
- [iconify](https://github.com/iconify/iconify)
- [tdesign-vue-next](https://github.com/Tencent/tdesign-vue-next)
- [cz-git](https://github.com/Zhengqbbb/cz-git)

## Using Unreleased Commits [​](https://vitest.dev/guide/\#using-unreleased-commits)

Each commit on main branch and a PR with a `cr-tracked` label are published to [pkg.pr.new](https://github.com/stackblitz-labs/pkg.pr.new). You can install it by `npm i https://pkg.pr.new/vitest@{commit}`.

If you want to test your own modification locally, you can build and link it yourself ( [pnpm](https://pnpm.io/) is required):

bash

```
git clone https://github.com/vitest-dev/vitest.git
cd vitest
pnpm install
cd packages/vitest
pnpm run build
pnpm link --global # you can use your preferred package manager for this step
```

Then go to the project where you are using Vitest and run `pnpm link --global vitest` (or the package manager that you used to link `vitest` globally).

## Community [​](https://vitest.dev/guide/\#community)

If you have questions or need help, reach out to the community at [Discord](https://chat.vitest.dev/) and [GitHub Discussions](https://github.com/vitest-dev/vitest/discussions).