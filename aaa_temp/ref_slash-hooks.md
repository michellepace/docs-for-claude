# Claude Code: Slash Commands vs Hooks

**Report Generated:** 2025-10-13

---

## Overview

### What are Slash Commands?

Slash commands are user-defined or built-in prompts that extend Claude Code's functionality through markdown files. They provide a way to create reusable, parameterized instructions that Claude executes on demand.

**Key characteristics:**

- User-triggered operations that start with `/`
- Defined as markdown files with optional frontmatter
- Can accept arguments and execute bash commands
- Support file references using `@` prefix
- Available from project (`.claude/commands/`), user (`~/.claude/commands/`), plugins, or MCP servers

### What are Hooks?

Hooks are automated shell commands that execute in response to specific events during Claude Code sessions. They enable reactive workflows by intercepting tool calls, prompt submissions, and session lifecycle events.

**Key characteristics:**

- Event-driven automation triggered by Claude Code events
- Configured in JSON settings files
- Execute shell commands automatically
- Can approve, deny, or modify tool operations
- Receive JSON input via stdin and return structured output

---

## Comparison Tables

### 1. Trigger Mechanism

| Aspect | Slash Commands | Hooks |
|--------|---------------|-------|
| **Activation** | Manual user invocation | Automatic event-driven execution |
| **Syntax** | `/command-name [args]` | N/A (configured in settings) |
| **Control** | User decides when to run | System triggers based on events |
| **Frequency** | On-demand, explicit | Every matching event occurrence |

### 2. Configuration and Location

| Aspect | Slash Commands | Hooks |
|--------|---------------|-------|
| **Definition Format** | Markdown files (`.md`) | JSON in settings files |
| **Project-Level** | `.claude/commands/*.md` | `.claude/settings.json` |
| **User-Level** | `~/.claude/commands/*.md` | `~/.claude/settings.json` |
| **Local Override** | N/A | `.claude/settings.local.json` |
| **Parameters** | Frontmatter in markdown | JSON configuration objects |

### 3. Capabilities

| Feature | Slash Commands | Hooks |
|---------|---------------|-------|
| **Execute bash commands** | Yes (with `!` prefix) | Yes (primary function) |
| **Accept arguments** | Yes (`$ARGUMENTS`, `$1`, `$2`, etc.) | Yes (via JSON stdin) |
| **File references** | Yes (using `@` prefix) | No (must use bash commands) |
| **Claude execution** | Yes (prompts for Claude to follow) | Limited (provides feedback/blocks) |
| **Modify tool behavior** | No | Yes (approve/deny/modify) |
| **Add context** | Yes (entire command is context) | Yes (via `additionalContext`) |
| **Block operations** | No | Yes (via decision control) |
| **Access conversation** | Yes (via `transcript_path` in bash) | Yes (via `transcript_path` in JSON) |

### 4. Use Cases

| Scenario | Slash Commands | Hooks |
|----------|---------------|-------|
| **Code review workflow** | Excellent - `/review [file]` | Good - validate after edits |
| **Automated formatting** | Poor - requires manual trigger | Excellent - auto-format on save |
| **Git operations** | Excellent - `/commit`, `/pr` | Good - validate before commit |
| **Security validation** | Moderate - must remember to run | Excellent - automatic enforcement |
| **Documentation generation** | Excellent - `/generate-docs` | Poor - no clear event trigger |
| **Testing workflows** | Excellent - `/test [suite]` | Good - run tests after edits |
| **File protection** | N/A | Excellent - block unsafe operations |
| **Context injection** | Excellent - deliberate context | Good - automatic context |
| **Notification/logging** | Poor - manual process | Excellent - automatic tracking |

### 5. Execution Model

| Aspect | Slash Commands | Hooks |
|--------|---------------|-------|
| **Timing** | Synchronous (user waits) | Can be async (depends on event) |
| **Timeout** | Inherits from tool/model | 60s default, configurable per command |
| **Parallelization** | N/A (single command) | Multiple hooks run in parallel |
| **Output destination** | Claude's context + user display | Varies by event type |
| **Error handling** | Claude sees errors | Exit codes control behavior |
| **Blocking capability** | No | Yes (via exit code 2 or JSON) |

### 6. Permission and Security

