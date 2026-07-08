# 📅 Day 4 - Python Strings (Part 1)

## 🎯 Topics Covered

- What is a String?
- Types of Quotes
- len() Function
- Positive Indexing
- Negative Indexing
- String Slicing
- Slicing Shortcuts
- Step Slicing
- Reverse String using Slicing

---

# 📌 What is a String?

A string is a sequence of characters enclosed in quotes.

Examples

```python
name = "Samiksha"

city = 'Pune'

course = "Python"
```

---
# 📌 Types of Quotes

## Single Quotes

```python
name = 'Python'
```

## Double Quotes

```python
name = "Python"
```

Both are exactly the same.

---

## Triple Quotes

Used for multiple lines.

```python
message = """
Hello
Welcome
Good Morning
"""
```

---
# 📌 len() Function

Returns the total number of characters.

```python
name = "Python"

print(len(name))
```

Output

```
6
```

Remember:

Spaces are also counted.

```python
len("Hello World")
```

Output

```
11
```

---
# 📌 Positive Indexing

Python starts indexing from **0**.

Example

```text
Character : P  y  t  h  o  n
Index     : 0  1  2  3  4  5
```

Examples

```python
name[0]
```

Output

```
P
```

```python
name[3]
```

Output

```
h
```

---

# 📌 Negative Indexing

Negative indexing starts from the end.

```text
Character : P  y  t  h  o  n
Positive  : 0  1  2  3  4  5
Negative  : -6 -5 -4 -3 -2 -1
```

Examples

```python
name[-1]
```

Output

```
n
```

```python
name[-2]
```

Output

```
o
```
# 📌 String Slicing

Syntax

```python
string[start:stop]
```

Rule

- Start index is included.
- Stop index is excluded.

Example

```python
name = "Samiksha"

print(name[0:4])
```

Output

```
Sami
```

---

# 📌 Slicing Shortcuts

## From Beginning

```python
name[:4]
```

Output

```
Sami
```

Equivalent to

```python
name[0:4]
```

---

## Till End

```python
name[4:]
```

Output

```
ksha
```

---

## Copy Entire String

```python
name[:]
```

Output

```
Samiksha
```

---

# 📌 Step Slicing

Syntax

```python
string[start:stop:step]
```

Example

```python
word = "Placement"

print(word[0:9:2])
```

Indexes

```
0 → 2 → 4 → 6 → 8
```

Output

```
Paeet
```

---

Example

```python
word[1:9:2]
```

Indexes

```
1 → 3 → 5 → 7
```

Output

```
lcmn
```

---

# 📌 Reverse a String

Using slicing.

```python
text = "Python"

print(text[::-1])
```

Output

```
nohtyP
```

Meaning

- Start from the end.
- Move backwards.
- Stop at the beginning.

---

# ⭐ Important Rules

✅ Python indexing starts from 0.

✅ Last character can be accessed using -1.

✅ Stop index is never included.

✅ If start is omitted, Python starts from index 0.

✅ If stop is omitted, Python goes till the end.

✅ Step tells Python how many indexes to jump.

✅ Negative step moves backwards.

---

# 🧠 Tricks to Remember

## Indexing

```
0 1 2 3 ...
```

Starts from left.

```
-1 -2 -3 ...
```

Starts from right.

---

## Slicing

```
[start : stop]
```

Think

```
Start → Included

Stop → Excluded
```

---

## Step Slicing

Always follow the indexes first.

Example

```
0 → 2 → 4 → 6
```

Then read the characters.

---

# 📚 Functions Learned

```python
len()
```

---

# 🏆 Today's Achievement

✅ Strings

✅ Quotes

✅ len()

✅ Positive Indexing

✅ Negative Indexing

✅ String Slicing

✅ Slicing Shortcuts

✅ Step Slicing

✅ Reverse String

🎉 String Basics Completed!