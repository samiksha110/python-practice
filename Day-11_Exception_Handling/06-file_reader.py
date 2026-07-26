# read the file

try:
    file = open("sample.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:
    print("File not found.")

except Exception:
    print("Something went wrong.")
