# Homework 3

# Calculator Project

This project is a simple calculator implemented in Python that performs basic arithmetic operations: addition, subtraction, multiplication, and division. The calculator is designed using object-oriented principles and showcases various design patterns, including class methods, static methods, and a calculation history feature.

## Features

- Perform basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division (with error handling for division by zero)
- Store a history of calculations
- Retrieve the last calculation
- Clear the calculation history
- Uses `Decimal` for high-precision arithmetic

## Install Instructions

1. Clone
2. Install the requirements
```bash
pip3 install -r requirments.txt
```

## Testing
This project includes extensive unit tests for each feature and operation. Testing is done using the pytest framework, and code linting is handled by pylint to ensure code quality.

The project has been fully tested, with 100% code coverage.

```bash
pytest
pytest --pylint
pytest --pylint --cov
```