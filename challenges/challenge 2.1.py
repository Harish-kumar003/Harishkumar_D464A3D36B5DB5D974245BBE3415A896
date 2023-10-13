class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance
    
    def deposit(self, amount):
        self.__account_balance += amount
    
    def withdraw(self, amount):
        if self.__account_balance >= amount:
            self.__account_balance -= amount
        else:
            print("Insufficient balance.")
    
    def display_balance(self):
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Balance: {self.__account_balance}")



account = BankAccount("1234567890", "Harish kumar", 1500)
account.display_balance()

account.deposit(600)
account.display_balance()

account.withdraw(300)
account.display_balance()
