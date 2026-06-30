import assignment_functions as af

def main():
    names = []
    marks = []
    
    while True:
        print("\n==================================")
        print("   MARKS MANAGEMENT SYSTEM")
        print("==================================")
        print("1. Add Student Record")
        print("2. Show All Student Records")
        print("3. Find Student with Highest Marks")
        print("4. Calculate Class Average Marks")
        print("5. Search Student by Name")
        print("6. Exit")
        print("==================================")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            name = input("Enter student name: ").strip()
            if not name:
                print("Error: Student name cannot be empty.")
                continue
            try:
                mark = float(input("Enter student marks (0-100): "))
                if mark < 0 or mark > 100:
                    print("Error: Marks must be between 0 and 100.")
                    continue
                af.add_student(names, marks, name, mark)
                print(f"Success: Added student '{name}' with marks {mark}.")
            except ValueError:
                print("Error: Marks must be a valid numeric value.")
                
        elif choice == '2':
            print("\n" + af.show_students(names, marks))
            
        elif choice == '3':
            name, mark = af.find_highest_marks(names, marks)
            if name is None:
                print("No student records available.")
            else:
                print(f"Highest Scorer: {name} (Marks: {mark})")
                
        elif choice == '4':
            if len(marks) == 0:
                print("No student records available to calculate average.")
            else:
                avg = af.calculate_class_average(marks)
                print(f"Class Average Marks: {avg:.2f}")
            
        elif choice == '5':
            name = input("Enter student name to search: ").strip()
            idx = af.search_student(names, marks, name)
            if idx == -1:
                print(f"Result: Student '{name}' not found.")
            else:
                print(f"Result: Found student '{names[idx]}' at index {idx} with marks {marks[idx]}.")
                
        elif choice == '6':
            print("Exiting Marks Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose an option from 1 to 6.")

if __name__ == "__main__":
    main()
