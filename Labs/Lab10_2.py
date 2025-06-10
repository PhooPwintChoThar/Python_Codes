def listing(list):
    count=0
    for x in list:
        if count!=2:
            count+=1
            continue
        else :
            list.remove(x)
            count=1

list1=[3,6,6,3,7,2,0,1,5,4]
listing(list1)

print(list1)