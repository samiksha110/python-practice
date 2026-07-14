# 📚 Python Lists - Notes

## What is a List?

A **list** is a collection of multiple items stored in a single variable.

```python
fruits = ["apple", "banana", "mango"]
print(fruits)
```

Output:

```
['apple', 'banana', 'mango']
```

---

# Characteristics of Lists

- Ordered ✅
- Mutable (can be changed) ✅
- Allows duplicate values ✅
- Can store different data types ✅

Example:

```python
data = ["Samiksha", 22, True, 5.3]
print(data)
```

---

# Creating a List

```python
fruits = ["apple", "banana", "mango"]

numbers = [1, 2, 3, 4]

empty_list = []
```

---

# Indexing

Python uses **0-based indexing**.

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[2])   # mango
```

### Negative Indexing

```python
print(fruits[-1])   # mango
print(fruits[-2])   # banana
```

---

# Updating Elements

Lists are mutable, so values can be changed.

```python
fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"

print(fruits)
```

Output:

```
['apple', 'orange', 'mango']
```

---

# Adding Elements

## append()

Adds one element to the end.

```python
fruits.append("kiwi")
```

Output:

```
['apple', 'orange', 'mango', 'kiwi']
```

---

## insert()

Adds an element at a specific index.

```python
fruits.insert(2, "pineapple")
```

Output:

```
['apple', 'orange', 'pineapple', 'mango', 'kiwi']
```

---

# Removing Elements

## remove()

Removes an element by value.

```python
fruits.remove("orange")
```

---

## pop()

Removes an element by index.

```python
fruits.pop()
```

Removes the last element.

```python
fruits.pop(2)
```

Removes the element at index 2.

### Important

`pop()` returns the removed element.

```python
nums = [10, 20, 30]

removed = nums.pop()

print(removed)
print(nums)
```

Output:

```
30
[10, 20]
```

---

# Length of a List

Use `len()` to count the number of elements.

```python
fruits = ["apple", "banana", "mango"]

print(len(fruits))
```

Output:

```
3
```

---

# Membership Operator (`in`)

Checks whether an element exists in a list.

```python
fruits = ["apple", "banana", "mango"]

print("mango" in fruits)
```

Output:

```
True
```

```python
print("grapes" in fruits)
```

Output:

```
False
```

---

# Looping Through a List

## Method 1

```python
for fruit in fruits:
    print(fruit)
```

---

## Method 2 (Using Index)

```python
for i in range(len(fruits)):
    print(i, fruits[i])
```

Output:

```
0 apple
1 banana
2 mango
```

---

# Difference Between append() and insert()

| append() | insert() |
|----------|----------|
| Adds element at the end | Adds element at a specified index |
| Takes one argument | Takes two arguments (index, value) |

---

# Difference Between remove() and pop()

| remove() | pop() |
|-----------|--------|
| Removes by value | Removes by index |
| Returns nothing | Returns the removed element |

---

# Common Functions

| Function | Purpose |
|-----------|---------|
| append() | Add element at end |
| insert() | Add element at index |
| remove() | Remove by value |
| pop() | Remove by index |
| len() | Number of elements |
| in | Check if element exists |

---

# Time Complexity

| Operation | Complexity |
|------------|------------|
| Access by index | O(1) |
| Append | O(1) |
| Insert | O(n) |
| Remove | O(n) |
| Search (`in`) | O(n) |
| Length | O(1) |

---

# Important Points

- Lists are **mutable**.
- Index starts from **0**.
- Negative indexing starts from **-1**.
- `append()` adds at the end.
- `insert()` adds at a specific position.
- `remove()` removes by value.
- `pop()` removes by index and returns the removed element.
- `len()` gives the number of elements.
- `in` checks whether an element exists.
- Lists can be traversed using a `for` loop.

---

# Practice Questions Completed

- ✅ Create a list
- ✅ Access elements
- ✅ Print first and last element
- ✅ Modify list elements
- ✅ append()
- ✅ insert()
- ✅ remove()
- ✅ pop()
- ✅ len()
- ✅ in operator
- ✅ Loop through a list

---

