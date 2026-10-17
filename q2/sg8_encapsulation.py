# Creates BankAccount class
class BankAccount:

# Initializes both account number and balance
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

# Updates account number
    def set_account_number(self, account_number):
        self.__account_number = account_number

# Only updates balance if input is not negative
    def set_balance(self, balance):
        if balance < 0:
            print("The balance must not be a negative number.")
        else:
            self.__balance = balance

# Obtain account number
    @property
    def account_number(self):
        return self.__account_number

# Obtain balance
    @property
    def balance(self):
        return self.__balance

a1 = BankAccount(12345, 1000) # Makes BankAccount object
a1.set_account_number(12345) # Upfates account number

# Displays account information
print("Account 1")
print("Account Number:", a1.account_number)
print(f"Balance: {a1.balance:.2f}")
print()
# Tries to change balance to negative value
print("Update balance to -100")
a1.set_balance(-100)
# Displays retained account information after the attempted update
print("Account Number:", a1.account_number)
print(f"Balance: {a1.balance:.2f}")