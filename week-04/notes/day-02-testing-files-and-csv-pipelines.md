# Day 2 — Testing, files and CSV pipelines

13 October 2026

[← Week 4](../README.md) · [Previous notes: Python control flow, functions and OOP](day-01-python-control-flow-functions-and-oop.md) · [Next notes: ETL review, JSON and API preparation](day-03-etl-review-json-and-api-preparation.md)

Today connected Monday's Python concepts to a small data pipeline. We compared `unittest` and `pytest`, wrote assertions and parameterised tests, handled file errors, and read and wrote text and CSV files. The practical task was to filter IMDb records and save the selected movies to a new CSV.

The recurring idea was to understand the type of data at each stage. A filename, an open file, a CSV reader, a list of rows and a transformed result are different objects with different jobs.

## Morning recap and interview answers

The recap covered lambdas, the four OOP pillars, classes and objects, TDD and unit testing. I explained that a class is a blueprint and an object is an instance, and linked OOP to organisation, reuse and managing complex programs. The extra point to include is that objects can model relevant real-world entities and their behaviour.

Use a specific example from my own work and explain the principle it demonstrates. A base account class and specialised accounts illustrate inheritance; a method that validates an update illustrates encapsulation. Merely naming several classes does not explain abstraction.

Saif's football-club example used a common person class with player, manager and coach subclasses. Shared details were inherited, while pay calculations could differ. The useful presentation habit was to explain the overall structure, then show how a caller uses it, rather than reading every line aloud.

## What makes a useful unit test?

A unit test checks a small piece of behaviour against an independently chosen expectation. It helps identify bugs; it does not prevent every bug or fix failures automatically. Tests can be written alongside development; **TDD specifically means writing the next test before implementing that behaviour**.

The session introduced the **FIRST** principles:

| Principle | What it means in practice |
| --- | --- |
| Fast | Keep individual unit tests quick enough to run frequently. |
| Independent | A test should not depend on another test running first. |
| Repeatable | The same controlled setup should give the same result. |
| Self-validating | Assertions determine pass or fail without someone inspecting printed output. |
| Timely | Write tests while developing, early enough to influence the design. |

For a bank-account example, create a fresh account for each test rather than relying on the balance left by a previous test. Real networks, clocks and shared files can introduce changing conditions; isolate those dependencies when testing a unit.

## Modules, imports and installation

A **module** is an importable unit of Python code, commonly a `.py` file. A **package** organises modules under a namespace. A **library** is a broader term for reusable functionality and may include several modules or packages.

Python includes a **standard library**, with tools such as `unittest`, `csv` and `json`. They are available with Python, but still need importing where their names are used. `pytest` is a third-party package that normally needs installing into the environment running the project.

Installation makes a package available to an interpreter. Importing loads a module as needed and binds names for use in the current code. These are separate steps.

Avoid naming a local file `pytest.py`, `csv.py`, `json.py` or `unittest.py` when trying to import that library. The local file can shadow the intended module. Prefer names such as `test_calculator.py`, `csv_pipeline.py` and `json_examples.py`.

## Testing with unittest

The demonstration used a calculator so the expected results were easy to check. Save the implementation and tests side by side in a practice folder.

```python
# calculator.py
def add(first, second):
    return first + second


def subtract(first, second):
    return first - second
```

```python
# test_calculator.py
import unittest
from calculator import add, subtract


class TestCalculator(unittest.TestCase):
    def test_add_positive_numbers(self):
        actual = add(10, 5)
        expected = 15
        self.assertEqual(actual, expected)

    def test_subtract_same_number(self):
        self.assertEqual(subtract(4, 4), 0)

    def test_subtract_larger_number(self):
        self.assertEqual(subtract(3, 7), -4)


if __name__ == "__main__":
    unittest.main()
```

Run from that folder:

```bash
python -m unittest -v test_calculator
```

Use `python3` or `py` if that is how the intended Python interpreter is launched on the machine. `-m` runs a module; here `unittest` is the test runner, and `test_calculator` is the module it should test. `-v` requests more detailed results.

