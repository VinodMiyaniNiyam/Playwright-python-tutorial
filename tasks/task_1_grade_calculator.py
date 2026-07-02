# Task 1: Student Grade Calculator

def calculate_grade(marks):
    # Check if marks are outside the valid range [0, 100] or non-numeric
    if marks < 0 or marks > 100:
        return "Invalid"
    
    # Branching logic to determine the grade
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# Test Section
if __name__ == "__main__":
    # Test Case 1: Normal score in B range
    marks1 = 82
    result1 = calculate_grade(marks1)
    print(f"Test Case 1: Marks = {marks1} -> Grade = {result1} (Expected: B)")
    
    # Test Case 2: Score at the lower boundary of A range
    marks2 = 90
    result2 = calculate_grade(marks2)
    print(f"Test Case 2: Marks = {marks2} -> Grade = {result2} (Expected: A)")
    
    # Test Case 3: Out of bounds score
    marks3 = 105
    result3 = calculate_grade(marks3)
    print(f"Test Case 3: Marks = {marks3} -> Grade = {result3} (Expected: Invalid)")
