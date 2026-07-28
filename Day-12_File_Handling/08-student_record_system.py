# student record system

# Student Record System

while True:

    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":

        name = input("Enter student name: ")
        marks = input("Enter student marks: ")

        with open("students.txt", "a") as file:
            file.write(f"{name} - {marks}\n")

        print("Student added successfully!")

    # View Students
    elif choice == "2":

        try:
            with open("students.txt", "r") as file:
                students = file.readlines()

            if len(students) == 0:
                print("No student records found.")
            else:
                print("\nStudent Records:")
                for student in students:
                    print(student.strip())

        except FileNotFoundError:
            print("students.txt file not found.")

    # Delete Student
    elif choice == "3":

        name = input("Enter student name to delete: ")

        try:
            with open("students.txt", "r") as file:
                students = file.readlines()

            with open("students.txt", "w") as file:
                for student in students:
                    if name not in student:
                        file.write(student)

            print("Student deleted successfully!")

        except FileNotFoundError:
            print("students.txt file not found.")

    # Exit
    elif choice == "4":
        print("Thank You!")
        break

    # Invalid Choice
    else:
        print("Invalid Choice! Please try again.")
