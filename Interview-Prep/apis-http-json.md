# APIs, HTTP and JSON

## Working with Files

### 1. What is JSON?

“JSON stands for JavaScript Object Notation. It’s a lightweight text format used to exchange data between systems, especially through APIs.

It organises information using objects with key-value pairs and arrays. For example, a weather service could return a city, temperature and forecast.

It’s useful because people can read it, and most programming languages can process it.”

### 2. What is CSV?

“CSV stands for Comma-Separated Values. It stores tabular data as text, with records arranged in rows and commas usually separating the fields.

For example, our IMDb file contained information about titles, such as their names and release years.

It’s widely supported, so it’s useful for moving data between tools like Excel, Python and databases.”

### 3. What does the `with` statement do when working with files?

“`with` manages the file for the duration of a block of code. When the block finishes, it closes the file automatically—even if an exception occurs.

For example, I can read a CSV inside `with open(...)` without needing a separate `close()` call.

It handles the cleanup, but it doesn’t automatically handle errors such as a missing file.”

### 4. Why is using `with` considered best practice?

“It makes cleanup reliable and keeps the code straightforward.

If I manually open and close a file, an error between those steps could prevent the closing code from running. Using `with` handles that automatically.

That helps avoid leaving resources open and makes it clear which part of the code uses the file.”

### 5. What happens if you open a file that does not exist?

“It depends on the mode. Opening a missing file in read mode raises `FileNotFoundError`.

Write and append modes can create the file, provided the parent folder exists and we have permission.

For example, reading a missing customer CSV should fail, while opening a new output CSV in write mode can create it.”

### 6. What are the common modes used with `open()`?

“The main modes are:

- `r` — reads an existing file.
- `w` — writes a file, replacing existing contents.
- `a` — appends to the end.
- `x` — creates a file only if it doesn’t already exist.

Adding `b` selects binary mode, and `+` enables reading and writing.

For example, I’d read the source CSV with `r` and deliberately choose how to create the output.”

### 7. What is the difference between `w` and `a`?

“`w` replaces the contents of an existing file, while `a` preserves the contents and adds to the end. Both can create a new file.

For example, I might use `w` to produce a fresh daily report and `a` to add another entry to a log.

The distinction matters because using `w` accidentally could erase information.”

### 8. What is the difference between `json.load()` and `json.loads()`?

“Both parse JSON into Python objects. `json.load()` reads from a file-like object, while `json.loads()` reads from a string.

For example, I’d use `load()` with an opened JSON file and `loads()` if I already had the JSON text in a variable.

The result can contain dictionaries, lists and other Python values.”

### 9. How would you write a Python dictionary to a JSON file?

“I’d open the destination using `with`, then use `json.dump()` to serialise the dictionary.”

```python
import json

customer = {"name": "Sumiyya", "city": "Bradford"}

with open("customer.json", "w", encoding="utf-8") as file:
    json.dump(customer, file, indent=2)
```

“`indent=2` makes the file easier to read. I’d also check that the values are JSON-compatible—for example, dates need converting into an agreed representation.”

### 10. Some CSV rows are missing values. How would you handle this?

“I’d first check which fields are missing and whether they’re required.

For example, a missing optional phone number might be acceptable, but a missing customer ID could prevent us from linking the record correctly.

Depending on the agreed rules, I’d retain the missing value, use a justified default or set the record aside for investigation. I wouldn’t automatically delete every incomplete row.”

### 11. How would you merge CSV and JSON data?

“I’d read both files, inspect their structures and identify a shared field, such as customer ID. If the JSON is nested, I may need to flatten the relevant records first.

For example, the CSV could contain customers and the JSON their orders.

I could merge them using pandas, checking that the IDs have compatible types and that duplicate matches don’t unexpectedly multiply the rows.”

### 12. What would you consider when writing data back to a file?

“I’d check the destination, format, encoding and whether I should replace or append to an existing file.

For a CSV, I’d also check the headers, column order and quoting. Then I’d verify that the output contains the expected records.

For important outputs, I’d consider writing to a temporary file first, so a failure doesn’t leave the final file only partly written.”

### 13. How would you prevent accidentally overwriting an important file?

“I could use `x` mode, which fails if the file already exists, rather than silently replacing it.

I’d also keep source and output paths separate and consider versioned filenames or backups.

For example, writing a transformed dataset to a new dated filename lets me preserve the original and compare the results.”

### 14. How would you process a file that causes memory issues?

“I’d avoid loading the whole file into memory. Instead, I’d process it incrementally, either record by record or in manageable chunks.

For example, I could iterate through a CSV reader and write qualifying records straight to the output.

The approach depends on the format. JSON Lines supports record-by-record reading, while one large JSON document may need a streaming parser.”

## Error Handling

