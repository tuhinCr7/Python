class Bank:
    
    def __init__(self,accounts_holder,balance):
        self.accounts_holder=accounts_holder
        self.balance=balance
    
    def deposit(self,amount):
            self.balance+=amount

    def display(self):
         print(f"Account's holder name : {self.accounts_holder}")
         print(f" balance is : {self.balance}") 

class SavingsAccount(Bank):
     def __init__(self, accounts_holder, balance,interest_rate):
          super().__init__(accounts_holder, balance)
          self.interest_rate=interest_rate
     def Add_interest(self):
          interest=self.balance*(self.interest_rate/100)
          self.balance+=interest     

tuhin=Bank("Tuhin",50000)
tuhin.deposit(5000)
tuhin.display()
armaan=SavingsAccount("armaan",15000,20) 
armaan.Add_interest()
armaan.display()