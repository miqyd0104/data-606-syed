"""Small functions for the testing exercises."""


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def divide(first, second):
    if second == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return first / second
