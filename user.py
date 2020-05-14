class User:
    def __init__(self, rate, balance):
        self.account_balance = balance
        self.rate = rate 

    def make_deposit(self, amount):
        self.account_balance += amount 
        return self 

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print("Balace", self.account_balance)
        return self

    def yield_interest(self):
        if self.account_balance > 0: 
            print("Int", self.account_balance * self.rate)
        return self 

guido = User(0.04, 300)
michael = User(0.05, 200)

guido.make_deposit(50).make_deposit(200).make_deposit(100).make_withdrawal(100).yield_interest().display_user_balance()

michael.make_deposit(100).make_deposit(300).make_withdrawal(50).make_withdrawal(100).yield_interest().display_user_balance()



