[Skip to content](https://docs.marimo.io/guides/lint_rules/#lint-rules)

# Lint Rules [¶](https://docs.marimo.io/guides/lint_rules/\#lint-rules "Permanent link")

marimo includes a comprehensive linting system that helps you write better, more reliable notebooks. The linter checks for various issues that could prevent your notebook from running correctly or cause confusion.

## How to Use [¶](https://docs.marimo.io/guides/lint_rules/\#how-to-use "Permanent link")

You can run the linter using the CLI:

```bash
# Check all notebooks in current directory
marimo check .

# Check specific files
marimo check notebook1.py notebook2.py

# Auto-fix fixable issues
marimo check --fix .
```

## Rule Categories [¶](https://docs.marimo.io/guides/lint_rules/\#rule-categories "Permanent link")

marimo's lint rules are organized into three main categories based on their severity:

### 🚨 Breaking Rules [¶](https://docs.marimo.io/guides/lint_rules/\#breaking-rules "Permanent link")

These errors prevent notebook execution.

| Code | Name | Description | Fixable |
| --- | --- | --- | --- |
| [MB001](https://docs.marimo.io/guides/lint_rules/rules/unparsable_cells/) | unparsable-cells | Cell contains unparsable code | ❌ |
| [MB002](https://docs.marimo.io/guides/lint_rules/rules/multiple_definitions/) | multiple-definitions | Multiple cells define the same variable | ❌ |
| [MB003](https://docs.marimo.io/guides/lint_rules/rules/cycle_dependencies/) | cycle-dependencies | Cells have circular dependencies | ❌ |
| [MB004](https://docs.marimo.io/guides/lint_rules/rules/setup_cell_dependencies/) | setup-cell-dependencies | Setup cell cannot have dependencies | ❌ |
| [MB005](https://docs.marimo.io/guides/lint_rules/rules/invalid_syntax/) | invalid-syntax | Cell contains code that throws a SyntaxError on compilation | ❌ |

### ⚠️ Runtime Rules [¶](https://docs.marimo.io/guides/lint_rules/\#runtime-rules "Permanent link")

These issues may cause runtime problems.

| Code | Name | Description | Fixable |
| --- | --- | --- | --- |
| [MR001](https://docs.marimo.io/guides/lint_rules/rules/self_import/) | self-import | Importing a module with the same name as the file | ❌ |

### ✨ Formatting Rules [¶](https://docs.marimo.io/guides/lint_rules/\#formatting-rules "Permanent link")

These are style and formatting issues.

| Code | Name | Description | Fixable |
| --- | --- | --- | --- |
| [MF001](https://docs.marimo.io/guides/lint_rules/rules/general_formatting/) | general-formatting | General formatting issues with the notebook format. | 🛠️ |
| [MF002](https://docs.marimo.io/guides/lint_rules/rules/parse_stdout/) | parse-stdout | Parse captured stdout during notebook loading | ❌ |
| [MF003](https://docs.marimo.io/guides/lint_rules/rules/parse_stderr/) | parse-stderr | Parse captured stderr during notebook loading | ❌ |
| [MF004](https://docs.marimo.io/guides/lint_rules/rules/empty_cells/) | empty-cells | Empty cells that can be safely removed. | ⚠️ |
| [MF005](https://docs.marimo.io/guides/lint_rules/rules/sql_parse_error/) | sql-parse-error | SQL parsing errors during dependency analysis | ❌ |
| [MF006](https://docs.marimo.io/guides/lint_rules/rules/misc_log_capture/) | misc-log-capture | Miscellaneous log messages during processing | ❌ |
| [MF007](https://docs.marimo.io/guides/lint_rules/rules/markdown_indentation/) | markdown-indentation | Markdown cells in `mo.md()` should be dedented. | 🛠️ |

## Legend [¶](https://docs.marimo.io/guides/lint_rules/\#legend "Permanent link")

- 🛠️ = Automatically fixable with `marimo check --fix`
- ⚠️ = Fixable with `marimo check --fix --unsafe-fixes` (may change code behavior)
- ❌ = Not automatically fixable

## Configuration [¶](https://docs.marimo.io/guides/lint_rules/\#configuration "Permanent link")

Most lint rules are enabled by default. You can configure the linter behavior through marimo's configuration system.

## Related Documentation [¶](https://docs.marimo.io/guides/lint_rules/\#related-documentation "Permanent link")

- [Understanding Errors](https://docs.marimo.io/guides/understanding_errors/) \- Detailed explanations of common marimo errors
- [CLI Reference](https://docs.marimo.io/cli/) \- Complete CLI documentation including `marimo check`

Back to top

![Project Logo](https://marimo.io/logo.png)

Ask

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)
