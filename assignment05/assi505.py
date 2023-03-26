class BankAccount:
    def _init_(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}. New balance is {self.balance:.2f}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}. New balance is {self.balance:.2f}.")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        print(f"Current balance is {self.balance:.2f}.")

    def get_owner(self):
        print(f"Account owner is {self.owner}.")