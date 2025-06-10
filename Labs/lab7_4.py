import math

class QuadraticEquation:
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c

    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getDiscriminant(self):
        return self.getB()**2-(4*self.getA()*self.getC())
    
    def  getRoot1(self):
        return abs(math.sqrt(self.getDiscriminant()))
    
    def getRoot2(self):
        return -abs(math.sqrt(self.getDiscriminant()))
    
equation=QuadraticEquation(4,8,2)
if equation.getDiscriminant()<=0:
    print("0")
else :
    ans1=(-equation.getB()+equation.getRoot1()/(2*equation.getA()))
    ans2=(-equation.getB()+equation.getRoot2()/(2*equation.getA()))
    print("answers are :",ans1," and ",ans2)