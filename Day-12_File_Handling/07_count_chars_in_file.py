# count characters in a file

with open("article.txt", "r") as file:
    text = file.read()

characters = len(text)

print("Total characters =", characters)

# with open("article.txt", "r") as file:
#    text = file.read()

# Count characters
# characters = len(text)

# Count words
# words = len(text.split())

# Count lines
# ines = len(text.splitlines())

# print("Total lines =", lines)
# print("Total words =", words)
# print("Total characters =", characters)
