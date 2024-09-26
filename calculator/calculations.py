from typing import List
from calculator.calculation import Calculation

class Calculations:
    """A class to manage a history of mathematical calculations. It allows adding 
    calculations to the history, retrieving the last calculation, and clearing 
    the history"""

    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        """Get the latest calculation. Returns None if there's no history."""
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Gets the entire history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clears the calculation history"""
        cls.history.clear()