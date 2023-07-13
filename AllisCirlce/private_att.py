class BankAccount:
    def __init__(self, account_number, balance, pin):
        self.__account_number = account_number
        self.__balance = balance
        self.__pin = pin
    
    def display_balance(self):
        print(f"Account balance: {self.__balance}")
    def display_account(self):
        print(f"Account Number: {self.__account_number}")

my_account = BankAccount("456382945627384950112746", 20000, 2023)

input_pin = int(input("Enter your PIN: "))

if input_pin == my_account._BankAccount__pin:
    print()
    my_account.display_balance()
    my_account.display_account()
    print()

    def check_input():
        input_choise = int(input("Choose Operation:\n\t1- Check my Balance\n\t2-  Withdraw \n\t3- Exit \n"))
        if input_choise == 1:
            print(f"Your current balance: {my_account._BankAccount__balance}")
            check_input()
        if input_choise == 2:
            amount = int(input("Enter your amount: "))
            my_account._BankAccount__balance = my_account._BankAccount__balance - amount
            print(f"\t\tYou withdrow: {amount}\n\t\tYour current balance: {my_account._BankAccount__balance}")
            check_input()
        elif input_choise == 3:
            print("Good bye! have a nice day!")
            pass
        else:
            print("Invalid: back to main Menu")
            check_input()
    check_input()
else:
    print("Incorrect PIN. Access denied.")
