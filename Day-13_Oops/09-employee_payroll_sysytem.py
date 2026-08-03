class Employee:

    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_tax(self):
        return self.salary * 10 / 100

    def calculate_net_salary(self):
        return self.salary + self.bonus - self.calculate_tax()

    def display(self):
        print("=====Employee Payroll System======")
        print("Name:     ", self.name)
        print("Salary:      ", self.salary)
        print("Bonus:     ", self.bonus)

        print("Tax:    ", self.calculate_tax())
        print("Net Salary:      ", self.calculate_net_salary())


name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))
bonus = float(input("Enter Bonus: "))

e1 = Employee(name, salary, bonus)

e1.display()
