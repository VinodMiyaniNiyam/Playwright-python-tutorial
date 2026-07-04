# Task 13: Module - mycalculator.py
# Topics: Creating and importing modules, functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None, "Error: Division by zero."
    return a / b, None

def power(a, b):
    result = 1
    if b >= 0:
        for _ in range(int(b)):
            result *= a
    else:
        for _ in range(int(-b)):
            result *= a
        result = 1 / result
    return result
