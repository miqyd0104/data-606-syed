# Python

Interview questions and answers for our Data Engineering course.

## Data Types

### 1. What are the main built-in data types in Python?

“The main ones I’ve worked with are strings for text, integers for whole numbers, floats for decimal numbers and booleans for `True` or `False`.

We also have collections like lists, tuples, dictionaries and sets. For example, a customer record could be a dictionary containing a name as a string and an age as an integer. Choosing the right type helps us process the values correctly.”

### 2. What is the difference between mutable and immutable data types?

“Mutable means we can change an object after creating it. Immutable means we can’t change the object itself.

For example, we can add an item to an existing list, but changing a string produces a new string.

This matters when objects are shared between different parts of a program, because changing a mutable object can affect other code using it.”

### 3. Can you give examples of mutable and immutable objects?

“Lists, dictionaries and sets are mutable. We can add, remove or change their contents.

Strings, integers, floats, booleans and tuples are immutable. For example, we can replace a variable’s integer value, but that binds it to another object rather than changing the original integer.

A tuple’s elements can’t be reassigned, although an object inside it, like a list, can still be mutable.”

### 4. What is the difference between a string, integer and float?

“A string represents text, an integer represents a whole number, and a float represents a number with a fractional part.

For example, `"25"` is text, `25` is an integer and `25.5` is a float. That affects what we can do with them: adding two strings joins them, while adding two integers performs arithmetic.

That’s why we often convert values read from CSV files.”

### 5. When might you choose a tuple instead of a list?

“I’d choose a tuple when I have an ordered group of values whose positions and membership shouldn’t change.

For example, I could store a latitude and longitude as a pair. A tuple makes it clear that those values belong together in a fixed structure.

If I needed to keep adding or removing items, I’d normally choose a list.”

## Lists and Collections

### 6. What is a list, and when would you use one?

“A list is an ordered collection of items that we can change. It allows duplicates, and we access items by their position, starting at zero.

For example, I could collect the movie records that pass my filtering rules into a list.

It’s useful when I need to process several items and potentially add, remove or update them.”

### 7. What are some common operations you can perform on a list?

“We can access items by index, take slices, loop through the list, and add or remove items.

For example, `append()` adds one item, `extend()` adds items from another iterable, and `pop()` removes and returns an item.

We can also sort or filter the contents. In the IMDb task, I could loop through records and append the qualifying movies to a results list.”

### 8. How does a list differ from a tuple?

“They both store ordered collections and allow duplicates. The main difference is that a list can be changed, while a tuple’s elements can’t be reassigned.

For example, I’d use a list for records I’m collecting during processing and a tuple for a fixed pair of values.

Lists use square brackets, while tuples are commonly written with parentheses.”

### 9. What is the difference between a list and a dictionary?

“A list stores items in a sequence, so we usually access them by position. A dictionary stores key-value pairs, so we access information by its key.

For example, `customer[0]` depends on knowing what position zero means. `customer["name"]` tells us directly what we’re retrieving.

Lists suit sequences, while dictionaries are useful for named fields or lookups.”

### 10. What are the advantages of using a set?

“A set stores unique elements, so it’s useful for removing duplicates and checking membership.

For example, I could put customer IDs into a set to find the distinct IDs or check whether I’ve already processed one.

Sets also support operations like finding IDs shared between two datasets. They don’t provide positional access, so I wouldn’t use one when I need a sequence.”

## Dictionaries

### 11. How would you describe a dictionary to someone new to programming?

“A dictionary stores information using names, called keys, linked to values.

For example, a customer dictionary could contain `"name": "Sumiyya"` and `"city": "Bradford"`. I can then ask for the city using its key rather than remembering a position.

That makes dictionaries useful for representing records with clearly named fields.”

### 12. What are keys and values in a dictionary?

“The key identifies a piece of information, and the value is the information associated with it.

For example, in `{"city": "Bradford"}`, `"city"` is the key and `"Bradford"` is the value.

Values can also be collections. A customer dictionary could contain an `"orders"` key whose value is a list of their orders.”

### 13. Why are dictionary keys required to be unique?

“Each key needs to identify one value within that dictionary. Otherwise, looking up the key would be ambiguous.

