def reverse (num):
    number=str(num)
    result=""
    for i in range(len(number)-1,-1,-1):
        result+=number[i]
    return int(result)

number=8732
result=reverse(number)
print(f"Reverse of {number}  is" , result)

