# Task 13: Module-Based Calculator (main file)
# Topics: Creating and importing modules, functions

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import mycalculator as calc

def run_calculator_tests():
    print("=" * 40)
    print("    MODULE-BASED CALCULATOR")
    print("=" * 40)

    # Test Case 1: Basic operations
    print("Test Case 1: Basic Operations")
    print(f"  10 + 5  = {calc.add(10, 5)}")
    print(f"  10 - 5  = {calc.subtract(10, 5)}")
    print(f"  10 * 5  = {calc.multiply(10, 5)}")
    result, err = calc.divide(10, 5)
    print(f"  10 / 5  = {result}")
    print(f"  2 ^ 8   = {calc.power(2, 8)}")
    print()

    # Test Case 2: Division by zero
    print("Test Case 2: Division by Zero")
    result, err = calc.divide(10, 0)
    print(f"  10 / 0  = {err}")
    print()

    # Test Case 3: Negative power
    print("Test Case 3: Negative Power")
    print(f"  2 ^ -2  = {calc.power(2, -2)}")

    print("=" * 40)

if __name__ == "__main__":
    run_calculator_tests()
