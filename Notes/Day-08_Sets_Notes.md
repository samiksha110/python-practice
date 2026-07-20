# 📘 Python Sets - One Page Cheat Sheet

## What is a Set?
- Unordered collection of **unique** elements.
- No duplicates allowed.
- Mutable (can add/remove elements).
- No indexing.

---

## Create a Set

```python
numbers = {10, 20, 30}
```

### Empty Set

```python
numbers = set()      # ✅ Correct
numbers = {}         # ❌ Dictionary
```

---

## Add Element

```python
numbers.add(40)
```

---

## Remove Element

```python
numbers.remove(20)      # Raises KeyError if not found
numbers.discard(20)     # No error if not found
```

---

## Membership

```python
print(20 in numbers)      # True
print(50 in numbers)      # False
```

---

## Set Operations

### Union (All unique elements)

```python
A | B
```

### Intersection (Common elements)

```python
A & B
```

### Difference (Elements in A but not B)

```python
A - B
```

---

## Useful Functions

```python
len(numbers)          # Number of elements

set(list_name)        # Convert list to set

set(text)             # Convert string to set
```

---

# Programs

## Remove Duplicates

```python
numbers = [10,20,10,30,20]
print(set(numbers))
```

---

## Count Unique Elements

```python
numbers = [10,20,10,30,20]
print(len(set(numbers)))
```

---

## Check Duplicates

```python
numbers = [10,20,30,20]

if len(numbers) == len(set(numbers)):
    print("No Duplicates")
else:
    print("Duplicates Found")
```

---

## Find First Duplicate

```python
numbers = [10,20,30,20,40]

seen = set()

for num in numbers:
    if num in seen:
        print(num)
        break
    else:
        seen.add(num)
```

---

## Count Distinct Characters

```python
text = "programming"

print(len(set(text)))
```

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Add | O(1) |
| Remove | O(1) |
| Search (`in`) | O(1) |
| Union | O(n+m) |
| Intersection | O(min(n,m)) |

---

# Remember

✅ Unique elements only

✅ Empty set → `set()`

❌ `{}` is a dictionary

✅ Add → `add()`

✅ Remove → `remove()`

✅ Safe remove → `discard()`

✅ Search → `in`

✅ Union → `|`

✅ Intersection → `&`

✅ Difference → `-`

✅ Fast lookup → **O(1)**

**DSA Uses:** Remove duplicates, Find duplicates, Fast searching, Distinct characters.

