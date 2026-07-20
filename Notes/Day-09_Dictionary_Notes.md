# 🐍 Python Dictionaries Cheat Sheet

## 📌 Create
```python
student = {
    "name": "Samiksha",
    "age": 22
}
```

## 📌 Access
```python
student["name"]          # Samiksha
student.get("name")      # Samiksha
student.get("city")      # None
student.get("city","NA") # NA
```
⚠️ `student["city"]` → KeyError

---

## 📌 Add / Update
```python
student["city"] = "Pune"   # Add
student["age"] = 23        # Update
```

---

## 📌 Delete
```python
del student["city"]        # Delete

x = student.pop("age")     # Remove + Return value
print(x)
```

---

## 📌 Check Key
```python
"name" in student      # True
"course" in student    # False
```

---

## 📌 Length
```python
len(student)           # Number of keys
```

---

## 📌 Methods
```python
student.keys()         # Keys
student.values()       # Values
student.items()        # Key-Value pairs
student.update(d2)     # Merge dictionaries
student.clear()        # Empty dictionary
```

---

## 📌 Loop
```python
for key, value in student.items():
    print(key, value)
```

---

## ⭐ Frequency Count (DSA Pattern)
```python
freq = {}

for ch in text:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1
```

### Shortcut
```python
freq[ch] = freq.get(ch, 0) + 1
```

---

## ⭐ Most Frequent Character
```python
text = "banana"

freq = {}

for ch in text:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1

for key, value in freq.items():
    max_char = key
    max_count = value
    break

for key, value in freq.items():
    if value > max_count:
        max_count = value
        max_char = key

print(max_char, max_count)
```

---

## ⏱️ Time Complexity

| Operation | Time |
|-----------|------|
| Access | O(1) |
| Search | O(1) |
| Insert | O(1) |
| Update | O(1) |
| Delete | O(1) |

---

## 🚀 Quick Revision
```python
student["key"]          # Access
student.get("key")      # Safe Access
student["key"] = value  # Add/Update
del student["key"]      # Delete
student.pop("key")      # Remove + Return
student.keys()          # Keys
student.values()        # Values
student.items()         # Key-Value
student.update(d2)      # Merge
student.clear()         # Empty
"key" in student        # Exists?
len(student)            # Size
```

### 🎯 Interview Problems
- Character Frequency
- Number Frequency
- Most Frequent Character
- First Non-Repeating Character
- Find Duplicates
- Two Sum
- Group Anagrams

> **Golden Pattern**
```python
freq = {}

for item in data:
    if item not in freq:
        freq[item] = 1
    else:
        freq[item] += 1
```