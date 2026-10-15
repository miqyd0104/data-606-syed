# Day 4 — Python with SQL Server, query results and API revision

15 October 2026

[← Week 4](../README.md) · [Previous notes: ETL review, JSON and API preparation](day-03-etl-review-json-and-api-preparation.md)

Today began with interview practice on Python, APIs, HTTP methods and JSON. We then connected Python to the Northwind SQL Server database using `pyodbc`, executed queries, compared the fetch methods and passed Python values into SQL safely. The afternoon finished with connection cleanup and priorities for independent work.

The main progression is **SQL selects the data; Python can then process the returned results**. Fetching rows gives me Python objects to work with. Changing those objects does not automatically change the database.

## Where to start when revisiting this

- [Interview practice and my feedback](#interview-practice-and-my-feedback)
- [API, HTTP and JSON recap](#api-http-and-json-recap)
- [Set up the Python environment](#set-up-the-python-environment)
- [Connect to SQL Server](#connect-to-sql-server)
- [Query results and Python types](#query-results-and-python-types)
- [Choose a fetch method](#choose-a-fetch-method)
- [Pass values safely into SQL](#pass-values-safely-into-sql)
- [Close resources and understand transactions](#close-resources-and-understand-transactions)
- [Complete follow-along example](#complete-follow-along-example)
- [Troubleshooting and practice](#troubleshooting-and-practice)

The examples reconstruct the teaching into reusable code. They include corrections to points that were uncertain in the live discussion. Database examples require my own working SQL Server instance, Northwind database and appropriate permissions; the transcript does not establish that my setup was fully fixed by the end of the day.

## Interview practice and my feedback

Luke emphasised explaining concepts to clients and colleagues as well as answering interview questions. A correct answer can still be difficult to follow if it contains too much detail, starts with exceptions or never explains why the topic matters.

The suggested structure was **what → why → impact**:

| Part | Purpose | Example about APIs |
| --- | --- | --- |
| What | Define the concept in plain language. | An API defines how software can request information or actions from another system. |
| Why | Explain the reason for using it. | It lets systems exchange information without people copying it manually. |
| Impact | Explain why the listener should care. | A reporting process can collect current data automatically, reducing repetitive work. |

Give the core answer first, then one useful example. Adapt the language to the audience without changing the facts or speaking down to them. Speak at a deliberate pace, use enough energy to be heard, and use first-person experience where it is true.

### Why Python is useful for data work

A concise answer could be:

> Python is useful for data work because its readable syntax makes processing steps easy to follow, and its ecosystem provides tools for files, databases and analysis. I can connect those steps into a repeatable pipeline without implementing every low-level operation myself.

Readability, development speed and reusable tools are stronger general points than claiming Python is always fast at execution. Python loops can be slower than compiled alternatives, while libraries can delegate intensive work to optimised native code. A library is not inherently slower just because it contains pre-written code.

### My JSON answer and handling uncertainty

I identified that JSON stores text-based data, but I needed a clearer explanation of its structure: **objects contain key–value pairs, separated by colons, inside curly braces**. I also needed to distinguish a string value from an entire object.

The communication feedback was to take ownership of an incomplete answer. State the limit of my knowledge, explain the part I do understand and hand the conversation back clearly instead of making the interviewer draw out every detail.

A useful practice response is:

> I understand that JSON is a text format for exchanging structured data. Objects use curly braces and key–value pairs. I’m still practising the more detailed syntax, so I would check an example before claiming I know every rule.

The aim is honest, clear communication, not sounding certain about something I have not learned. As I revise, replace the uncertainty with an accurate explanation and a small example.

### “Tell me about a time you made a mistake”

The non-technical question tested ownership, honesty, response to feedback and learning. Choose a real situation, explain my action and its result, and explicitly say what I would do differently in future. Avoid disguising a strength as a weakness or giving several vague examples without developing one.

A preparation outline is: what happened, what my responsibility was, how I responded, what changed, and what I learned. The session discussed another trainee's example; it is not an experience to present as my own.

## API, HTTP and JSON recap

### APIs connect software systems

**API** stands for Application Programming Interface. It describes how one piece of software can interact with another. A web API commonly exposes HTTP endpoints, but not every API is a web API or a REST API.

The benefit is that independently built systems can share data or capabilities through an agreed interface. A Python program could request book information, process the response and use it in a report rather than hard-coding the catalogue itself.

To explain an HTTP API call in Python:

1. Find the endpoint and read its request requirements.
2. Send the appropriate request, including authentication if required.
3. Check the response status and handle failures.
4. Parse the returned format and use the data.

Not every endpoint requires an API key. Mention authentication as a requirement of the particular service rather than implying that all APIs use the same login process. [Day 3's URL example](day-03-etl-review-json-and-api-preparation.md#read-json-from-a-url) provides a reusable JSON-fetching function.

### HTTP methods

| Method | Usual purpose | Example |
| --- | --- | --- |
| `GET` | Retrieve a representation of a resource. | Read a product or search results. |
| `POST` | Submit data for processing, often creating a resource. | Submit a registration form. |
| `PUT` | Create or replace the state at a target resource, according to the API contract. | Replace a saved profile representation. |
| `PATCH` | Apply a partial modification. | Change one profile field. |
| `DELETE` | Request removal of a resource. | Delete a draft record. |

**Clarification:** searching does not inherently require `POST`. Searches often use `GET` with query parameters, such as `/books?title=python`; some APIs use `POST` for structured search requests. Follow the endpoint documentation. A form can also use different methods depending on its purpose. See [MDN's HTTP method reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods).

HTTP status codes describe the response outcome; JSON describes a data format. An HTTP response can contain JSON, HTML or another format. JSON itself does not mean “status 200” or a successful request.

### JSON syntax to practise

**JSON** means **JavaScript Object Notation**, not Java Object Notation. It is a language-independent text format commonly used to exchange structured data and also used for storage.

```json
{
  "first_name": "Sam",
  "role": "Junior Data Consultant",
  "active": true,
  "completed_sessions": 3,
  "skills": ["Python", "SQL"],
  "manager": null,
  "office": {"city": "London"}
}
```

This is an illustrative record. The key points are:

- An **object** uses `{}` and contains key–value pairs.
- Keys are double-quoted strings; a colon separates each key from its value.
- Commas separate pairs or array elements, with no trailing comma after the last one.
- An **array** uses `[]` and can contain multiple values or objects.
- Values can be strings, numbers, booleans, `null`, arrays or objects.
- JSON uses `true`, `false` and `null`; Python uses `True`, `False` and `None`.

A JSON document has one top-level value. To store several records in one ordinary JSON document, wrap them in an array rather than writing separate objects next to each other. Newline-delimited JSON is a separate convention.

```python
import json

text = '{"name": "Sam", "skills": ["Python", "SQL"], "active": true}'
person = json.loads(text)

print(type(text))             # <class 'str'>
print(type(person))           # <class 'dict'>
print(person["skills"][0])   # Python
print(person["active"])      # True
```

The JSON text becomes Python objects when parsed. A dictionary uses **keys**, so `person[0]` would look for the key `0`; it does not mean “the first dictionary item”. Lists and tuples use positional indexing. See [Python's JSON documentation](https://docs.python.org/3/library/json.html).

## Why combine Python and SQL?

SQL is well suited to selecting, joining, filtering and aggregating relational data. Python adds general programming, reusable functions, file handling, API calls and other libraries around those queries.

```text
SQL Server / Northwind
    ↓ SQL query selects the required data
ODBC driver + pyodbc
    ↓ cursor fetches result rows
Python objects
    ↓ validation, transformation, reporting or another pipeline stage
Output destination
```

The database still executes the SQL. Python sends the statement and processes its results. This is another version of the extract–transform–load thinking used with the IMDb CSV work.

Use the strengths of both: filtering or aggregating in SQL often avoids transferring unnecessary data. Python is useful for steps that need its broader tools. Neither language replaces the other, and database roles are not limited to “basic SQL”.

## Set up the Python environment

### Virtual environments, pip and import

A **virtual environment** gives a project a separate Python package environment. It helps prevent one project's dependency versions from disrupting another project. It is not mainly a speed improvement or a compiler.

The important point is **which interpreter runs the code**. A file does not automatically use a virtual environment just because it sits inside a particular directory. The terminal or IDE must use that environment's interpreter. See [Python's venv documentation](https://docs.python.org/3/library/venv.html).

For macOS/Linux, from the practice project's folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pyodbc
```

For Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pyodbc
```

If PowerShell activation is unavailable under the machine's policy, I can use the interpreter directly instead of changing that policy:

```powershell
.\.venv\Scripts\python.exe -m pip install pyodbc
```

`python -m pip` runs the package installer belonging to that Python interpreter. Installation makes the package available; `import pyodbc` makes its functionality available in my code. Standard-library modules such as `json` need importing but normally do not need installing.

A module is an importable unit, a package organises modules, and “library” is a broader description of reusable functionality. The distinction is not simply that a library is physically bigger than a package.

### Check the environment before debugging the database

```bash
python -c "import sys; print(sys.executable)"
python -m pip show pyodbc
python -c "import pyodbc; print(pyodbc.drivers())"
```

`pyodbc.drivers()` lists registered ODBC drivers. Seeing the SQL Server driver confirms its availability to this setup; it does **not** prove that a database connection works. An empty list does not by itself mean the Python package failed to install.

**ODBC** stands for Open Database Connectivity. `pyodbc` is the Python interface, while a database-specific ODBC driver handles communication with the database. Installing the Python package is separate from installing Microsoft's SQL Server driver. For a Mac, use [Microsoft's macOS driver installation guide](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver17) if that driver is missing.

### The virtual-environment error I encountered

My error said the virtual-environment directory did not exist. That points first to a missing environment or an incorrect interpreter path, not to a SQL query problem.

Check the actual project folder, whether `.venv` exists there, and the interpreter configured in PyCharm. Create an environment if needed, or select the correct existing one. Install dependencies into that interpreter. If terminal execution works but the IDE fails, compare interpreter paths, working directories and run settings before changing the program.

The broader debugging lesson was to report the exact message, action and environment instead of only saying “it doesn't work”. An error narrows the investigation; read the useful part before guessing a fix.

## Connect to SQL Server

The connection needs a driver, a server address, a database and an authentication method. The demonstration used SQL Server Express on Windows with Windows authentication. Mac/Linux or Docker setups need their own matching connection details.

### Choose one connection configuration

For the follow-along example later, save **one** of the following configurations as `connection_settings.py` in a practice folder. Use the server, database and driver that actually exist on my machine.

**Option A — the Windows Express setup used in the demonstration:**

```python
# connection_settings.py — local Windows training database
connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    r"SERVER=localhost\SQLEXPRESS;"
    "DATABASE=Northwind;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)
```

Adjacent string literals inside parentheses form one string. Semicolons separate the ODBC settings. The raw string prefix `r` preserves the backslash in the named instance.

The instructor first tried `localhost`, then corrected it to `localhost\SQLEXPRESS` to match the server used in the database client. `localhost` alone is not interchangeable with every named instance.

**Option B — Python running on the host, connecting to an existing local SQL Server container using a SQL login:**

```python
# connection_settings.py — local container training database
from getpass import getpass


def odbc_value(value):
    # Quote an ODBC value, including any semicolons or closing braces.
    return "{" + value.replace("}", "}}") + "}"


username = input("SQL username: ")
password = getpass("SQL password: ")

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=Northwind;"
    f"UID={odbc_value(username)};"
    f"PWD={odbc_value(password)};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)
```

This prompts for the existing login rather than saving its password in the source file. The use of an f-string here builds connection settings; the later SQL examples bind query values separately.

Port `1433` is only an example: use the host port published by the container. The container must be running and Northwind must already exist. If Python runs inside another container, its `localhost` refers to that container, so use the appropriate network address instead. Copy connection details from the working database-client setup where possible; this snippet does not install or create a SQL Server instance.

| Setting | Meaning |
| --- | --- |
| `DRIVER` | Exact registered driver name, as shown by `pyodbc.drivers()`. |
| `SERVER` | Server/instance name or host and port. |
| `DATABASE` | Database to use after connecting. |
| `Trusted_Connection=yes` | Use integrated authentication in the Windows example. |
| `UID` / `PWD` | SQL login credentials in the container example. |
| `Encrypt=yes` | Request an encrypted connection. |
| `TrustServerCertificate=yes` | Skip certificate validation; used here only for a controlled local training setup. |

`Trusted_Connection` and `TrustServerCertificate` do different jobs. The first concerns authentication; the second concerns certificate validation. For a shared or production server, follow its certificate configuration and validate the certificate rather than copying the local exception. Microsoft documents these [connection-string settings](https://learn.microsoft.com/en-us/sql/connect/odbc/dsn-connection-string-attribute?view=sql-server-ver17).

### Connection, cursor, execute and fetch

Here is a reusable version of the sequence used in class, with cleanup included:

```python
from contextlib import closing

import pyodbc
from connection_settings import connection_string

with closing(pyodbc.connect(connection_string, timeout=5)) as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT @@VERSION;")
        row = cursor.fetchone()
        print(row[0])
```

`connection` represents the database connection. `cursor` executes statements and manages their results. `execute()` submits the SQL; `fetchone()` retrieves a row from its result. `row[0]` selects the first column of that row.

`SELECT @@VERSION` returns SQL Server version information. It does not count customers. The instructor briefly expected `91` while running the version query; changing the query changes what the output means.

The snippets below assume an open `cursor`. Run them inside the inner `with` block above, replacing its query section, or use the complete example further down. They are not intended to run after the cursor has closed. The cleanup behaviour is explained later in these notes.

## Query results and Python types

### Count customer rows

```python
cursor.execute("SELECT COUNT(*) FROM dbo.Customers;")
row = cursor.fetchone()
print(row[0])
```

`COUNT(*)` returns one aggregate value in one result row. The demonstration's Northwind database returned **91 customers**. My count can differ if my copy has changed. This is the number of customer records, not the number of columns.

### Retrieve rows and use named columns

```python
cursor.execute(
    "SELECT ProductName, UnitPrice "
    "FROM dbo.Products ORDER BY ProductID;"
)
rows = cursor.fetchall()

print(type(rows))             # <class 'list'>
if rows:
    print(type(rows[0]))      # <class 'pyodbc.Row'>

for row in rows:
    print(row.ProductName, row.UnitPrice)
```

The live discussion mixed together the outer collection and each record. The precise distinction is:

| Expression | Meaning |
| --- | --- |
| `rows` | A list containing fetched `pyodbc.Row` objects. |
| `rows[0]` | The first row in that list, if present. |
| `rows[0][0]` | The first selected column of the first row. |
| `row.ProductName` | A selected column on one row. |

A `pyodbc.Row` is tuple-like, but it is not a built-in tuple. It supports indexed access, named column access and replacement of its field values. Checking `type(rows)` tells me only about the outer list. Calling the whole result a “2D array” is an informal picture, not its actual Python type. See the [pyodbc Row documentation](https://github.com/mkleehammer/pyodbc/wiki/Row).

`rows.ProductName` does not work because the list itself has no such column attribute. Loop over its rows. For awkward or duplicate column names, use clear, unique SQL aliases or positional access.

### Get the column headings

The class asked how to retrieve headings. The result metadata provides them:

```python
cursor.execute(
    "SELECT ProductName, UnitPrice "
    "FROM dbo.Products ORDER BY ProductID;"
)
column_names = [column[0] for column in cursor.description]
print(column_names)  # ['ProductName', 'UnitPrice']

for row in cursor.fetchall():
    record = dict(zip(column_names, row))
    print(record)
```

Each item in `cursor.description` describes one returned column; its first item is the name. This can help build dictionaries or CSV headers. Capture metadata for the query I intend to process, since another query on the same cursor replaces its current result context. See the [cursor reference](https://github.com/mkleehammer/pyodbc/wiki/Cursor).

### Local changes do not write back to SQL Server

Calling `rows.pop()` removes an item from the Python list. Changing a field on a fetched row changes that local object. Neither operation issues a database update.

Database writes require appropriate SQL, such as `INSERT`, `UPDATE` or `DELETE`, and the relevant transaction handling. `ALTER` changes structures such as a table definition; it is not the normal command for changing a customer's city. The main walkthrough today was retrieval, not a demonstrated write-back pipeline.

## Choose a fetch method

All three fetch methods consume the **remaining rows of an already executed result set**:

| Method | Returns | When there are no more rows | Typical use |
| --- | --- | --- | --- |
| `fetchone()` | The next row | `None` | A single result or one-row-at-a-time processing. |
| `fetchall()` | A list of all remaining rows | `[]` | Small results that are convenient to hold together. |
| `fetchmany(n)` | A list containing up to `n` remaining rows | `[]` | Processing bounded batches. |

Calling `fetchone()` and then `fetchall()` does not return the first row twice: the second call retrieves what is left. Re-execute the query to start a fresh result. A fetch without a suitable executed query is an error, not simply an empty result. These behaviours follow the [Python database API](https://peps.python.org/pep-0249/).

### Fetch one row at a time

```python
cursor.execute(
    "SELECT ProductName FROM dbo.Products ORDER BY ProductID;"
)

while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(row.ProductName)
```

The query executes **once**, before the loop. Each fetch advances through its result; it is not a new `SELECT` per row. Test `row is None` before accessing its fields. A row that contains a SQL `NULL` is still a row and is different from having no row left.

### Fetch batches

```python
cursor.execute(
    "SELECT ProductName FROM dbo.Products ORDER BY ProductID;"
)

while True:
    batch = cursor.fetchmany(10)
    if not batch:
        break
    for row in batch:
        print(row.ProductName)
```

Here the outer loop obtains a batch; the inner loop processes its rows. The final nonempty batch can contain fewer than ten rows. `if not batch` detects the empty list at the end. Changing the batch size changes the grouping, not which matching records the complete loop ultimately processes.

In `pyodbc`, `cursor.execute(...)` returns the cursor itself, so the chained form below is also valid. The name `results` would still refer to a cursor if assigned only the result of `execute()`.

```python
rows = cursor.execute("SELECT CustomerID FROM dbo.Customers;").fetchall()
```

### Memory, speed and scale

`fetchall()` materialises the remaining result as a Python list, which can be expensive for a large result. Processing a row or batch and then discarding it can reduce the Python objects retained at once. Appending every batch to one growing list defeats that benefit.

The discussion about memory being kept until the script ends, or only being released with SQLAlchemy, should not be treated as a general rule. Python objects can become reclaimable when they are no longer referenced. Database drivers and servers can also buffer results, so batching alone does not guarantee a fixed total memory footprint or immediate return of memory to the operating system.

Likewise, `fetchmany()` is not guaranteed to be faster in every setup, and one fetch call does not necessarily equal one network request. Compare representative workloads rather than assuming a fixed speed or cloud-cost saving. Cloud charges depend on the service and data movement, not a universal “one fee per fetch” rule.

### `TOP`, `WHERE` and `fetchmany()` do different jobs

```sql
SELECT TOP (20) ProductID, ProductName
FROM dbo.Products
WHERE Discontinued = 0
ORDER BY ProductID;
```

This SQL selects at most twenty matching products in a defined order. If Python then repeatedly calls `fetchmany(5)`, it processes that result in batches of up to five. It does not fetch five new products outside the selected twenty.

`WHERE` selects eligible records. `TOP` limits the query result. `ORDER BY` defines the order. `fetchmany()` controls how Python consumes the result. Use SQL to restrict rows and columns when practical, then choose a fetching strategy appropriate to the result size.

Without `ORDER BY`, do not rely on a stable “first ten” or “next ten”. Batch boundaries are also not a durable pagination system for returning later to a changing database.

## Pass values safely into SQL

The final query filtered customers by city, using `London` as the example. The demonstration first inserted the value with an f-string, then changed to a parameter placeholder.

```python
city = "London"
cursor.execute(
    "SELECT CompanyName, City FROM dbo.Customers "
    "WHERE City = ? ORDER BY CompanyName;",
    (city,),
)

for row in cursor.fetchall():
    print(row.CompanyName, row.City)
```

`?` marks a value parameter. `(city,)` is a one-item tuple; its comma matters. The SQL text and parameter value are supplied separately. The driver binds the value as data rather than treating it as additional SQL syntax. Do not put quotation marks around the `?` in the statement.

This is why parameter binding is preferable to composing `WHERE City = '...value...'` through string interpolation. A legitimate apostrophe in a name should not break the query, and untrusted input should not be able to alter its structure.

**Clarification:** rejecting spaces or selected special characters is not a substitute for parameterised queries. It can reject legitimate values and still miss dangerous input. Parameters protect value positions; table names, column names and other SQL structure require controlled choices rather than arbitrary user text. See [OWASP's SQL injection prevention guidance](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) and [pyodbc's getting-started examples](https://github.com/mkleehammer/pyodbc/wiki/Getting-started).

## Close resources and understand transactions

The class ended by closing the cursor and then the connection:

```python
cursor.close()
connection.close()
```

Use cleanup that also runs when something fails. Leaving these two lines only at the bottom of a script can skip them if an earlier operation raises an exception.

The question about `with` was left uncertain in the recording. **Context managers are not limited to files.** `pyodbc` connections support `with`, but their context-manager behaviour concerns transactions and does not automatically close the connection. For closing specifically, [contextlib.closing](https://docs.python.org/3/library/contextlib.html#contextlib.closing) calls the object's `close()` method on exit. See the [pyodbc connection documentation](https://github.com/mkleehammer/pyodbc/wiki/Connection#context-manager).

The complete example below uses nested `closing` blocks so the cursor closes before the connection, including when an error occurs. This also handles a failure while creating the cursor after a connection has already opened.

**Commit is different from close.** For writes with autocommit disabled, explicitly decide when to `commit()` the transaction or `rollback()` after failure. Closing a connection is not a substitute for committing intended changes. The read queries in these notes do not need a write transaction to be committed.

## Complete follow-along example

Save this as `query_northwind.py` beside the chosen `connection_settings.py`. It checks the connection, counts customers, then reads customers from one city in batches. It only issues `SELECT` statements.

```python
# query_northwind.py
import argparse
from contextlib import closing

import pyodbc


def main():
    parser = argparse.ArgumentParser(description="Read Northwind customers")
    parser.add_argument("--city", default="London")
    parser.add_argument("--batch-size", type=int, default=10)
    args = parser.parse_args()
    if args.batch_size < 1:
        parser.error("--batch-size must be at least 1")

    # Load settings after argument validation; the container option prompts.
    from connection_settings import connection_string

    with closing(pyodbc.connect(connection_string, timeout=5)) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT @@VERSION;")
            print("Connected to:", cursor.fetchone()[0])

            cursor.execute("SELECT COUNT(*) FROM dbo.Customers;")
            print("Total customers:", cursor.fetchone()[0])

            cursor.execute(
                "SELECT CustomerID, CompanyName, City "
                "FROM dbo.Customers WHERE City = ? ORDER BY CustomerID;",
                (args.city,),
            )

            processed = 0
            while True:
                batch = cursor.fetchmany(args.batch_size)
                if not batch:
                    break
                for row in batch:
                    print(row.CustomerID, row.CompanyName, row.City)
                    processed += 1

            print(f"Customers returned for {args.city!r}: {processed}")


if __name__ == "__main__":
    main()
```

Run it from that practice folder using the environment where `pyodbc` is installed:

```bash
python query_northwind.py --city London --batch-size 5
python query_northwind.py --city Berlin --batch-size 2
```

The version output depends on the server. The total customer count reflects the whole table, while `processed` counts only the selected city's rows. An unmatched city should produce a filtered count of zero, not an endless loop or an attempt to access fields on `None`.

### Why use the terminal?

The session used a hypothetical image-thumbnail script to show how arguments can choose an input and output folder without editing code. The city and batch-size options above apply the same idea to querying.

Command-line execution also works on servers and containers without an IDE. The program must parse and use the supplied arguments; adding text after a filename does not automatically change its behaviour. The example uses Python's [argparse module](https://docs.python.org/3/library/argparse.html) for that job. IDEs such as PyCharm can also pass arguments through run configurations, so arguments are not exclusive to terminal execution.

A script can perform several related steps and can produce different outputs as its inputs change. “Script” does not guarantee a single operation or identical output every run.

## Troubleshooting and practice

### Match the symptom to the layer

| Symptom | First checks |
| --- | --- |
| Virtual-environment directory missing | Project path, whether the environment exists, IDE interpreter path. |
| `ModuleNotFoundError: pyodbc` | Which Python executable is running and where the package was installed. |
| Driver not found / driver cannot load | Registered driver name, OS driver installation and compatible architecture. |
| Server not found / connection timeout | Server or instance name, running service/container, published port and network access. |
| Login failed | Authentication method, account permissions and credentials. |
| Certificate validation failure | Server certificate and connection configuration; distinguish local training from a shared server. |
| Cannot open Northwind / invalid object name | Database exists, correct database selected, schema and table names. |
| `rows.CompanyName` fails | `rows` is a list; access the column on each row. |
| A later fetch returns nothing | The result may already be consumed; re-execute the query if restarting is intended. |
| Terminal works, IDE does not | Interpreter, working directory, environment variables and run arguments. |

A useful help request is: “I ran this command from this folder, using this interpreter. I expected this result, but received this exact error. These are the checks I have already tried.” Remove credentials before sharing connection details.

### Practice sequence

1. Confirm the interpreter and available ODBC drivers.
2. Connect and run `SELECT @@VERSION`; explain why it returns a version rather than a customer count.
3. Count `dbo.Customers` and compare with the same query in the database client.
4. Select product names and prices; inspect the types of both the collection and an individual row.
5. Retrieve column names using `cursor.description`.
6. Run the same ordered query separately with `fetchall`, repeated `fetchone` and repeated `fetchmany`; compare the complete sequences and counts.
7. With more than ten selected rows, fetch ten and then fetch again. Explain why the cursor continues instead of restarting.
8. Change the city parameter, including a city with no matches. Confirm that the query remains unchanged and only the bound value differs.
9. Try batch sizes of one and five, then zero. The complete script should reject zero before connecting.
10. Explain which changes happen only in Python and what would be needed to persist a change in SQL Server.

These are suggested revision tasks based on the lesson, not a claim that the later task-board exercises or submissions have been completed.

## Priorities and what was left for later

The end-of-day priorities were:

1. Complete the AI assignment first. The separate [AI Fundamentals notes](../../ai-fundamentals/README.md) contain the session and assignment summaries.
2. Finish the REST API learning videos, revisiting unclear sections. I was among those identified as still needing to finish them.
3. Practise Python with SQL; additional tasks and SQLAlchemy material were to be put on the task board.
4. If time remained, explore Jupyter notebooks and prepare for Python for data, including NumPy and pandas.

SQLAlchemy, loading results into pandas and writing transformed data back to SQL were discussed as extensions, but were **not walked through** in the supplied recordings. The planned next session was Jupyter notebooks and NumPy, possibly beginning pandas. Later API-to-MongoDB/cloud pipeline work was previewed rather than implemented today.

## Revision checkpoints

- Explain an API using what, why and impact, without starting with unnecessary detail.
- Write a valid JSON object and explain keys, values, arrays and nesting.
- Distinguish package installation, module import, the Python interpreter and the ODBC driver.
- Explain the roles of connection, cursor, execution and fetching.
- Identify a list of rows, one `pyodbc.Row`, and one column value.
- Explain why a fetch consumes results and why `fetchmany(10)` differs from `TOP (10)`.
- Choose a fetching approach without claiming guaranteed memory, speed or billing behaviour.
- Bind query values separately from SQL text and explain why character filtering is insufficient.
- Distinguish local edits, database writes, commit/rollback and resource cleanup.
- Describe my next debugging step from an actual error message.

## Recording guide

Based on the two supplied transcripts, both dated 15 October 2026:

| Recording and approximate timestamp | Topic |
| --- | --- |
| Part 1, 00:27–39:55 | Interview delivery, Python, HTTP methods and APIs. |
| Part 1, 40:09–50:00 | JSON, my answer and feedback on handling uncertainty. |
| Part 1, 51:16–57:00 | Learning from mistakes and explaining the outcome. |
| Part 1, around 1:15–1:38 | Python/SQL overview, environments, pip, imports and drivers. |
| Part 1, 1:39–end | Environment troubleshooting, connection settings and version check. |
| Part 2, 03:23–14:00 | Terminal execution, script arguments and setup recap. |
| Part 2, 14:00–32:00 | Counting, fetching, row types and local versus database changes. |
| Part 2, 32:00–48:00 | Scale, batching and SQL filtering versus fetching. |
| Part 2, 1:02–1:12 | City query, SQL injection, parameters and cleanup. |
| Part 2, 1:12–end | Independent-work priorities and the next session. |

The technical references linked beside clarifications resolve uncertain statements from the discussion. The raw transcripts include speech-recognition errors, so the code uses the actual Python and SQL spellings.
