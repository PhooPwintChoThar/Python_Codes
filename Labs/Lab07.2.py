class BankAccount:
    def __init__(self,bankName,ownerName,accountNumber,currentBalance=0):
        self.bankName=bankName
        self.ownerName=ownerName
        self.accountNumber=accountNumber
        self.currentBalance=currentBalance

    def deposit(self, depositMoney):
        self.currentBalance+=depositMoney

    def withdraw(self, withdrawMoney):
        self.currentBalance-=withdrawMoney

    def printBalance(self):
        print("Current balance of ",self.ownerName," in " ,self.bankName, " bank : ",self.currentBalance)


user=BankAccount("SCB","Tom","78865")
user.deposit(1000)
user.withdraw(230)
user.printBalance()
