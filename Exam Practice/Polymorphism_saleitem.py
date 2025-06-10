from abc import ABC, abstractmethod

class Sale_item(ABC):
    @abstractmethod
    def get_price(self):
        pass

class Food(Sale_item):
    @abstractmethod
    def get_price(self):
        pass

class ItemizedFood(Sale_item):
    def __init__(self,count, price):
        self.price=price
        self.count=count

    def get_price(self):
        return self.count*self.price
    
class MeasuredFood(Food):
    def __init__(self,weight, price):
        self.weight=weight
        self.price=price

    def get_price(self):
        return self.weight*self.price
    
class Book(Sale_item):
    def __init__(self, price) :
       self.price=price

    def get_price(self):
        return self.price*0.85
    
class Appliance(Sale_item):
    def __init__(self, price):
        self.price=price

    def get_price(self):
        return self.price*1.07
    

def main():
    purchased_item=[ItemizedFood(2,40), MeasuredFood(1.8, 70), Book(200), Appliance(1200)]
    t=total_cost(purchased_item)
    print("Total cost is:",t)




def total_cost(items):
    total=0
    for item in items:
        total+=item.get_price()

    return total


main()



