<div align="center">

# ⚠️ Exception Handling in Python

*"Handle errors without crashing your program."*

</div>

---

## 🎯 What is Exception Handling?

Exception Handling is used to **handle runtime errors** so that the program continues running instead of stopping unexpectedly.

---

## ✨ Why Use It?

✅ Prevents program crash

✅ Handles unexpected errors

✅ Improves user experience

✅ Makes code more reliable

---

# 📝 Syntax

```python
try:
    # Risky Code

except ExceptionName:
    # Handle Error

finally:
    # Always Executes
```

---

# 🚨 Common Exceptions

| ⚠️ Exception | 📌 Cause |
|--------------|----------|
| ZeroDivisionError | Divide by 0 |
| ValueError | Invalid Input |
| FileNotFoundError | File Not Found |
| IndexError | Invalid List Index |
| KeyError | Dictionary Key Missing |

---

# 💻 Examples

### 🔹 ZeroDivisionError

```python
try:
    print(10/0)

except ZeroDivisionError:
    print("Cannot Divide by Zero")
```

---

### 🔹 ValueError

```python
try:
    age = int(input("Enter Age: "))

except ValueError:
    print("Enter Numbers Only")
```

---

### 🔹 FileNotFoundError

```python
try:
    file = open("student.txt", "r")

except FileNotFoundError:
    print("File Not Found")
```

---

# 🔥 Multiple Exceptions

```python
try:
    num = int(input())
    print(10/num)

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Cannot Divide by Zero")
```

---

# ⭐ finally Block

```python
try:
    print("Hello")

finally:
    print("Program Ended")
```

✔ Runs whether an exception occurs or not.

---

# 📊 Flow

```
        try
         │
  ┌──────┴──────┐
  │             │
 No Error      Error
  │             │
  ▼             ▼
finally      except
                 │
                 ▼
             finally
```

---

# 🎯 Interview Questions

- Difference between Error & Exception?
- Why use try-except?
- Difference between except & finally?
- Name 5 common exceptions.

---

# 📌 Quick Revision

| Keyword | Purpose |
|---------|---------|
| try | Risky Code |
| except | Handle Error |
| finally | Always Executes |

---

<div align="center">

## 🎉 Day 11 Completed ✅

</div>