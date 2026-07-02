# Task 14: Print Right Triangle Pattern

def print_triangle(n):
    result = ""
    for i in range(1, n + 1):
        row = ""
        for _ in range(i):
            row += "*"
        print(row)
        result += row
        if i < n:
            result += "\n"
    return result

# Test Section
if __name__ == "__main__":
    # Test Case 1: Print 4 rows
    rows1 = 4
    print(f"Test Case 1: Rows = {rows1}")
    print_triangle(rows1)
    print()
    
    # Test Case 2: Print 2 rows
    rows2 = 2
    print(f"Test Case 2: Rows = {rows2}")
    print_triangle(rows2)
