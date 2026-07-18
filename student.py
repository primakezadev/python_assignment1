# student.py

def calculate_grade(scores):
    """Calculate the student's grade based on average score."""
    average = sum(scores) / len(scores)

    if average >= 90:
        return average, "A"
    elif average >= 80:
        return average, "B"
    elif average >= 70:
        return average, "C"
    elif average >= 60:
        return average, "D"
    else:
        return average, "F"


def calculate_status(grade, active):
    """Determine student status."""
    if grade in ["A", "B", "C"] and active:
        return "PASS ACTIVE"
    elif grade in ["A", "B", "C"] and not active:
        return "PASS INACTIVE"
    else:
        return "FAIL"


def add_student(students):
    """Add a new student."""

    print("\n========== ADD STUDENT ==========")

    # Prevent duplicate names (Bonus)
    existing_names = set()

    for student in students:
        existing_names.add(student["name"].lower())

    while True:
        name = input("Enter student name: ").strip()

        if name == "":
            print("Name cannot be empty.")
            continue

        if name.lower() in existing_names:
            print("Student already exists.")
            continue

        break

    # Age Validation
    while True:
        age_input = input("Enter student age: ")

        try:
            age = int(age_input)

            if 10 <= age <= 100:
                break
            else:
                print("Age must be between 10 and 100.")

        except ValueError:
            print("Age must be a whole number.")

    # Scores Validation
    scores = []

    for i in range(3):

        while True:

            try:
                score = float(input(f"Enter score {i+1}: "))

                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")

            except ValueError:
                print("Invalid score.")

    # Active Status
    while True:

        active_input = input("Is student active? (true/false): ").lower().strip()

        if active_input == "true":
            active = True
            break

        elif active_input == "false":
            active = False
            break

        else:
            print("Enter only true or false.")

    # Grade
    average, grade = calculate_grade(scores)

    # Status
    status = calculate_status(grade, active)

    # Student Dictionary
    student = {
        "name": name,
        "age": age,
        "scores": scores,
        "grade": grade,
        "status": status,
        "active": active
    }

    # append() (Required)
    students.append(student)

    print("\nStudent added successfully!")
    print(f"Average : {average:.2f}")
    print(f"Grade   : {grade}")
    print(f"Status  : {status}")


def view_students(students):
    """Display all students."""

    print("\n========== STUDENT LIST ==========")

    if len(students) == 0:
        print("No students available.")
        return

    for index, student in enumerate(students, start=1):

        average = sum(student["scores"]) / len(student["scores"])

        print(f"\nStudent {index}")
        print("-" * 30)
        print("Name    :", student["name"])
        print("Age     :", student["age"])
        print("Scores  :", student["scores"])
        print("Average :", round(average, 2))
        print("Grade   :", student["grade"])
        print("Status  :", student["status"])
        print("Active  :", student["active"])


def search_student(students):
    """Search student by name."""

    if len(students) == 0:
        print("No students available.")
        return

    search_name = input("\nEnter student name: ").strip().lower()

    found = False

    for student in students:

        if student["name"].lower() == search_name:

            average = sum(student["scores"]) / len(student["scores"])

            print("\nStudent Found")
            print("-" * 30)
            print("Name    :", student["name"])
            print("Age     :", student["age"])
            print("Scores  :", student["scores"])
            print("Average :", round(average, 2))
            print("Grade   :", student["grade"])
            print("Status  :", student["status"])
            print("Active  :", student["active"])

            found = True
            break

    if not found:
        print("Student not found.")