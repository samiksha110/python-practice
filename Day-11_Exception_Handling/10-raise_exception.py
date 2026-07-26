# raise exception error
try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("You must be 18 or older to vote.")

    print("You are eligible to vote.")

except ValueError as e:
    print(e)
