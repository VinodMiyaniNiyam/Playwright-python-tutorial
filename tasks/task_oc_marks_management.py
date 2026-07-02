# Optional Challenge: Marks Management System

def add_student(names_list, marks_list, name, mark):
    names_list.append(name)
    marks_list.append(mark)
    return True

def show_students(names_list, marks_list):
    # Get list length manually
    length = 0
    for _ in names_list:
        length += 1
        
    if length == 0:
        return "No records found."
        
    result = "Student Records:\n"
    for i in range(length):
        result += f"- {names_list[i]}: {marks_list[i]}"
        if i < length - 1:
            result += "\n"
    return result

def find_highest_marks(names_list, marks_list):
    # Get list length manually
    length = 0
    for _ in marks_list:
        length += 1
        
    if length == 0:
        return None, None
        
    highest_idx = 0
    highest_val = marks_list[0]
    for i in range(1, length):
        if marks_list[i] > highest_val:
            highest_val = marks_list[i]
            highest_idx = i
            
    return names_list[highest_idx], highest_val

def calculate_class_average(marks_list):
    # Get list length manually
    length = 0
    for _ in marks_list:
        length += 1
        
    if length == 0:
        return 0.0
        
    total = 0.0
    for m in marks_list:
        total += m
    return total / length

def _to_lower(s):
    res = ""
    for char in s:
        if 'A' <= char <= 'Z':
            res += chr(ord(char) + 32)
        else:
            res += char
    return res

def search_student(names_list, marks_list, name):
    # Get list length manually
    length = 0
    for _ in names_list:
        length += 1
        
    search_name_lower = _to_lower(name)
    for i in range(length):
        if _to_lower(names_list[i]) == search_name_lower:
            return i
            
    return -1

# Test Section
if __name__ == "__main__":
    names = []
    marks = []
    
    # 1. Add students
    print("1. Adding student records...")
    add_student(names, marks, "Vinod", 85.0)
    add_student(names, marks, "Rahul", 92.0)
    add_student(names, marks, "Amit", 78.0)
    
    # 2. Show all student records
    print("\n2. Showing student records:")
    print(show_students(names, marks))
    
    # 3. Find student with highest marks
    print("\n3. Finding student with highest marks:")
    h_name, h_mark = find_highest_marks(names, marks)
    print(f"Highest Scorer: {h_name} with {h_mark}")
    
    # 4. Calculate class average
    print("\n4. Calculating class average:")
    avg = calculate_class_average(marks)
    print(f"Class Average: {avg:.2f}")
    
    # 5. Search student (case-insensitive)
    print("\n5. Searching student 'rahul' (case-insensitive):")
    idx = search_student(names, marks, "rahul")
    if idx != -1:
        print(f"Found: {names[idx]} (Marks: {marks[idx]}) at index {idx}")
    else:
        print("Student not found.")
