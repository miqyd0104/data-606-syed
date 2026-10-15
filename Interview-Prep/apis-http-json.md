[apis-http-json-updated.md](https://github.com/user-attachments/files/33503993/apis-http-json-updated.md)
# APIs, HTTP and JSON

## Working with Files

### 1. What is JSON?

“JSON stands for JavaScript Object Notation. It’s a lightweight text format used to exchange data between systems, especially through APIs.

It uses key-value pairs. For example, the key could be ‘city’ and the value ‘Leeds’, separated by a colon. Both are text, so they use double quotation marks, and the object sits inside curly brackets.

It’s useful because most programming languages can read it, making data easier to share.”

### 2. What is CSV?

“CSV stands for Comma-Separated Values. It stores tabular data as text, with each row representing a record and commas usually separating the fields.

For example, our IMDb file contained information like the title, release year and genre.

It’s useful for moving data between tools because Excel, Python and databases can all work with it.”

### 3. What does the `with` statement do when working with files?

“When I use ‘with’ to open a file, Python closes it automatically when the block finishes, even if an error happens.

For example, I can read a CSV inside that block without needing a separate closing step.

It handles the cleanup, although I’d still need to handle problems like the file not existing.”

### 4. Why is using `with` considered best practice?

“It means I don’t have to rely on remembering to close the file myself.

If I open it manually and an error happens before the closing instruction, that instruction might never run. Using ‘with’ avoids that problem.

It keeps the code simpler and makes sure the file is closed when I’m finished.”

### 5. What happens if you open a file that doesn’t exist?

“It depends on the mode. In read mode, Python raises a file-not-found error because there’s nothing to read.

Write and append modes can create the file, provided the folder exists and I have permission.

So reading a missing source file would fail, but writing a new output file could create it.”

### 6. What are the common file modes used with `open()`?

“The main ones are ‘r’ for reading, ‘w’ for writing, ‘a’ for appending and ‘x’ for creating a new file only if it doesn’t already exist.

Adding ‘b’ selects binary mode, and a plus sign enables reading and writing.

For example, I’d use read mode for the original IMDb file. I’d be careful with write mode because it replaces existing contents.”

### 7. What is the difference between write and append modes?

“Write mode replaces the contents of an existing file. Append mode keeps what’s already there and adds new content to the end. Both can create a new file.

For example, I might use write mode for a fresh report and append mode for another log entry.

Choosing the wrong mode could erase information or create repeated data.”

### 8. What is the difference between `json.load()` and `json.loads()`?

“They both turn JSON into Python data, but they read it from different places.

‘Json load’ reads from an opened file. ‘Json loads’, with an ‘s’ at the end, reads JSON text from a string already in the program.

So I’d use load for a JSON file and loads when the JSON text is already held in a variable.”

### 9. How would you write a Python dictionary to a JSON file?

“I’d import Python’s JSON module, open the output file using ‘with’, and use ‘json dump’ to write the dictionary as JSON.

For example, my dictionary could contain a customer’s name and city. I could also add indentation so the output is easier for someone to read.

I’d check that the values can be represented in JSON and that I’m happy to replace the destination file if it already exists.”

### 10. A CSV contains customer data, but some rows are missing values. How would you handle this?

“I’d first check which values are missing and whether they’re required.

A missing phone number might be acceptable, but a missing customer ID could stop us linking the record correctly.

I’d follow the agreed rules—perhaps leaving an optional field empty or setting the record aside for investigation. I wouldn’t automatically delete every incomplete row or fill it with a guess.”

### 11. How would you merge data from a CSV and a JSON file?

“I’d read both files and find a shared field, like customer ID. If the JSON contains nested records, I may need to flatten the relevant information first.

For example, the CSV could contain customer details and the JSON their orders.

I could merge them using pandas, then check that the IDs have matching types and that missing or duplicate matches haven’t produced unexpected results.”

### 12. What would you consider when writing data back to a file?

“I’d check the location, required format and whether I should replace the file or add to it.

For a CSV, I’d check the headers, column order, encoding and how missing values should appear.

Then I’d check the output against what I expected. For an important file, I could write a temporary version first so a failure doesn’t leave the final output partly written.”

### 13. How would you prevent accidentally overwriting an important file?

“I could use exclusive creation mode—the letter ‘x’—which raises an error if the file already exists.

I’d also keep source and output paths separate and use dated filenames or backups where needed.

For example, creating a new report version lets me keep the previous one rather than replacing it accidentally.”

### 14. A file is extremely large and causes memory issues. How would you process it?

“I’d avoid loading the whole file into memory. Instead, I’d process records one at a time or in smaller chunks.

For example, with a CSV, I could read a record, apply the filtering rules and write it straight to the output if it qualifies.

That keeps memory use down. A large JSON document may need a streaming parser, depending on its structure.”

## Error Handling

### 15. What is an exception in Python?

“An exception interrupts the normal flow of a program when an operation fails or signals a problem.

For example, trying to convert the word ‘hello’ into an integer raises a value error.

We can handle expected exceptions so the program responds sensibly, such as explaining the problem or asking for another input.”

### 16. What is the difference between a syntax error and an exception?

“A syntax error means the code isn’t written in a way Python can parse, like leaving a colon off an ‘if’ statement.

A runtime exception happens when the code runs into a problem, such as trying to open a missing file.

So I’d fix the code structure for a syntax error, while an expected runtime problem might need handling with ‘try’ and ‘except’.”

### 17. What is the purpose of a `try` block?

“A ‘try’ block contains an operation that might fail in a way we want to handle.

For example, I could try converting someone’s input into a number. If that raises an exception, Python looks for a matching ‘except’ block.

It doesn’t prevent the error—it gives us a way to respond to it.”

### 18. What is the purpose of an `except` block?

“An ‘except’ block says what to do when a particular exception happens in the ‘try’ block.

For example, if someone enters text instead of a number, I could catch a value error, explain what’s needed and let them try again.

That makes the problem manageable rather than stopping the program without useful guidance.”

### 19. What happens if an exception is raised but not handled?

“Python works back through the function calls looking for something that can handle it. If nothing does, execution stops and Python reports the error with a traceback.

For example, a missing-file error could stop a pipeline before processing begins.

The traceback helps locate the problem, and clear logging helps us understand the context.”

### 20. What is `FileNotFoundError`?

“A file-not-found error happens when an operation needs a file or folder that can’t be found.

For example, trying to read a customer CSV fails if it isn’t at the supplied path.

I’d check the spelling, location and working directory, because the program might be looking somewhere different from where I expected.”

### 21. Why is exception handling important in production applications?

“Real applications encounter missing files, unavailable services and invalid data. We need to respond to those problems clearly and predictably.

For example, a pipeline should report which file failed rather than appear successful with incomplete data.

Sometimes we can recover, but sometimes stopping and reporting the problem is safer than carrying on with incorrect results.”

### 22. What does the `finally` block do?

“‘Finally’ runs when we leave the ‘try’ statement, whether the operation succeeded or an exception occurred. We normally use it for cleanup.

For example, it could close a connection or release another resource.

It doesn’t automatically handle the error—the exception can still continue after the cleanup.”

### 23. When would you use `raise`?

“I’d use ‘raise’ when I detect a problem that means the function can’t complete its task correctly.

For example, if an input file is missing a required customer ID column, I could raise a clear error rather than produce an incomplete result.

That lets the calling code decide what should happen next.”

### 24. What are the benefits of catching specific exceptions?

“It helps us respond to the actual problem without hiding other mistakes.

For example, a missing file needs different handling from a file containing invalid JSON.

If I catch everything and return an empty result, a serious failure might look like a successful run with no records. Specific exceptions help keep that distinction clear.”

### 25. How can exception handling improve the user experience?

“It gives someone a useful explanation and, where possible, a way to recover.

For example, instead of showing a technical traceback when they enter invalid text, I could explain that a number is required and let them try again.

Technical details can still be logged separately so the problem can be investigated.”

### 26. A user enters text when a number is expected. What would you do?

“I’d try converting the input and catch a value error if it isn’t a valid number. Then I’d explain what’s needed and ask again.

I’d also check the value after conversion. A negative number is still a number, but it might not be a valid order quantity.

That checks both the format and the business rule.”

### 27. A user supplies a file path that doesn’t exist. What would you do?

“I’d try opening it and catch a file-not-found error.

In an interactive program, I could explain which path wasn’t found and ask for another one. In a scheduled pipeline, I’d log the issue and follow the agreed failure process.

I wouldn’t silently create an empty input file, because that could hide the missing data.”

### 28. A JSON file contains invalid syntax. What would you do?

“I’d catch the JSON decoding error and use its details to help find the problem.

For example, there could be a missing comma or a string written without the required double quotation marks.

I’d report the issue and keep the original file for investigation. I wouldn’t guess at a correction because that could change the meaning of the data.”

### 29. How would you ensure a file closes even if an exception occurs?

“I’d open it using ‘with’. Python closes the file when that block finishes, even if processing fails halfway through.

That takes care of the cleanup without needing a separate closing step.

I’d still decide how to handle the exception itself, because closing the file doesn’t resolve the underlying problem.”

### 30. What exceptions would you expect in a data pipeline, and how would you handle them?

“I’d expect missing files, permission problems, invalid values and failed API or database connections.

The response depends on the cause. A temporary connection issue might justify a limited retry. An invalid record might be set aside, while a missing required column could mean stopping the task.

I’d log the problem clearly and make sure retries don’t accidentally duplicate data.”

## HTTP & APIs

### 31. What is HTTP?

“HTTP stands for Hypertext Transfer Protocol. It defines how a client and server exchange requests and responses.

For example, when I open a shopping website, my browser requests content and the server sends it back.

Programs can use it too, which is how many APIs let applications request data automatically.”

### 32. What does a request-response style protocol mean?

“It means the client asks for something and the server sends a response.

For example, my weather app requests the forecast for Leeds. The server processes that request and sends back a status and, if successful, the forecast data.

The app checks the response and decides what to display.”

### 33. What does statelessness mean with HTTP?

“HTTP doesn’t automatically remember earlier requests. Each request is treated separately, so information from a previous interaction isn’t automatically carried over.

For example, after I log into a shopping website, my browser can send a session cookie with later requests so the website recognises my session.

This supports independent request handling, but remembering things like a login needs an additional mechanism.”

### 34. What is found in an HTTP request?

“A request contains a method, a target, headers and sometimes a body.

The method says what we want to do, the target identifies what we’re requesting, and headers provide details such as authentication and data format.

For example, submitting a registration form typically sends a POST request to the registration endpoint, with the form details in the body.”

### 35. What is included in an HTTP response?

“A response contains a status code, headers and sometimes a body.

The status tells us the outcome, the headers describe the response, and the body contains any returned content.

For example, requesting an order could return status 200 and a JSON body containing its details. Checking the status helps us avoid treating an error response as valid order data.”

### 36. What are the types of HTTP response status codes?

“The first digit tells us the category. Codes in the hundreds are informational, the two hundreds indicate success, and the three hundreds relate to redirection.

The four hundreds indicate a client-error response, while the five hundreds indicate a server-error response.

For example, 200 means success, 404 means the resource wasn’t found, and 500 means an internal server error. These help the client decide what to do next.”

### 37. What HTTP methods do we use for CRUD?

“CRUD stands for Create, Read, Update and Delete.

We commonly use POST to create, GET to read, PUT or PATCH to update, and DELETE to remove.

For example, a customer API could let me create a profile, retrieve it, change the address or delete it. I’d check the documentation to confirm exactly which operations that API supports.”

### 38. What is the difference between POST, PUT and PATCH?

“POST sends data for processing and often creates a new resource. PUT creates or replaces the resource at a particular address. PATCH changes selected parts.

For example, POST could create my profile, PUT could replace its full details, and PATCH could change just my delivery address.

With PUT, I’d normally send the complete details the API expects, because omitted fields could be removed or reset.”

### 39. What is DNS?

“DNS stands for Domain Name System. It helps resolve a domain name to an IP address so we can reach the service.

For example, I can enter a shop’s website name rather than remember its numerical address.

The same applies when Python calls an API using a hostname—DNS helps find where the connection should go.”

### 40. What is the difference between HTTP and HTTPS?

“HTTPS is HTTP protected using TLS. It encrypts the information travelling between the client and server, protects against undetected changes and helps verify the server’s identity.

For example, it protects my login details while they travel to a website.

It secures the connection, but it doesn’t automatically mean the website itself is trustworthy.”

### 41. What is a REST API?

“A REST API lets applications interact with resources following REST’s design principles, usually over HTTP. REST stands for Representational State Transfer.

A resource could be a customer or order. For example, a GET request could retrieve an order, while DELETE could request its removal.

It gives applications a consistent way to interact. JSON is commonly used for the data, but it isn’t required by REST.”

### 42. What are the REST API criteria?

“The main constraints are client-server separation, statelessness, cacheability, a uniform interface and a layered system. Code on demand is optional.

That means the client and server have separate responsibilities, requests carry the context needed to process them, and resources are accessed consistently. Responses also indicate whether they can be cached.

For example, a client can use an orders API without knowing which database or intermediary services are behind it.”

### 43. What is a REST endpoint?

“A REST endpoint is an address where we interact with an API resource.

For example, an endpoint could have a path of ‘orders’, followed by a slash and an order ID such as 123. Sending GET to that address retrieves that order’s details.

The address identifies what we mean, and the method tells the server what we want to do.”

### 44. What is an API key?

“An API key is a credential a service uses to identify the application or project making requests. It can also help control access, track usage or apply billing.

For example, a weather API might require a key alongside each request.

I’d keep it out of shared code and store it securely, because exposing it could let someone use the service under our account.”

---

[Back to Interview Prep](README.md)
