list1=[3,1,1,1,2,7]
list2=[4,1,1,2,2,5]


def get_the_difference(list1,list2):
    difference=[]
    for x in list1:
        for y in list2:
            if y==x:
                break
            else:
                if y==list2[len(list2)-1]:
                    difference.append(x)
                continue

    for a in list2:
        for b in list1:
            if b==a:
                break
            else:
                if b==list1[len(list1)-1] and a not in difference:
                    difference.append(a)
                continue
    return difference

print(get_the_difference(list1,list2))
            
