"""
This module contains unit tests for the Calculator class, which provides
methods for basic arithmetic operations: addition, subtraction, multiplication,
and division. The tests validate the expected outcomes for each operation 
using parameterized inputs and ensure that appropriate exceptions are raised 
when necessary, such as in the case of division by zero.
"""

# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator import Calculator

@pytest.mark.parametrize("a, b, expected_result", [
    (Decimal('1'), Decimal('2'), Decimal('3')),  # Test case for addition
    (Decimal('5'), Decimal('3'), Decimal('8'))   # Additional test case for addition
])
def test_add(a, b, expected_result):
    """Test the addition method of the Calculator class."""
    assert Calculator.add(a, b) == expected_result

@pytest.mark.parametrize("a, b, expected_result", [
    (Decimal('5'), Decimal('3'), Decimal('2')),  # Test case for subtraction
    (Decimal('3'), Decimal('2'), Decimal('1'))   # Additional test case for subtraction
])
def test_subtract(a, b, expected_result):
    """Test the subtraction method of the Calculator class."""
    assert Calculator.subtract(a, b) == expected_result

@pytest.mark.parametrize("a, b, expected_result", [
    (Decimal('2'), Decimal('3'), Decimal('6')),  # Test case for multiplication
    (Decimal('0'), Decimal('5'), Decimal('0'))   # Edge case for multiplication with zero
])
def test_multiply(a, b, expected_result):
    """Test the multiplication method of the Calculator class."""
    assert Calculator.multiply(a, b) == expected_result

@pytest.mark.parametrize("a, b, expected_result", [
    (Decimal('6'), Decimal('2'), Decimal('3')),  # Test case for division
    (Decimal('0'), Decimal('5'), Decimal('0'))   # Edge case for division resulting in zero
])
def test_divide(a, b, expected_result):
    """Test the division method of the Calculator class."""
    assert Calculator.divide(a, b) == expected_result

def test_divide_by_zero():
    """Test the division method of the Calculator class to ensure it raises 
    ZeroDivisionError when attempting to divide by zero."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(Decimal('1'), Decimal('0'))