For example, if I assign a new value to an existing `"city"` key, Python replaces the previous value rather than keeping two separate entries.

If one key needs several values, I can store those values in a list.”

### 14. In what business scenarios might dictionaries be useful?

“They’re useful for records and lookups where information has meaningful labels.

For example, I could represent a customer using keys for their ID, name and email. I could also map product codes to prices, so I can look up a price directly.

They’re common when working with APIs because JSON objects are normally parsed into Python dictionaries.”

### 15. What are some advantages of dictionaries over lists?

“Dictionaries let us access values using meaningful keys instead of positions, which can make the code clearer.

For example, `order["total"]` is easier to understand than relying on a particular list position. Dictionaries also generally provide efficient key lookups.

They aren’t always better than lists, though. I’d use a list when I need a sequence and a dictionary when I need a mapping.”

### 16. What types of values can be dictionary keys?

“Dictionary keys must be hashable, meaning they have a stable hash value that Python can use for lookups.

Common examples are strings, integers and tuples containing only hashable elements. Lists, dictionaries and sets can’t normally be keys because they’re mutable and unhashable.

In practice, I’d often use something clear and stable, like a customer ID.”

### 17. What happens if you access a dictionary key that doesn’t exist?

“Using square brackets raises a `KeyError` if the key is missing.

If a missing value is expected, I can use `get()` to return `None` or a default instead. For example, `customer.get("phone", "Not provided")`.

I’d choose based on the requirement: an optional phone number is different from a missing customer ID that the processing depends on.”

## Control Flow

### 18. What is control flow in programming?

“Control flow is the order in which a program runs its instructions.

Normally, Python works through statements in sequence, but conditions, loops and function calls can change that flow.

For example, in the IMDb task, the program loops through records and uses conditions to decide which movies should be included in the output.”

### 19. What is the purpose of an if statement?

“An `if` statement lets the program make a decision. It runs a block of code only when a condition is true.

For example, I could check whether a movie’s year is at least 2010 before adding it to the results.

That lets us apply rules rather than perform the same action on every record.”

### 20. When would you use if, elif and else together?

“I’d use them when there are several possible outcomes and I want to select one.

For example, I could classify stock as unavailable, low or sufficient. Python checks the conditions in order and runs the first matching branch. The `else` handles anything left over.

That order matters, especially if more than one condition could be true.”

### 21. What is the difference between a for loop and a while loop?

“A `for` loop goes through items in an iterable, such as a list or CSV reader. A `while` loop repeats while a condition remains true.

For example, I’d use `for` to process each record in a file. I might use `while` to keep requesting API pages until there are no more pages.

The choice depends on what controls the repetition.”

### 22. What are some risks associated with while loops?

“The main risk is that the condition never becomes false, so the loop doesn’t stop.

For example, an API loop could repeatedly request the same page if I forget to update the page number.

That can waste resources or send too many requests. I’d make sure the loop makes progress and consider limits, timeouts and error handling where appropriate.”

### 23. What is an infinite loop, and how can it happen?

“An infinite loop keeps running because it never reaches a stopping condition.

For example, if I write `while count < 5` but never increase `count`, the condition stays true.

Some programs deliberately run continuously, but accidental infinite loops are usually a bug. I’d check that the condition changes or that there’s a clear way to exit.”

### 24. What is the purpose of break?

“`break` immediately exits the nearest loop, even if more items remain or the loop’s condition is still true.

For example, in a prime checker, once I find a divisor, I know the number isn’t prime. I can stop checking rather than carry out unnecessary work.

After the loop ends, execution continues with the code after it.”

### 25. What is the purpose of continue?

“`continue` skips the remaining code in the current iteration and moves to the next one.

For example, if a record is missing a required field, I could record the issue and skip that record while continuing with the others.

I’d only do that if skipping is an agreed rule, so invalid records don’t disappear without explanation.”

### 26. What is the difference between break and continue?

“`break` stops the loop completely, while `continue` skips just the current iteration.

For example, if I’m searching for one order, I might use `break` once I find it. If I’m processing many orders and one is invalid, I might use `continue` after recording the problem.

So one ends the search; the other lets processing carry on.”

## Functions

### 27. What is a function?

“A function is a reusable block of code that performs a particular task. It can take inputs, carry out some processing and return a result.

