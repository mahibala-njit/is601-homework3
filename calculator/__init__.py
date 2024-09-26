from calculator.calculations import Calculations 
from calculator.operations import add, subtract, multiply, divide  
from calculator.calculation import Calculation 
from decimal import Decimal 
from typing import Callable 

class Calculator:
    """A simple calculator class providing static methods to perform basic arithmetic operations."""

    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result """
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Add two Decimal numbers"""
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Subtract the second Decimal number from the first"""
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Multiply two Decimal numbers"""
        return Calculator._perform_operation(a, b, multiply)
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Divide the first Decimal number by the second"""
        return Calculator._perform_operation(a, b, divide)
