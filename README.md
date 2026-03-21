# 🎓 University Student Management System

A Python-based command-line interface (CLI) application designed to manage student records, track course enrollments, and calculate academic performance.

## ✨ Key Features
The system provides an interactive menu with the following capabilities:
*   **Add New Student:** Create a student profile with their name, age, and a unique student number.
*   **Delete Student:** Remove a student from the records using their specific student number.
*   **Display Student Details:** View complete information, including system-generated IDs, name, age, and student number.
*   **Manage Courses:** Enroll students in specific courses and assign marks for each.
*   **Calculate Averages:** Automatically compute and display a student's average grade across all enrolled subjects.

## 🛠 Technical Overview
The application is built using **Object-Oriented Programming (OOP)** and is structured into two primary classes:

### 1. Course Class
*   Generates a random `course_id` between 1000 and 9999.
*   Stores the `course_name` and the `course_mark` achieved.

### 2. Student Class
*   Tracks the total number of registered students via a class variable.
*   Generates a unique 5-digit `student_id` for internal tracking.
*   Maintains a list of `Course` objects and includes methods to calculate grade averages.

## 🚀 How to Use
When you run the script, use the following menu options:
1. **Add New Student:** Register a new user by providing their number, name, and age.
2. **Delete Student:** Enter the student number to remove them from the system.
3. **Display Student:** View the full profile of a specific student.
4. **Get Student Average:** View the calculated GPA based on enrolled courses.
5. **Add Course:** Link a new course and grade to a student's record.
6. **Exit:** Safely close the application.

