# Task 20: Mini Project - Student Management System
# Topics: All covered topics (dicts, datetime, functions, modules)

import datetime

students = {}

def calculate_age(dob_str):
    try:
        dob   = datetime.datetime.strptime(dob_str.strip(), "%d-%m-%Y").date()
        today = datetime.date.today()
        age   = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age, None
    except ValueError:
        return None, "Invalid DOB format. Use DD-MM-YYYY."

def validate_mobile(mobile):
    mobile = mobile.strip()
    if len(mobile) != 10:
        return False
    for ch in mobile:
        if not ch.isdigit():
            return False
    return True

def add_student(roll, name, dob, mobile, course):
    if roll in students:
        return False, f"Roll number {roll} already exists."
    if not validate_mobile(mobile):
        return False, "Mobile must be exactly 10 digits."
    age, err = calculate_age(dob)
    if err:
        return False, err
    students[roll] = {
        "roll":   roll,
        "name":   name.strip(),
        "dob":    dob.strip(),
        "mobile": mobile.strip(),
        "course": course.strip(),
        "age":    age
    }
    return True, f"Student '{name}' added with Roll No: {roll}"

def search_student(query):
    query = query.strip().lower()
    results = []
    for roll, info in students.items():
        if (query in info["name"].lower() or
            query == str(roll).lower() or
            query in info["course"].lower()):
            results.append(info)
    return results

def update_student(roll, mobile=None, course=None):
    if roll not in students:
        return False, f"Roll No {roll} not found."
    if mobile:
        if not validate_mobile(mobile):
            return False, "Mobile must be exactly 10 digits."
        students[roll]["mobile"] = mobile
    if course:
        students[roll]["course"] = course
    return True, f"Student Roll No {roll} updated."

def delete_student(roll):
    if roll in students:
        name = students[roll]["name"]
        del students[roll]
        return True, f"Student '{name}' deleted."
    return False, f"Roll No {roll} not found."

def view_all_students():
    if not students:
        print("  No students found.")
        return
    print("=" * 65)
    print("    ALL STUDENTS")
    print("=" * 65)
    print(f"  {'Roll':<6} {'Name':<20} {'DOB':<12} {'Mobile':<12} {'Course':<12} {'Age'}")
    print("-" * 65)
    for roll, info in students.items():
        print(f"  {info['roll']:<6} {info['name']:<20} {info['dob']:<12} {info['mobile']:<12} {info['course']:<12} {info['age']}")
    print("=" * 65)

# Test Section
if __name__ == "__main__":
    # Test Case 1: Add Students
    print("Test Case 1: Add Students")
    print(add_student(101, "Vinod Miyani",  "15-08-2000", "9876543210", "BCA")[1])
    print(add_student(102, "Priya Sharma",  "22-03-1999", "8765432109", "MCA")[1])
    print(add_student(103, "Rahul Gupta",   "10-11-2001", "7654321098", "BCA")[1])
    print(add_student(104, "Anita Singh",   "05-07-2000", "6543210987", "BSc")[1])
    print()

    # Test Case 2: View all students
    print("Test Case 2: View All Students")
    view_all_students()
    print()

    # Test Case 3: Search student
    print("Test Case 3: Search 'bca'")
    results = search_student("bca")
    for r in results:
        print(f"  Roll {r['roll']}: {r['name']} - {r['course']}")
    print()

    # Test Case 4: Age calculation
    print("Test Case 4: Age Calculation")
    for roll, info in students.items():
        age, _ = calculate_age(info["dob"])
        print(f"  {info['name']}: {age} years old")
    print()

    # Test Case 5: Update and delete
    print("Test Case 5: Update and Delete")
    ok, msg = update_student(102, mobile="9999999999")
    print(f"  Update: {msg}")
    ok, msg = delete_student(104)
    print(f"  Delete: {msg}")
    view_all_students()
