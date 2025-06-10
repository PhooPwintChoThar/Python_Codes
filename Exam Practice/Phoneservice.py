from abc import ABC, abstractmethod

class PhoneService(ABC):
    def __init__ (self, phone_no, customer_name, mm_yy):
        self.phnum=phone_no
        self.customer_name=customer_name
        self.month_of_service=mm_yy

    @abstractmethod
    def find_cost(self):
        pass

class Post_paid(PhoneService):
    def __init__(self,ph_no, customer, date, fixed_cost, allowance_minute, used_minutes):
        super().__init__(ph_no, customer, date)
        self.fixed_cost=fixed_cost
        self.allowance_minutes=allowance_minute
        self.used_minutes=used_minutes
        self.cost_extra_minute=1

    def find_cost(self):
        if self.used_minutes<=self.allowance_minutes:
            return self.fixed_cost
        else:
            extra_minute=self.used_minutes-self.allowance_minutes
            return self.fixed_cost+extra_minute*self.cost_extra_minute
        
class Pre_paid(PhoneService):
    def __init__(self,ph, name, date, minutes):
        super().__init__(ph, name, date)
        self.used_minutes=minutes
        self.cost_per_minute=2

    def find_cost(self):
        return self.used_minutes*self.cost_per_minute
    
class Fixed_line(PhoneService):
    def __init__(self,ph,name,date, calls):
        super().__init__(ph, name, date)
        self.num_of_calls=calls
        self.cost_per_call=3

    def find_cost(self):
        return self.num_of_calls*self.cost_per_call
    
