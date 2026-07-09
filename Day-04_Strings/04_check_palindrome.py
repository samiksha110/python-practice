# check if string is palindrome

text = input().lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
