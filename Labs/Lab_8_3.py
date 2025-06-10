short=input(" Enter a short string : ")
long=input(" Enter a long string : ")
check=0
for x in range(len(long)):
    if long[x]==short[0]:
        check=x
        if long[check:check+len(short)]==short:
            print("The short string is a substring of long string? : ", long[check:check+len(short)]==short)
            break
        else:
            if x==len(long)-1:
                print("The short string is a substring of long string? : ", long[check:check+len(short)]==short)
                break
            else:
                continue
    else:
        if x==len(long)-1:
            print("The short string is a substring of long string? : ", long[check:check+len(short)]==short)
            break
        else:
            continue


