# Day 3 — ETL review, JSON and API preparation

14 October 2026

[← Week 4](../README.md) · [Previous notes: Testing, files and CSV pipelines](day-02-testing-files-and-csv-pipelines.md)

Today reviewed the IMDb pipelines, including my own extract–transform–load implementation, and connected the feedback to testing and code organisation. We then completed the explanation of `finally`, introduced JSON serialisation and deserialisation, and read JSON from a URL. The session ended by setting a REST API fundamentals course for independent study.

The key progression is from processing a local CSV to handling structured data that may arrive over the internet. The underlying questions stay the same: what type do I currently have, what transformation is needed, and what should happen if a step fails?

## Morning recap

The questions revisited testing tools, file paths, exceptions, context managers and CSV processing. Two distinctions are particularly useful to revise:

- A **unit test** checks a small piece of behaviour; a user story can require several such pieces and broader checks of the feature.
- `readline()` reads one line, while `readlines()` returns the remaining lines as a list of strings. Neither produces a separate list of fields for each line; CSV parsing is what supplies that structure.

For interview answers, explain the task, the approach, the tool and the result. Only describe tests as completed if I actually wrote and ran them. Printing values is useful for investigation, but saved assertions give repeatable evidence.

## Review of my IMDb pipeline

I shared the pipeline stored in [the Week 4 exercises](../exercises/). The trainer reviewed extraction first, then transformation, loading and the main script.

```text
imdbtitles.csv
    ↓ extract_movies(filename)
list of dictionaries, with CSV field values as strings
    ↓ transform_movies(movies)
selected movie dictionaries, with startYear converted to int
    ↓ load_movies(filename, movies)
transformed_movies.csv
```

### What was working well

The feedback was positive about the separation into `extract.py`, `transform.py`, `load.py` and `main.py`. Each stage had a clear purpose, and the main script connected their returned values.

Extraction used `csv.DictReader`, so `movies` was a **list of dictionaries**. Printing `type(movies)` confirmed the outer list; individual records can be inspected with `type(movies[0])` when the list is nonempty. Curly braces in the printed records do not mean the CSV has become JSON. These are Python dictionaries in memory.

The transformation checked the year and title type, selected the required fields and returned the resulting list. Loading wrote that prepared data to a new file. I said that I had not yet double-checked the output; the review showed the core stages were in place and highlighted the remaining checks and improvements.

### Improvements identified in the review

| Area | What to improve | Why it matters |
| --- | --- | --- |
| Error handling | Handle file and data failures deliberately, with useful messages. | A missing input should not look like a successful empty run. |
| Transformation responsibilities | Split rules into smaller helpers if the logic grows. | A change to one rule becomes easier to understand and test. |
| Missing values | Give the IMDb missing-value marker a clear meaning. | An absent runtime is not a runtime of zero. |
| Verification | Check output contents, boundaries and record counts. | A file existing does not establish that its data is correct. |

These are follow-up improvements, not a claim that the existing exercise files already implement them. The comment in `load.py` should refer to `try` and **`except`**, not “accept”. Error handling can be placed around the pipeline call and receive exceptions from its helpers; it does not have to be duplicated in every function.

### The missing-value marker is not a newline

