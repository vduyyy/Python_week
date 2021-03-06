class BankAccount:
    def __init__(self,rate, balance):
        self.account_balance = balance 
        self.rate = rate

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if  self.account_balance > amount:
             self.account_balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5 
        return self

    def display_account_info(self):
        print("Net Balance =", self.account_balance)
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            print ("Interest:" ,self.account_balance * self.rate)
        return self

michael = BankAccount(0.05,200)
monty = BankAccount(0.01,100)

michael.deposit(100).deposit(50).deposit(20).withdraw(90).yield_interest().display_account_info()
monty.deposit(200).deposit(400).withdraw(30).withdraw(50).withdraw(200).yield_interest().display_account_info()

