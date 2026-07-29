# wap to perform bank functions

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

        print("Deposited ₹", amount)
        print("Current Balance ₹", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount

        print("Withdrawn ₹", amount)
        print("Current Balance ₹", self.balance)

    def display(self):
        print("Account Holder :", self.name)
        print("Current Balance : ₹", self.balance)


# Creating Object
acc1 = BankAccount("Samiksha", 5000)

print("===== Initial Account =====")
acc1.display()

print()

print("===== Deposit =====")
acc1.deposit(2000)

print()

print("===== Withdraw =====")
acc1.withdraw(1000)

print()

print("===== Final Account =====")
acc1.display()
