string="book,dog,drink,rain,pen"
for i in string:
    if i==",":
        print("\n")
    else:
        print(i,end="")
