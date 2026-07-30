<div align="center">

# 🚀 Object-Oriented Programming (OOP) in Python

*"OOP is a way of organizing code using Classes and Objects."*

</div>

---

# 📖 What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm where we create **objects** that contain both **data (attributes)** and **functions (methods)**.

Example:

Student

- Name
- Age
- Marks

Actions

- Study()
- Display()
- Give Exam()

---

# 🏗️ Class

A **Class** is a **blueprint** or **template** for creating objects.

```python
class Student:
    pass
```

Example

```
Blueprint → House

Class → Student
```

---

# 📦 Object

An **Object** is an instance of a class.

```python
s1 = Student()
s2 = Student()
```

Here,

- s1 → Object
- s2 → Object

One Class ➜ Many Objects

---

# 🧠 Memory

```
        Student Class
             │
     ┌───────┴───────┐
     │               │
    s1              s2
```

---

# 🔨 Constructor (__init__)

The constructor runs **automatically** whenever an object is created.

```python
class Student:

    def __init__(self):
        print("Object Created")

s1 = Student()
```

Output

```
Object Created
```

---

# 👤 self Keyword

`self` refers to the **current object**.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Example

```python
s1 = Student("Samiksha")
```

Internally Python does

```python
Student.__init__(s1, "Samiksha")
```

So,

```
self → s1
```

---

# 📌 Instance Variables

Variables that belong to an object.

```python
self.name = name
self.marks = marks
```

Each object has its own copy.

Example

```python
s1 = Student("Samiksha",95)

s2 = Student("Rahul",80)
```

Memory

```
s1
Name = Samiksha
Marks = 95

s2
Name = Rahul
Marks = 80
```

---

# ⚙ Methods

Methods are functions inside a class.

```python
class Student:

    def display(self):
        print(self.name)
```

Calling Method

```python
s1.display()
```

---

# 📥 Methods with Parameters

Methods can accept parameters.

```python
def greet(self, message):
    print(message, self.name)
```

Calling

```python
s1.greet("Welcome")
```

Output

```
Welcome Samiksha
```

---

# 🔙 return

Methods can return values.

```python
def get_marks(self):
    return self.marks
```

Calling

```python
print(s1.get_marks())
```

Output

```
95
```

---

# 🖨 print vs return

| print() | return |
|---------|---------|
| Displays value | Sends value back |
| Cannot be reused | Can be stored |
| Used for output | Used in calculations |

Example

```python
marks = s1.get_marks()

print(marks + 5)
```

---

# 🧮 Methods Calling Methods

A method can call another method.

```python
def total(self):
    return self.marks1 + self.marks2 + self.marks3

def percentage(self):
    return (self.total() / 300) * 100
```

Flow

```
display()

↓

grade()

↓

percentage()

↓

total()
```

---

# 📊 Store vs Calculate

### Store

```
Name

Marks1

Marks2

Marks3
```

### Calculate

```
Total

Percentage

Grade
```

Rule

```
Store User Input

Calculate Remaining Values
```

---

# 🏗 Program 1

## Student Details

Learned

- Constructor
- display()

---

# 🏗 Program 2

## Employee Details

Learned

- Multiple Objects
- Methods

---

# 🏗 Program 3

## Rectangle Calculator

Learned

- area()
- perimeter()
- return

Formula

```
Area = Length × Width

Perimeter = 2 × (Length + Width)
```

---

# 🏗 Program 4

## Bank Account

Methods

```
deposit()

withdraw()

display()
```

Learned

Updating Object Data

Example

```python
self.balance += amount
```

---

# 🏗 Program 5

## Student Result System

Methods

```
total()

percentage()

grade()

display()
```

Learned

Method Calling

---

# 🏗 Program 6

## ATM System

Features

```
Deposit

Withdraw

Check Balance

Exit
```

Concepts Used

- OOP
- while loop
- if-else
- User Input
- Object Methods

---

# ⭐ Common Mistakes

❌ Multiple Constructors

```python
def __init__()
```

Only one constructor is allowed.

---

❌ Forgetting self

```python
def display():
```

Correct

```python
def display(self):
```

---

❌ Forgetting ()

Wrong

```python
self.total
```

Correct

```python
self.total()
```

---

❌ Using Variable Instead of Object Variable

Wrong

```python
balance = balance + amount
```

Correct

```python
self.balance += amount
```

---

# 🎯 OOP Interview Questions

1. What is OOP?
2. What is a Class?
3. What is an Object?
4. Difference between Class and Object?
5. What is a Constructor?
6. What is self?
7. What are Instance Variables?
8. Difference between Method and Function?
9. Difference between print() and return()?
10. Difference between Stored Data and Calculated Data?

---

# 📌 Quick Revision

| Concept | Meaning |
|----------|---------|
| Class | Blueprint |
| Object | Instance of Class |
| Constructor | Automatically runs when object is created |
| self | Current Object |
| Instance Variable | Data stored in object |
| Method | Function inside class |
| return | Sends value back |
| print | Displays value |
| Object.method() | Calling a method |
| self.method() | Calling another method |

---

# 🎓 OOP Programs Completed

✅ Student Details

✅ Employee Details

✅ Rectangle Calculator

✅ Bank Account

✅ Student Result System

✅ ATM System

---

<div align="center">

# 🎉 OOP Basics Completed

### Next Topic

➡️ Inheritance

➡️ Method Overriding

➡️ Polymorphism

➡️ Encapsulation

➡️ Abstraction

</div>