names=[]
def name_list():
    
    name=input("Enter name 1: ")
    name_no=1
    while name!="":
        names.append(name)
        name_no+=1
        name=input("Enter name "+str(name_no)+": ")

name_list()
print(names)