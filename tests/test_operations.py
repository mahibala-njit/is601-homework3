"""
This module contains unit tests for the arithmetic operations provided by 
the calculator.operations module. It includes tests for addition, 
subtraction, multiplication, and division, ensuring each function performs 
as expected. It also tests for correct handling of division by zero.
"""

# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, expected_result", [
    (Decimal('1'), Decimal('2'), Decimal('3')),  # Basic addition case
    (Decimal('5'), Decimal('3'), Decimal('8')),  # Another addition case
    (Decimal('0'), Decimal('0'), Decimal('0'))   # Edge case: adding zero
])
def test_add(a, b, expected_result):
    """Test the add function from the operations module."""
    assert add(a, b) == expected_result

@pytest.mark.parametrize("a, b, expected_result", [
    (Decimal('5'), Decimal('3'), Decimal('2')),  # Basic subtraction case
    (Decimal('3'), Decimal('2'), Decimal('1')),  # Another subtraction case
    (Decimal('0'), Decimal('0'), Decimal('0'))   # Edge case: subtracting zero
])
def test_subtract(a, b, expected_result):
    """Test the subtract function from the operations module."""
    assert subtract(a, b) == expected_result

@pytest.mark.parametrize("a, b, expected_result", [
    (Decimal('2'), Decimal('3'), Decimal('6')),  # Basic multiplication case
    (Decimal('0'), Decimal('5'), Decimal('0')),  # Edge case: multiplying by zero
    (Decimal('5'), Decimal('5'), Decimal('25'))  # Another multiplication case
])
def test_multiply(a, b, expected_result):
    """Test the multiply function from the operations module."""
    assert multiply(a, b) == expected_result

@pytest.mark.parametrize("a, b, expected_result", [
    (Decimal('6'), Decimal('2'), Decimal('3')),  # Basic division case
    (Decimal('0'), Decimal('5'), Decimal('0'))   # Edge case: dividing zero
])
def test_divide(a, b, expected_result):
    """Test the divide function from the operations module."""
    assert divide(a, b) == expected_result

def test_divide_by_zero():
    """Test the divide function to ensure it raises ZeroDivisionError 
    when dividing by zero."""
    with pytest.raises(ZeroDivisionError):
        divide(Decimal('1'), Decimal('0'))
