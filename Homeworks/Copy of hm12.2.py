def composite(dict1, dict2):
    composite={}
    for x in dict1:
        for y in dict2:
            if dict1[x]==y:
                composite[x]=dict2[y]

    return composite


dict1={'a':'p', 'b':'r', 'c':'q', 'd':'p',  'e':'s'}
dict2={'p':'1', 'q':'2', 'r':'3'}
print(composite(dict1, dict2))