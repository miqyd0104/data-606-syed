# Object-Oriented Programming (OOP)

## OOP

### 1. What is Object-Oriented Programming?

“OOP is a way of organising code into objects that keep related data and behaviour together.

For example, a bank account object could hold a balance and have methods to deposit or withdraw money.

This helps us keep related responsibilities in one place, making the program easier to understand and maintain as it grows.”

### 2. What are the advantages of OOP compared to procedural programming?

“Procedural programming organises work around functions and steps. OOP organises it around objects that manage related data and behaviour.

For example, if we’re working with several bank accounts, each object can hold its own balance while sharing the same deposit and withdrawal methods.

That can make managing separate pieces of state easier. Both approaches support reusable code, though, so OOP isn’t automatically better.”

### 3. What is the difference between a class and an object?

“A class defines the attributes and methods a type of object will have. An object is a particular instance created from that class.

For example, a `BankAccount` class could define how accounts work. We could then create separate account objects for different customers, each with its own balance.

They share the same behaviour, but their information can be different.”

### 4. How do you create an object from a class?

“We call the class name with parentheses and supply any arguments it needs.

For example:”

```python
account = BankAccount("Sumiyya", 100)
```

“This creates a `BankAccount` object and assigns it to `account`. Assuming the class accepts those arguments, its initialisation code can store the account holder and opening balance.”

### 5. What is an instance of a class?

“An instance is a particular object created from a class. In this context, ‘object’ and ‘instance’ describe the same thing.

For example, if I create two bank accounts, they’re two instances of `BankAccount`. They use the same class definition but have their own identity and account details.”

### 6. What is the purpose of `__init__()`?

“`__init__()` sets up an object’s starting state after it has been created.

For example, when creating a bank account, we could use it to store the account holder and opening balance. We could also validate those values.

That means the object starts with the information it needs, rather than relying on someone to add everything afterwards.”

### 7. What does `self` represent?

“`self` refers to the particular object whose instance method is being called.

For example, inside a withdrawal method, `self.balance` means the balance belonging to that account. If we call the method on another account, it works with that account’s balance instead.

It lets objects share the same method while keeping their own state. `self` is the conventional name, rather than a reserved Python keyword.”

### 8. What is the difference between an attribute and a method?

“An attribute holds information, while a method provides behaviour.

For example, a bank account’s balance is an attribute. `deposit()` is a method that changes the balance.

In a data pipeline, the source file path could be an attribute, and `extract()` could be a method that reads the data.”

### 9. What is the difference between instance variables and class variables?

“Instance variables hold information for individual objects. Class variables are defined on the class and shared through it.

For example, each account would have its own balance, while a class variable could hold a bank name shared by the accounts.

We need to be careful with mutable class variables, like lists, because changing that shared list can affect multiple instances.”

### 10. How would you refactor procedural code into an OOP solution?

“I’d first look for related data and functions that belong together. Then I’d decide whether grouping them into a class would make the responsibilities clearer.

For example, if several extraction functions keep receiving the same source configuration, an extractor class could store that configuration and provide an `extract()` method.

I’d make the change in small steps and check that the behaviour stays the same. I wouldn’t turn every function into a class.”

### 11. When is OOP the wrong choice?

“OOP can be the wrong choice when it adds structure without making the problem easier to understand.

For example, a small script that reads a CSV, filters rows and saves the result may only need a few functions.

Adding several classes could make that simple process harder to follow. I’d use classes when managing related state and behaviour provides a clear benefit.”

## Encapsulation

### 1. What is encapsulation?

“Encapsulation means keeping related data and behaviour together and providing controlled ways to change that data.

For example, a bank account could use a withdrawal method that checks the amount and available balance before making a change.

That helps keep the account in a valid state instead of relying on every caller to remember the rules.”

### 2. Why is encapsulation important?

“It helps us apply rules consistently and reduce accidental changes.

For example, a pipeline’s batch size should be positive. If we validate it through a property or method, different parts of the program don’t each need to repeat that check.

The benefit is that invalid settings are caught where they’re assigned, rather than causing a confusing failure later.”

### 3. How does Python implement private attributes?

“Python mainly uses naming conventions rather than strictly enforced private access.

A single underscore, like `_balance`, signals that an attribute is intended for internal use. A double underscore, like `__balance`, triggers name mangling, which helps prevent accidental naming conflicts in subclasses.

These don’t make the data completely inaccessible. We can use methods and properties to provide a controlled interface, but underscores aren’t a security measure.”

## Inheritance

### 1. What is inheritance?

“Inheritance lets a child class reuse or extend behaviour from a parent class.

For example, a `SavingsAccount` could inherit shared account behaviour from `BankAccount`, then add interest-related behaviour.

It works best when the child really is a specialised type of the parent, so the relationship makes sense.”

### 2. Why is inheritance useful?

“Inheritance can keep shared behaviour in one place while allowing specialised classes to add what they need.

For example, different account types could share deposit behaviour but apply different withdrawal rules.

That can reduce duplication, although I’d avoid complicated inheritance chains. The child classes still need to behave consistently with what the parent’s users expect.”

### 3. What happens when a child class overrides a parent method?

“The child provides its own version of an inherited method. When that method is called on the child object, Python normally uses the child’s version.

For example, a savings account could override `withdraw()` to apply an additional rule.

The parent’s implementation still exists. The child can use `super()` to call it if it wants to extend the behaviour rather than replace it completely.”

## Polymorphism

### 1. What is polymorphism?

“Polymorphism means different objects can be used through the same interface while each provides its own behaviour.

For example, CSV and API extractors could both have an `extract()` method. One reads a file, while the other requests data from a service.

The pipeline can use either in the same way, as long as they return records in the format it expects.”

### 2. How does polymorphism improve code flexibility?

“It means the calling code doesn’t need separate instructions for every implementation.

For example, if a pipeline already works with objects that provide `extract()`, we could introduce another compatible extractor without changing the main processing logic.

That makes the system easier to extend and test. In Python, those objects don’t have to share a parent class, but they do need to meet the same expected contract.”

## Abstraction

### 1. What is abstraction?

“Abstraction means providing a clear way to use something without requiring the caller to manage all its internal steps.

For example, I can call an extractor’s `extract()` method without handling file opening, parsing and closing in the main pipeline.

I still need to know what inputs it expects and what it returns. Hiding the unnecessary detail makes the main code easier to follow.”

### 2. How is abstraction different from encapsulation?

“Abstraction focuses on making something simpler to use. Encapsulation focuses on keeping related state and behaviour together and controlling how that state changes.

For example, a bank account’s `withdraw()` method abstracts the steps involved in a withdrawal. Checking the amount and updating the balance through that method supports encapsulation.

Together, they make the account easier to use correctly without spreading its internal rules throughout the program.”

---

[Back to Interview Prep](README.md)
