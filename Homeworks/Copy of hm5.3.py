integer=int(input("Enter any integer greater than or equal to 1 : "))
while integer<1:
    integer=int(input("Invalid!\nEnter any integer greater than or equal to 1 : "))
if integer==1:
    print("*")
else:
    for a in range(integer,-1,-1):
        if a==0:
            print("*")
            break
        for b in range (a):
            for c in range (b+1):
                print("*",end="")
            print("\n")
            if b==a-1:
                for d in range(b-1):
                    for e in range (b-d):
                        print("*",end="")
                    print("\n")

    

    