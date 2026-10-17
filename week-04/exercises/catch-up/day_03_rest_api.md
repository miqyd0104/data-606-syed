# REST API study and recall

[← Exercises](README.md)

These notes support the assigned REST API course. They do not record completion of the videos or a knowledge check.

## Core ideas

An API defines how software interacts with another system. An HTTP API exposes URLs that a client can request. REST is an architectural style: client/server separation, stateless requests, cacheability, a uniform interface, layers and optional code on demand. Using HTTP and JSON alone does not establish that every REST constraint is met.

A request has a method, target URL and headers, and may have a body. A response has a status code and headers, and may have a body. `Content-Type` describes the representation being sent; `Accept` describes representations the client can accept.

| Method | Typical purpose |
| --- | --- |
| GET | Retrieve a representation. |
| POST | Submit data for the resource to process, often creating something. |
| PUT | Create or replace the state at a known resource URL. |
| PATCH | Apply a partial modification. |
| DELETE | Request removal of a resource. |

GET is safe in HTTP semantics. PUT and DELETE are idempotent in their intended effects: repeating the same request should not add an additional intended change. Identical status codes on every repetition are not required. POST is not generally idempotent. An API can define additional safeguards such as idempotency keys.

| Status | Meaning to investigate |
| --- | --- |
| 200 | Request succeeded. |
| 201 | A resource was created. |
| 204 | Request succeeded with no response content. Do not blindly parse JSON. |
| 400 | The server considers the request invalid. |
| 401 | Authentication is needed or failed. |
| 403 | Access is forbidden; supplying a different request body is not automatically a fix. |
| 404 | Resource not found or not disclosed to this caller. |
| 429 | Too many requests; follow the service's retry guidance. |
| 500 | Server-side failure. |

## JSON and Python

JSON is text, not a Python dictionary. An object normally parses to a dictionary; an array parses to a list. JSON uses double-quoted strings, `true`, `false` and `null`; Python uses `True`, `False` and `None`.

- `json.dumps(data)`: Python value → JSON string.
- `json.loads(text)`: JSON text → Python value.
- `json.dump(data, file)`: write JSON to an open file.
- `json.load(file)`: read and parse JSON from a file-like object.

A successful parse does not validate the expected business fields. A URL can return HTML or an empty body instead of JSON. The accompanying script applies a timeout, requests JSON, handles common request failures and parses the response.

Use HTTPS and the service's authentication method. Keep credentials out of source files, screenshots, URLs and GitHub. Validate inputs and response structure. Avoid automatically retrying writes without understanding whether repeating them could duplicate an action.

## Answer before opening

<details><summary>What is the difference between a URL and an API?</summary>
A URL identifies a location/resource. An API defines an interface and behaviour; an HTTP API uses URLs for its endpoints.
</details>

<details><summary>What does stateless mean?</summary>
Each request supplies the information needed to understand it. The server can still store database records; stateless does not mean there is no persistent data.
</details>

<details><summary>What happens after Python receives JSON?</summary>
Parse the representation into Python values, check the structure and fields, then process them. Inspect whether the result is a list or dictionary instead of assuming.
</details>

<details><summary>Why might fetch_json fail?</summary>
An unreachable server, timeout, HTTP error status, invalid JSON or incompatible text encoding can fail. Valid JSON can still have the wrong business structure.
</details>

<details><summary>How would you explain an API in an interview?</summary>
An API is an agreed interface between software systems. For example, a Python client sends an HTTP GET to a data endpoint, checks the response, parses its JSON and processes the resulting records.
</details>

## References

- [Python JSON documentation](https://docs.python.org/3/library/json.html)
- [HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
- [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)
- [REST constraints in Fielding's dissertation](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)
