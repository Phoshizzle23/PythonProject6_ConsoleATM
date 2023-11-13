# ATM Project
balance = 10000

while True:
    print("    ATM    ")
    print("""
    1)          Balance
    2)          Withdraw
    3)          Deposit
    4)          Quit
    """)
    try:
        option = int(input("Enter Option: "))
    except ValueError as e:
        print("Error:", e)
        print("Enter 1, 2, 3, or 4 only")
        continue

    if option == 1:
        print("Balance $", balance)

    elif option == 2:
        print("Balance $", balance)
        withdraw = float(input("Enter amount to withdraw $: "))
        if withdraw > 0:
            if withdraw <= balance:
                balance -= withdraw
                print("Forward Balance $", balance)
            else:
                print("Insufficient funds!")
        else:
            print("Invalid amount!")

    elif option == 3:
        print("Balance $", balance)
        deposit = float(input("Enter amount to deposit $: "))
        if deposit > 0:
            balance += deposit
            print("Forward Balance $", balance)
        else:
            print("Invalid amount!")

    elif option == 4:
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid option. Please enter 1, 2, 3, or 4 only.")
