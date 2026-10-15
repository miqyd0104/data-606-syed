# Day 1 — Python control flow, functions and OOP

12 October 2026

[← Week 4](../README.md) · [Next notes: Testing, files and CSV pipelines](day-02-testing-files-and-csv-pipelines.md)

Today built on Friday's introduction to Python. We worked through control flow and function exercises, introduced lambda functions, and used classes to understand object-oriented programming. The afternoon finished with unit testing and the red–green–refactor cycle of test-driven development.

The main connection between these topics is organising logic so it can be understood, reused and tested. A data pipeline needs more than code that runs once: each part should have a clear job and behave predictably when the input changes.

## Interview practice and learning independently

The morning questions covered control flow, loops, dictionaries, functions and variables. A short definition is a useful start, but an interview answer should also explain why the concept matters and give an example I can discuss confidently.

For a technical answer, a useful structure is **purpose → explanation → example → result**. STAR is another option when describing experience: situation, task, action and result. Use work I have actually done rather than presenting a hypothetical example as experience.

When stuck, first identify the intended logic, try a small example, check the official documentation and discuss the problem with a colleague. The skill is not memorising every method; it is knowing how to find and use the right one. Short revision sessions before the morning questions can help with recall.

## Control flow and indentation

**Control flow** is the order in which a program's instructions run. Conditions choose between paths; loops repeat work; `return` finishes a function and supplies its result.

| Construct | Purpose |
| --- | --- |
| `if`, `elif`, `else` | Choose a branch according to conditions. |
| `for` | Take items from an iterable, such as a list, string or dictionary. |
| `while` | Repeat while a condition remains true. |
| `break` | Leave the innermost loop immediately. |
| `continue` | Skip the rest of this iteration and move to the next one. |
| `return` | Leave the current function, optionally returning a value. |

A `for` loop does not require the number of items to be known in advance. A `while` loop is useful when repetition depends on something changing, such as receiving valid input.

Python uses indentation to define blocks. A colon introduces the block, and the indented statements belong to it. Use four spaces per indentation level and avoid mixing tabs and spaces.

```python
numbers = [2, 5, 4, 34, 9, 2]

for number in numbers:
    if number % 2 == 0:
        print(number)

print("Finished")
```

The condition is checked for each number. Only even numbers are printed inside the loop; `Finished` is printed once afterwards. `%` is the remainder operator, so `number % 2 == 0` checks whether an integer divides evenly by two.

For ordinary Boolean conditions, Python uses lowercase `and`, `or` and `not`. It does not use `&&`, `||` or uppercase `AND`. The Boolean literals are `True` and `False`. `==` compares values; `=` assigns a value to a name.

### Count the items examined, not only the matches

One exercise asked for even numbers **within the first five elements**. This is different from finding the first five even numbers anywhere in the list.

```python
numbers = [2, 5, 4, 34, 9, 2]
counter = 1

for number in numbers:
    if counter > 5:
        break
    if number % 2 == 0:
        print(number)
    counter += 1
```

The output is `2`, `4`, `34`. The final `2` is the sixth element, so it is excluded.

The demonstration initially incremented the counter inside the even-number condition. That counted matches rather than all elements examined. Moving the increment back one indentation level fixed the logic.

For a list, a shorter equivalent is:

```python
for number in numbers[:5]:
    if number % 2 == 0:
        print(number)
```

