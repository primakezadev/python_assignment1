# main.py

from student import add_student, view_students, search_student
from statistics import (
    show_statistics,
    sort_students,
    top_three_students,
    search_by_grade
)
from handler import save_students, load_students

# List to store all students
students = []


def menu():
    while True:

        print("\n" + "=" * 50)
        print("      STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Show Statistics")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Sort Students by Average")
        print("8. Top 3 Students")
        print("9. Search by Grade")
        print("10. Exit")
        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            show_statistics(students)

        elif choice == "5":
            save_students(students)

        elif choice == "6":
            load_students()

        elif choice == "7":
            sort_students(students)

        elif choice == "8":
            top_three_students(students)

        elif choice == "9":
            search_by_grade(students)

        elif choice == "10":
            print("\nThank you for using the Student Management System!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from the menu.")


# Start the program
if __name__ == "__main__":
    menu()