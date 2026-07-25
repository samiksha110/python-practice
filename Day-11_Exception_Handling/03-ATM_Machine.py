# Features :
# Check Balance
# Deposit
# Withdraw
# Exception Handling

balance = 10000

try:
    print("\n====== ATM MENU ======")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance = ₹", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Invalid amount")

        else:
            balance += amount
            print("Deposit Successful!")
            print("Current Balance = ₹", balance)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Invalid amount")

        elif amount > balance:
            print("Insufficient Balance")

        else:
            balance -= amount
            print("Please collect your cash.")
            print("Current Balance = ₹", balance)

    elif choice == 4:
        print("Thank you for using our ATM!")

    else:
        print("Invalid Choice")

except ValueError:
    print("Please enter valid numbers only.")
