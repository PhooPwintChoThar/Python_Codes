typed_number=input("Enter a four-digit integer:")
while len(typed_number) >4:
    print("Please type only 4 digits. ")
    typed_number=input("Enter a four-digit integer:")
else :
    print("The number you typed is :  ", typed_number)

    reversed_number=""
    x=len(typed_number)-1
    while x>=0:
      reversed_number+=typed_number[x]
      x-=1

    print("The number in reverse order is : ", reversed_number)