For example, a function could receive movie records and return only the ones that meet our filtering rules.

Giving that task a clear name makes the program easier to follow.”

### 28. Why are functions useful?

“Functions help us reuse code, organise responsibilities and test behaviour separately.

For example, if several files need the same date-cleaning rule, I can call one function rather than copy the logic everywhere.

If the rule changes, I can update it in one place and test it without running the whole application.”

### 29. What is the difference between defining and calling a function?

“Defining a function tells Python what it should do when it’s used. Calling the function actually runs that behaviour.

For example, `def clean_data(records):` starts the definition. Later, `clean_data(customer_records)` calls it with particular data.

Defining it alone doesn’t run the function’s body.”

### 30. What are function parameters?

“Parameters are the names written in a function definition to receive inputs.

For example, in `def calculate_total(price, quantity):`, `price` and `quantity` are parameters.

They let the function work with different values each time it’s called instead of having those values fixed inside the code.”

### 31. What are function arguments?

“Arguments are the values we supply when calling a function.

For example, in `calculate_total(10, 3)`, the arguments are `10` and `3`. They’re passed into the function’s parameters.

We can also name them, such as `price=10` and `quantity=3`, which can make a call clearer.”

### 32. What is a return value?

“A return value is the result a function gives back to the code that called it.

For example, a function could return a list of cleaned records, which we store in a variable and pass to the loading stage.

The `return` statement also ends that function call. If a function finishes without returning a value explicitly, it returns `None`.”

### 33. Why is returning a value often more useful than printing it?

“Returning makes the result available for the rest of the program to use. Printing only displays it.

For example, if my transformation returns cleaned records, I can save them, test them or send them to another function.

If it only prints them, I can see the output, but the next stage hasn’t received those records.”

### 34. What are the benefits of breaking a large program into smaller functions?

“It makes the program easier to understand because each function can have a clear responsibility.

For example, extraction, transformation and loading can be separate functions. If the output is wrong, I can check each stage rather than work through one large block.

It also makes testing and changing individual parts easier.”

### 35. Can a function call another function? Why would you do that?

“Yes. One function can use another function’s result as part of its work.

For example, a transformation function could call a separate year-validation function before deciding whether to include a movie.

That lets us reuse smaller pieces of logic and keeps the main function focused on the overall task.”

## Understanding and Reasoning

### 36. What is the difference between a syntax error and a logical error?

“A syntax error means the code doesn’t follow Python’s grammar, such as a missing colon after an `if` statement.

A logical error means the code runs but produces the wrong behaviour. For example, using `year > 2010` instead of `year >= 2010` would incorrectly exclude movies from 2010.

Syntax errors are reported by Python, while logical errors often need tests or careful checking to find.”

### 37. Have you encountered bugs while learning Python? How did you identify and fix them?

“One example was my prime-checking exercise. I tried to run the code before defining the number it was supposed to check, so Python raised a `NameError`.

The error message pointed to the missing name. Once I defined `number` before the loop, that issue was resolved.

It reminded me to check the inputs and setup as well as the main logic, and to use the error message to narrow down the problem.”

### 38. What does DRY mean, and how do functions help?

“DRY means ‘Don’t Repeat Yourself’. The idea is to avoid maintaining the same logic in several places.

For example, if several datasets need the same validation rule, I can put it in a function and reuse it.

That reduces the chance of fixing one copy but forgetting another. I’d still make sure the logic really is shared before combining it.”

### 39. What makes code maintainable and easy to read?

“Clear names, consistent formatting and small functions with clear responsibilities all help. I’d also avoid unnecessary repetition and use comments to explain decisions that aren’t obvious.

For example, `filter_movies()` tells me more than `process_stuff()`.

Useful tests and clear error handling also make changes safer, especially when someone else needs to work on the code later.”

### 40. If you inherited someone else’s Python script, what would you look at first?

“I’d first work out its purpose, what inputs it expects and what output it produces. Then I’d find where execution starts and follow the main function calls.

I’d check the imports, configuration, tests and any external files, APIs or databases it uses.

Before running it, I’d check whether it changes or deletes anything. Then I’d use a safe environment and small inputs to confirm my understanding.”

---

[Back to Interview Prep](README.md)
