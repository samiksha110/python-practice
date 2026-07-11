# to reverse each word

text = input()

words = text.split()

for word in words:
    print(word[::-1], end=" ")
