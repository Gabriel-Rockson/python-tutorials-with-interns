class Account:
    def __init__(self,*,account_number: str,balance: float) -> None:
       self.account_number=account_number
       self.balance=balance 

class SavingsAccount(Account):
   def __init__(self,interest_rate: float, minimum_balance: float): 
       self.interest_rate= interest_rate
       self.minimum_balance = minimum_balance
       account_number=1234567890
       balance=  300000000 
       super().__init__(account_number, balance) 