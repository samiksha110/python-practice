# finally block

try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    file.close()
    print("File Closed")

# finally executes whether error is present or not
