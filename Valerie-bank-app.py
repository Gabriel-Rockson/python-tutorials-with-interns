class Account:
    def __init__(self, *, account_number: str, balance: float) -> None:
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        print("Current balance:", self.balance)


class SavingsAccount(Account):
    def __init__(
        self,
        account_number: str,
        balance: float,
        interest_rate: float,
        minimum_balance: float,
    ):
        super().__init__(account_number=account_number, balance=balance)
        self.interest_rate = interest_rate
        self.minimum_balance = minimum_balance

    def apply_interest(self):
        interest = self.interest_rate * self.balance
        self.balance += interest

    def withdraw(self, amount: float):
        if self.balance - amount < self.minimum_balance:
            print("Unable to redraw funds")
        else:
            self.balance -= amount


class CheckingAccount(Account):
    def __init__(
        self,
        account_number: str,
        balance: float,
        transaction_limit: int,
        transaction_fee: float,
    ):
        super().__init__(account_number=account_number, balance=balance)
        self.transaction_limit = transaction_limit
        self.transaction_fee = transaction_fee

    def withdraw(self, amount: float):
        if self.amount > self.transaction_limit:
            self.balance - self.transaction_fee
        self.balance -= amount

    def deposit(self, amount: float):
        self.balance += amount


account_number = "1234567890"
balance = 30000000
interest_rate = 0.5
minimum_balance = 0.5
transaction_limit = 500
transaction_fee = 50

savings_account = SavingsAccount(
    account_number, balance, interest_rate, minimum_balance
)
checking_account = CheckingAccount(
    account_number,
    balance,
    transaction_limit,
    transaction_fee,
)
savings_account.display_balance()
savings_account.withdraw(50000)
savings_account.display_balance()
checking_account.deposit(20)
