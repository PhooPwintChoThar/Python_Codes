from ewallet import EWallet

class SmartEWallet(EWallet):
    def __init__(self, owner_name, max_keep, max_take_out):
        super().__init__(owner_name, max_keep)
        self.maximun_take_out=max_take_out
        self.history=[]

    def put_money(self, amount):
       if  super().put_money(amount):
            self.history.append("Put "+str(amount)+" to the account.")

    def take_out_money(self, amount):
        if super().take_out_money(amount):
            self.history.append("Took out  "+str(amount)+" from the account.")

    def view_history(self):
        for record in self.history:
            print(record)


swallet1=SmartEWallet("KO KO", 50000, 20000)
swallet1.put_money(30000)
swallet1.put_money(5000)
swallet1.take_out_money(19000)
swallet1.take_out_money(5000)
swallet1.put_money(6000)
swallet1.put_money(50000)

swallet1.view_history()
print(swallet1.check_current_money())
swallet1.take_out_money(18000)
print(swallet1.check_current_money())
swallet1.take_out_money(16999)
print(swallet1.check_current_money())