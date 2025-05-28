def my_union(list1,list2):
    union=[]
    union.extend(list1)
    for y in list2:
        if y in union:
            continue
        else:
            union.append(y)
    
    
    return (union)


def my_intersection(list1,list2):
    same=[]
    for x in list1:
        for y in list2:
            if y==x and x not in same:
                #print("append",x)
                same.append(x)
                break
            else:
                continue

    return same

def my_difference(list1,list2):
    difference=[]
    for x in list1:
       if x in list2:
           continue
       else:
           difference.append(x)
    return difference

list1=[3,1,2,7]
list2=[4,1,2,5]

list3=my_union(list1, list2)
print(list3)

list4=my_intersection(list1, list2)
print(list4)

list5=my_difference(list1, list2)
print(list5)