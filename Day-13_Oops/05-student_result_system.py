# 🎓 Student Result System

# Features:

# Enter Student Name
# Enter Marks in 3 Subjects
# Calculate Total
# Calculate Percentage
# Display Grade (A+, A, B, C, Fail)

class Student:

    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def total(self):
        return self.marks1 + self.marks2 + self.marks3

    def percentage(self):
        return (self.total() / 300) * 100

    def grade(self):
        per = self.percentage()

        if per >= 90:
            return "A+"
        elif per >= 80:
            return "A"
        elif per >= 70:
            return "B"
        elif per >= 60:
            return "C"
        else:
            return "Fail"

    def display(self):
        print("===== Student Result =====")
        print("Name       :", self.name)
        print("Marks 1    :", self.marks1)
        print("Marks 2    :", self.marks2)
        print("Marks 3    :", self.marks3)
        print("Total      :", self.total())
        print("Percentage :", self.percentage(), "%")
        print("Grade      :", self.grade())


# Creating Object
s1 = Student("Samiksha", 95, 90, 85)

s1.display()
