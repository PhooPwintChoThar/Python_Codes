import random
times=int(input("Times :"))
if times<0:
    print("Invalid time")
face1=0
face2=0
face3=0
face4=0
face5=0
face6=0
for time in range(times):
    face=random.randint(0,6)
    while face==0:
        face=random.randint(0,6)
    if face==1:
        face1+=1
    elif face==2:
        face2+=1
    elif face==3:
        face3+=1
    elif face==4:
        face4+=1
    elif face==5:
        face5+=1
    else:
        face6+=1

print(f" 1 : {face1}")
print(f" 2 : {face2}")
print(f" 3 : {face3}")
print(f" 4 : {face4}")
print(f" 5 : {face5}")
print(f" 6 : {face6}")
