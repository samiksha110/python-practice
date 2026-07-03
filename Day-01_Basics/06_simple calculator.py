# 6] simple calculator

num1 = int(input("Enter a Number"))
num2 = int(input("Enter a Number"))
operator = str(input("Enter a Opeartor"))
# operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    print(num1+num2)

elif operator == "-":
    print(num1-num2)

elif operator == "*":
    print(num1*num2)

elif operator == "/":
    print(num1/num2)

else:
    print("Invalid")
