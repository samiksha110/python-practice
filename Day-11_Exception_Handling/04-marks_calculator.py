# Marks Calculator

try:
    marks = int(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid Marks")

    elif marks >= 90:
        print("Grade A")

    elif marks >= 80:
        print("Grade B")

    elif marks >= 70:
        print("Grade C")

    elif marks >= 60:
        print("Grade D")

    elif marks >= 40:
        print("Pass")

    else:
        print("Fail")

except ValueError:
    print("Please enter valid marks.")
