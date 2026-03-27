# Simple ATM Simulator

balance = 10000   # starting money
pin = "1234"      # default pin

print("===== Welcome to Python ATM =====")

entered_pin = input("Enter your PIN: ")

if entered_pin != pin:
    print("Wrong PIN. Access Denied!")
else:
    while True:
        print("\n--- MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose option (1-4): ")

        if choice == "1":
            print("Your balance is:", balance)

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            balance += amount
            print("Deposit successful!")

        elif choice == "3":
            amount = int(input("Enter withdraw amount: "))
            if amount > balance:
                print("Insufficient balance!")
            else:
                balance -= amount
                print("Withdrawal successful!")

        elif choice == "4":
            print("Thank you for using ATM. Bye!")
            break

        else:
            print("Invalid option. Try again.")
