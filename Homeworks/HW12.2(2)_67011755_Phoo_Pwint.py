from abc import ABC, abstractmethod

class StationaryGood(ABC):
    @abstractmethod
    def get_cost(self):
        pass

class Magazine(StationaryGood):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_cost(self):
        return self.price

class Book(StationaryGood):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_cost(self):
        return self.price * 0.9 

class Ribbon(StationaryGood):
    def __init__(self, length):
        self.length = length
    
    def get_cost(self):
        return self.length * 5  

def getTotalCost(basket):
    return sum(item.get_cost() for item in basket)


basket = [
    Magazine("Computer World", 70),
    Magazine("Computer World", 70),
    Magazine("Computer World", 70),
    Book("Windows 7 for Beginners", 200),
    Book("Windows 7 for Beginners", 200),
    Ribbon(10)
]

total_cost = getTotalCost(basket)
print(f"The total cost of the goods is: {total_cost} Bahts")
