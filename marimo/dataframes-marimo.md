[Skip to content](https://docs.marimo.io/guides/working_with_data/dataframes/#interactive-dataframes)

# Interactive dataframes [¶](https://docs.marimo.io/guides/working_with_data/dataframes/\#interactive-dataframes "Permanent link")

**marimo makes you more productive when working with dataframes**.

- [Display dataframes](https://docs.marimo.io/guides/working_with_data/dataframes/#displaying-dataframes) in a rich, interactive table and chart views
- [Transform dataframes](https://docs.marimo.io/guides/working_with_data/dataframes/#transforming-dataframes) with filters, groupbys,
aggregations, and more, **no code required**
- [Select data](https://docs.marimo.io/guides/working_with_data/dataframes/#selecting-dataframes) from tables or charts and get selections
back in Python as dataframes

_marimo integrates with [Pandas](https://pandas.pydata.org/) and_
_[Polars](https://pola.rs/) dataframes natively_.

## Displaying dataframes [¶](https://docs.marimo.io/guides/working_with_data/dataframes/\#displaying-dataframes "Permanent link")

marimo lets you page through, search, sort, and filter dataframes, making it
extremely easy to get a feel for your data.

marimo brings dataframes to life.

Display dataframes by including them in the last expression of the
cell, just like any other object.

[pandas](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_1_1)[polars](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_1_2)[live example](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_1_3)

```python
import pandas as pd

df = pd.read_json(
    "https://raw.githubusercontent.com/vega/vega-datasets/master/data/cars.json"
)
df
```

```python
import polars as pl

df = pl.read_json(
    "https://raw.githubusercontent.com/vega/vega-datasets/master/data/cars.json"
)
df
```

marimo \| a next-generation Python notebook

notebook.py

Loading notebook and dependencies...

To opt out of the rich dataframe viewer, use [`mo.plain`](https://docs.marimo.io/api/layouts/plain/#marimo.plain "            marimo.plain"):

[pandas](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_2_1)[polars](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_2_2)[live example](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_2_3)

```python
import pandas as pd
import marimo as mo

df = pd.read_json(
    "https://raw.githubusercontent.com/vega/vega-datasets/master/data/cars.json"
)
mo.plain(df)
```

```python
import polars as pl
import marimo as mo

df = pl.read_json(
    "https://raw.githubusercontent.com/vega/vega-datasets/master/data/cars.json"
)
mo.plain(df)
```

marimo \| a next-generation Python notebook

notebook.py

Loading notebook and dependencies...

## Transforming dataframes [¶](https://docs.marimo.io/guides/working_with_data/dataframes/\#transforming-dataframes "Permanent link")

### No-code transformations [¶](https://docs.marimo.io/guides/working_with_data/dataframes/\#no-code-transformations "Permanent link")

Use [`mo.ui.dataframe`](https://docs.marimo.io/api/inputs/dataframe/#marimo.ui.dataframe "            marimo.ui.dataframe") to interactively
transform a dataframe with a GUI, no coding required. When you're done, you
can copy the code that the GUI generated for you and paste it into your
notebook.

Build transformations using a GUI

The transformations you apply will turn into code which is accessible via the "code" tab.

![](https://docs.marimo.io/_static/docs-dataframe-transform-code.png)Copy the code of the transformation

[pandas](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_3_1)[polars](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_3_2)[live example](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_3_3)

```python
# Cell 1
import marimo as mo
import pandas as pd

df = pd.DataFrame({"person": ["Alice", "Bob", "Charlie"], "age": [20, 30, 40]})
transformed_df = mo.ui.dataframe(df)
transformed_df
```

```python
# Cell 2
# transformed_df.value holds the transformed dataframe
transformed_df.value
```

```python
# Cell 1
import marimo as mo
import polars as pl

df = pl.DataFrame({"person": ["Alice", "Bob", "Charlie"], "age": [20, 30, 40]})
transformed_df = mo.ui.dataframe(df)
transformed_df
```

```python
# Cell 2
# transformed_df.value holds the transformed dataframe
transformed_df.value
```

marimo \| a next-generation Python notebook

notebook.py

Loading notebook and dependencies...

### Custom filters [¶](https://docs.marimo.io/guides/working_with_data/dataframes/\#custom-filters "Permanent link")

Create custom filters with marimo UI elements, like sliders and dropdowns.

[pandas](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_4_1)[polars](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_4_2)[live example](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_4_3)

```python
# Cell 1 - create a dataframe
df = pd.DataFrame({"person": ["Alice", "Bob", "Charlie"], "age": [20, 30, 40]})
```

```python
# Cell 2 - create a filter
age_filter = mo.ui.slider(start=0, stop=100, value=50, label="Max age")
age_filter
```

```python
# Cell 3 - display the transformed dataframe
filtered_df = df[df["age"] < age_filter.value]
mo.ui.table(filtered_df)
```

```python
# Cell 1
import marimo as mo
import polars as pl

df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "city": ["New York", "London", "Paris", "Tokyo"]
})

age_filter = mo.ui.slider.from_series(df["age"], label="Max age")
city_filter = mo.ui.dropdown.from_series(df["city"], label="City")

mo.hstack([age_filter, city_filter])
```

```python
# Cell 2
filtered_df = df.filter((pl.col("age") <= age_filter.value) & (pl.col("city") == city_filter.value))
mo.ui.table(filtered_df)
```

marimo \| a next-generation Python notebook

notebook.py

Loading notebook and dependencies...

## Select dataframe rows [¶](https://docs.marimo.io/guides/working_with_data/dataframes/\#selecting-dataframes "Permanent link")

Display dataframes as interactive, [selectable charts](https://docs.marimo.io/guides/working_with_data/plotting/) using
[`mo.ui.altair_chart`](https://docs.marimo.io/api/plotting/#marimo.ui.altair_chart "            marimo.ui.altair_chart") or
[`mo.ui.plotly`](https://docs.marimo.io/api/plotting/#marimo.ui.plotly "            marimo.ui.plotly"), or as a row-selectable table with
[`mo.ui.table`](https://docs.marimo.io/api/inputs/table/#marimo.ui.table "            marimo.ui.table"). Select points in the chart, or select a table
row, and your selection is _automatically sent to Python as a subset of the original_
_dataframe_.

Select rows in a table, get them back as a dataframe

[pandas](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_5_1)[polars](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_5_2)[live example](https://docs.marimo.io/guides/working_with_data/dataframes/#__tabbed_5_3)

```python
# Cell 1 - display a dataframe
import marimo as mo
import pandas as pd

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
table = mo.ui.table(df, selection="multi")
table
```

```python
# Cell 2 - display the selection
table.value
```

```python
# Cell 1 - display a dataframe
import marimo as mo
import polars as pl

df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
table = mo.ui.table(df, selection="multi")
table
```

```python
# Cell 2 - display the selection
table.value
```

marimo \| a next-generation Python notebook

notebook.py

Loading notebook and dependencies...

## Dataframe panels [¶](https://docs.marimo.io/guides/working_with_data/dataframes/\#dataframe-panels "Permanent link")

Dataframe outputs in marimo come with several panels to help you visualize, explore, and page through your data interactively. These panels are accessible via toggles at the bottom-left of a dataframe output. If you need further control, after opening a panel you can

- **pin the panel** to the side of your editor for persistent access;
- **toggle focus** to automatically display the currently focused dataframe in the panel.

Note

Toggles are visible when editing notebooks (with `marimo edit ...`) but not when running notebooks as apps (with `marimo run ...`), except for the row viewer which is available in both.

### Row viewer panel [¶](https://docs.marimo.io/guides/working_with_data/dataframes/\#row-viewer-panel "Permanent link")

To inspect individual rows, open the **row viewer**. This presents a vertical view of the selected row.

- **Press `Space`** to select/deselect the current row
- **Use arrow keys** (`←``→`) to navigate between rows
- **Click** on any row in the dataframe to view its data in the panel

### Column explorer panel [¶](https://docs.marimo.io/guides/working_with_data/dataframes/\#column-explorer-panel "Permanent link")

To explore your data, open the **column explorer** where you can find summary statistics and charts for each column. Click the `+` button to add the chart code to a new cell.

This requires the `altair` package to be installed. For large dataframes, `vegafusion` is also needed to render charts. To use the generated Python code, enable vegafusion in your notebook:

```python
import altair

altair.data_transformers.enable("vegafusion")
```

### Chart builder [¶](https://docs.marimo.io/guides/working_with_data/dataframes/\#chart-builder "Permanent link")

The chart builder toggle lets you rapidly develop charts using a GUI, while also generating Python code to insert in your notebook. Refer to the [chart builder guide](https://docs.marimo.io/guides/working_with_data/plotting/#chart-builder) for more details.

## Preferences [¶](https://docs.marimo.io/guides/working_with_data/dataframes/\#preferences "Permanent link")

When you run a SQL cell in marimo, you can get the output returned as a dataframe. If you have a preference for a specific dataframe library as a default you can configure the "default SQL output" in the user settings by going to the "Runtime" tab.

![](https://docs.marimo.io/_static/docs-dataframe-default-setting.png)Configure the default SQL output

Alternatively you can also use the [marimo configuration file](https://docs.marimo.io/guides/configuration/#user-configuration) to configure the default SQL output.

```toml
[runtime]
default_sql_output = "native"
```

## Example notebook [¶](https://docs.marimo.io/guides/working_with_data/dataframes/\#example-notebook "Permanent link")

For a comprehensive example of using Polars with marimo, check out our [Polars example notebook](https://github.com/marimo-team/marimo/blob/main/examples/third_party/polars/polars_example.py).

Run it with:

```bash
marimo edit https://raw.githubusercontent.com/marimo-team/marimo/main/examples/third_party/polars/polars_example.py
```

Back to top

![Project Logo](https://marimo.io/logo.png)

Ask

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)
