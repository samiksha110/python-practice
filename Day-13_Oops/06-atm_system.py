# ===== ATM MENU =====
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit

# Classes , Objects , Methods , if-elif-else , while loop , User input

class Atm:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\n ₹{amount} deposited successfully.")
            print(f"Current Balance : ₹{self.balance}")
        else:
            print("\n Invalid Deposit Amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("\n Invalid Withdraw Amount!")

        elif amount <= self.balance:
            self.balance -= amount
            print(f"\n ₹{amount} withdrawn successfully.")
            print(f"Current Balance : ₹{self.balance}")

        else:
            print("\n Insufficient Balance!")

    def check_balance(self):
        print("\n===== Account Details =====")
        print("Account Holder :", self.name)
        print("Current Balance : ₹", self.balance)


# Creating Object
atm1 = Atm("Samiksha", 5000)


while True:

    print("\n========== ATM MENU ==========")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        amount = int(input("Enter Deposit Amount : ₹"))
        atm1.deposit(amount)

    elif choice == 2:
        amount = int(input("Enter Withdraw Amount : ₹"))
        atm1.withdraw(amount)

    elif choice == 3:
        atm1.check_balance()

    elif choice == 4:
        print("\n Thank You For Using Our ATM!")
        break

    else:
        print("\n Invalid Choice! Please Try Again.")
