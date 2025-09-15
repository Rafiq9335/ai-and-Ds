# Student Records Management System (SRMS) using Nested List

# Main list to store all student records
students = []  # Each student = [name, roll, subject, marks]

def add_student():
    """Add a new student record"""
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    subject = input("Enter Subsject: ")
    marks = float(input("Enter Marks: "))
    student = [name, roll, subject, marks]
    students.append(student)
    print(" Student record added successfully!\n")

def display_students():
    """Display all student records"""
    if not students:
        print("No student records found!\n")
    else:
        print("\n--- Student Records ---")
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student[0]}, Roll: {student[1]}, "
                  f"Subject: {student[2]}, Marks: {student[3]}")
        print()

def search_student():
    """Search a student by roll number"""
    roll = input("Enter Roll Number to search: ")
    found = False
    for student in students:
        if student[1] == roll:
            print(f" Student Found: Name: {student[0]}, Roll: {student[1]}, "
                  f"Subject: {student[2]}, Marks: {student[3]}\n")
            found = True
            break
    if not found:
        print("Student record not found.\n")

def update_student():
    """Update marks of a student using roll number"""
    roll = input("Enter Roll Number to update marks: ")
    for student in students:
        if student[1] == roll:
            new_marks = float(input("Enter new Marks: "))
            student[3] = new_marks
            print(" Marks updated successfully!\n")
            return
    print(" Student record not found.\n")

def delete_student():
    """Delete a student record using roll number"""
    roll = input("Enter Roll Number to delete: ")
    for student in students:
        if student[1] == roll:
            students.remove(student)
            print(" Student record deleted successfully!\n")
            return
    print(" Student record not found.\n")

def sort_students():
    """Sort students by marks (descending order)"""
    if not students:
        print("No student records to sort!\n")
    else:
        students.sort(key=lambda x: x[3], reverse=True)
        print(" Students sorted by marks (highest first)!\n")

def menu():
    """Main menu loop"""
    while True:
        print("===== Student Records Management System (SRMS) =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student Record")
        print("6. Sort Students by Marks (Descending)")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            sort_students()
        elif choice == "7":
            print("Exiting SRMS... Goodbye!")
            break
        else:
            print(" Invalid choice! Please try again.\n")

# Run the program
menu()
