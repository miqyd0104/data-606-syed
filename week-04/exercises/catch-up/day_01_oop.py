"""A staff-pay example demonstrating all four OOP pillars."""
from abc import ABC, abstractmethod
from decimal import Decimal


class Employee(ABC):
    # Abstraction: every employee has a monthly_pay interface.
    def __init__(self, name):
        if not name.strip():
            raise ValueError('Name cannot be blank')
        self._name = name  # Encapsulation through a read-only public property.

    @property
    def name(self):
        return self._name

    @abstractmethod
    def monthly_pay(self):
        pass


class SalariedEmployee(Employee):
    # Inheritance: a salaried employee is an Employee.
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self._annual_salary = Decimal(str(annual_salary))
        if not self._annual_salary.is_finite() or self._annual_salary < 0:
            raise ValueError('Salary must be a finite non-negative amount')

    def monthly_pay(self):
        return (self._annual_salary / 12).quantize(Decimal('0.01'))


class HourlyEmployee(Employee):
    def __init__(self, name, rate, hours):
        super().__init__(name)
        self._rate = Decimal(str(rate))
        self._hours = Decimal(str(hours))
        if any(not value.is_finite() or value < 0 for value in [self._rate, self._hours]):
            raise ValueError('Rate and hours must be finite and non-negative')

    def monthly_pay(self):
        return (self._rate * self._hours).quantize(Decimal('0.01'))


def payroll(employees):
    # Polymorphism: the same call uses each employee's implementation.
    return [(employee.name, employee.monthly_pay()) for employee in employees]


if __name__ == '__main__':
    staff = [SalariedEmployee('Ada', 36000), HourlyEmployee('Alan', 20, 120)]
    for name, amount in payroll(staff):
        print(f'{name}: £{amount:.2f}')
