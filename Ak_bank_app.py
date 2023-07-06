class Account():
    def __init__(self, account_number: str, balance: float) -> None:
        self.account_number = account_number
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, account_number: str, balance: float, interest_rate, minimum_balance) -> None:
        super().__init__(account_number, balance, )
        self.interest_rate = interest_rate 
        self.minimum_balance = minimum_balance
        