def IntegerToBinary(integer):
    RAnswer=""
    dividend=integer
    divisor=2
    while dividend!=1:
        RAnswer+=str(dividend%divisor)
        dividend=dividend//divisor
    RAnswer+="1"
    return RAnswer[::-1]

def BinaryToInteger(binary):
    reverse=binary[::-1]
    integer=0
    for power in range(len(reverse)):
        integer+=int(reverse[power])*2**power
    return integer

def main():
   while True:
        integer=int(input(" Type an integer : "))
        if integer==0:
            print("It is 0.")
            break
        elif integer<0:
            print("It is negative.")
            break
        else:
            binary=IntegerToBinary(integer)
            decimal=BinaryToInteger(binary)
            print("The binary value of ",integer," is : " ,binary)
            print("Converting the binary of ",integer," is the same with ", integer," ? : ", decimal==integer)
main()
