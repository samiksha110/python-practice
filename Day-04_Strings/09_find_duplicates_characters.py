# Find Duplicate Characters

text = input("Enter a string: ")

printed = ""

for ch in text:
    if text.count(ch) > 1 and ch not in printed:
        print(ch)
        printed += ch
