text=input("Enter some text : ")
check=''
for c in text:
    if c in check:
        continue
    else:
        check+=c

for a in check:
    count=0
    for b in text:
        if b==a:
            count+=1
        else:
            continue
    print(f"{a}\t{(count/len(text)):>7.2%}")
