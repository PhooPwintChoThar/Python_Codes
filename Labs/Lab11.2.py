class Calculator(object):
    def __init__(self, acc=0.00):
        self.acc=float(acc)

    def set_accumulator(self, a):
        self.acc=float(a)

    def get_accumulator(self):
        return self.acc
    
    def add(self, x):
        self.acc+=float(x)

    def subtract(self, x):
        self.acc-=float(x)

    def multiply(self, x):
        self.acc*=float(x)

    def divide(self, x):
        self.acc/=float(x)

    def print_result(self):
        print(f"Result : {self.get_accumulator()}")

class Sci_calc(Calculator):
    def __init__ (self, x):
        super().__init__(x)
    def square(self):
        self.acc=self.acc**2
    
    def exp(self, x):
        for i in range(1,x):
            self.acc*=self.acc

    def factorial(self):
        a=self.acc-1
        while a!=0:
            self.acc*=a
            a-=1
    
    def print_result(self):
        print(f" Result :{self.get_accumulator():.1e}")


ca=Sci_calc(10)
ca.exp(2)
ca.print_result()
ca.factorial()
ca.print_result()

