class Account():
    def __init__(self, account_number: str, balance: float) -> None:
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        print("The current balance is ", self.balance)

class SavingsAccount(Account):
    def __init__(self, account_number: str, balance: float, interest_rate: float, minimum_balance: float) -> None:
        super().__init__(account_number, balance, )
        self.interest_rate = interest_rate 
        self.minimum_balance = minimum_balance

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("You cannot withdraw because you are broke!!!")
        else:
            self.balance -= amount
            

class CheckingAccount(Account):
    def __init__(self, account_number: str, balance: float, transaction_limit: int, transaction_fee: float) -> None:
        super().__init__(account_number, balance)
        self.transaction_limit = transaction_limit
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        if amount > self.transaction_limit:
            self.balance -= (self.transaction_fee + amount)
        self.balance -= amount

    def deposit(self, amount):
            self.balance += amount

#instance of savings account
savings_account = SavingsAccount("S221cs011", 558.1, 67.3, 20)
#displaying it
savings_account.display_balance()



my_withdraw = CheckingAccount("S221cs015", 9000, 500, 0.5)
print("-- CHECKINGS ACCOUNT --")
my_withdraw.display_balance()
my_withdraw.withdraw(50)
my_withdraw.display_balance()



#instance of checking account
checking_account = CheckingAccount("S221cs015", 558.1, 500, 0.5)
#Displaying it
checking_account.display_balance()
