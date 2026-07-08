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