| Aspect | Slash Commands | Hooks |
|--------|---------------|-------|
| **Requires approval** | Yes (if using restricted tools) | No (executes automatically) |
| **Permission control** | Via `allowed-tools` frontmatter | Via exit codes and JSON output |
| **Risk level** | Lower (user-initiated) | Higher (automatic execution) |
| **Validation** | Manual review before use | Must test thoroughly |
| **Tool restriction** | Can specify `allowed-tools` | Can approve/deny any tool |

---

## When to Use Each

### Use Slash Commands When

1. **User-initiated workflows** - Tasks that require deliberate human decision
   - Example: `/review-pr`, `/deploy`, `/generate-report`

2. **Complex multi-step operations** - Workflows needing Claude's reasoning
   - Example: `/refactor [component]`, `/add-feature [description]`

3. **Parameterized tasks** - Operations with variable inputs
   - Example: `/test-suite [name]`, `/analyze-performance [file]`

4. **Documentation and analysis** - Research or explanation tasks
   - Example: `/explain-architecture`, `/security-audit`

5. **Git operations** - Commit, PR creation, branch management
   - Example: `/commit [message]`, `/pr`, `/sync-branch`

6. **Project-specific workflows** - Team-shared procedures
   - Example: `/deploy-staging`, `/run-migrations`, `/check-deps`

### Use Hooks When

1. **Automatic validation** - Enforce rules without manual intervention
   - Example: Lint checks, security scans, style validation

2. **File protection** - Prevent accidental modifications
   - Example: Block writes to production configs, protect `.env` files

3. **Logging and monitoring** - Track operations automatically
   - Example: Log all bash commands, track file modifications

4. **Formatting and cleanup** - Auto-format code on save
   - Example: Run `prettier`, `black`, or `gofmt` after edits

5. **Context enrichment** - Inject relevant information automatically
   - Example: Add current branch info, recent commits, or issue status

6. **Security enforcement** - Block dangerous operations
   - Example: Prevent force pushes, validate command patterns

7. **Testing automation** - Run tests after changes
   - Example: Execute test suite after code modifications

8. **Session management** - Setup/teardown operations
   - Example: Load environment on start, cleanup on exit

---

## Best Practices

### Slash Commands Best Practices

#### 1. Design and Organization

- **Use descriptive names**: `/analyze-performance` not `/ap`
- **Organize with directories**: Group related commands in folders
- **Share project commands**: Commit to `.claude/commands/` for team use
- **Keep personal commands separate**: Use `~/.claude/commands/` for individual preferences

#### 2. Documentation

- **Write clear descriptions**: Use `description` frontmatter field
- **Document arguments**: Use `argument-hint` to show expected parameters
- **Add usage examples**: Include examples in command markdown
- **Explain purpose**: Start commands with a clear objective statement

#### 3. Arguments and Parameters

```markdown
---
argument-hint: [pr-number] [priority] [assignee]
description: Review pull request with specific focus
---

Review PR #$1 with priority $2 and assign to $3.
Focus on security, performance, and code style.
```

- **Use positional arguments**: `$1`, `$2` for specific parameters
- **Use `$ARGUMENTS`**: For all arguments as a single string
- **Provide defaults**: Handle missing arguments gracefully
- **Validate inputs**: Check for required arguments

#### 4. Tool Restrictions

```markdown
---
allowed-tools: Bash(git:*), Read, Grep
description: Safe git operation command
---

Check git status and suggest next steps.
Only use git commands, file reading, and search.
```

- **Restrict tools**: Use `allowed-tools` to limit what Claude can do
- **Be specific**: Limit bash commands with patterns like `Bash(git:*)`
- **Review permissions**: Ensure tools match command purpose

#### 5. File References

```markdown
Review the implementation in @src/utils/helpers.js
Compare @src/old-version.js with @src/new-version.js
```

- **Use `@` prefix**: Reference files directly in commands
- **Support wildcards**: Use patterns like `@src/**/*.test.js`
- **Provide context**: Explain why files are referenced

#### 6. Bash Execution

```markdown
---
allowed-tools: Bash(git:*)
---

## Context
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -5`

