def calculate_grade(marks):
    """Return the grade and encouraging message for the given marks."""

    if marks >= 90:
        return "A", "Excellent! Outstanding work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! You're doing well! 😊"
    elif marks >= 60:
        return "D", "You passed! Keep practicing! 💪"
    else:
        return "F", "Don't give up! Keep learning and improving! 🌱"


def get_valid_marks():
    """Keep asking until the user enters marks between 0 and 100."""

    while True:
        try:
            marks = float(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Please enter a number from 0 to 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    print("===== STUDENT GRADE CALCULATOR =====")

    student_name = input("Enter student name: ").strip()

    while not student_name:
        print("Student name cannot be empty.")
        student_name = input("Enter student name: ").strip()

    marks = get_valid_marks()
    grade, message = calculate_grade(marks)

    print("\n📊 RESULT FOR", student_name.upper() + ":")
    print(f"Marks: {marks:g}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


if __name__ == "__main__":
    main()
