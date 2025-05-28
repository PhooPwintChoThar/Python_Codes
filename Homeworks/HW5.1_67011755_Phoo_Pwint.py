n=int(input("Type a number which you want to find it square root : "))
guess=n/2
temp=n/guess
guess=(guess+temp)/2

for x in range(5):
    temp=n/guess
    guess=(guess+temp)/2
print("Square root of",n," by iterating 5 times: ",format(guess,".3f"))
for y in range(6):
    temp=n/guess
    guess=(guess+temp)/2
print("Square root of",n," by iterating 6 times: ",format(guess,".3f"))
for z in range(7):
    temp=n/guess
    guess=(guess+temp)/2
print("Square root of",n," by iterating 7 times: ",format(guess,".3f"))
