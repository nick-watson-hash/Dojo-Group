class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
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

class User:
    def __init__(self, username):
        self.username = username
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def display_user_balance(self):
        print(f"User: {self.username}, Balance: ${self.account.balance}")
        return self
    
    def transfer_money(self, other_user, amount):
        other_user.account.deposit(amount)
        self.account.withdraw(amount)
        return self
    
    def sensei_account(self):
        self.account.deposit(100)
        print(self.account.balance)

nick = User("Nick")
nick.make_deposit(100).make_deposit(23).make_deposit(69).make_withdrawal(121).display_user_balance()

jacob = User("Jacob")
jacob.make_deposit(100).make_deposit(23).make_withdrawal(40).make_withdrawal(25).display_user_balance()

dominic = User("Dominic")
dominic.make_deposit(500).make_withdrawal(65).make_withdrawal(109).make_withdrawal(44).display_user_balance()

#Bonus
nick.transfer_money(jacob,250)
nick.display_user_balance()
jacob.display_user_balance()