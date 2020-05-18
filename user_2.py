class User:
    def __init__(self, username, balance = 0):
        self.name = username
        self.account_balance = balance

    def make_deposit(self, amount):
        self.account_balance += amount 
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        self.display_user_balance
        return self

    def transfer_money(self, other_user, amount):
        self.transfer_money = amount 

guido = User("Guido Van Rossum", 150)
monty = User("Monty")
michael = User("Michael")

guido.make_deposit(50).make_deposit(200).make_deposit(100).make_withdrawal(100)

monty.make_deposit(20).make_deposit(250).make_withdrawal(100).make_withdrawal(50)

michael.make_deposit(50).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100)


print("User" , guido.name, "Balance:" , guido.account_balance)
print("User" , monty.name, "Balance:" , monty.account_balance)
print("User" , michael.name, "Balance:" ,michael.account_balance)



