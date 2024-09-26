
from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    """A class to represent a mathematical calculation that encapsulates two operands 
    and an operation (such as addition, subtraction, etc.)"""

    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Initializes a Calculation object with two operands and an operation"""
        self.a = a
        self.b = b
        self.operation = operation
    
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Static method to create a new Calculation instance"""
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        """Executes the operation stored in this Calculation object on the two operands"""
        return self.operation(self.a, self.b)

    def __repr__(self):
        """Returns a string representation of the Calculation object"""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"