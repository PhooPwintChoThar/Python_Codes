

def merge(list1, list2):
    new = list1
    for y in list2:
        inserted = False
        for i in range(len(new)):
            if y < new[i]:
                new.insert(i, y)
                inserted = True
                break
        if not inserted:
            new.append(y)
    
    return new

list1 = [1, 5, 16, 61, 111]
list2 = [2, 4, 5, 6]
print(merge(list1, list2))
