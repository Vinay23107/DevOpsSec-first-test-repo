class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance


# Example usage:
account_holder_name = "Steven Walker"
initial_balance = 1000
Stevens_account = BankAccount(account_holder_name, initial_balance)

print(f"{Stevens_account.account_holder}'s initial balance: ${Stevens_account.get_balance()}")

Stevens_account.deposit(500)
Stevens_account.withdraw(200)
Stevens_account.withdraw(1000)
Stevens_account.deposit(-50)  # Invalid deposit amount

print(f"{Stevens_account.account_holder}'s final balance: ${Stevens_account.get_balance()}")
