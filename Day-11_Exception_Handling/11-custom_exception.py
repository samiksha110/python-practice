# If marks are less than 0 or greater than 100, raise InvalidMarksError.

class InvalidMarksError(Exception):
    pass


try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Invalid Marks")

    print("Valid Marks")

except InvalidMarksError as e:
    print(e)


