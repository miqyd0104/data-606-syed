# Day 5 — Jupyter notebooks and NumPy

16 October 2026

[← Week 4](../README.md) · [Previous notes: Python with SQL Server, query results and API revision](day-04-python-sql-server-and-api-revision.md)

Today moved from working mainly in Python scripts to using Jupyter notebooks for data exploration. The useful difference is being able to put an explanation, a piece of Python and its output together, then build up an analysis one step at a time. We also revisited technical interview answers before starting the practical work.

NumPy was the main library covered. My main reference points are the difference between a list and an array, how to read an array's shape, and how that shape affects calculations and indexing. Pandas was introduced as the next step, with optional preparation tasks rather than a full taught session.

## Where to start when revisiting this

- [Technical interview recap](#technical-interview-recap) — explaining the purpose of tools and clarifying vague requirements.
- [Starting Jupyter locally](#starting-jupyter-locally) — installation, environments and the notebook server.
- [Cells, outputs and kernel state](#cells-outputs-and-kernel-state) — why visible output is different from live Python variables.
- [Creating NumPy arrays](#creating-numpy-arrays) — `array`, `arange`, shape, dimensions and size.
- [Calculations and broadcasting](#calculations-and-broadcasting) — element-wise operations and compatible shapes.
- [Accessing and summarising values](#accessing-and-summarising-values) — indexing, slices and statistical functions.
- [Iteration and saving arrays](#iteration-and-saving-arrays) — loops, `nditer`, `.npy` and text files.
- [Class exercises and consolidation](#class-exercises-and-consolidation) — the tasks set during the day.

## Technical interview recap

The recurring point was to answer the actual question clearly before adding detail. A useful structure is a plain definition, why it matters, and a small example. Explaining a concept before introducing its jargon makes it easier for the listener to follow.

| Topic | Main point to explain | Example or distinction |
| --- | --- | --- |
| Data engineering | Collect, move and transform data into a usable form. | An ETL pipeline prepares data for another system or an analyst. |
| Data analysis | Find useful insights and communicate what the data shows. | A dashboard highlights changes in sales performance. |
| Data science | Apply statistics and modelling to solve problems. | Predict customer churn or recommend products. |
| Relational databases | Store structured entities and their relationships, with constraints and transaction support. | Customers, accounts and transactions in a banking system. |
| Python scripting | Automate a defined workflow that can be run repeatedly. | Execute database queries and process their results. |
| Git | Track snapshots of files and their history in a distributed version control system. | Commit a change, branch for a feature or restore an earlier version. |
| GitHub | Host Git repositories remotely and provide collaboration tools. | Share a repository and review a pull request. |

These roles overlap. Data science is not limited to prediction, and using AI is not the defining difference between the roles. Likewise, Git supports distributed collaboration; GitHub provides a hosted place and additional tools for that collaboration. GitLab and Bitbucket are other hosting options.

For relational databases, the useful business explanation is about structured relationships, avoiding unnecessary duplication and maintaining reliable transactions. Those benefits depend on the schema, constraints and transaction handling; simply choosing a relational database does not make every operation correct automatically.

### Agile, Scrum and unit testing

Agile is a set of values and principles around iterative delivery and responding to change. Scrum is a framework that can help a team work in that way. The revision covered Sprint Planning, Sprint Review and Sprint Retrospective, alongside the Product Backlog, Sprint Backlog and Increment.

I should also remember the Daily Scrum and the Sprint itself when listing Scrum events. The review concerns the product and what was delivered; the retrospective concerns how the team worked and how to improve. The Definition of Done describes the required quality of an Increment. User stories and a Definition of Ready can be useful practices, but they are not required Scrum artifacts. See the [Scrum Guide](https://scrumguides.org/scrum-guide.html) for the complete framework.

Unit testing came up as another revision topic: test a small unit of behaviour so that changes can be checked against expected results. That becomes particularly useful when refactoring existing code.

### Clarifying a scenario before choosing a solution

One interview prompt asked how to merge data from a CSV file and a JSON file. The first step is to clarify what “merge” means: append records, join on a shared identifier, or convert one format into another? I would also ask about the schema, nested JSON, data types, missing values, scale and required output.

Then I can describe an ETL approach: extract both inputs, transform them into compatible structures, combine them according to the requirement, and load the result. JSON and CSV can represent related data even though their structures differ. A small example might be handled manually, but a repeatable or larger task is a good candidate for a Python script.

For acronyms, accuracy matters. ETL is **Extract, Transform, Load** and API is **Application Programming Interface**. If I forget the expansion in an interview, it is better to explain the concept honestly than guess the words.

## Starting Jupyter locally

A Jupyter notebook combines executable code, Markdown and saved outputs in an `.ipynb` file. It is useful for exploration because I can run a small section, inspect the result and explain what I learned beside the code.

The class used the browser interface on the local machine. Using a browser does not mean the work is necessarily running in the cloud: `localhost` refers to the computer running the server.

### Install into the environment I intend to use

From the project's activated Python environment, a direct setup is:

```bash
python -m pip install notebook numpy
jupyter notebook
```

On a system where the interpreter is named `python3`, use `python3 -m pip` instead. Running pip through an interpreter makes clear which Python installation receives the packages. The selected notebook kernel must still use that environment; merely having a `.venv` folder does not activate it.

The lesson installed Jupyter and then NumPy separately. `notebook` is the package needed for the Notebook application, and the launch command includes `notebook`; running `jupyter` alone generally shows available commands. The [official Jupyter installation page](https://jupyter.org/install) gives the standard installation and launch instructions.

The terminal running Jupyter stays occupied by the server. To install another package while leaving it running, open a second terminal in the same environment. If an import fails after installation, check which Python the kernel is using:

```python
import sys
print(sys.executable)
```

### What the browser address means

The server normally opens a browser window and displays the files in the directory from which it was started. An address might look like `http://localhost:8888/tree`.

| Part | Meaning |
| --- | --- |
| `localhost` | This computer. |
| `8888` | The port on which the notebook server is listening. |
| `/tree` | The file browser route in the Notebook interface. |

A port identifies a service endpoint on a machine; it is useful to think of the host as a building and the port as a room number. Port 8888 is a common default, but the server can use another port if necessary. HTTP and HTTPS commonly use 80 and 443, respectively, but those are defaults rather than the only permitted ports.

Create a new Python notebook and rename it promptly, keeping the `.ipynb` extension. The demonstration used separate learning notebooks for Jupyter and NumPy. A descriptive name such as `learning-numpy.ipynb` is easier to recognise later than `Untitled.ipynb`.

## Cells, outputs and kernel state

The two cell types used today were **Code** and **Markdown**. Select the appropriate type from the cell menu, then use `Shift + Enter` to run the cell and move to the next one.

### Code and Markdown serve different purposes

In a code cell:

```python
print("Hello, world!")
```

The output appears below that cell. In a Markdown cell, I can write headings, explanations, lists, links and images. Running the Markdown cell renders the formatting rather than executing Python.

For example, a Markdown cell could contain:

```markdown
# Sales analysis

Investigating sales performance in Q3 2026.

## Load data
Explain the source and what each row represents.
```

In the usual Python notebook kernel, the last expression in a code cell is displayed automatically. `print()` is still useful when I want several explicit outputs or a particular format:

```python
numbers = [10, 20, 30]
numbers
```

This displays `[10, 20, 30]`. An assignment alone usually has no visible output, but it still needs to be executed to create the variable.

### Separate cells share the same Python state

Cells have separate displayed outputs, but they are not isolated Python programs. Code cells in the same notebook use the same running kernel.

```python
# Run this in one code cell.
name = "Sam"
```

```python
# Run this in a later code cell.
print(name)
```

The second cell can access `name` because the first cell has already run. The order in which I execute cells matters, even if I later move them into a different visual order.

Deleting the cell that created `name` does not remove the variable from a running kernel. Closing and reopening the browser tab can reconnect to that same kernel too. Restarting the kernel clears its in-memory variables; running the second cell after a restart, without recreating `name`, raises `NameError`.

### Saved output is not proof that the notebook still runs

Editing code does not automatically refresh its previous output. A saved notebook may display results from an earlier run even after the kernel has been restarted. Saving the file preserves the document and its saved outputs, not a complete copy of the live Python session.

My check before sharing a notebook is to restart the kernel, run all cells from top to bottom, inspect the outputs and save. That catches missing setup cells and dependencies on an accidental execution order. The [Jupyter Notebook documentation](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html) explains the relationship between the document, cells and running kernel.

## Structuring a useful analysis notebook

The demonstration outlined a simple analysis structure:

1. State the question and the context.
2. Import the libraries and load the data.
3. Explore the structure and check data quality.
4. Clean and transform the data, explaining decisions.
5. Analyse the data and visualise useful findings.
6. Write conclusions that answer the original question.

Markdown should explain why a step is needed and what an output means. A notebook made only of code cells loses much of the benefit of the format. GitHub can display saved notebooks, so the document should make sense to someone reading it without running anything.

“Explore in a notebook, deploy in a script” is a useful starting rule. Scripts and modules suit repeatable automation and production systems; notebooks suit exploration and explanation. Functions, classes and imports still work in notebooks, and reusable logic can be moved into a module instead of copying it between cells. Notebooks can also be automated, so this is a workflow preference rather than a technical restriction.

## Creating NumPy arrays

NumPy provides an N-dimensional array type, `ndarray`, and operations for working with numerical data. It is a separate library rather than part of Python's standard library.

```python
import numpy as np
```

`np` is the conventional alias. It is not compulsory syntax, but following the convention makes examples and shared code easier to read.

### Convert an existing list with `np.array`

The first example used a regular Python list and converted it into an array:

```python
list1 = [10, 20, 30]
arr1 = np.array(list1)

print(list1)
print(arr1)
print(type(arr1))
```

```text
[10, 20, 30]
[10 20 30]
<class 'numpy.ndarray'>
```

They look similar, but a list and an `ndarray` have different behaviour. A Python list is a general-purpose collection; a NumPy array has one `dtype` describing its elements and supports array operations. Mixed values may be converted to a common type rather than kept as their original Python types.

The `array` name from Python's standard-library `array` module is a different type from `np.array`. For these exercises, the intended tool is NumPy. The [NumPy beginner guide](https://numpy.org/doc/stable/user/absolute_beginners.html) is a useful reference for the basic terminology.

### Generate a sequence with `np.arange`

Use `np.array` when supplying existing values; use `np.arange` when generating a sequence:

```python
arr2 = np.arange(10, 20, 1)
print(arr2)
```

```text
[10 11 12 13 14 15 16 17 18 19]
```

The arguments are `start`, `stop` and `step`. The stop value is excluded, so 20 is not included here. A step of 1 is the default. For evenly spaced floating-point values, `linspace` is often easier to reason about than repeatedly adding a floating-point step.

### Shape, dimensions and size describe different things

| Attribute | Question it answers | For `arr1` |
| --- | --- | --- |
| `.shape` | How many positions are there along each axis? | `(3,)` |
| `.ndim` | How many axes does the array have? | `1` |
| `.size` | How many elements are there in total? | `3` |
| `.dtype` | What data type do the elements use? | An integer dtype in this example. |

These are attributes, so use `arr1.shape`, not `arr1.shape()`. In `(3,)`, the comma makes this a one-item tuple: one axis containing three elements.

## Reading multidimensional arrays

A dimension here means an axis of the array. The array can represent a grid, a stack of grids or other structured data; the axes do not have to represent physical space.

### Two dimensions: rows and columns

The lesson added a second list and combined the two:

```python
list2 = [40, 50, 60]
list3 = [list1, list2]
arr3 = np.array(list3)

print(arr3)
print(arr3.shape)
```

```text
[[10 20 30]
 [40 50 60]]
(2, 3)
```

The shape means **two rows and three columns**. It has two dimensions and six elements; it does not have “two dimensions because there are two rows”. A `(5, 3)` array would still be two-dimensional.

Python can already hold nested lists. NumPy converts a regular nested structure into a multidimensional array with array operations. Combining arrays does not always add a dimension either: concatenating along an existing axis and stacking along a new axis are different operations.

### Three dimensions: a stack of two-dimensional blocks

The three-dimensional example was:

```python
arr3dim = np.array([
    [[1, 2, 3], [3, 4, 5]],
    [[5, 6, 7], [7, 8, 9]],
])

print(arr3dim.shape)
print(arr3dim.ndim)
print(arr3dim.size)
```

```text
(2, 2, 3)
3
12
```

Read `(2, 2, 3)` from the outside inward: two blocks, each containing two rows, each containing three values. The total is `2 × 2 × 3 = 12`. The length of the shape tuple tells me the number of dimensions.

An extra axis preserves a grouping that matters to the data. For example, a grayscale image can be a height-by-width array; several same-sized grayscale frames can be a frame-by-height-by-width array. Similarly, a time axis could group comparable measurements from different periods. More dimensions are useful when the data needs them, rather than automatically being better.

## Calculations and broadcasting

NumPy applies ordinary arithmetic operators element by element. A single value used in an operation is a **scalar**.

### A list repeats; an array calculates

```python
print(list1 * 3)
print(arr1 * 3)
```

```text
[10, 20, 30, 10, 20, 30, 10, 20, 30]
[30 60 90]
```

Multiplying the list repeats its contents. Multiplying the array calculates a result for each element. The same idea works with more dimensions: `arr3dim * 3` multiplies every value in that array while retaining its shape.

### Two arrays: match corresponding values

```python
arr_second = np.array(list2)
print(arr1 * arr_second)
```

```text
[ 400 1000 1800]
```

This is `10 × 40`, `20 × 50` and `30 × 60`. Addition, subtraction and division work element by element too. These expressions produce new arrays; they do not change `arr1` unless I assign a result back or use an in-place operation.

`*` is not matrix multiplication. For matrix multiplication use `@` or `np.matmul`, with the appropriate dimension rules. A dot product is a different operation, not a general fix for any incompatible pair of shapes.

### Different shapes can sometimes work together

The lesson showed that `arr1 * arr2` fails: their shapes are `(3,)` and `(10,)`. There is no matching element-wise arrangement under NumPy's broadcasting rules.

Broadcasting compares dimensions from the right. Two corresponding dimensions are compatible if they are equal or one of them is 1; missing leading dimensions behave as 1. Therefore, arrays do not always need identical shapes.

```python
print(arr3 * arr1)
```

```text
[[ 100  400  900]
 [ 400 1000 1800]]
```

Here `(2, 3)` and `(3,)` are compatible. The three values in `arr1` are applied across each row. Likewise, `(2, 2, 3)` and `(3,)` are compatible, so `arr3dim * arr1` works and produces shape `(2, 2, 3)`.

When an operation fails, inspect both shapes before changing the code. The [NumPy broadcasting guide](https://numpy.org/doc/stable/user/basics.broadcasting.html) explains the rule and why “different shapes always fail” is too broad.

## Accessing and summarising values

NumPy uses zero-based indexing, like Python lists. For the class array `arr3`, index 1 selects the second row and index 2 selects the third column.

### Individual values, rows and columns

```python
print(arr3[1, 2])
print(arr3[1][2])
print(arr3[-1, -1])
print(arr3[1])
print(arr3[:, 2])
```

```text
60
60
60
[40 50 60]
[30 60]
```

For this simple lookup the first two forms reach the same value; the comma form states the axes together. Negative indices count from the end, so `-1` means the last position. This is also supported by Python's built-in sequences.

In `arr3[:, 2]`, the colon selects all rows and `2` selects the third column. For the three-dimensional example, `arr3dim[1, 0, 2]` selects the second block, first row and third column, giving `7`.

Slices can select ranges, and their stop position is excluded. For example, `arr3[:, :2]` selects the first two columns of both rows. Basic slices normally share data with the original array, so use `.copy()` when I need an independent array to change.

### Statistical functions

The same array contains the values 10, 20, 30, 40, 50 and 60:

```python
print(arr3.sum())
print(arr3.mean())
print(arr3.min())
print(arr3.max())
print(round(arr3.std(), 2))
print(round(arr3.var(), 2))
```

```text
210
35.0
10
60
17.08
291.67
```

The mean method is `.mean()`, not `.avg()`. Variance measures squared spread around the mean; standard deviation is its square root and returns to the original measurement units.

By default, NumPy's `.std()` and `.var()` use `ddof=0`, dividing by the number of values. For the usual sample variance estimate, use `ddof=1`; `.std(ddof=1)` takes the square root of that estimate. The choice should match what the data and calculation represent. See the [`numpy.std` reference](https://numpy.org/doc/stable/reference/generated/numpy.std.html).

### Use `axis` to control what is reduced

```python
print(arr3.sum(axis=0))
print(arr3.sum(axis=1))
```

```text
[50 70 90]
[ 60 150]
```

For this two-dimensional array, `axis=0` reduces across the rows and leaves a total for each column. `axis=1` reduces across the columns and leaves a total for each row. Omitting `axis` sums all six values. It helps to name the argument explicitly rather than relying on `sum(0)` or `sum(1)`.

## Iteration and saving arrays

### Iteration follows the outer axis

A loop over a one-dimensional array produces its values:

```python
for number in arr1:
    print(number)
```

This prints 10, 20 and 30 on separate lines. A loop over `arr3` produces one row at a time, so a nested loop reaches the individual values:

```python
for row in arr3:
    for number in row:
        print(number)
```

For a three-dimensional array, an ordinary nested-loop approach would step through blocks, then rows, then values. When I only need the individual elements, `np.nditer` avoids writing a loop for every axis:

```python
for number in np.nditer(arr3dim):
    print(number)
```

For this example it visits `1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9`. For a calculation such as adding a bonus to every score, an array expression is usually clearer than an explicit Python loop.

### Save an array in NumPy's binary format

```python
np.save("class-array", arr3)
loaded_array = np.load("class-array.npy")
print(np.array_equal(loaded_array, arr3))
```

This creates `class-array.npy` and prints `True` after loading it. `.npy` preserves the array's shape and dtype, including arrays with more than two dimensions. The filename is relative to the kernel's current working directory unless I supply a path.

Saving an array is different from saving the notebook: this creates a separate data file that another notebook or script can load.

### Save and load delimited text

```python
np.savetxt("class-array.txt", arr3, delimiter=",", fmt="%d")
loaded_text = np.loadtxt("class-array.txt", delimiter=",", dtype=int)
print(loaded_text)
```

```text
[[10 20 30]
 [40 50 60]]
```

A delimiter separates fields, so the saved lines here are `10,20,30` and `40,50,60`. The extension does not choose the delimiter. `fmt="%d"` writes integer text; `dtype=int` loads this integer example as integers. Without specifying a dtype, `loadtxt` normally returns floating-point values, which explains a display such as `10.`.

`savetxt` accepts one- or two-dimensional arrays. For the three-dimensional example, `.npy` preserves the structure directly. Text loading also requires agreement about delimiter and data types; see the [`savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html) and [`loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html) references.

## Class exercises and consolidation

### Create the requested shapes and check them

Before lunch, the task was to create a one-dimensional array with 12 elements, a two-dimensional array of shape `(3, 4)`, and a three-dimensional array of shape `(2, 5, 4)`. The values were not the focus; checking the structure was.

This is a compact way to reconstruct those requirements using a range:

```python
one_d = np.arange(1, 13)
two_d = np.arange(1, 13).reshape(3, 4)
three_d = np.arange(1, 41).reshape(2, 5, 4)

print(one_d.shape, one_d.size)
print(two_d.shape, two_d.size)
print(three_d.shape, three_d.size)
```

```text
(12,) 12
(3, 4) 12
(2, 5, 4) 40
```

The class also built the arrays from explicit nested lists. For `(3, 4)`, that means three lists with four values each; for `(2, 5, 4)`, two blocks containing five rows of four values. `reshape` needs the same total number of elements before and after: `2 × 5 × 4 = 40`, so 39 values cannot fill that shape.

### End-of-day NumPy tasks

The baseline consolidation was to use a Jupyter notebook with Markdown explanations, research unfamiliar functions when needed, and explain what those functions do. The task areas were:

| Task | What to practise |
| --- | --- |
| Student scores | Find highest, lowest, average and total scores; add five bonus marks to each score. |
| Weather data | Select values above 25°C and below 20°C, and calculate the average temperature. |
| Retail sales | Treat rows as stores and columns as weekly sales; calculate summaries along the appropriate axes. |
| Customer purchases | Research NumPy's random tools and generate purchase amounts between £1 and £500. |
| Array structure | Experiment with `reshape` and transpose, and explain the difference. |

The transcript does not include the full numeric datasets from the task board, so these are the exercise requirements rather than claimed results. For the weather task, a useful pattern to research is Boolean indexing: `temperatures[temperatures > 25]` selects matching temperatures; `(temperatures > 25).sum()` counts them.

For random integer purchase amounts, NumPy's generator uses an [exclusive upper bound](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html): `rng = np.random.default_rng()` followed by `rng.integers(1, 501, size=10)` would create ten illustrative values from 1 to 500 inclusive. The choice of ten here is just an example, not a specified class requirement.

`reshape` changes the shape without changing the number of elements. For a two-dimensional array, transpose swaps rows and columns: `arr3.T` has shape `(3, 2)`. These are different operations even when the resulting shapes happen to match.

The class submission instruction was to commit and push the notebooks to GitHub and share their link. The important standard was that the notebook should be readable by another person, with explanations and meaningful outputs, even for a simple exercise.

## Optional Pandas preparation

Pandas was the next topic, with the main teaching planned for the following week. The optional preparation was to research what problem it solves, the difference between a Series and a DataFrame, and why it is useful for working with tabular data, recording the research in a separate Markdown file.

In a separate notebook, the suggested tasks were to install and import Pandas as `pd`, create and display a DataFrame, inspect it with `head()`, `shape`, `columns`, `info()` and `describe()`, select columns and rows, add data and try basic statistical methods. Notice that `shape` and `columns` are attributes, while `head()` and `info()` are methods.

The next suggested step was loading a CSV with `pd.read_csv(...)`. Exploring a larger dataset and handling missing values were optional extensions to prepare for the later cleaning and exploration lessons. SQLAlchemy remained an alternative optional follow-up to the previous day's SQL work. These were preparation options, not topics fully worked through in today's NumPy session.

The planned progression was NumPy arrays, then Pandas for cleaning and exploration, followed by Matplotlib and Seaborn for visualisation. The later consolidation project was to choose a dataset, load and clean it, analyse it and present the useful findings in a notebook. That project was previewed today rather than completed.

## Common mistakes to watch for

| Mistake | Better check |
| --- | --- |
| A package is installed, but the notebook cannot import it. | Check the selected kernel and its `sys.executable`. |
| Assuming deleting a cell deletes its variables. | Restart the kernel to clear live state, then run the notebook in order. |
| Trusting an output after editing its code. | Run the cell again; before sharing, restart and run all. |
| Treating a list and a NumPy array as interchangeable. | Check the type and test the operation's meaning. |
| Confusing shape, size and number of dimensions. | Inspect `.shape`, `.size` and `.ndim` separately. |
| Saying every pair of different shapes is incompatible. | Apply broadcasting rules from the trailing dimensions. |
| Using `*` when I mean matrix multiplication. | Use `@` for matrix multiplication and check dimensions. |
| Summing the wrong axis. | Check whether I want one result per row or per column. |
| Writing `.avg()` for a NumPy array. | Use `.mean()`. |
| Trying to save a 3D array with `savetxt`. | Use `.npy`, or deliberately reshape and record how to restore it. |

## Key takeaways

- A useful notebook explains the question, the code and the interpretation of its outputs.
- Cells share a kernel, so execution order and a clean restart matter.
- NumPy arrays support numerical operations that behave differently from Python lists.
- Shape describes the length of each axis; dimensions count axes; size counts elements.
- Broadcasting, indexing and axis reductions become easier when I write down the shapes first.
- The consolidation tasks are about understanding the operation and presenting the work clearly, not only producing an answer.

## Revision checkpoints

1. Why can a variable still exist after I delete the cell that created it?
2. What does restarting the kernel clear, and what might still be visible in the document?
3. When would I choose `np.array` rather than `np.arange`?
4. What are the shape, dimensions and size of a `(2, 5, 4)` array?
5. Why do `[10, 20, 30] * 3` and `np.array([10, 20, 30]) * 3` differ?
6. Why can `(2, 2, 3)` and `(3,)` broadcast, while `(10,)` and `(3,)` cannot?
7. How would I select the final column of `arr3`, and what would its shape be?
8. What is the difference between `arr3.sum()`, `arr3.sum(axis=0)` and `arr3.sum(axis=1)`?
9. Why must the element count stay the same when reshaping?
10. When would I choose `.npy` rather than a delimited text file?
