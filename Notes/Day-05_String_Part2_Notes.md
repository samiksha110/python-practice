# 📅 Day 5 - Python Strings (Interview Questions)

## 🎯 Topics Covered

- Print every character
- Count vowels
- Count consonants
- Check palindrome
- Count words
- Reverse each word
- Remove all spaces
- Count frequency of a character
- Find duplicate characters
- Check anagram

---

# 1️⃣ Print Every Character

### Problem

Print each character of a string on a new line.

### Code

```python
text = input("Enter a string: ")

for char in text:
    print(char)
```

### Example

Input

```
Python
```

Output

```
P
y
t
h
o
n
```

---

# 2️⃣ Count Vowels

### Problem

Count the total number of vowels.

### Code

```python
text = input("Enter a string: ").lower()

count = 0

for char in text:
    if char in "aeiou":
        count += 1

print(count)
```

---

# 3️⃣ Count Consonants

### Problem

Count the total number of consonants.

### Code

```python
text = input("Enter a string: ").lower()

count = 0

for char in text:
    if char.isalpha() and char not in "aeiou":
        count += 1

print(count)
```

---

# 4️⃣ Check Palindrome

### Problem

Check whether a string is palindrome.

### Code

```python
text = input("Enter a string: ").lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

---

# 5️⃣ Count Words

### Problem

Count total words in a sentence.

### Code

```python
text = input("Enter a sentence: ")

words = text.split()

print(len(words))
```

---

# 6️⃣ Reverse Each Word

### Problem

Reverse every word without changing the word order.

### Code

```python
text = input("Enter a sentence: ")

words = text.split()

for word in words:
    print(word[::-1], end=" ")
```

Example

Input

```
I love Python
```

Output

```
I evol nohtyP
```

---

# 7️⃣ Remove All Spaces

### Problem

Remove every space from a string.

### Method 1 (Built-in)

```python
text = input()

print(text.replace(" ", ""))
```

### Method 2 (Using Loop)

```python
text = input()

for char in text:
    if char != " ":
        print(char, end="")
```

---

# 8️⃣ Count Frequency of a Character

### Method 1 (Built-in)

```python
text = input("Enter a string: ")
char = input("Enter character: ")

print(text.count(char))
```

### Method 2 (Without count())

```python
text = input("Enter a string: ")
char = input("Enter character: ")

count = 0

for ch in text:
    if ch == char:
        count += 1

print(count)
```

---

# 9️⃣ Find Duplicate Characters

### Code

```python
text = input()

printed = ""

for ch in text:
    if text.count(ch) > 1 and ch not in printed:
        print(ch)
        printed += ch
```

Example

Input

```
programming
```

Output

```
r
g
m
```

---

# 🔟 Check Anagram

### Problem

Check whether two strings are anagrams.

### Code

```python
word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()

if sorted(word1) == sorted(word2):
    print("Anagram")
else:
    print("Not Anagram")
```

Example

Input

```
listen
silent
```

Output

```
Anagram
```

---

# ⭐ New Methods Learned

```python
isalpha()
isupper()
islower()
count()
replace()
split()
sorted()
```

---

# ⭐ Important Operators Learned

```python
==
!=
in
not in
and
```

---

# ⭐ Important Concepts

✅ Strings are iterable.

```python
for char in text:
```

---

✅ Reverse a string

```python
text[::-1]
```

---

✅ Count using a loop

```python
count = 0

for item in collection:
    if condition:
        count += 1
```

---

✅ Remove spaces

```python
replace(" ", "")
```

or

```python
if char != " ":
```

---

✅ Count words

```python
len(text.split())
```

---

# 🧠 Problem Solving Pattern

Most interview questions follow this structure:

```python
Take Input

↓

Initialize Variable

↓

Loop

↓

Check Condition

↓

Update Counter / Print

↓

Display Final Answer
```

---

# 🏆 Interview Questions Completed

✅ Print Every Character

✅ Count Vowels

✅ Count Consonants

✅ Check Palindrome

✅ Count Words

✅ Reverse Each Word

✅ Remove All Spaces

✅ Count Frequency of Character

✅ Find Duplicate Characters

✅ Check Anagram

🎉 Beginner String Interview Questions Completed!