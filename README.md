#  Student Management System

A console-based **Student Management System** built with **Python** to demonstrate Python fundamentals such as functions, modules, data structures, loops, conditions, input validation, file handling, and exception handling.

---

##  Project Overview

This application allows users to manage student records through a simple menu-driven interface.

Users can:

- Add students
- View all students
- Search for a student
- Show student statistics
- Save student records to a file
- Load student records from a file

The project is divided into modules to make the code organized, reusable, and easier to maintain.

---

##  Features

###  Add Student

The system allows users to enter:

- Student Name
- Student Age
- Three Scores
- Active Status (True/False)

Input validation ensures:

- Name cannot be empty.
- Age must be between 10 and 100.
- Scores must be between 0 and 100.
- Active status must be either `true` or `false`.

---

###  Grade Calculation

The student's average score is calculated automatically.

Grades are assigned as follows:

| Average | Grade |
|---------:|:-----:|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

---

###  Student Status

Student status is determined automatically.

| Grade | Active | Status |
|--------|--------|----------------|
| A, B, C | True | PASS ACTIVE |
| A, B, C | False | PASS INACTIVE |
| D or F | Any | FAIL |

---

###  View Students

Displays all stored students with:

- Name
- Age
- Scores
- Average Score
- Grade
- Status
- Active Status

---

###  Search Student

Search for a student using their name.

If the student exists, all details are displayed.

Otherwise:

```
Student not found
```

---

###  Statistics

Displays:

- Total Students
- Number of Grade A Students
- Number of Grade B Students
- Number of Grade C Students
- Number of Grade D Students
- Number of Grade F Students
- Average Age
- Percentage of Active Students

---

###  File Handling

The application can:

- Save all student records to `students.txt`
- Read data from `students.txt`
- Display saved records

---

##  Project Structure

```
Assignment/
│
├── main_modules.py
├── student.py
├── statistics.py
├── handler.py
├── students.txt

```

---

##  Module Description

### `main_modules.py`

The entry point of the application.

Responsibilities:

- Displays the menu
- Calls functions from other modules
- Controls program flow

---

### `student.py`

Handles all student-related operations.

Functions:

- Add Student
- View Students
- Search Student
- Grade Calculation
- Status Calculation

---

### `statistics.py`

Responsible for generating student statistics.

Functions:

- Total Students
- Grade Counts
- Average Age
- Active Student Percentage

---

### `handler.py`

Handles file operations.

Functions:

- Save students to file
- Load students from file

---

##  Technologies Used

- Python 3
- Functions
- Modules
- Lists
- Dictionaries
- Sets
- Loops
- Conditions
- Exception Handling
- File Handling

---

##  Python Concepts Demonstrated

- Variables
- Data Types
- Input and Output
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- If / Elif / Else
- While Loops
- For Loops
- Functions
- Modules
- Lists
- Dictionaries
- Sets
- Boolean Values
- Exception Handling (`try` / `except`)
- File Handling (`read()` and `write()`)

---

##  How to Run

Clone the repository:

```bash
git clone https://github.com/primakezadev/python_assignment1.git
```

Navigate into the project:

```bash
cd Assignment
```

Run the application:

```bash
python main_modules.py
```

---

##  Sample Menu

```
=========================================
      STUDENT MANAGEMENT SYSTEM
=========================================
1. Add Student
2. View All Students
3. Search Student
4. Show Statistics
5. Save to File
6. Load from File
7. Exit
=========================================
Enter your choice:
```

---

##  Learning Objectives

This project demonstrates how to:

- Organize Python code using modules
- Build reusable functions
- Validate user input
- Store structured data using dictionaries and lists
- Perform calculations dynamically
- Read and write files
- Build an interactive console application

---

##  Author

**Keza Prima**
