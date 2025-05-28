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