The longer version helps explain the control flow; the slice expresses the limit directly. `break` is a normal Python feature, not inherently bad practice. Choose the version that makes the stopping condition clear. See [Python's control flow guide](https://docs.python.org/3/tutorial/controlflow.html).

## Strings, lists and sets

A string is a sequence of characters. Spaces count as characters, and indexing starts at zero. Python has no separate built-in character type: indexing a string returns another string containing one character.

```python
name = "Ada Lovelace"

print(name[0])             # A
print(name[0:2])           # Ad
print(name.index(" "))    # 3
print(name[4:])            # Lovelace
```

In `text[start:stop]`, the start is included and the stop is excluded. Omitting the start means beginning at the start; omitting the stop means continuing to the end.

### Build a list of initials

The exercises asked for a list of first initials, a list of space positions, and then first-and-last initials. Printing individual characters does not satisfy a request to create a list.

```python
names = ["Ada Lovelace", "Alan Turing", "Grace Hopper"]
first_initials = []
space_positions = []
initials = []

for name in names:
    space_index = name.index(" ")
    first_initials.append(name[0])
    space_positions.append(space_index)
    initials.append(name[0] + name[space_index + 1])

print(first_initials)     # ['A', 'A', 'G']
print(space_positions)   # [3, 4, 5]
print(initials)          # ['AL', 'AT', 'GH']
```

`append()` adds one item to the end of a list. Joining strings with `+` is **concatenation**. These examples assume nonempty names containing a first name, one separating space and a surname. `index(" ")` raises `ValueError` if no space exists; real names may need a different rule.

### Find lists without duplicates

A set stores distinct, hashable values. For a list of simple strings or numbers, compare its length with the length of a set made from it:

```python
groups = [[1, 2, 3], [1, 1, 2], ["red", "blue"]]
without_duplicates = []

for group in groups:
    if len(group) == len(set(group)):
        without_duplicates.append(group)

print(without_duplicates)  # [[1, 2, 3], ['red', 'blue']]
```

Keep the original list in the result so its order and type are preserved. This technique does not directly work for lists containing unhashable values such as other lists or dictionaries. Print the final collection after the loop if the requirement is one completed result.

## User input and conversion

`input()` returns a string even when the user types digits. Before comparing input numerically, convert it to an appropriate numeric type and decide what should happen for invalid input.

The class used `isdigit()` as an initial check. This is useful for simple digit strings, but it rejects signs and decimal points and is not a general guarantee that `int()` will accept every Unicode digit character. Tuesday's exception handling provides a more direct way to handle conversion failures.

This version deliberately accepts only ordinary, unsigned whole numbers:

```python
waiting = True

while waiting:
    text = input("Enter a whole number greater than 100: ").strip()
    if not (text.isascii() and text.isdigit()):
        print("Please enter digits only.")
        continue

    number = int(text)
    if number > 100:
        waiting = False
        print(number)
    else:
        print("The number must be greater than 100.")
```

The boundary matters: “greater than 100” means `> 100`; “at least 100” means `>= 100`. Match the requirement exactly. When changing validation, rerun earlier working cases as well as the new invalid cases. This checks for **regressions**: behaviour that worked before but was broken by a change.

## Functions and reusable logic

A function is a reusable block of code defined with `def`. Parameters are the names in its definition; arguments are the values supplied when calling it.

```python
def divisors(number: int) -> list[int]:
    result = []
    for candidate in range(1, number + 1):
        if number % candidate == 0:
            result.append(candidate)
    return result

print(divisors(12))  # [1, 2, 3, 4, 6, 12]
```

This version assumes a positive integer. `range(1, number + 1)` includes the number itself because the upper endpoint is excluded. `return result` belongs inside the function but outside the loop: returning inside the loop would stop too early.

Defining a function does not run its body. Calling `divisors(12)` runs it. The returned list can then be printed, checked, passed to another function or stored for later use.

### Print and return are different

| `print(value)` | `return value` |
| --- | --- |
| Displays something for a person to see. | Supplies a result to the caller. |
| Useful for inspecting progress. | Useful for composing functions and testing results. |
| Does not make the printed value the function's result. | Ends the current function call. |

A function that reaches its end without returning a value returns `None`. This explains the extra `None` seen later when wrapping a method that already prints in another `print()` call.

### Type hints describe the contract

In the example, `number: int` describes the expected argument and `-> list[int]` describes the expected result. These are **type hints**. Python does not automatically reject a wrong argument or return type just because of an annotation. Editors and type-checking tools can flag mismatches; runtime validation must be implemented separately. See [Python's typing documentation](https://docs.python.org/3/library/typing.html).

A misspelt variable that is not defined usually causes `NameError`, rather than `SyntaxError`. A missing colon is a syntax problem. Distinguishing these helps when reading error messages.

### Reuse one function inside another

The factor exercise checked whether either positive integer was a factor of the other:

```python
def is_factor(first: int, second: int) -> bool:
    return first in divisors(second) or second in divisors(first)

print(is_factor(9, 36))  # True
print(is_factor(9, 7))   # False
```

This reuses the existing divisor logic. A more specific function could instead answer only “is the first number a factor of the second?”; make that direction clear in the name or documentation.

### Alphabet positions and the ID exercise

The alphabet exercise used indexing and lowercase conversion. For this zero-based version, `a` is 0, `b` is 1 and `t` is 19. Add one only if the requirement specifies positions 1–26.

```python
def alphabet_position(letter: str) -> int:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = letter.lower()
    if len(letter) != 1 or letter not in alphabet:
        raise ValueError("Expected one letter from A to Z")
    return alphabet.index(letter)


def id_generator(name: str) -> str:
    if not name:
        raise ValueError("Name must not be empty")
    result = ""
    for letter in name:
        result += str(alphabet_position(letter))
    return result


def exercise_password(name: str) -> int:
    identifier = id_generator(name)
    total = 0
    for digit in identifier:
        total += int(digit)
    return int(identifier) - total


print(id_generator("Bob"))       # '1141'
print(exercise_password("Bob"))  # 1134
```

`raise ValueError(...)` deliberately rejects input that does not meet the function's rule; error handling is covered next day. This example accepts names made only of A–Z letters. It illustrates string-to-number conversion and combining functions. Concatenated alphabet positions are not guaranteed to be unique, and this predictable classroom “password” calculation is not a real password-generation method.

### Check whether a number is prime

A prime is an integer greater than one with exactly two positive divisors: one and itself.

```python
def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for candidate in range(2, number):
        if number % candidate == 0:
            return False
    return True

print(is_prime(1))    # False
print(is_prime(2))    # True
print(is_prime(101))  # True
print(is_prime(100))  # False
```

The early `False` handles 0, 1 and negative integers, which a loop-only version can accidentally call prime. Finding one divisor is enough to stop. Returning `True` happens only after all candidates have been checked. For larger inputs, checking up to the square root is sufficient, but the full range makes the introductory logic easier to follow.

## Lambda functions and map

A **lambda** creates a small anonymous function using one expression. It can take multiple arguments and returns the expression's value automatically.

```python
def add(first, second):
    return first + second

print((lambda first, second: first + second)(2, 3))  # 5

savings = [100, 200, 500]
with_bonus = list(map(lambda amount: amount * 1.1, savings))
print([round(amount, 2) for amount in with_bonus])   # [110.0, 220.0, 550.0]
```

`map()` applies the supplied function to successive items. In Python 3, it returns an iterator; `list()` consumes that iterator and collects the results. The original `savings` list is unchanged. Floating-point arithmetic can display tiny representation differences, hence the rounding for display here.

Lambdas are useful for short transformations and sort keys. A normal `def` is clearer when logic needs multiple steps, validation or a descriptive reusable name. Merely using functions does not automatically make a program “functional programming”; Python supports several programming styles.

## Object-oriented programming

**Object-oriented programming (OOP)** organises related data and behaviour into objects. A class describes the kind of object; each instance has its own identity and can hold its own state.

I used a car as a real-world example: it can travel and accelerate. The distinction we developed was **state** — what it has, such as colour or mileage — and **behaviour** — what it can do, such as accelerate or brake.

| Term | Meaning |
| --- | --- |
| Class | The definition or blueprint for a type of object. |
| Object / instance | A particular object created from a class. |
| Attribute | Data associated with an object, such as its name. |
| Method | Behaviour accessed through an object or class. |
| Instantiation | Creating an instance. |
| Initialisation | Setting up that instance's starting state. |
| `self` | The conventional name for the current instance in an instance method. |

### Create and use a class

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} barked"


dog_one = Dog("Luna")
dog_two = Dog("Lassie")

print(dog_one.name)      # Luna
print(dog_two.bark())    # Lassie barked
print(type(dog_one))     # <class '__main__.Dog'> when run as a script
print(dog_one is dog_two)  # False
```

Both dogs use the same class, but they are separate instances. `dog_one` is a name referring to an object; assigning `another_name = dog_one` would refer to the same dog, not create a copy.

Calling a class normally creates and initialises an instance. More precisely, `__new__` creates it and `__init__` initialises it. `__init__` need not be the first method in the file. `self` is a naming convention, not a reserved keyword. Class names conventionally use `CapWords`; functions and modules use `snake_case`.

Python fully supports OOP. Different privacy conventions from Java do not make it “not real OOP”. See [Python's classes tutorial](https://docs.python.org/3/tutorial/classes.html).

Printing a custom object without a custom string representation usually shows its type and an identity-related representation. That is not a persistent database ID or a value to rely on between runs. Printing an attribute such as `dog_one.name` is more useful here.

## The four pillars of OOP

### Abstraction: use an interface without knowing every detail

A caller can ask an object to perform a task without managing all its internal steps. In a pipeline, `extract_movies(filename)` can hide the details of opening and parsing a CSV.

The class demonstration put definitions in their own modules and used a controller to create objects and call methods:

```python
# controller.py, with Dog defined in dog.py
from dog import Dog

dog = Dog("Luna")
print(dog.bark())
```

Separating files helps organisation, but abstraction is about the interface and hidden complexity, not a rule that every class must have its own file. Explicit imports also make dependencies easier to see than `from module import *`.

### Inheritance: share behaviour through an is-a relationship

The lesson used `Animal → Reptile → Snake → Python` as a hierarchy. A subclass can reuse or extend behaviour from a superclass.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} eats food"


class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.cold_blooded = True


class Snake(Reptile):
    def use_tongue(self):
        return "Sensing the surroundings"


class Python(Snake):
    def eat(self):
        return f"{self.name}: yum, yum, yum"


animals = [Animal("Cathy"), Reptile("Jeremy"), Snake("Samantha"), Python("Patricia")]
for animal in animals:
    print(animal.eat())
```

`class Reptile(Animal)` establishes inheritance. `super().__init__(name)` runs inherited initialisation for the same object; it does not create a separate animal inside the reptile. If a subclass supplies its own `__init__`, call the base initialiser when its setup is required. A subclass without its own initialiser can inherit one, as `Snake` does here.

When the base initialiser requires a name, the relevant subclass calls must supply it too. `super()` follows Python's method resolution order; in this simple hierarchy, that means progressing through the parent classes.

### Encapsulation: manage state through a controlled interface

Encapsulation groups data with the operations that manage it. A setter can check a new value before changing the object's state; a getter retrieves it.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value


employee = Employee("Alex", 30000)
employee.salary = 32000
print(employee.salary)  # 32000
```

The initial assignment also goes through the setter. This example assumes a numeric salary; the validation shown is specifically for negative values. A property without a setter can expose a read-only interface.

Python's naming rules need care:

- `name` is an ordinary public attribute.
- `_name` signals a non-public implementation detail by convention. Python does not enforce a package-level “protected” boundary.
- `__name` triggers **name mangling**, mainly to avoid accidental clashes in subclasses. It is still accessible through its mangled name; it is not security or strict privacy.

An editor warning is not a Python runtime restriction. Getters, setters and underscores do not by themselves implement authentication or access control. See [Python's private variable explanation](https://docs.python.org/3/tutorial/classes.html#private-variables).

### Polymorphism: one operation, different implementations

In the animal example, every item responds to `eat()`. The `Python` subclass overrides that method, so the same loop calls its different implementation. The others inherit the existing behaviour.

A professional example is calculating weekly pay: a player, coach and manager may all expose `weekly_pay()`, with different bonus rules. Different employees merely having different names or salaries is not, by itself, the behaviour-based polymorphism demonstrated here.

Python lists can hold different types, and a common superclass is not required for every form of polymorphism. What matters to the calling code is that each object supports the operation it needs.

## DRY, simplicity and choosing a structure

**DRY — Don't Repeat Yourself** encourages keeping a piece of logic in one place. **KISS — Keep It Simple** encourages clear, focused implementations. Functions and classes can help, but adding classes or a separate file for every tiny operation is not automatically an improvement.

For data work, ask what each part is responsible for: reading data, applying a business rule, representing a record or writing the result. Keep those responsibilities understandable and testable.

## Unit testing and test-driven development

A **unit test** checks a small piece of behaviour, often a function, against an expected result. An integration test checks how components work together. A **test suite** is a collection of tests that can be rerun, including after changes to check for regressions.

**Test-driven development (TDD)** is a development practice in which a test drives the next small change:

1. **Red:** write a test for the next behaviour and confirm it fails for the expected reason.
2. **Green:** write enough implementation to make it pass.
3. **Refactor:** improve the structure without changing the required behaviour, then rerun the tests.

The class used a function intended to return the numbers 1–100. A first test checking only that the first element is 1 can be passed by returning `[1]`. That is a temporary step, not the completed solution. Further tests must establish the remaining requirements, such as the full sequence and endpoint.

The temperature-conversion worksheet used the same approach: begin with a known input and expected result, then add cases until a general conversion is needed. Keep implementation and test code in separate files so the tests remain available.

Passing tests gives evidence for the cases checked, not proof that all possible inputs work. A test failure can also come from a mistaken expected result or setup, so investigate both the implementation and the test.

## Practice to consolidate

The work set for the afternoon was to build an example demonstrating all four OOP pillars, work through the testing worksheet and continue the lambda exercises. Bank accounts, staff records and football-club data were suggested as examples that can be explained in a professional context.

Before moving on, I should be able to:

- Trace a loop and explain which indentation level each statement belongs to.
- Explain the difference between printing a value and returning it.
- Build and call a function, including what happens for boundary inputs.
- Explain class, object, attribute, method, `self` and `__init__` using one example.
- Distinguish abstraction, inheritance, encapsulation and polymorphism.
- Describe red–green–refactor and why earlier tests are kept and rerun.
