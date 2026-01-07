# Convex MCP Server

The Convex [Model Context Protocol](https://docs.cursor.com/context/model-context-protocol) (MCP) server provides several tools that allow AI agents to interact with your Convex deployment.

## Setup[​](#setup "Direct link to Setup")

Add the following command to your MCP servers configuration:

`npx -y convex@latest mcp start`

For Cursor you can use this quick link to install:

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=convex\&config=eyJjb21tYW5kIjoibnB4IC15IGNvbnZleEBsYXRlc3QgbWNwIHN0YXJ0In0%3D)

or see editor specific instructions:

* [Cursor](/ai/using-cursor.md#setup-the-convex-mcp-server)
* [Windsurf](/ai/using-windsurf.md#setup-the-convex-mcp-server)
* [VS Code](/ai/using-github-copilot.md#setup-the-convex-mcp-server)
* Claude Code: add the MCP server and test with
  <!-- -->
  ```
  claude mcp add-json convex '{"type":"stdio","command":"npx","args":["convex","mcp","start"]}'
  claude mcp get convex
  ```

## Available Tools[​](#available-tools "Direct link to Available Tools")

### Deployment Tools[​](#deployment-tools "Direct link to Deployment Tools")

* **`status`**: Queries available deployments and returns a deployment selector that can be used with other tools. This is typically the first tool you'll use to find your Convex deployment.

### Table Tools[​](#table-tools "Direct link to Table Tools")

* **`tables`**: Lists all tables in a deployment along with their:

  * Declared schemas (if present)
  * Inferred schemas (automatically tracked by Convex)
  * Table names and metadata

* **`data`**: Allows pagination through documents in a specified table.

* **`runOneoffQuery`**: Enables writing and executing sandboxed JavaScript queries against your deployment's data. These queries are read-only and cannot modify the database.

### Function Tools[​](#function-tools "Direct link to Function Tools")

* **`functionSpec`**: Provides metadata about all deployed functions, including:

  * Function types
  * Visibility settings
  * Interface specifications

* **`run`**: Executes deployed Convex functions with provided arguments.

* **`logs`**: Fetches a chunk of recent function execution log entries, similar to `npx convex logs` but as structured objects.

### Environment Variable Tools[​](#environment-variable-tools "Direct link to Environment Variable Tools")

* **`envList`**: Lists all environment variables for a deployment
* **`envGet`**: Retrieves the value of a specific environment variable
* **`envSet`**: Sets a new environment variable or updates an existing one
* **`envRemove`**: Removes an environment variable from the deployment

[Read more about how to use the Convex MCP Server](https://stack.convex.dev/convex-mcp-server)
