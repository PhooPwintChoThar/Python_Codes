#No.1
class Clock:
    def __init__ (self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second

    def setTime(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second

    def getTime(self):
        print(f"It is {self.hour:02} hr {self.minute:02} minutes {self.second:02} seconds in 24hr format.")
    
    def tick(self):
        self.second+=1
        if self.second>=60:
            self.minute+=1
            self.second-=60
            if self.minute>=60:
                self.hour+=1
                if self.hour==24:
                    self.hour=0
                self.minute-=60
    
    def displayTime(self):
        if 0<=self.hour<=11:
            format="AM"
        else:
            format="PM"

        print(f"{self.hour%12:02} hr {self.minute:02} minutes {self.second} seconds "+format)

time=Clock()
#time.setTime(22,45,33)
#time.setTime(23,59,59)
time.setTime(8,42,59)
time.getTime()
time.tick()
print("increased 1 second.")
time.displayTime()


#No.2(without using arrays)
class Poly:
    def __init__(self,poly=(0,0,0,0,0,0)):
        self.poly=poly+(0,)*(6-len(poly))
        (self.x0,self.x1,self.x2,self.x3,self.x4,self.x5)=self.poly

    def add (self,p):
        if len(p.poly)>6:
            return "Poly is out of range"
        else:
            addedPoly=Poly((self.x0+p.x0,self.x1+p.x1,self.x2+p.x2,self.x3+p.x3,self.x4+p.x4,self.x5+p.x5))
            return addedPoly
    
    def scalar_multiply(self,n):
        scalarmultipliedPoly=Poly((self.x0*n,self.x1*n,self.x2*n,self.x3*n,self.x4*n,self.x5*n))
        return scalarmultipliedPoly

    def multiply(self, p):#multiplied result will show only up to x^5
        mulitipliedPoly=Poly((p.x0*self.x0, p.x0*self.x1+p.x1*self.x0, p.x0*self.x2+p.x1*self.x1+p.x2*self.x0, p.x0*self.x3+p.x1*self.x2+p.x2*self.x1+p.x3*self.x0, p.x0*self.x4+p.x1*self.x3+p.x2*self.x2+p.x3*self.x1+p.x4*self.x0, p.x0*self.x5+p.x1*self.x4+p.x2*self.x3+p.x3*self.x2+p.x4*self.x1+p.x5*self.x0))
        return mulitipliedPoly

    def power(self,n):#please use n with will give x^5 and less than 
        if n==0:
            return Poly((1,))
        else:
            power=self
            for i in range(1,n):
                power=power.multiply(self)
            return power

    def diff(self):
        differentiatedPoly=Poly((self.x1,self.x2*2,self.x3*3,self.x4*4,self.x5*5,0))
        return differentiatedPoly

    def integrate(self):
        integratedPoly=Poly((0,self.x0,self.x1/2,self.x2/3,self.x3/4,self.x4/5))
        return integratedPoly
    
    def eval(self, n):
        evalResult=self.x0+self.x1*n+self.x2*n**2+self.x3*n**3+self.x4*n**4+self.x5*n**5
        return evalResult
    
    def print(self):
        text=""
        for i in range(len(self.poly)):
            if i==0:
                if self.poly[0]==0:
                    continue
                else:
                    text+=f"{self.poly[0]} "
            elif i==1:
                if self.poly[1]==0:
                    continue
                elif self.poly[1]==1:
                    text+="+ x "
                elif self.poly[1]==-1:
                    text+="- x "
                elif self.poly[1]<0:
                    text+=f"- {abs(self.poly[1])}x "
                else:
                    text+=f"+ {abs(self.poly[1])}x "
            else:
                if self.poly[i]==0:
                    continue
                elif self.poly[i]==1:
                    text+=f"+ x^{i} "
                elif self.poly[1]==-1:
                    text+=f"- x^{i} "
                elif self.poly[i]<0:
                    text+=f"- {abs(self.poly[i])}x^{i} "
                else:
                    text+=f"+ {abs(self.poly[i])}x^{i} "
        if text[0]=="+":
            for x in range (1,len(text)):
                print(text[x], end="")
            print()
        else:
                print(text)

p=Poly((1,0,-2))
print("\nPoly = ", end="")
p.print()
q=p.power(2)
print("\nSquare of P (q)is : ", end="")
q.print()
print("\nEvaluate Poly with x=3 is ", p.eval(3))
s=q.scalar_multiply(8)
print("\nMultiply q with 8 is : ", end="")
s.print()
r=p.add(q)
print("\nAdding Poly with q is : ", end="")
r.print()
d=r.diff()
print("\nDifferentiate result of r (d) is",end="")
d.print()
i=d.integrate()
print("\nIntegration of d is : ", end="")
i.print()

#No.2(with using arrays)
class Poly:
    def __init__(self,poly=(1,1,1)):
        self.poly=poly

    def add(self,p):
        addedPoly=[]
        if len(self.poly)>=len(p.poly):
            for x in range (len(self.poly)):
                if x>=len(p):
                    addedPoly.insert(x,self.poly[x])
                else:
                    addedPoly.insert(x,self.poly[x]+p.poly[x])
        else:
            for x in range (len(p.poly)):           
                if x >=len(self.poly):
                    addedPoly.insert(x,p.poly[x])
                else:
                    addedPoly.insert(x,self.poly[x]+p.poly[x])

        return Poly(tuple(addedPoly))

    def scalarMultiply(self,n):
        resultPoly=[]
        for i in range(len(self.poly)):
            resultPoly.insert(i,self.poly[i]*n)
        return Poly(tuple(resultPoly))
    
    def multiply(self, p):
        new=[]
        length=len(self.poly)+len(p.poly)-1
        for x in range(length):
            new.insert(x,0)
        for y in range (len(p.poly)):
            for z in range(len(self.poly)):
                new[y+z]+=p.poly[y]*self.poly[z]
        return Poly(tuple(new))
    
    def power(self,n):
        if n==0:
            return Poly((1,))
        else:
            result=self
            for i in range(1,n):
                result=result.multiply(self)
            return result
        
    def diff(self):
        result=list(self.poly)
        for i in range(len(self.poly)):
            if i==len(self.poly)-1:
                result[i]=0
            else:
                result[i]=result[i+1]*(i+1)
                
        return Poly(tuple(result))
    
    def integrate(self):
        result=list(self.poly)
        result.insert(0,0)
        for i in range(1,len(self.poly)+1):
            result[i]=self.poly[i-1]/(i)
        return Poly(tuple(result))
        
    def print(self):
        text=""
        for i in range(len(self.poly)):
            if i==0:
                if self.poly[0]==0:
                    continue
                else:
                    text+=f"{self.poly[0]} "
            elif i==1:
                if self.poly[1]==0:
                    continue
                elif self.poly[1]==1:
                    text+="+ x "
                elif self.poly[1]==-1:
                    text+="- x "
                elif self.poly[1]<0:
                    text+=f"- {abs(self.poly[1])}x "
                else:
                    text+=f"+ {abs(self.poly[1])}x "
            else:
                if self.poly[i]==0:
                    continue
                elif self.poly[i]==1:
                    text+=f"+ x^{i} "
                elif self.poly[1]==-1:
                    text+=f"- x^{i} "
                elif self.poly[i]<0:
                    text+=f"- {abs(self.poly[i])}x^{i} "
                else:
                    text+=f"+ {abs(self.poly[i])}x^{i} "
    
        if text[0]=="+":
            for x in range (1,len(text)):
                print(text[x], end="")
            print()
        else:
                print(text)
    

po=Poly((1,0,2,0,0,1))
print("\nPoly = ",end="")
po.print()
Adding=po.add(Poly((0,2,0,0,2,0,4)))
print("\nAdding 2x+2x^4+4x^6 to Poly = ", end="")
Adding.print()
Scalar=po.scalarMultiply(4)
print("\nMultiplying poly with 4 = ", end="")
Scalar.print()
Multiply=po.multiply(Poly((0,3,0,5)))
print("\nMultiplying Poly with (3x+5x^3) = ", end="")
Multiply.print()
Power=po.power(4)
print("\n4th power of poly is : ", end="")
Power.print()
Differ=po.diff()
print("\nDifferentiate result of Poly is : ",end="")
Differ.print()
Inte=Differ.integrate()
print("\nIntegrate result of Differentiated Poly is : c(constant) + ",end="")
Inte.print()




#No.3
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