Create a commit based on the above context.
```

- **Use `!` prefix**: Execute bash before command runs
- **Capture context**: Get current state with commands
- **Quote properly**: Escape quotes in bash commands
- **Keep it fast**: Avoid slow operations

#### 7. Model Selection

```markdown
---
model: claude-3-5-haiku-20241022
description: Fast code formatting check
---

Quick style check for modified files.
```

- **Choose appropriate models**: Use Haiku for simple tasks, Sonnet for complex
- **Override when needed**: Specify `model` in frontmatter
- **Consider cost**: Balance speed, quality, and cost

### Hooks Best Practices

#### 1. Security First

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/validate-write.py"
      }]
    }]
  }
}
```

- **USE AT YOUR OWN RISK**: Hooks execute arbitrary commands automatically
- **Test thoroughly**: Validate in safe environment before production
- **Validate inputs**: Never trust input data blindly
- **Quote variables**: Use `"$VAR"` not `$VAR`
- **Check paths**: Block `..` and validate file paths
- **Protect sensitive files**: Skip `.env`, `.git/`, keys
- **Use absolute paths**: Specify full paths for scripts
- **Review third-party hooks**: Understand code before enabling

#### 2. Configuration Management

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/format.sh",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

- **Use project path**: Reference scripts with `"$CLAUDE_PROJECT_DIR"`
- **Set appropriate timeouts**: Override 60s default when needed
- **Organize by event**: Group related hooks under same event
- **Use matchers wisely**: Target specific tools with regex
- **Avoid wildcards**: Be specific about what to match

#### 3. Exit Codes and Decisions

**Simple validation (exit codes):**

- **Exit 0**: Success, stdout shown to user (or added to context for `UserPromptSubmit`/`SessionStart`)
- **Exit 2**: Blocking error, stderr shown to Claude
- **Other**: Non-blocking error, stderr shown to user

**Advanced control (JSON output):**

```python
# PreToolUse: Control permission
output = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow" | "deny" | "ask",
        "permissionDecisionReason": "Explanation here"
    }
}

# PostToolUse: Provide feedback
output = {
    "decision": "block",  # or undefined
    "reason": "Why blocking",
    "hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": "Extra info for Claude"
    }
}

# UserPromptSubmit: Block or enrich
output = {
    "decision": "block",  # or undefined
    "reason": "Why blocking (shown to user)",
    "hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": "Context to inject"
    }
}

# Stop/SubagentStop: Prevent stopping
output = {
    "decision": "block",  # or undefined
    "reason": "Why Claude must continue"
}

# SessionStart: Add initial context
output = {
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": "Initial context"
    }
}
```

#### 4. Event Selection

| Event | Best For | Avoid For |
|-------|----------|-----------|
| `PreToolUse` | Permission control, validation | Heavy operations (blocks UI) |
| `PostToolUse` | Formatting, cleanup, feedback | Operations requiring approval |
| `UserPromptSubmit` | Context injection, validation | Heavy processing |
| `Stop`/`SubagentStop` | Continuation logic, summaries | Blocking without good reason |
| `SessionStart` | Loading context, setup | Long-running operations |
| `SessionEnd` | Cleanup, logging | Critical operations (may fail) |
| `Notification` | Logging, monitoring | User-facing operations |
| `PreCompact` | Context preparation | Blocking (can't stop compact) |

#### 5. Input/Output Handling

```python
#!/usr/bin/env python3
import json
import sys

# Always validate JSON input
try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
    sys.exit(1)

# Extract relevant fields
tool_name = input_data.get("tool_name", "")
tool_input = input_data.get("tool_input", {})

# Your logic here

# Return structured output
output = {
    "decision": "allow",
    "suppressOutput": True
}
print(json.dumps(output))
sys.exit(0)
```

- **Parse JSON safely**: Handle `JSONDecodeError`
- **Validate schema**: Check required fields exist
- **Use stderr for errors**: Claude sees stderr on exit code 2
- **Return structured output**: Use JSON for complex decisions
- **Set appropriate exit codes**: Control blocking behavior

#### 6. Performance Considerations

- **Keep hooks fast**: Default 60s timeout can interrupt workflows
- **Avoid blocking UI**: Long operations in `PreToolUse` freeze Claude
- **Run in parallel**: Multiple hooks execute simultaneously
- **Cache when possible**: Reuse expensive computations
- **Optimize matchers**: Specific patterns are faster than `*`

#### 7. Debugging

```bash
# Run Claude in debug mode
claude --debug

# Check hook configuration
/hooks

# Test hook command manually
echo '{"tool_name":"Write","tool_input":{}}' | .claude/hooks/test.py

# Monitor hook execution
tail -f ~/.claude/logs/debug.log
```

- **Use `--debug` flag**: See detailed hook execution
- **Test manually first**: Run commands outside Claude
- **Check permissions**: Ensure scripts are executable (`chmod +x`)
- **Verify paths**: Use absolute paths for reliability
- **Review `/hooks` output**: Confirm hooks are registered
- **Log intermediate steps**: Add logging to complex hooks

#### 8. Common Patterns

**Auto-formatting:**

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/format.sh"
      }]
    }]
  }
}
```

**Security validation:**

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/validate-bash.py"
      }]
    }]
  }
}
```

