# 📅 Day 3 - Python Loops Mastery

## 🎯 Topics Covered

- for loop
- while loop
- range()
- break
- continue
- Nested loops (Introduction)
- Loop-based problem solving

---

# 📌 range()

## Syntax

```python
range(start, stop, step)
```

### Important Rule

The **stop value is NOT included.**

Example:

```python
range(1, 6)
```

Output

```
1 2 3 4 5
```

---

## Examples

```python
range(5)
```

Output

```
0 1 2 3 4
```

---

```python
range(2, 7)
```

Output

```
2 3 4 5 6
```

---

```python
range(2, 11, 2)
```

Output

```
2 4 6 8 10
```

---

```python
range(20, 0, -1)
```

Output

```
20 19 18 ... 1
```

---

# 📌 for Loop

Syntax

```python
for i in range(start, stop):
    print(i)
```

Use when the number of iterations is known.

---

# 📌 while Loop

Syntax

```python
while condition:
    # code
```

Use when the number of iterations is unknown.

Example

```python
while num != 0:
```

---

# 📌 break

Stops the loop immediately.

Example

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Output

```
0
1
2
3
4
```

---

# 📌 continue

Skips the current iteration.

Example

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output

```
0
1
3
4
```

---

# 📌 Nested Loop

Structure

```python
for i in range(rows):
    for j in range(columns):
        print(i, j)
```

Outer loop controls rows.

Inner loop controls columns.

---

# ⭐ Pattern Logic

Always ask yourself:

1. How many rows?
2. What changes in every row?
3. Find the formula.

Examples

Increasing Stars

```
*
**
***
****
*****
```

Formula

```python
range(i + 1)
```

---

Decreasing Stars

```
*****
****
***
**
*
```

Formula

```python
range(5 - i)
```

---

Number Pattern

```
1
22
333
4444
55555
```

Formula

```python
print(i + 1)
```

---

# 📌 Sum of First N Natural Numbers

Logic

1. Initialize total = 0
2. Loop from 1 to n
3. Add every number
4. Print total

Code

```python
total = 0

for i in range(1, n + 1):
    total += i
```

---

# 📌 Factorial

Logic

1. Initialize fact = 1
2. Multiply every number
3. Print fact

Code

```python
fact = 1

for i in range(1, n + 1):
    fact *= i
```

Important

Addition starts with **0**

Multiplication starts with **1**

---

# 📌 Count Digits

Logic

1. count = 0
2. Remove one digit every iteration
3. Increase count
4. Stop when number becomes 0

Code

```python
while num != 0:
    count += 1
    num = num // 10
```

---

# 📌 Sum of Digits

Logic

1. Extract last digit
2. Add it
3. Remove last digit
4. Repeat

Code

```python
while num != 0:
    digit = num % 10
    total += digit
    num = num // 10
```

---

# 📌 Reverse Number

Logic

1. Extract last digit
2. Multiply reverse by 10
3. Add digit
4. Remove last digit

Code

```python
while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
```

---

# 💡 Important Operators

```python
//  Integer Division

%   Remainder

+=  Add and Assign

*=  Multiply and Assign
```

Examples

```python
45678 // 10 = 4567

45678 % 10 = 8
```

---

# 🧠 Programming Patterns Learned

Sum

```python
total += value
```

Count

```python
count += 1
```

Factorial

```python
fact *= i
```

Reverse

```python
reverse = reverse * 10 + digit
```

---

# ⭐ Key Learnings

- range() excludes stop value.
- Use n + 1 when you want to include n.
- Use for loop when iterations are known.
- Use while loop when condition decides the loop.
- // removes the last digit.
- % extracts the last digit.
- Addition starts with 0.
- Multiplication starts with 1.
- Every digit problem follows the same while-loop structure.

---

# 🏆 Day 3 Achievement

✅ for loop

✅ while loop

✅ range()

✅ break

✅ continue

✅ Nested loops (Basics)

✅ Pattern logic

✅ Sum of N numbers

✅ Factorial

✅ Count digits

✅ Sum of digits

✅ Reverse number

🎉 Loop Mastery Completed!