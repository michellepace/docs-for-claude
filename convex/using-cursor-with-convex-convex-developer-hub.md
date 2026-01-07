# Using Cursor with Convex

[Cursor](https://cursor.com), the AI code editor, makes it easy to write and maintain apps built with Convex. Let's walk through how to setup Cursor for the best possible results with Convex.

## Add Convex `.cursor/rules`

To get the best results from Cursor put the model specific `.mdc` files in your project's `.cursor/rules` directory.

* [Convex Cursor Rules](https://convex.link/convex_rules.mdc)

[](/video/showing_where_to_put_convex_rules.mp4)

We're constantly working on improving the quality of these rules for Convex by using rigorous evals. You can help by [contributing to our evals repo](https://github.com/get-convex/convex-evals).

## Setup the Convex MCP Server[​](#setup-the-convex-mcp-server "Direct link to Setup the Convex MCP Server")

The Convex CLI comes with a [Convex Model Context Protocol](/ai/convex-mcp-server.md) (MCP) server built in. The Convex MCP server gives your AI coding agent access to the your Convex deployment to query and optimize your project.

### Quick Install[​](#quick-install "Direct link to Quick Install")

You can click this handy deep-link below:

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=convex\&config=eyJjb21tYW5kIjoibnB4IC15IGNvbnZleEBsYXRlc3QgbWNwIHN0YXJ0In0%3D)

### Manual Install[​](#manual-install "Direct link to Manual Install")

To get started with Cursor, open "Cursor Settings > Tools & Integrations", click on "New MCP Server", and add a "convex" section to "mcpServers" in the `mcp.json` file that's opened.

```
{
  "mcpServers": {
    "convex": {
      "command": "npx",
      "args": ["-y", "convex@latest", "mcp", "start"]
    }
  }
}
```

You can also install the Convex MCP [for just one project](https://docs.cursor.com/en/context/mcp#configuration-locations).

After adding the server, ensure the "convex" server is enabled and lit up green (it make take a minute the first time while the NPM package downloads).

Now start asking it questions like:

* Evaluate my convex schema and suggest improvements
* What are this app's public endpoints?
* Run the `my_convex_function` query

## Tips and tricks[​](#tips-and-tricks "Direct link to Tips and tricks")

### Install and run Convex yourself[​](#install-and-run-convex-yourself "Direct link to Install and run Convex yourself")

Keeping Convex running is crucial because [it automatically generates](https://docs.convex.dev/cli#run-the-convex-dev-server) the client-side types. Without this, the agent can get stuck in a linting loop since it can't access the types for the queries and mutations it created.

We recommended that you install (`npm install convex`) and run convex (`npx convex dev`) yourself in a terminal window.

### Keep your requests small[​](#keep-your-requests-small "Direct link to Keep your requests small")

The best results when using agentic LLMs can be found when keeping the amount of changes you want to make small and git commit frequently. This lets you be more specific around the context you provide the agent and it means the agent doesn't need to do a lot of searching for context.

After each successful prompt or series of prompts it is a good idea to commit your changes so that its simple to rollback to that point should the next prompt cause issues.

### Update and reference your `README.md`[​](#update-and-reference-your-readmemd "Direct link to update-and-reference-your-readmemd")

The agent needs context about the specific business goals for your project. While it can infer some details from the files it reads, this becomes more challenging as your project grows. Providing general information about your project gives the agent a helpful head start.

Rather than including this information in each prompt, it's better to write a comprehensive README.md file in your project root and reference it.

[Some people](https://youtu.be/2PjmPU07KNs?t=145) advocate for crafting a Product Requirements Document (PRD), this may be a good idea for more complex projects.

### Add Convex docs[​](#add-convex-docs "Direct link to Add Convex docs")

Adding Convex docs can let you specifically refer to Convex features when building your app.

From **`Cursor Settings`** > **`Indexing & Docs`** > **`Docs`** add new doc, use the URL "<https://docs.convex.dev/home>"

Cursor will then index all of the Convex docs for the LLM to use.

![Chat UI](/assets/images/indexed_docs-90bb59330756c00540015c53da6a484c.webp)

You can then reference those docs in your prompt with the `@Convex` symbol.

![Chat UI](/assets/images/reference_convex_docs-c791c41ddbd7663244fda1c4c59a43d9.webp)

Add more Convex knowledge

You can perform the above steps for <https://stack.convex.dev/> too if you would like to provide even more context to the agent.
