from abc import ABC, abstractmethod

class Transporation(ABC):
    def __init__(self, start_place, end_place, distance):
        self.start_place=start_place
        self.end_place=end_place
        self.distance=distance

    @abstractmethod
    def find_cost(self):
        pass

class Walk(Transporation):
    def find_cost(self):
        return 0
    

class Taxi(Transporation):

    def __init__(self, start, end, distance):
        super().__init__(start, end, distance)
        self.cost_per_kilometer=40

    def find_cost(self):
        return self.distance*self.cost_per_kilometer
    
class Train(Transporation):
    def __init__(self, start, end, distance, stations):
        super().__init__(start, end, distance)
        self.stations=stations
        self.cost_per_station=5

    def find_cost(self):
        return self.stations*self.cost_per_station

def calculate_cost(activities):
    total_cost=0
    for a in activities:
        total_cost+=a.find_cost()

    return total_cost

def main():
    JohnActivities=[Walk("KMITL", "Lawson at KMITL", 0.6),
                    Taxi("Lawson at KMITL", "Latkrabang Station", 5),
                    Train("Ladkrabang Station", "Payathai Station", 40, 6),
                    Taxi("Phayathai Station", "The British Council",3)]
    
    total_cost=calculate_cost(JohnActivities)
    print(total_cost)

main()