def isAnagram(str1,str2):

    if len(str1)!=len(str2):
        return f"{str1} and {str2} are not anagrams."
    else:
        check1=[]
        check1.extend(str1)
        check2=[]
        check2.extend(str2)

        for x in check1:
            for y in check2:
                if y==x:
                    check2.remove(y)

        if len(check2)==0:
            return f"{str1} and {str2} are  anagrams."
        else:
            return f"{str1} and {str2} are not anagrams."


print(isAnagram("silent", "listen"))  
print(isAnagram("triangle", "integral"))  
print(isAnagram("apple", "papel"))  
print(isAnagram("evil", "vile"))  
print(isAnagram("fluster", "restful"))  
print(isAnagram("abcd", "dcba")) 
print(isAnagram("rat", "car"))  
print(isAnagram("hello", "world"))  # isAnagram("hello", "world")
