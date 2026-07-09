# count number of constants
text = input("Enter a string: ").lower()

count = 0

for char in text:
    if char.isalpha() and char not in "aeiou":
        count += 1

print("Number of consonants:", count)
