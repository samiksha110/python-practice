<div align="center">

# 📂 File Handling in Python

*"Store data permanently using files."*

</div>

---

# 🎯 What is File Handling?

Variables ➜ Temporary Storage

Files ➜ Permanent Storage

---

# 📂 Opening a File

```python
file = open("student.txt", "r")
```

---

# 📚 File Modes

| Mode | Meaning |
|------|----------|
| 📖 r | Read |
| ✍ w | Write (Overwrite) |
| ➕ a | Append |
| 🆕 x | Create New File |

### 💡 Memory Trick

```
w = Wipe + Write

a = Add
```

---

# 📖 Reading Files

## Read Entire File

```python
file.read()
```

---

## Read One Line

```python
file.readline()
```

---

## Read All Lines

```python
file.readlines()
```

Returns

```python
[
'Python\n',
'Java\n',
'C++'
]
```

---

# ✍ Writing Files

```python
with open("student.txt","w") as file:
    file.write("Hello")
```

⚠ Deletes previous content before writing.

---

# ➕ Append Mode

```python
with open("student.txt","a") as file:
    file.write("\nPython")
```

Adds data without deleting old data.

---

# ⭐ Best Practice

```python
with open("student.txt","r") as file:
    text = file.read()
```

✔ Automatically closes the file.

No need for

```python
file.close()
```

---

# 📍 File Cursor

Each read moves the cursor.

```python
file.readline()
```

↓

First Line

```python
file.readline()
```

↓

Second Line

---

# 🚀 read() Twice

```python
print(file.read())
print(file.read())
```

Second output is empty because the cursor reaches

**EOF (End Of File)**

---

# ✂ split()

Splits into words.

```python
text.split()
```

Output

```python
['Python','is','easy']
```

---

# 📄 splitlines()

Splits into lines.

```python
text.splitlines()
```

Output

```python
['Python','Java','C++']
```

---

# 📊 Counting

### Characters

```python
len(text)
```

### Words

```python
len(text.split())
```

### Lines

```python
len(text.splitlines())
```

---

# 💻 Mini Projects

✅ Word Counter

✅ Character Counter

✅ Student Record System

---

# 🎯 Interview Questions

- Difference between read(), readline() & readlines()?
- Difference between "w" & "a"?
- Why use with open()?
- What is File Cursor?
- Difference between split() & splitlines()?
- What happens if read() is called twice?

---

# ⚡ Quick Revision

| Function | Purpose |
|----------|---------|
| read() | Entire File |
| readline() | One Line |
| readlines() | List of Lines |
| write() | Write Data |
| split() | Words |
| splitlines() | Lines |

---

<div align="center">


</div>