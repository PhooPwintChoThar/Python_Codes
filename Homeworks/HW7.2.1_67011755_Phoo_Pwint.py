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
