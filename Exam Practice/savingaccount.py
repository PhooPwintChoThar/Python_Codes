class SavingAccount:
    def __init__(self, bank_name, acc_name, acc_id):
        self.bank_name=bank_name
        self.acc_name=acc_name
        self.acc_id=acc_id
        self.balance=0
        self.transcation_history=[]

    def deposit(self, money, person, date):
        self.balance+=money
        self.transcation_history.append("Deposit "+str(money)+" by "+person+" to the account on "+date)

    def withdraw(self, money, person, date):
        if self.balance>=money:
            self.balance-=money
            self.transcation_history.append("Withdraw "+str(money)+" by "+person+" from the account on "+date)

    def get_balance(self):
        print("Your balance is : ", self.balance)
    
    def print_statement(self):
        for x in self.transcation_history:
            print(x)


class OverDrawnAccount(SavingAccount):
    def __init__(self,bank_name, acc_name, acc_id):
        super().__init__(bank_name, acc_name, acc_id)
        self.over_drawn_limit=2000

    def withdraw(self, money, person,date):
        if money<=(self.balance+self.over_drawn_limit):
            self.balance-=money
            self.transcation_history.append("Withdraw "+str(money)+" by "+person+" from the account on "+date)


Account1=SavingAccount("K-Bank", "Visit", "42342")
Account1.deposit(50000, "VisitHi", "11.2.2024")
Account1.withdraw(30000, "Hi", "16.2.2024")
Account1.withdraw(30000, "Hi", "17.2.2024")

Account2=OverDrawnAccount("Kasikorn Bank", "Sweet", "099877")
Account2.deposit(50000, "pp", "11.2.2024")
Account2.withdraw(30000, "CT", "16.2.2024")
Account2.withdraw(21000, "Sweet", "17.2.2024")
Account2.withdraw(1100, "Sweet", "17.2.2024")

Account1.get_balance()
Account1.print_statement()
Account2.get_balance()
Account2.print_statement()

