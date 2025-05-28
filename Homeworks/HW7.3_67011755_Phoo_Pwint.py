class LinearEquation:
    def __init__(self, a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f

    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getD(self):
        return self.__d
    
    def getE(self):
        return self.__e
    
    def getF(self):
        return self.__f
    
    def isSolvable(self):
        if self.getA()*self.getD()-self.getB()*self.getC()==0:
            return False
        else:
            return True
#coefficients=LinearEquation(2,3,4,6,6,10)    
coefficients=LinearEquation(2,3,1,-4,6,5)
if coefficients.isSolvable():
    print("x = ", (coefficients.getE()*coefficients.getD()-coefficients.getB()*coefficients.getF())/(coefficients.getA()*coefficients.getD()-coefficients.getB()*coefficients.getC()))
    print("y = ", (coefficients.getA()*coefficients.getF()-coefficients.getE()*coefficients.getC())/(coefficients.getA()*coefficients.getD()-coefficients.getB()*coefficients.getC()))
else:
    print("It is unsolvable")
