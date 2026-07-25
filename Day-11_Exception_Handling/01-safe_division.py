# Write a program that:

# Takes two numbers as input.
# Divides the first number by the second.

# If the second number is 0, print:
# Cannot divide by zero

# If the user enters something other than a number, print:
# Invalid input
try:
    # Take input from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Perform division
    result = num1 / num2

    # Display result
    print("Result =", result)

# Handles division by zero
except ZeroDivisionError:
    print("Cannot divide by zero")

# Handles invalid integer input
except ValueError:
    print("Invalid input")