**Context injection:**

```json
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{
        "type": "command",
        "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/add-context.py"
      }]
    }]
  }
}
```

#### 9. MCP Tool Integration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [{
          "type": "command",
          "command": "echo 'Memory operation' >> ~/mcp-ops.log"
        }]
      },
      {
        "matcher": "mcp__.*__write.*",
        "hooks": [{
          "type": "command",
          "command": "/home/user/scripts/validate-mcp-write.py"
        }]
      }
    ]
  }
}
```

- **Use `mcp__` prefix**: Target MCP tools specifically
- **Match by server**: `mcp__servername__.*` for all server tools
- **Match by operation**: `mcp__.*__write.*` for write operations across servers
- **Combine with regular tools**: Hooks work seamlessly with both

---

## Combining Slash Commands and Hooks

### Complementary Usage

The most powerful workflows combine both mechanisms:

**Example: Safe Deployment Workflow**

```markdown
<!-- .claude/commands/deploy.md -->
---
allowed-tools: Bash(git:*), Bash(npm:*), Read
description: Deploy application to staging
---

1. Check current git status: !`git status`
2. Ensure tests pass: !`npm test`
3. Build application: !`npm run build`
4. Deploy to staging server
5. Verify deployment

Create deployment following this workflow.
```

```json
// .claude/settings.json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/validate-deployment.py"
      }]
    }],
    "PostToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/notify-deployment.py"
      }]
    }]
  }
}
```

**Result:**

- User triggers deliberate deployment with `/deploy`
- Command provides structured workflow for Claude
- Hooks automatically validate bash commands before execution
- Hooks send notifications after successful deployment steps

---

## Summary

### Slash Commands

**Strengths:**

- User-controlled, deliberate execution
- Excellent for complex workflows requiring judgment
- Easy to share and version control
- Rich parameterization and file references
- Clear intent and documentation

**Weaknesses:**

- Requires manual triggering
- Can be forgotten in fast-paced work
- Less suitable for enforcement policies
- No blocking capability

**Best for:** Workflows, analysis, documentation, git operations, project-specific procedures

### Hooks

**Strengths:**

- Automatic enforcement of policies
- Proactive validation and protection
- Context enrichment without user action
- Can approve, deny, or modify operations
- Excellent for consistency and security

**Weaknesses:**

- Higher security risk (automatic execution)
- Can slow down operations if heavy
- More complex to configure and debug
- Requires careful testing
- Less discoverable than slash commands

**Best for:** Validation, formatting, security, logging, automatic context, file protection

### Recommendation

**Use both together:**

- **Slash commands** for deliberate, user-initiated workflows
- **Hooks** for automatic validation, formatting, and enforcement
- **Combine them** for powerful, safe, and efficient development workflows

---

## References

- [Official Slash Commands Documentation](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- [Official Hooks Reference](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Hooks Guide (Get Started)](https://docs.anthropic.com/en/docs/claude-code/hooks-guide)
- [Plugins Documentation](https://docs.anthropic.com/en/docs/claude-code/plugins)
- [MCP Documentation](https://docs.anthropic.com/en/docs/claude-code/mcp)

---

**Community Mirror:** <https://github.com/ericbuess/claude-code-docs>
**Not affiliated with Anthropic**
