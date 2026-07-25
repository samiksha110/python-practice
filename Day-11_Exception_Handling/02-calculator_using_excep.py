# Enter first number: 20
# Enter operator: /
# Enter second number: 5

# Answer = 4.0

try:
    num1 = int(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %): ")
    num2 = int(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        result = num1 / num2

    elif operator == "%":
        result = num1 % num2

    else:
        print("Invalid operator")

    if operator in ["+", "-", "*", "/", "%"]:
        print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")
