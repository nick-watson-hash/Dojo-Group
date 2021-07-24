class BankAccount:
    def __init__(self, int_rate=0.75, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
            self.balance += amount
            return self
    def withdraw(self, amount):
        self.balance -= amount
        if amount < 0:
            print("Insufficient funds: Charging a 5$ fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        self.balance = self.balance + self.balance * self.int_rate
        return self

naccount=BankAccount()
naccount.deposit(100).deposit(1000).deposit(500).withdraw(330).yield_interest().display_account_info()

jaccount=BankAccount()
jaccount.deposit(200).deposit(300).withdraw(75).withdraw(20).withdraw(10).withdraw(20).yield_interest().display_account_info()