### 15. What is an exception in Python?

“An exception is an event that interrupts normal execution when an operation fails or signals a problem.

For example, converting `"hello"` into an integer raises `ValueError`.

We can handle expected exceptions so the program responds appropriately, rather than stopping without a useful explanation.”

### 16. What is the difference between a syntax error and an exception?

“A syntax error means Python can’t parse the code, such as when a colon is missing after an `if` statement.

Other exceptions happen while valid code is running, such as dividing by zero or opening a missing file.

Technically, `SyntaxError` is itself an exception type, but the practical distinction is invalid code structure versus a problem during execution.”

### 17. What is the purpose of a `try` block?

“A `try` block contains an operation that might raise an exception we want to handle.

For example, I could try converting a user’s input into a number.

If an exception occurs, execution leaves the remaining code in that block and Python looks for a matching handler. I’d keep the block focused so it’s clear which operation we’re protecting.”

### 18. What is the purpose of an `except` block?

“An `except` block defines how to respond to a matching exception raised in the `try` block.

For example, if converting input raises `ValueError`, I could explain that a number is required and ask again.

It lets us handle an expected problem deliberately rather than allowing it to stop the program unexpectedly.”

### 19. What happens if an exception is not handled?

“The exception moves back through the function calls looking for a matching handler.

If nothing handles it, normal execution stops and Python reports the error with a traceback. In a larger application, a framework or task runner might catch it.

For a pipeline, that could mean the task fails, so we need useful logging to understand where and why.”

### 20. What is `FileNotFoundError`?

“`FileNotFoundError` is raised when an operation needs a file or directory that can’t be found.

For example, reading `customers.csv` fails if that path doesn’t exist.

I’d check the supplied path and the program’s working directory, because a relative path might point somewhere different from what I expected.”

### 21. Why is exception handling important in production applications?

“Production systems encounter problems such as unavailable services, missing files and invalid input. Exception handling lets us respond predictably and record enough detail to investigate.

For example, a pipeline could report which source file failed instead of leaving an unexplained partial result.

It doesn’t mean hiding every error or continuing regardless. Sometimes stopping clearly is the correct response.”

### 22. What does `finally` do?

“`finally` runs as control leaves a `try` statement, whether the operation succeeded or an exception occurred. It’s mainly used for cleanup.

For example, it could release a resource that was opened earlier.

An exception still propagates if it hasn’t been handled; `finally` doesn’t automatically fix or suppress it.”

### 23. When would you use `raise`?

“I’d use `raise` when the program detects a condition that prevents it from proceeding correctly.

For example, if a customer file is missing a required ID column, I could raise a clear exception rather than produce an unusable output.

I can also re-raise an exception after logging it so the caller knows the operation failed.”

### 24. What are the benefits of catching specific exceptions?

“It lets me respond differently to different problems and avoids hiding unrelated bugs.

For example, a missing file needs a different response from a file containing invalid JSON.

If I catch everything and return an empty result, a serious problem might look like a successful run with no data. Specific handling makes the behaviour clearer.”

### 25. How can exception handling improve user experience?

“It replaces confusing failures with clear information and, where possible, a way to recover.

For example, if someone enters text instead of a number, I can explain what’s needed and let them try again.

The user gets useful guidance, while technical details can be logged separately for investigation.”

### 26. A user enters text when a number is expected. What would you do?

“I’d try converting the input and catch `ValueError` if it isn’t a valid number. Then I’d explain the problem and ask again.

After conversion, I’d also validate the range. For example, `-5` is a valid integer but might not be a valid order quantity.

That separates the correct data type from the business rules.”

### 27. A user supplies a file path that does not exist. What would you do?

“I’d attempt to open it and handle `FileNotFoundError` with a clear message identifying the path.

In an interactive program, I could ask for another path. In an automated pipeline, I’d log the issue and follow the agreed failure policy.

I wouldn’t silently create an empty input file, because that could hide the missing data.”

### 28. A JSON file contains invalid syntax. What would you do?

“I’d catch `json.JSONDecodeError` and use its details to identify where parsing failed.

For example, the file might have a missing comma or incorrectly quoted text. I’d report the issue and preserve the original for investigation.

In a pipeline, I might quarantine the file or fail the task. I wouldn’t guess at corrections and risk changing its meaning.”

### 29. How would you ensure a file closes if an exception occurs?

“I’d use `with open(...)`. The context manager closes the file when the block exits, including when an exception occurs.

For example, if processing fails halfway through reading a CSV, the file is still closed.

That handles the resource cleanup; I’d separately decide whether to catch the exception or let the caller handle it.”

### 30. What exceptions would you expect in a data pipeline, and how would you handle them?

“I’d expect missing files, permission problems, invalid formats, conversion errors and failures connecting to APIs or databases.

