def reverse_list(list):
    if len(list) == 1:
        return list
    return reverse_list(list[1:]) + [list[0]]

my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)
print(reversed_list) 
