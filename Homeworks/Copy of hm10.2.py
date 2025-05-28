def bubble_sort(inputList):
    list=[]
    list.extend(inputList)
    anySort=True
    print("Initial", list)

    while anySort:
        anySort=False
        for number in range(len(list)-1):
            print(list)
            if list[number]>list[number+1]:
                temp=list[number+1]
                list[number+1]=list[number]
                list[number]=temp
                anySort=True
            
    return list

print(bubble_sort([22,4,5,3,9,6,8,0]))