I’d handle them according to their cause. A temporary network failure might justify a limited retry, while an invalid record might be quarantined under agreed rules. A missing required column would usually stop that processing.

I’d log the stage and cause clearly, and make sure retries don’t create duplicate data.”

## HTTP & APIs

### 31. What is HTTP?

“HTTP stands for Hypertext Transfer Protocol. It defines how clients and servers exchange requests and responses.

For example, when I open a shopping website, my browser requests content and the server sends a response.

It also supports many APIs, allowing programs to exchange data without someone manually using the website.”

### 32. What does request-response mean?

“It means one side sends a request, and the other sends a response to it.

For example, my weather app requests the forecast for Leeds. The server processes that request and returns a status and the forecast data.

The client then checks the result and decides what to display or process.”

### 33. What does statelessness mean with HTTP?

“HTTP doesn’t automatically remember earlier requests. Each request is a separate interaction, so previous context isn’t automatically carried over.

For example, after I log into a website, my browser can send a session cookie with later requests so the site recognises my session.

This supports independent request handling, but applications need additional mechanisms when they want to remember a login or shopping basket.”

### 34. What is found in an HTTP request?

“An HTTP request includes a method, a target, headers and sometimes a body. It also uses a particular HTTP version.

The method describes the operation, the target identifies the resource, and headers carry information such as authentication or content type.

For example, submitting a registration form typically sends a POST request with the form details in its body.”

### 35. What is included in an HTTP response?

“A response includes a status code, headers and sometimes a body, using the relevant HTTP version.

The status describes the outcome, headers provide information about the response, and the body contains any returned content.

For example, requesting order details might return `200 OK`, a JSON content-type header and a body containing the order.”

### 36. What are the types of HTTP response status codes?

“They’re grouped into five categories:

- **1xx:** informational.
- **2xx:** successful.
- **3xx:** redirection.
- **4xx:** client-error responses.
- **5xx:** server-error responses.

For example, `200` indicates success, `404` means the resource wasn’t found, and `500` indicates an internal server error.

These codes help a program decide what to do next, rather than assuming every response contains usable data.”

### 37. What HTTP methods correspond to CRUD?

“CRUD means Create, Read, Update and Delete. Common mappings are:

- **Create:** POST.
- **Read:** GET.
- **Update:** PUT or PATCH.
- **Delete:** DELETE.

For example, a customer API could use POST to create a profile, GET to retrieve it and PATCH to change an address.

These are common conventions; the API documentation defines its actual supported operations.”

### 38. What is the difference between POST, PUT and PATCH?

“POST submits data for processing and often creates a resource. PUT creates or replaces the state at a particular URL. PATCH applies a partial modification.

For example, POST could create my customer profile, PUT could replace its full editable details, and PATCH could change just my delivery address.

With PUT, I’d normally send the complete representation the API expects, because leaving fields out could remove or reset them.”

### 39. What is DNS?

“DNS stands for Domain Name System. It resolves names such as a website’s domain into information including the IP address needed to reach the service.

For example, I can enter a shop’s website name instead of remembering its numerical address.

When a program calls an API using a hostname, DNS resolution helps it find where to connect.”

### 40. What is the difference between HTTP and HTTPS?

“HTTPS is HTTP protected using TLS. It encrypts traffic, protects it against undetected changes and authenticates the server through certificates.

For example, when I log into a website, HTTPS protects my credentials while they travel.

It protects the connection, though—it doesn’t automatically mean the website itself is trustworthy or the stored data is secure.”

### 41. What is a REST API?

“A REST API is an interface designed around REST’s architectural constraints, commonly using HTTP to interact with resources.

For example, an orders API could let me retrieve an order using GET or request its removal using DELETE.

It gives different applications a consistent way to interact. Responses often use JSON, although JSON isn’t a requirement of REST.”

### 42. What are the REST API criteria?

“The main constraints are client-server separation, statelessness, cacheability, a uniform interface and a layered system. Code on demand is optional.

In practice, that means clear separation of responsibilities, requests containing the context needed to process them, and consistent ways to identify and work with resources. Responses also specify whether they can be cached.

For example, a client shouldn’t need to know which database sits behind an orders API.”

### 43. What is a REST endpoint?

“A REST endpoint is an address through which we interact with an API resource.

For example, `/orders/123` could identify order 123. A GET request retrieves its representation, while another supported method performs a different operation.

The address identifies what we’re working with, and the HTTP method tells the server what we want to do.”

### 44. What is an API key?

“An API key is a credential that a service can use to identify the application or project making requests. It may also control access, usage limits or billing.

For example, a weather service might require a key alongside requests.

I’d follow its instructions for sending the key and keep it out of shared code, using environment variables or a secret store instead.”

---

[Back to Interview Prep](README.md)
