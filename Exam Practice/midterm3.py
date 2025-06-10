line=1
while line<10:
    num=1
    while num<10:
        if num==line:
            num+=1
            continue
        else:
            print(num,end="")
            num+=1
    print()
    line+=1