class Account():
    def __init__(self, account_number: str, balance: float) -> None:
        self.account_number = account_number
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, account_number: str, balance: float, interest_rate: float, minimum_balance: float) -> None:
        super().__init__(account_number, balance, )
        self.interest_rate = interest_rate 
        self.minimum_balance = minimum_balance

class CheckingAccount(Account):
    def __init__(self, account_number: str, balance: float, transaction_limit: int, transaction_fee: float) -> None:
        super().__init__(account_number, balance)
        self.transaction_limit = transaction_limit
        self.transaction_fee = transaction_fee
