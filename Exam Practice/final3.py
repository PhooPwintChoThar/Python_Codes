def check_depth(x):
    if type(x)==int:
        return 0
    elif type(x)==list:
        inner_depth=0
        for item in x:
            if type(item)==list:
                each_depth=check_depth(item)
                if each_depth>inner_depth:
                    inner_depth=each_depth
        return inner_depth+1
    else:
        print("Invalid Type")


print(check_depth([1,[2,5,[3,[[1,[2]]]]],[4,[3]]]))