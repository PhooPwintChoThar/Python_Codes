def print_table(list):
    longestLengths = []
    for i in range(len(list[0])):
        tempLength = 0
        for j in range(len(list)):
            tempString = str(list[j][i])
            if len(tempString) > tempLength:
                tempLength = len(tempString)
        longestLengths.append(tempLength)

    for x in range(len(list)):
        for y in range(len(list[0])):
            strLength = longestLengths[y]+3
            print(f"{str(list[x][y]):{strLength}s}", end=" ")
        print()


print_table([["X","Y"],[0,0],[10,10],[200,200]])

print("\n\n")

print_table([
    ["ID", "Name", "Surname"],
    ["001", "Guido", "van Rossum"],
    ["002", "Donald", "Knuth"],
    ["003", "Gordon", "Moore"]
])

print("\n\n")

print_table([
    ["ID", "Name", "Surname"],
    ["001", "Guido van Rossum the Creator of Python", "van Rossum"],
    ["002", "Donald Knuth the Author of The Art of Computer Programming", "Knuth"],
    ["003", "Gordon Moore the Co-founder of Intel Corporation", "Moore"],
    ["004", "Grace Hopper the Pioneer of Computer Programming", "Hopper"]
])
