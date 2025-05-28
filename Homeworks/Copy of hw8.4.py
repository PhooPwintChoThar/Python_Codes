BookNumber=input("Enter the first 9 digits of an ISBN-10 as a string : ")
while len(BookNumber)!=9 or BookNumber[0]!="0" :
    BookNumber=input("Invalid!\nEnter the first 9 digits of an ISBN-10 as a string : ")

checksum=0
for i in range(1,10):
    checksum+=int(BookNumber[i-1])*i
checksum%=11

if checksum==10:
    BookNumber+="X"
else:
    BookNumber+=str(checksum)

print("Your ISBN-10 number is : ",BookNumber)