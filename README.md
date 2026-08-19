README.md — Student Grade Calculator
1. Project Overview
Project Title

Student Grade Calculator

Project Description

This project is a simple interactive Python program created as part of my internship task. The program accepts a student's name and marks and calculates the student's grade based on the marks entered.

The program asks the user for:

Student name
Student marks between 0 and 100

The information entered by the user is processed using if-elif-else statements. The program then displays the student's marks, grade, and an encouraging message.

The program also includes input validation using a while loop to make sure that the marks entered are between 0 and 100.

Project Objectives

The main objectives of this project are:

To understand Python conditional statements.
To learn how to use if-elif-else.
To practice using functions.
To learn how to validate user input.
To practice using while loops.
To create a simple interactive Python program.
To implement a real-life grading system.
To provide encouraging messages based on the student's grade.
To test the program with different marks and invalid inputs.
2. Setup Instructions
Requirements

The project requires:

Python 3.x
VS Code, Python IDLE, or any Python-compatible code editor
Terminal or Command Prompt

No external Python libraries are required.

Step 1: Install Python

Install Python 3 on the computer.

Step 2: Create the Project Folder

Create a folder named:

student-grade-calculator

Step 3: Create the Python File

Create the following file inside the project folder:

grade_calculator.py

Step 4: Run the Program

Open the terminal inside the project folder and run:

python grade_calculator.py

Step 5: Enter Student Information

The program will ask for:

Enter student name:
Enter marks (0-100):


Enter the required information and press Enter.

If invalid marks are entered, the program will continue asking until a valid value between 0 and 100 is provided.

3. Code Structure
Project File Structure
student-grade-calculator/
│
├── README.md
├── grade_calculator.py
├── test_cases.txt
└── screenshots/
    ├── successful_result.png
    └── invalid_input.png

File Description
File	Description
README.md	Project documentation
grade_calculator.py	Main Python program
test_cases.txt	Test cases used to verify the program
screenshots/successful_result.png	Screenshot showing successful program output
screenshots/invalid_input.png	Screenshot showing input validation
Program Flow
Start
  ↓
Ask for Student Name
  ↓
Ask for Marks
  ↓
Validate Marks
  ↓
If Marks Are Invalid
  ↓
Ask for Marks Again
  ↓
Calculate Grade
  ↓
Display Marks, Grade and Message
  ↓
End

4. Visual Documentation

Screenshots of the program execution are included in the project.

Successful Result
screenshot/successful_result.png

Invalid Input
screenshot/invalid_input.png

Sample Output
===== STUDENT GRADE CALCULATOR =====
Enter student name: Priya
Enter marks (0-100): 85

📊 RESULT FOR PRIYA:
Marks: 85/100
Grade: B
Message: Very Good! Keep it up! 👍


The screenshots provide visual evidence that the program successfully accepts student information, validates marks, calculates the appropriate grade, and displays an encouraging message.

5. Technical Details
Programming Language

Python 3

Input

The input() function is used to collect the student's name and marks.

Example:

student_name = input("Enter student name: ").strip()


Marks are converted into a numeric value:

marks = float(input("Enter marks (0-100): "))

Variables

The program uses variables to store the student's information:

student_name
marks
grade
message
Grading Logic

The program uses if-elif-else statements to determine the grade.

Marks	Grade	Message
90–100	A	Excellent! Outstanding work! 🌟
80–89	B	Very Good! Keep it up! 👍
70–79	C	Good job! You're doing well! 😊
60–69	D	You passed! Keep practicing! 💪
0–59	F	Don't give up! Keep learning and improving! 🌱
Input Validation

The program accepts marks only between 0 and 100.

A while loop is used to handle invalid input.

For example:

