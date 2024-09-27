"""
This module contains tests for the calculator operations and Calculation class.
The tests are designed to verify the correctness of basic arithmetic operations.
"""


# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('5'), Decimal('5'), add, Decimal('10')),  # Test addition
    (Decimal('9'), Decimal('4'), subtract, Decimal('5')),  # Test subtraction
    (Decimal('6'), Decimal('7'), multiply, Decimal('42')),  # Test multiplication
    (Decimal('4'), Decimal('2'), divide, Decimal('2')),  # Test division
    (Decimal('1.5'), Decimal('0.5'), add, Decimal('2.0')),  # Test addition with decimals
    (Decimal('8.2'), Decimal('0.5'), subtract, Decimal('7.7')),  # Test subtraction with decimals
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),  # Test multiplication with decimals
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),  # Test division with decimals
])
def test_calculation_operations(a, b, operation, expected):
    """
    Test calculation operations with various scenarios.
    """
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ZeroDivisionError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calc.perform()

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('-5'), Decimal('5'), add, Decimal('0')),  # Test negative + positive
    (Decimal('-10'), Decimal('-5'), subtract, Decimal('-5')),  # Test subtraction with negatives
    (Decimal('3'), Decimal('-2'), multiply, Decimal('-6')),  # Test multiplication with one negative
    (Decimal('-10'), Decimal('-2'), divide, Decimal('5')),  # Test division with negatives
])
def test_calculation_with_negative_numbers(a, b, operation, expected):
    """
    Test calculation with negative numbers to ensure correct behavior.
    """
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('0'), Decimal('5'), add, Decimal('5')),  # Test zero + positive
    (Decimal('5'), Decimal('0'), subtract, Decimal('5')),  # Test positive - zero
    (Decimal('0'), Decimal('0'), multiply, Decimal('0')),  # Test zero * zero
    (Decimal('0'), Decimal('10'), divide, Decimal('0')),  # Test zero divided by non-zero
])
def test_calculation_with_zero(a, b, operation, expected):
    """
    Test calculation with zero as one or both operands.
    """
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected

def test_invalid_operator():
    """Test that an invalid operator raises an exception."""
    # Pass an invalid operator (None) to trigger an exception
    with pytest.raises(TypeError):
        calc = Calculation(Decimal('10'), Decimal('9'), None)
        calc.perform()
