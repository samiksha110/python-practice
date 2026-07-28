# count the number of words in file

with open("article.txt", "r") as file:
    text = file.read()

words = text.split()

print("Total words =", len(words))
