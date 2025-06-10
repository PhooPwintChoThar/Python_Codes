def tower(n,fromone, toone, axuone):
    if n==1:
        print(n, "moved from ",fromone," to ",toone)
    else:
        tower(n-1, fromone, axuone, toone)
        print(n, "moved from ",fromone," to ",toone)     
        tower(n-1, axuone, toone, fromone)


tower(4, "A", "B", "C")