while True:
    try:
        marks = float(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            return marks
        else:
            print("Invalid marks! Please enter a number from 0 to 100.")

    except ValueError:
        print("Invalid input! Please enter a number.")


This prevents invalid values such as:

105
-10
abc


from being accepted as valid marks.

Functions

The program uses functions to organize the code.

Example:

def calculate_grade(marks):


This function receives the marks and returns the appropriate grade and encouraging message.

Another function is used to validate the marks:

def get_valid_marks():

Output

The print() function is used to display the final result.

Example:

print(f"Grade: {grade}")
print(f"Message: {message}")

Program Architecture

The program follows a simple structured approach:

Get the student's name.
Get the student's marks.
Validate the marks.
Calculate the grade.
Generate an encouraging message.
Display the final result.

No external libraries or complex data structures are required.

Algorithm
Start the program.
Display the program title.
Ask the user for the student's name.
Validate that the name is not empty.
Ask the user for marks.
Check whether the marks are between 0 and 100.
If the marks are invalid, ask the user again.
Use if-elif-else statements to determine the grade.
Generate an encouraging message.
Display the student's name, marks, grade, and message.
End the program.
6. Testing Evidence

The program was tested using different marks to verify that the grading logic and input validation work correctly.

Test Case 1 – Grade A

Input:

Name: Priya
Marks: 95


Expected Output:

Grade: A
Message: Excellent! Outstanding work! 🌟


Result: Passed ✅

Test Case 2 – Grade B

Input:

Name: Rahul
Marks: 85


Expected Output:

Grade: B
Message: Very Good! Keep it up! 👍


Result: Passed ✅

Test Case 3 – Grade C

Input:

Name: Anu
Marks: 75


Expected Output:

Grade: C
Message: Good job! You're doing well! 😊


Result: Passed ✅

Test Case 4 – Grade D

Input:

Name: Arjun
Marks: 65


Expected Output:

Grade: D
Message: You passed! Keep practicing! 💪


Result: Passed ✅

Test Case 5 – Grade F

Input:

Name: Neha
Marks: 45


Expected Output:

Grade: F
Message: Don't give up! Keep learning and improving! 🌱


Result: Passed ✅

Test Case 6 – Minimum Valid Marks

Input:

Name: Kiran
Marks: 0


Expected Output:

Grade: F


Result: Passed ✅

Test Case 7 – Maximum Valid Marks

Input:

Name: Riya
Marks: 100


Expected Output:

Grade: A


Result: Passed ✅

Test Case 8 – Invalid Marks Above 100

Input:

Name: Amit
Marks: 105


Expected Output:

Invalid marks! Please enter a number from 0 to 100.


The program asks the user to enter the marks again.

Result: Passed ✅

Test Case 9 – Negative Marks

Input:

Name: Sneha
Marks: -10


Expected Output:

Invalid marks! Please enter a number from 0 to 100.


The program asks the user to enter the marks again.

Result: Passed ✅

Test Case 10 – Non-Numeric Input

Input:

Name: Varun
Marks: abc


Expected Output:

Invalid input! Please enter a number.


The program asks the user to enter the marks again.

Result: Passed ✅

Testing Summary

The program was executed with different student names, valid marks, boundary values, invalid marks, negative values, and non-numeric input.

The grading logic correctly assigned grades from A to F, and the input validation successfully rejected values outside the 0–100 range.

Overall Testing Result: Passed ✅

7. What I Learned

Through this project, I learned how to create a practical Python program using basic programming concepts.

I learned how to use if-elif-else statements to make decisions based on student marks. I also learned how to create and use functions to organize program logic.

I practiced using while loops to repeatedly request input when invalid data is entered. I also learned how to use try-except to handle invalid non-numeric input.

This project helped me understand input validation, conditional logic, functions, loops, and how these concepts can be combined to solve a real-life problem.

I also practiced testing the program with different inputs and checking boundary conditions such as 0, 59, 60, 69, 70, 79, 80, 89, 90, and 100.

8. Conclusion

The Student Grade Calculator successfully meets the requirements of the internship task.

The program:

Uses input() to collect student information.
Uses variables to store student information.
Uses if-elif-else statements for grading logic.
Uses a function to calculate the grade.
Uses a while loop to handle invalid inputs.
Validates that marks are between 0 and 100.
Handles non-numeric input.
Provides encouraging messages for every grade.
Has been tested using different inputs.
Includes documentation and visual evidence.

This project provided practical experience with Python fundamentals, conditional statements, functions, loops, input validation, error handling, and program testing.
