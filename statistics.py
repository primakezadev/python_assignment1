# statistics.py

def show_statistics(students):
    """Display statistics about students."""

    print("\n========== STUDENT STATISTICS ==========")

    if len(students) == 0:
        print("No students available.")
        return

    total_students = len(students)

    grade_counts = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    total_age = 0
    active_students = 0
    failing_students = 0

    for student in students:

        grade = student["grade"]

        if grade in grade_counts:
            grade_counts[grade] += 1

        total_age += student["age"]

        if student["active"]:
            active_students += 1

        if grade in ["D", "F"]:
            failing_students += 1

    average_age = total_age / total_students
    active_percentage = (active_students / total_students) * 100

    print(f"Total Students      : {total_students}")
    print(f"Grade A Students    : {grade_counts['A']}")
    print(f"Grade B Students    : {grade_counts['B']}")
    print(f"Grade C Students    : {grade_counts['C']}")
    print(f"Grade D Students    : {grade_counts['D']}")
    print(f"Grade F Students    : {grade_counts['F']}")
    print(f"Average Age         : {average_age:.2f}")
    print(f"Active Percentage   : {active_percentage:.2f}%")
    print(f"Failing Students    : {failing_students}")


def sort_students(students):
    """Sort students from highest to lowest average."""

    if len(students) == 0:
        print("No students available.")
        return

    sorted_students = sorted(
        students,
        key=lambda student: sum(student["scores"]) / len(student["scores"]),
        reverse=True
    )

    print("\n========== STUDENTS SORTED BY AVERAGE ==========")

    for index, student in enumerate(sorted_students, start=1):

        average = sum(student["scores"]) / len(student["scores"])

        print(f"{index}. {student['name']} - {average:.2f} ({student['grade']})")


def top_three_students(students):
    """Display the top three students."""

    if len(students) == 0:
        print("No students available.")
        return

    sorted_students = sorted(
        students,
        key=lambda student: sum(student["scores"]) / len(student["scores"]),
        reverse=True
    )

    print("\n========== TOP 3 STUDENTS ==========")

    limit = min(3, len(sorted_students))

    for i in range(limit):

        student = sorted_students[i]

        average = sum(student["scores"]) / len(student["scores"])

        print(f"\nRank {i+1}")
        print(f"Name    : {student['name']}")
        print(f"Average : {average:.2f}")
        print(f"Grade   : {student['grade']}")


def search_by_grade(students):
    """Search students by grade."""

    if len(students) == 0:
        print("No students available.")
        return

    grade = input("Enter grade (A, B, C, D, F): ").upper()

    if grade not in ["A", "B", "C", "D", "F"]:
        print("Invalid grade.")
        return

    found = False

    print(f"\n========== STUDENTS WITH GRADE {grade} ==========")

    for student in students:

        if student["grade"] == grade:

            average = sum(student["scores"]) / len(student["scores"])

            print(f"{student['name']} - Average: {average:.2f}")

            found = True

    if not found:
        print("No students found with this grade.")