IMDb uses the literal text **`\N`** to represent a missing or null field. It is different from the lowercase newline escape **`\n`**. See [IMDb's dataset documentation](https://developer.imdb.com/non-commercial-datasets/).

In Python, `r"\N"` or `"\\N"` represents that literal marker. Decide how it should map into the next representation: `None` can mean missing in Python, `null` in JSON, and a blank field or an agreed marker can be used in a CSV. The choice should be consistent and understood by the next consumer.

The current saved output retains `\N` in 95 runtime fields. That is a reason to define the missing-value rule, not to invent durations for those films. The supplied exercise is a CSV; IMDb's published source datasets are TSV files, so their delimiter must be checked if using those directly.

## Make transformations easier to change

The trainer suggested separating conditions when they become more complex. The following is an illustrative refactoring of the filtering rule, rather than a replacement already made to the exercise:

```python
def parse_year(value):
    if value in (None, "", r"\N"):
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def should_include(record, minimum_year=2010, title_type="movie"):
    year = parse_year(record.get("startYear"))
    return (
        record.get("titleType") == title_type
        and year is not None
        and year >= minimum_year
    )


example = {"titleType": "movie", "startYear": "2010"}
print(should_include(example))                    # True
print(should_include(example, minimum_year=2011)) # False
```

This helper is intended for CSV field strings or a missing value. It deliberately treats invalid or missing years as ineligible. That is a policy choice: another pipeline might instead reject the batch or record rejected rows for investigation. Converting to an integer alone does not validate every business rule about acceptable years.

Parameters such as `minimum_year` and `title_type` make the rule reusable without editing the function body. Defaults preserve the original movie-from-2010 task. The review of Dylan's object-based solution made the same point: methods can accept filter criteria instead of hard-coding every detail.

For a small filter, keeping the conditions together is reasonable. Split code when the responsibilities or complexity justify it. Use names such as `extract_movies` or `write_movies` that describe the pipeline stage; “convert” can be ambiguous about whether it means parsing, transformation or output.

### Avoid changing a list while filtering it

One approach shown in the review removed records from the original list. Removing items while iterating over that same list can shift the remaining items and skip checks. Building a separate result is easier to reason about:

```python
records = [
    {"titleType": "movie", "startYear": "2009"},
    {"titleType": "movie", "startYear": "2010"},
    {"titleType": "short", "startYear": "2020"},
]
selected = [record for record in records if should_include(record)]
print(len(selected))  # 1
```

The list comprehension applies the predicate to each record and builds a new outer list. It does not make deep copies of the retained dictionaries.

## Keep tests as part of the project

The review encouraged keeping tests rather than deleting them once a function appears to work. A saved suite can be rerun when a filter, input schema or loading process changes.

Useful cases for this pipeline include:

| Case | Expected behaviour for the exercise |
| --- | --- |
| Movie from 2009 | Excluded. |
| Movie from 2010 | Included: the boundary is inclusive. |
| Movie from a later year | Included. |
| Short or TV series from a later year | Excluded. |
| Missing or invalid year | Follow the explicit policy, rather than accidentally treating it as a valid year. |
| Empty input with valid headings | Produce no data records, with the intended output headings. |
| CSV reader versus DictReader | Handle headings correctly without losing the first real record. |
| Run twice with the same input | No unintended duplicate output records. |
| Missing source file | Report failure clearly; do not report a successful save. |

For the helper above, a small retained test could be:

```python
def test_year_boundary():
    assert not should_include({"titleType": "movie", "startYear": "2009"})
    assert should_include({"titleType": "movie", "startYear": "2010"})
    assert not should_include({"titleType": "short", "startYear": "2010"})
    assert not should_include({"titleType": "movie", "startYear": r"\N"})
```

In a separate test file, import the helper from its implementation module. The predicate can be unit-tested without reading an actual CSV. A separate integration check can read a small fixture, run the stages, and compare the saved result.

Record counts are useful checks, but not complete validation: the wrong rows can still have the expected count. Count parsed CSV records rather than assuming physical text lines always correspond one-to-one to records; quoted fields can contain line breaks.

Code coverage was mentioned as an optional way to see which code tests execute. Execution coverage is not proof that the assertions check the right behaviour. Passing tests narrow an investigation to the extent of the cases checked; they do not prove every tested function is bug-free.

## Finally and context managers

`finally` runs as Python leaves a `try` statement, whether the work succeeded, a handler dealt with an exception, or an exception is propagating to the caller. It is useful for cleanup that must happen along those paths.

```python
def show_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as source:
            print(source.read())
    except FileNotFoundError as error:
        print(f"Cannot find the file: {error}")
    finally:
        print("Read attempt finished")
```

With an existing file, it prints the contents and then the final message. With a missing file, it prints the error message and then the final message. If a different, uncaught exception occurs, the final message still runs before that exception propagates.

“Finished” here means the attempt ended, not that it succeeded. `finally` does not suppress an exception automatically. A `return` inside `finally` can mask an earlier result or exception, so avoid it for ordinary cleanup. Abrupt process termination can also prevent cleanup; “always” describes normal Python control flow, not every possible machine failure. See [Python's cleanup actions](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions).

For an open file, `with` already arranges closing, so there is no need to add a second `finally` just to close it again. `finally` remains useful for other cleanup or reporting. A `try` can have `finally` without `except`; cleanup and handling an exception are separate responsibilities.

## JSON structure

**JSON — JavaScript Object Notation** is a text format for exchanging structured data. It can represent nested records and collections, which makes it useful for files and API messages. Its name does not mean it can only be used with JavaScript.

```json
{
  "name": "Example car",
  "electric": true,
  "range_km": 320,
  "features": ["navigation", "heated seats"],
  "previous_owner": null
}
```

An object uses `{}` with named members; an array uses `[]` with ordered values. Names and string values use double quotes. JSON uses lowercase `true`, `false` and `null`. Standard JSON does not allow comments or trailing commas.

| JSON value | Default Python result when decoded |
| --- | --- |
| Object | `dict` |
| Array | `list` |
| String | `str` |
| Integer number | `int` |
| Number with a fraction or exponent | `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

A top-level JSON value does not have to be an object. An array decodes to a list, so do not assume every response becomes a dictionary.

## Dump, dumps, load and loads

**Serialisation** converts Python data into a representation suitable for storage or transfer. **Deserialisation** parses that representation back into Python values. In this lesson, “encode” means serialise to JSON and “decode” means parse JSON; neither means encrypting or decrypting data.

| Function | Input | Effect or result |
| --- | --- | --- |
| `json.dumps(data)` | A supported Python value | Returns a JSON-formatted string. |
| `json.dump(data, file)` | A supported Python value and writable file-like object | Writes JSON text to that object. |
| `json.loads(text)` | JSON text, also accepted as bytes or bytearray | Returns the decoded Python value. |
| `json.load(file)` | A readable file-like object containing JSON | Reads and returns the decoded Python value. |

The **s** in `dumps` and `loads` is a useful reminder of the string interface. `dump` and `load` work with file-like objects, not just disk files. See [Python's JSON reference](https://docs.python.org/3/library/json.html).

### Convert in memory

```python
import json

car = {"name": "Example car", "electric": True}
json_text = json.dumps(car)
restored = json.loads(json_text)

print(type(car))        # <class 'dict'>
print(type(json_text))  # <class 'str'>
print(type(restored))   # <class 'dict'>
print(restored == car)  # True
```

The printed dictionary and JSON text can look similar, but their types determine what operations make sense. After `dumps`, the result is a string, not a special Python “JSON” type. After `loads`, dictionary operations are available again if the JSON represented an object.

`dumps` is useful when an interface expects JSON text without a disk file, for example a message payload. For changing fields, it is usually clearer to edit the dictionary/list before serialising rather than manipulate JSON punctuation with string replacements.

### Lists work directly

```python
print(json.dumps(["movie", "short"]))  # ["movie", "short"]
print(json.loads('[1, 2, 3]'))          # [1, 2, 3]
```

A Python list serialises directly to a JSON array. It does not need conversion into key–value pairs. Dictionaries, lists and other supported basic values can be nested. Arbitrary custom objects are not automatically serialisable; convert their relevant data or provide a suitable encoder. See [the JSON conversion tables](https://docs.python.org/3/library/json.html#encoders-and-decoders).

### Write and read a file

```python
import json

car = {"name": "Example car", "electric": True, "previous_owner": None}

with open("car.json", "w", encoding="utf-8") as target:
    json.dump(car, target, indent=2)

with open("car.json", "r", encoding="utf-8") as source:
    restored_car = json.load(source)

print(restored_car["name"])  # Example car
```

The second argument to `dump` is the **open file object**, not the path string. `dump` writes into that object; it does not return a new stream for me to write later. `indent=2` makes the output easier to read.

The usual file-mode rules still apply: `"w"` replaces existing contents. Repeatedly appending separately dumped objects does not create a valid single JSON document. To save several records as one document, put them in a list and serialise that list.

Malformed JSON raises `json.JSONDecodeError`. Handle that separately from file problems when a caller needs a useful distinction between “could not read the source” and “read it, but it was not valid JSON”. A successful parse also does not guarantee the expected fields or business values are present.

## Read JSON from a URL

The last demonstration replaced a local file with a response from a URL. The same parser can read from a suitable response object.

This example is a reusable function; calling it requires a real endpoint that returns JSON:

```python
import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def fetch_json(url):
    try:
        with urlopen(url, timeout=10) as response:
            return json.load(response)
    except HTTPError as error:
        raise RuntimeError(f"Server returned HTTP {error.code}") from error
    except URLError as error:
        raise RuntimeError(f"Could not reach the source: {error.reason}") from error
    except TimeoutError as error:
        raise RuntimeError("The request timed out") from error
    except json.JSONDecodeError as error:
        raise ValueError("The response did not contain valid JSON") from error
```

`urlopen()` opens the URL and returns a response object; it does not return a dictionary itself. `json.load(response)` reads and parses its body. The result depends on the JSON structure: an object becomes a dictionary, an array becomes a list. `with` closes the response when the block ends.

`urllib.request` belongs to the standard library and needs no separate installation. `urllib3` and `requests` are different third-party libraries. Installing `urllib3` is not how `urllib.request` becomes available. Built-in `open()` is for local paths or file descriptors; it does not perform this HTTP request. See [the urllib.request documentation](https://docs.python.org/3/library/urllib.request.html).

### Bytes, text and parsed data

The conversion can also be understood as separate stages:

```text
response.read() → bytes
bytes decoded with the appropriate character encoding → text
json.loads(text) → Python data
```

For a known UTF-8 response, the middle operation could be `raw_bytes.decode("utf-8")`. That changes bytes into text; it does not parse the JSON structure. Python's JSON parser can also accept supported byte input directly, and `json.load(response)` combines reading and parsing for this example.

An API call and a URL request are not competing ideas: an HTTP API exposes endpoints identified by URLs. Whether a particular URL is an API endpoint or a static JSON document depends on what the service provides. A response could also be an HTML error page, so its content cannot be assumed to be valid JSON merely because a request returned something.

## REST API study and the next session

The recorded teaching ended with the assignment to work through a **REST API Fundamentals** course and take notes for a later knowledge check. These were preparation topics, rather than a full REST lesson demonstrated in this recording:

- What an API is and how clients interact with it.
- What an HTTP request contains, including its method, target, headers and possible body.
- What an HTTP response contains, including its status, headers and possible body.
- Common status codes and how they affect the client's next action.
- The constraints that make an API RESTful.
- Security considerations and data formats used for transfer.

The advice was to study actively, code along where appropriate and discuss unclear sections with colleagues. Further JSON work, SQL connections from Python, HTTP/API work and Python for data were mentioned as upcoming topics. Their detailed implementation belongs in the notes for the sessions where they are covered.

## Revision checkpoints

- Explain my pipeline from input file to output without reading every line aloud.
- Describe which stages are already implemented and which improvements remain.
- Explain why `\N`, `\n`, `None` and JSON `null` are different representations.
- Choose `dump`, `dumps`, `load` or `loads` from the input and required result.
- Distinguish a response object, JSON text and a parsed dictionary or list.
- Explain why `finally` runs after an attempted operation and why `with` closes a file.
