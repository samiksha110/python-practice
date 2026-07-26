# password validator

try:
    password = input("Enter password:")

    if len(password) < 8:
        print("Password must contain atleast 8 characters")

    elif " " in password:
        print("Password should not contain spaces")

    else:
        print("Password Accepted")

except Exception:
    print("Something went wrong")
