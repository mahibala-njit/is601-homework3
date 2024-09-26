"""
This module contains unit tests for the Calculations class, which manages 
a history of Calculation instances. The tests cover the following functionalities:
- Adding a calculation to the history
- Retrieving the last calculation from the history
- Retrieving the entire history
- Clearing the history

Each test ensures that the Calculations class behaves as expected in different scenarios.
"""

# pylint: disable=unnecessary-dunder-call, invalid-name
from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import add

def test_get_last_calculation_empty():
    """
    Test case for retrieving the last calculation when the history is empty.
    Ensures that `get_last_calculation` returns None when there are no calculations.
    """
    assert Calculations.get_last_calculation() is None

def test_add_calculation():
    """
    Test case for adding a new calculation to the history.
    Verifies that after adding a calculation, it becomes the last calculation in the history.
    """
    calc = Calculation.create(1, 2, add) # Create a calculation (1 + 2)
    Calculations.add_calculation(calc) # Add the calculation to the history
    assert Calculations.get_last_calculation() == calc  # Check if the last calculation in history is the one we just added

def test_get_history():
    """
    Test case for retrieving the history of calculations.
    Verifies that calculations are stored in the correct order and the length 
    of the history matches the number of added calculations.
    """
    # Clear the history to start fresh
    Calculations.clear_history()

    # Create two calculations
    calc1 = Calculation.create(1, 2, add)
    calc2 = Calculation.create(2, 3, add)

    # Add both calculations to the history
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)

    # Retrieve the history
    history = Calculations.get_history()

    assert len(history) == 2 # Assert that the history contains exactly 2 calculations
    assert history[0] == calc1 # Assert that the first calculation in the history is calc1
    assert history[1] == calc2 # Assert that the second calculation in the history is calc2

def test_clear_history():
    """
    Test case for clearing the calculation history.
    Ensures that after clearing the history, no calculations remain.
    """
    # Create a calculation and add it to the history
    calc = Calculation.create(1, 2, add)
    Calculations.add_calculation(calc)

     # Clear the history
    Calculations.clear_history()

    assert not Calculations.get_history() # Verify that the history is now empty
    