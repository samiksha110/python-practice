# Enter Employee Name , Enter Salary , Display Employee Details

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


e1 = Employee("Samiksha", 30000)
e2 = Employee("Sakshi", 20000)

e1.display()
print()
e2.display()
