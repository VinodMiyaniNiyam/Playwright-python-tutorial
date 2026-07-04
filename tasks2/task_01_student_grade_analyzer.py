# Task 1: Student Grade Analyzer
# Topics: Branching, loops, functions, dictionaries

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"

def analyze_student(name, marks):
    # Validate marks
    for i in range(len(marks)):
        if marks[i] < 0 or marks[i] > 100:
            return None, f"Invalid mark {marks[i]} for subject {i+1}. Must be between 0 and 100."

    total = 0
    for m in marks:
        total += m

    percentage = total / len(marks)
    grade = calculate_grade(percentage)

    result = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade
    }
    return result, None

def print_report(result):
    print("=" * 40)
    print(f"  STUDENT REPORT CARD")
    print("=" * 40)
    print(f"  Name       : {result['name']}")
    print(f"  Marks      : {result['marks']}")
    print(f"  Total      : {result['total']}")
    print(f"  Percentage : {result['percentage']}%")
    print(f"  Grade      : {result['grade']}")
    print("=" * 40)

# Test Section
if __name__ == "__main__":
    # Test Case 1: Good student scoring A
    result1, err1 = analyze_student("Alice", [92, 88, 95, 90, 87])
    if err1:
        print(f"Test Case 1 Error: {err1}")
    else:
        print_report(result1)

    print()

    # Test Case 2: Average student scoring C
    result2, err2 = analyze_student("Bob", [65, 60, 70, 55, 62])
    if err2:
        print(f"Test Case 2 Error: {err2}")
    else:
        print_report(result2)

    print()

    # Test Case 3: Invalid mark
    result3, err3 = analyze_student("Charlie", [80, 110, 70, 60, 55])
    if err3:
        print(f"Test Case 3 Error: {err3}")
    else:
        print_report(result3)