The class inherits from `unittest.TestCase`, which supplies assertion methods and test support. Test method names start with `test`. The `if __name__ == "__main__"` block also allows direct execution of the file without automatically running the tests whenever another module imports it.

| Assertion | Use |
| --- | --- |
| `self.assertEqual(actual, expected)` | Check that values compare equal. |
| `self.assertTrue(condition)` | Check that an expression is truthy. |
| `self.assertFalse(condition)` | Check that an expression is falsey. |
| `self.assertRaises(ErrorType)` | Check that an operation raises an expected exception. |

See [the unittest guide](https://docs.python.org/3/library/unittest.html) for discovery, setup and assertion options.

### Revisit red–green–refactor

The class began with an `add()` stub containing `pass`. That returns `None`, so a test expecting 2 fails. Temporarily returning 2 passes the first test, but a second case expecting 3 exposes the need for general addition logic.

Check that the test fails for the intended reason. An import problem or an undiscovered test does not demonstrate that the target behaviour was tested. Likewise, an incorrect expectation such as “1 + 1 equals 3” is a test mistake, not a calculator defect.

## Testing with pytest

Install into the project's selected environment, then run its test runner:

```bash
python -m pip install pytest
python -m pytest -v
```

`python -m pip` helps ensure installation uses the same interpreter as the later command. If the terminal and editor use different environments, installation may succeed while the editor still cannot import the package.

The session also showed `pip install -U pytest`. `-U` means **upgrade**, not “universal” or “make available everywhere”. It can upgrade an existing installation. See [pip's install options](https://pip.pypa.io/en/stable/cli/pip_install/).

### A plain assertion

```python
# test_calculator_pytest.py
from calculator import add, subtract


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(7, 2) == 5
```

`assert` is part of Python itself; importing a testing library does not create the keyword. `pytest` discovers the test functions and provides useful failure reporting around assertions. A file using only plain assertions does not need `import pytest`; it still needs to be run through pytest to discover and execute its tests.

For this layout, use filenames beginning with `test_` and function names beginning with `test_`. Running a file that only defines functions with `python filename.py` will not call those functions automatically. In the editor, check that the run configuration is a test configuration.

### Parameterised tests

Instead of writing several nearly identical test functions, provide several input-and-expectation combinations:

```python
# test_calculator_parameterised.py
import pytest
from calculator import add


@pytest.mark.parametrize(
    "first, second, expected",
    [(1, 2, 3), (2, 3, 5), (1, 10, 11), (-2, 2, 0)],
)
def test_add_cases(first, second, expected):
    assert add(first, second) == expected
```

The decorator applies to the function directly below it. The string names the arguments pytest will supply; it is not just descriptive text. Each tuple provides values in that order, so this produces four test cases.

A tuple is an immutable sequence, commonly written with parentheses; the outer square brackets here make a list of tuples. Immutability means the tuple's item references cannot be reassigned, not that a mutable object stored inside a tuple can never change.

The decorator supplies the cases automatically. Merely storing one input and expectation in local variables is not parameterisation. See [pytest's parameterisation guide](https://docs.pytest.org/en/stable/how-to/parametrize.html).

Pytest normally continues to other test cases after an assertion failure. Use `python -m pytest -x` to stop after the first failure. Within the failing test itself, later statements after the failed assertion do not run. See [pytest's failure-handling options](https://docs.pytest.org/en/stable/how-to/failures.html).

### unittest and pytest compared

| | unittest | pytest |
| --- | --- | --- |
| Availability | Python standard library | Normally installed separately |
| Typical introductory style | `TestCase` subclass and assertion methods | Plain test functions and `assert` |
| Several cases | Separate methods or `subTest()` | `@pytest.mark.parametrize` |
| Running tests | `python -m unittest` | `python -m pytest` |

Both can support more than unit tests. The distinction is their interfaces and supporting features, not a rule that one can only test units. A debugger is another tool again: it lets me pause execution and inspect values step by step.

## Reading errors without guessing

When an operation fails, read the traceback rather than treating all the red text as one problem:

1. Read the exception type and message near the bottom.
2. Find the relevant file and line in my own code.
3. Check the input, path, type and operation at that point.
4. Trace back through callers if the bad value originated earlier.

| Error | Example cause |
| --- | --- |
| `SyntaxError` | Missing a colon or another invalid Python construct. |
| `NameError` | Referring to a name that has not been defined or imported. |
| `TypeError` | Trying to concatenate a string and a float directly. |
| `ValueError` | Calling `int("hello")`: the type is acceptable but the value is not. |
| `ZeroDivisionError` | Attempting division by zero. |
| `FileNotFoundError` | Reading a file from a path that does not exist. |
| `FileExistsError` | Creating with mode `"x"` when the file already exists. |
| `PermissionError` | The process lacks permission for the operation. |

Syntax problems are generally found while parsing code; other exceptions arise during execution. Editor warnings can predict some problems, but do not define whether something is a syntax error or a runtime exception. `SyntaxError` is itself an exception class. A normal syntax mistake in the current module prevents it from running, so a surrounding `try` in that same invalid code cannot rescue it.

## Handling exceptions with try and except

```python
def print_order(filename):
    try:
        with open(filename, "r", encoding="utf-8") as order_file:
            for line in order_file:
                print(line.rstrip("\n"))
    except FileNotFoundError as error:
        print(f"Could not find the order file: {error}")
    except PermissionError as error:
        print(f"Could not read the order file: {error}")
```

Python attempts the `try` block. If a matching exception occurs, the rest of that block is skipped and the corresponding `except` block runs. `as error` gives access to the exception and its message. Errors without a matching handler continue to the caller.

Catching `FileNotFoundError` will not catch `FileExistsError`. Match the handler to the failure that can actually occur in the operation being performed.

Avoid an empty `except: pass` that hides a failure. Handle it meaningfully, report it, or let it propagate to a caller that can decide what to do. A bare `except` is especially broad and can catch interrupts as well as ordinary application errors.

`raise` is not only for testing. Inside an exception handler, a bare `raise` re-raises the current exception, for example after recording useful context. Deliberately raising an exception can also enforce an input rule. See [Python's exception-handling guide](https://docs.python.org/3/tutorial/errors.html).

A caught error may allow a script to finish normally, but that does not mean its task succeeded. A pipeline must not say “saved successfully” if its input was never read. Decide where failure should stop the run and where recovery is possible.

## Paths and file modes

The first argument to `open()` commonly identifies a local filesystem path. A string such as `"../user_details.csv"` means “go up one directory, then find this file”, relative to the process's **current working directory**. It is not automatically relative to the Python file containing the code.

This distinction matters when the editor and terminal launch the same program from different folders. For a saved script, a path tied to the script's location can be built explicitly:

```python
from pathlib import Path

folder = Path(__file__).resolve().parent
source = folder / "user_details.csv"
```

`__file__` describes the script/module file; it may not be available in an interactive console. A dotted import such as `from package.module import function` uses Python's import system, not the same rules as a quoted filesystem path. Built-in `open()` does not fetch an HTTP URL; Wednesday introduces a URL-specific function.

| Mode | Behaviour |
| --- | --- |
| `"r"` | Read an existing file; the default. |
| `"w"` | Write, creating the file or truncating its existing contents immediately on opening. |
| `"a"` | Append writes to the end; create the file if necessary. |
| `"x"` | Create a new file; fail if it already exists. |
| `"b"` | Use binary data, for example `"rb"`. |
| `"t"` | Use text; the default. |
| `"+"` | Add reading and writing, for example `"r+"`; the base mode still controls creation/truncation. |

Creating a file does not automatically create missing parent directories. Explicit `encoding="utf-8"` makes the text encoding clear.

## Reading and writing text

| Operation | Result |
| --- | --- |
| `file.read()` | Remaining contents as one string, unless a size limits it. |
| `file.readline()` | The next line as a string. |
| `file.readlines()` | Remaining lines as a list of strings. |
| `for line in file` | Iterate through the remaining lines without first building a full list. |

Reading advances the file's position. Repeating a read at the end does not start over automatically.

```python
with open("order.txt", "r", encoding="utf-8") as order_file:
    lines = order_file.readlines()

for line in lines:
    print(line.rstrip("\n"))
```

The newline character is `\n`, with a backslash. A line read from a file often already includes it, while `print()` adds another newline by default. Removing the existing newline avoids blank lines between items. Alternatively, `print(line, end="")` prints the existing line ending as-is.

### Why use with?

`with open(...) as file` uses the file as a context manager. Once successfully opened, the file is closed when execution leaves the block, including when an exception occurs inside it. This avoids forgetting `close()` or skipping it after a failure.

Closing releases resources and flushes buffered writes. It is not, by itself, protection against SQL injection. Also, closing the file does not delete data already read into a Python list.

`if`, `for` and `with` blocks do not create a separate local variable scope in Python. A variable assigned there can remain available afterwards in the surrounding function or module, provided that assignment actually ran. See [Python's reading and writing guide](https://docs.python.org/3/tutorial/inputoutput.html).

### Write or append an order

```python
with open("order.txt", "w", encoding="utf-8") as order_file:
    written = order_file.write("beans\n")
print(written)  # 6 characters, including the newline

with open("order.txt", "a", encoding="utf-8") as order_file:
    order_file.write("carrots\n")
```

The final file has two lines: beans and carrots. Mode `"w"` replaced the old contents; `"a"` added the second line. Text `write()` returns the number of characters written, not a success/failure flag. It does not add a newline automatically.

## CSV data and Python objects

CSV represents tabular records as text. A comma normally separates fields, but quoting matters: a field such as `"Drama,Comedy"` can contain a comma without becoming two columns. Use the `csv` module rather than splitting every line on commas manually.

The lesson's user-details file had title, first name, last name, gender and email columns. The first record supplied headings; later records supplied data.

```python
import csv

with open("user_details.csv", "r", newline="", encoding="utf-8") as source:
    reader = csv.reader(source)
    headers = next(reader, None)
    for row in reader:
        print(row[-1])  # Email, assuming the expected five-column layout
```

`csv.reader` produces lists whose field values are normally strings. `"2010"` still needs conversion before a numeric comparison. Printing `reader` itself shows an object representation, not all its records.

### Iterables, iterators and next

An iterable can provide an iterator. An iterator supplies successive items and tracks its progress. A CSV reader is already an iterator, so an extra `iter(reader)` is unnecessary.

`next(reader, None)` consumes the next row, returning `None` if there is none. Calling it once before the loop consumes the header; calling it twice would also consume the first data row. `list(reader)` collects the remaining rows and exhausts the reader.

Consume the reader while its file is open. Returning `list(reader)` from inside the `with` block preserves the records; returning the unconsumed reader would leave later iteration depending on a closed file.

For CSV files, use `newline=""` on both reading and writing. It lets the CSV module manage newline handling, including quoted newlines and platform differences. It does not concatenate all records into one line. See [Python's CSV documentation](https://docs.python.org/3/library/csv.html).

## A small CSV pipeline

The transformation in class kept first name, last name and email while removing title and gender. This illustrative version separates reading, transformation and writing. Save it beside a sample `user_details.csv` with the headings `title,first_name,last_name,gender,email` in that order.

```python
# csv_pipeline.py
import csv


def extract_users(filename):
    with open(filename, "r", newline="", encoding="utf-8") as source:
        reader = csv.reader(source)
        headers = next(reader, None)
        expected = ["title", "first_name", "last_name", "gender", "email"]
        if headers != expected:
            raise ValueError("Unexpected user-details headings")
        return list(reader)


def transform_users(rows):
    transformed = []
    for row in rows:
        if len(row) != 5:
            raise ValueError("Expected five fields in each user record")
        transformed.append([row[1], row[2], row[4]])
    return transformed


def load_users(filename, rows):
    with open(filename, "w", newline="", encoding="utf-8") as target:
        writer = csv.writer(target)
        writer.writerow(["first_name", "last_name", "email"])
        writer.writerows(rows)


if __name__ == "__main__":
    try:
        users = extract_users("user_details.csv")
        selected = transform_users(users)
        load_users("selected_users.csv", selected)
    except (OSError, ValueError, csv.Error) as error:
        raise SystemExit(f"User pipeline failed: {error}") from error
    else:
        print(f"Saved {len(selected)} user records")
```

The destination is a separate output file; rerunning this example replaces that output. Extraction and validation finish before the output is opened for writing. This is still a small teaching pipeline, not an atomic production load: an error during writing can leave a partial output file.

The outer list is created once before the transformation loop. A fresh row list is appended for each user. Repeatedly assigning a new outer list inside the loop would lose earlier results; reusing the same mutable row object can also produce unintended results.

`writerow()` writes one row; `writerows()` writes the collection of rows. A writer is given an open writable file, while the write call is given the prepared data. Confusing the output filename with the data list was one of the troubleshooting points in class.

This example handles failures at the point coordinating the pipeline. Helpers can let exceptions propagate there; every helper does not need an identical `try` block. The caller must still know when the operation failed.

## The IMDb exercise

The task was to read the supplied titles, retain **movies released in 2010 or later**, and write the selected data to a new CSV. Films before 2010, shorts, videos and TV series should not pass those filters.

My implementation is already saved in [the Week 4 exercises](../exercises/):

| File | Responsibility |
| --- | --- |
| [extract.py](../exercises/extract.py) | Use `csv.DictReader` and return a list of dictionaries. |
| [transform.py](../exercises/transform.py) | Check year and title type, then select the output fields. |
| [load.py](../exercises/load.py) | Write the header and records using `csv.DictWriter`. |
| [main.py](../exercises/main.py) | Call extraction, transformation and loading in order. |

With `DictReader`, the first row supplies dictionary keys by default and is excluded from the data rows. Do not add another `next()` to skip headers here, or the first actual record will be lost. Named fields such as `movie["startYear"]` are easier to understand than remembering numeric column positions.

The transformation retains `titleType`, `primaryTitle`, `startYear`, `runtimeMinutes` and `genres`. It converts the selected year to `int`, while the other extracted fields remain strings. The source is read with `utf-8-sig`, which also handles an optional UTF-8 byte-order mark before the first heading.

The checked-in input contains **850 data records**; the checked-in output contains **722 selected movies**, both excluding headers. Those are counts for this repository's files, not universal counts for an IMDb dataset. CSV file contents are text, so reading the saved numeric years again normally yields strings until converted.

### Why reruns matter

For a complete regenerated output, append mode would add the selected rows again on every run. Write mode replaces the output, avoiding that particular duplication problem.

This illustrates **idempotence**: rerunning against the same input should produce the same intended state. Larger pipelines may instead use keys, updates or incremental loads. Truncating every target is not a universal rule for ETL.

### Collections or objects?

Rows can be handled as lists, dictionaries or custom objects. A `MovieDetails` class can be helpful when related behaviour belongs with each record. Dictionaries can be simpler for straightforward filtering and column selection.

Separating functions into modules is modular design; it does not by itself make code object-oriented. Pick the representation that makes the transformations clear, rather than adding objects solely to satisfy a label.

## Practice and follow-up

The afternoon focused on the IMDb pipeline, with JSON research introduced as preparation. The code-review feedback and JSON walkthrough continue in [Day 3](day-03-etl-review-json-and-api-preparation.md).

Before moving on, I should be able to explain:

- Why a test has passed, failed or not been discovered at all.
- How parameterised inputs reach a pytest test function.
- What `try`, `except` and `with` each contribute.
- The differences between `read()`, `readline()` and `readlines()`.
- Why `"w"` replaces contents and `"a"` can duplicate a pipeline's output.
- How a CSV row becomes a list or dictionary, then becomes a written row again.
