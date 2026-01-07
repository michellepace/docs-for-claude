# AI Code Generation

## [Prompt to build an app with Convex Chef](https://chef.convex.dev)

Convex is designed around a small set of composable abstractions with strong guarantees that result in code that is not only faster to write, but easier to read and maintain, whether written by a team member or an LLM. Key features make sure you get bug-free AI generated code:

1. **Queries are Just TypeScript** Your database queries are pure TypeScript functions with end-to-end type safety and IDE support. This means AI can generate database code using the large training set of TypeScript code without switching to SQL.
2. **Less Code for the Same Work** Since so much infrastructure and boiler plate is automatically managed by Convex there is less code to write, and thus less code to get wrong.
3. **Automatic Reactivity** The reactive system automatically tracks data dependencies and updates your UI. AI doesn't need to manually manage subscriptions, WebSocket connections, or complex state synchronization—Convex handles all of this automatically.
4. **Transactional Guarantees** Queries are read-only and mutations run in transactions. These constraints make it nearly impossible for AI to write code that could corrupt your data or leave your app in an inconsistent state.

Together, these features mean AI can focus on your business logic while Convex's guarantees prevent common failure modes. For up-to-date information on which models work best with Convex, check out our LLM [leaderboard](https://convex.dev/llm-leaderboard).

## Convex AI rules[​](#convex-ai-rules "Direct link to Convex AI rules")

AI code generation is most effective when you provide it with a set of rules to follow.

See these documents for install instructions:

* [Cursor](/ai/using-cursor.md#add-convex-cursorrules)
* [Windsurf](/ai/using-windsurf.md#add-convex-rules)
* [GitHub Copilot](/ai/using-github-copilot.md#add-convex-instructions)

For all other IDEs, add the following rules file to your project and refer to it when prompting for changes:

* [convex\_rules.txt](https://convex.link/convex_rules.txt)

We're constantly working on improving the quality of these rules for Convex by using rigorous evals. You can help by [contributing to our evals repo](https://github.com/get-convex/convex-evals).

## Using Convex with Background Agents[​](#using-convex-with-background-agents "Direct link to Using Convex with Background Agents")

Remote cloud-based coding agents like Jules, Devin, Codex, and Cursor background agents can use Convex deployments when the CLI is in [Agent Mode](/cli/agent-mode.md). This limits the permissions necessary for these remote dev environments while letting agents run codegen, iterate on code, run tests, run one-off functions.

A good setup script for e.g. ChatGPT Codex might include

```
npm i
CONVEX_AGENT_MODE=anonymous npx convex dev --once
```

or

```
bun i
CONVEX_AGENT_MODE=anonymous bun x convex dev --once
```

This command requires "full" internet access to download the binary.

## Convex MCP Server[​](#convex-mcp-server "Direct link to Convex MCP Server")

[Setup the Convex MCP server](/ai/convex-mcp-server.md) to give your AI coding agent access to your Convex deployment to query and optimize your project.
