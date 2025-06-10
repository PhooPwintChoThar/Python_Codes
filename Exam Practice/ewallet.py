class EWallet:
    def __init__(self, owner_name,maximum_keep ):
        self.ownername=owner_name
        self.maximum_keep_amount=maximum_keep
        self.current_balance=0

    def put_money(self, amount):
        if self.current_balance+amount<=self.maximum_keep_amount:
            self.current_balance+=amount
            return True
        return False

    def take_out_money(self, amount):
        if self.current_balance>=amount:
            self.current_balance-=amount
            return True
    
        return False

    def check_current_money(self):
        return self.current_balance
    

Account1=EWallet("MG MG", 50000)
Account1.put_money(30000)
#print(Account1.check_current_money())
Account1.put_money(30000)
#print(Account1.check_current_money())
Account1.take_out_money(10000)
#print(Account1.check_current_money())

    