FILE_NAME = "students.txt"

def save_students(students):
    """Save all students to students.txt"""

    if len(students) == 0:
        print("No students available to save.")
        return

    try:
        with open(FILE_NAME, "w") as file:

            for student in students:

                average = sum(student["scores"]) / len(student["scores"])

                line = (
                    f"Name: {student['name']} | "
                    f"Age: {student['age']} | "
                    f"Scores: {student['scores']} | "
                    f"Average: {average:.2f} | "
                    f"Grade: {student['grade']} | "
                    f"Status: {student['status']} | "
                    f"Active: {student['active']}\n"
                )

                file.write(line)

        print("Students saved successfully!")

    except Exception as e:
        print("Error saving file:", e)


def load_students():
    """Read and display students.txt"""

    try:
        with open(FILE_NAME, "r") as file:

            content = file.read()

            if content.strip() == "":
                print("The file is empty.")
            else:
                print("\n========== STUDENTS FROM FILE ==========\n")
                print(content)

    except FileNotFoundError:
        print("students.txt does not exist.")

    except Exception as e:
        print("Error reading file:", e)