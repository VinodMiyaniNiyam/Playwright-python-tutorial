# Task 18: Simple Calculator Function

def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    elif operator == '%':
        if b == 0:
            return "Error: Division by zero"
        return a % b
    else:
        return "Error: Invalid operator"

# Test Section
if __name__ == "__main__":
    # Test Case 1: Normal modulo division
    a1, b1, op1 = 20, 6, "%"
    res1 = calculator(a1, b1, op1)
    print(f"Test Case 1: {a1} {op1} {b1} = {res1} (Expected: 2)")
    
    # Test Case 2: Division by zero
    a2, b2, op2 = 5, 0, "/"
    res2 = calculator(a2, b2, op2)
    print(f"Test Case 2: {a2} {op2} {b2} = {res2} (Expected: Error: Division by zero)")
    
    # Test Case 3: Invalid operator
    a3, b3, op3 = 5, 5, "?"
    res3 = calculator(a3, b3, op3)
    print(f"Test Case 3: {a3} {op3} {b3} = {res3} (Expected: Error: Invalid operator)")
