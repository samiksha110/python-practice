# Concepts: Class, Object ,,Constructor self Methods

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name :", self.name)
        print("Marks:", self.marks)


s1 = Student("Samiksha", 95)
s2 = Student("Rahul", 82)

s1.display()
print()
s2.display()
