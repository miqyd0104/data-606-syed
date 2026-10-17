# Optional Pandas preparation

[← Exercises](README.md) · [Worked notebook](day_05_pandas_optional.ipynb)

Pandas helps load, inspect, clean and summarise tabular data with labelled columns and rows. It is useful when records have several fields, types and missing values. NumPy supplies array operations; Pandas adds labels and higher-level data-handling tools.

A **Series** is one-dimensional and labelled, such as a sales column. A **DataFrame** is a two-dimensional labelled table whose columns can have different types.

| Operation | Purpose |
| --- | --- |
| `pd.DataFrame(...)` | Build a table from supported input, such as a dictionary of lists. |
| `pd.read_csv(...)` | Parse a CSV into a DataFrame. |
| `frame.head()` | Preview the first rows. |
| `frame.shape` | Return `(number_of_rows, number_of_columns)`. |
| `frame.columns` | Inspect the column labels. |
| `frame.info()` | Display schema, non-null counts and memory information. |
| `frame.describe()` | Produce descriptive summaries, normally of numeric columns. |
| `frame['sales']` | Select one column as a Series. |
| `frame.loc[...]` | Select by labels or a Boolean condition. |
| `frame.iloc[...]` | Select by integer position. |
| `frame.isna().sum()` | Count missing values by column. |

`shape` and `columns` are attributes; they do not need parentheses. Methods such as `head()` do. The notebook adds a column and row, calculates summaries, reads a CSV from a text stream and explicitly excludes missing sales for its final calculation. A real pipeline should choose its missing-value policy from the meaning of the data rather than automatically filling every gap with zero.

[Pandas introductory tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
