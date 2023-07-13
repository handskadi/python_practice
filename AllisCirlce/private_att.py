class BankAccount:
    def __init__(self, account_holder, account_number, balance, pin):
        self.__account_holder = account_holder
        self.__account_number = account_number
        self.__balance = balance
        self.__pin = pin
    
    def display_balance(self):
        print(f"Account balance: {self.__balance}")
    def display_account(self):
        print(f"Account Number: {self.__account_number}")
    def display_account_holder(self):
        print(f"Account holder: {self.__account_holder}")
my_account = BankAccount("Mohamed KADI", "456382945627384950112746", 20000, 2023)

input_pin = int(input("Enter your PIN: "))

if input_pin == my_account._BankAccount__pin:
    print()
    my_account.display_account_holder()
    my_account.display_account()
    my_account.display_balance()
    print()

    def check_input():
        input_choise = int(input("Choose Operation:\n\t1- Check my Balance\n\t2-  Withdraw \n\t3- Exit \n"))
        if input_choise == 1:
            print(f"Mr {my_account._BankAccount__account_holder}: Your current balance: {my_account._BankAccount__balance}")
            check_input()
        if input_choise == 2:
            amount = int(input("Enter your amount: "))
            my_account._BankAccount__balance = my_account._BankAccount__balance - amount
            print(f"\t\tYou withdrow: {amount}\n\t\tYour current balance: {my_account._BankAccount__balance}")
            check_input()
        elif input_choise == 3:
            print("Good bye! have a nice day!")
            exit(0)
        else:
            print("Invalid: back to main Menu")
            check_input()
    check_input()
else:
    print("Incorrect PIN. Access denied.")
