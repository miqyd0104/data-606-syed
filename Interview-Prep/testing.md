# TDD & Unit Testing

### 1. What is the `unittest` library?

“`unittest` is a testing framework included with Python. It gives us tools to organise tests, check results and run them automatically.

We normally write tests inside a class that inherits from `unittest.TestCase`.

For example, I could test that a price-calculation function returns the correct total. Having that test means I can check the behaviour again whenever I change the code.”

### 2. What is the `pytest` library?

“Pytest is an external Python testing framework that we install separately. It lets us write tests as ordinary functions and check results using `assert`.

It also provides features like fixtures for reusable setup and parametrisation for testing several inputs.

For example, I could test several release years against my movie-filtering rule without writing a separate test function for each year.”

### 3. Why do test files often start with `test_`?

“It follows a naming convention that helps testing tools discover the tests automatically.

For example, `test_transform.py` clearly identifies a file containing transformation tests. Both unittest’s default discovery and pytest recognise filenames starting with `test_`, although their discovery rules differ slightly.

That makes it easier to run the test suite without listing every file manually.”

### 4. What assertion methods are available in `unittest`?

“Unittest provides different assertion methods depending on what we need to check. Common ones include:

- `assertEqual()` — checks that values are equal.
- `assertTrue()` and `assertFalse()` — check whether a condition is true or false.
- `assertIsNone()` — checks for `None`.
- `assertIn()` — checks that something is present in a collection.
- `assertAlmostEqual()` — compares numerical values approximately.
- `assertRaises()` — checks for an expected exception.

For example, I could use `assertEqual()` to compare the transformed records with the output I expected.”

### 5. How do assertions work in `pytest`?

“In pytest, we normally use Python’s `assert` statement to express what should be true.

For example:”

```python
assert calculate_total(10, 3) == 30
```

“If the condition is false, the test fails. Pytest gives us details about the failed comparison, which helps us see what went wrong.

The important part is choosing an expected result that checks the requirement properly.”

### 6. Why should unit tests focus on one piece of functionality?

“It makes failures easier to understand. If a test checks one clear behaviour, we can usually identify the problem quickly when it fails.

For example, I’d test the year-filtering rule separately from writing the output file. Otherwise, a failure could come from either part.

That doesn’t mean every test must have exactly one assertion—the assertions should support the same behaviour.”

### 7. How would you test that a function raises an exception?

“I’d call the function with an input that should cause a particular exception, and check that the expected exception is raised.

For example, if negative quantities aren’t allowed, I’d pass a negative quantity and expect `ValueError`.

With pytest, I can write:”

```python
import pytest

with pytest.raises(ValueError):
    calculate_total(price=10, quantity=-1)
```

“In unittest, I’d use `with self.assertRaises(ValueError):`. That checks the function rejects the input in the way we intended.”

### 8. Why should exceptions be tested?

“Handling invalid situations is part of the function’s behaviour, so it needs testing too.

For example, a function might correctly process valid years but crash unexpectedly when it encounters missing data.

Testing the expected exception helps confirm that it fails clearly and predictably, rather than silently producing an incorrect result or raising an unrelated error.”

### 9. What types of errors should be covered by tests?

“I’d cover the failures that are relevant to the requirements: invalid values, missing information, boundary cases and expected dependency failures.

For example, a transformation might receive an invalid year or a missing required column. A file reader might encounter a missing file, and an API client might receive an unsuccessful response.

I’d also test that valid input produces the right output, because some logical errors don’t raise exceptions at all.”

### 10. How would you test a function that reads a file that may not exist?

“I’d use a controlled temporary location and pass a path to a file that doesn’t exist.

Then I’d check the behaviour we’ve agreed on. If the function should raise `FileNotFoundError`, I’d assert that. If it should return a particular result, I’d check that instead.

I’d also test an existing temporary file with known contents. That covers both successful reading and the missing-file case without relying on files on my own computer.”

### 11. What is Test-Driven Development?

“Test-Driven Development, or TDD, means writing a test for a small piece of behaviour before implementing it.

I first describe the expected result in a test, see it fail, then write enough code to make it pass. After that, I improve the code while keeping the tests passing.

It helps me stay focused on the requirement and get feedback as I build.”

### 12. What are the three stages of the TDD cycle?

“The three stages are Red, Green and Refactor.

Red means writing a test and checking that it fails for the expected reason. Green means implementing enough code to pass it. Refactor means improving the code’s structure without changing its behaviour.

We repeat that cycle for the next small requirement.”

### 13. What is meant by “Red, Green, Refactor”?

“It describes building behaviour in small, checked steps.

For example, I could write a test saying that a movie from 2009 should be excluded. That’s Red until I implement the filtering rule. Once it passes, that’s Green. I can then tidy the filtering code and rerun the tests—that’s Refactor.

The idea is to improve the design while protecting the behaviour we’ve already checked.”

### 14. Why is the failing test written first in TDD?

“It helps confirm that the test can detect the behaviour we haven’t implemented yet.

For example, if my filtering test passes before the filtering exists, I’d question whether the test is checking the right thing.

Seeing it fail for the expected reason, then pass after the change, gives me more confidence that the test is useful. It also makes me clarify the expected behaviour before writing the implementation.”

### 15. How would TDD help when developing a data transformation pipeline?

“I’d break the transformation requirements into small rules and test them one at a time.

For the IMDb task, I could start by testing that non-movies are excluded. Then I’d test that 2010 is included, 2009 is excluded and missing years are handled correctly.

That gives me quick feedback while building the transformation. Later, if I change a rule, I can rerun the tests to check that the other behaviour still works. I’d also need integration tests to check the pipeline stages work together.”

---

[Back to Interview Prep](README.md)
