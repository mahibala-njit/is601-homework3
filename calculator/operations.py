from decimal import Decimal


def add(a: Decimal, b: Decimal) -> Decimal:
    """ Adds two Decimal numbers """
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """ Subtracts the second Decimal number from the first """
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """ Multiplies two Decimal numbers """
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """  Divides the first Decimal number by the second. Raises a ZeroDivisionError
    if the second number is zero"""
    
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b