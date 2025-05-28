def product(sets): 
    items = [list(x) for x in sets] 

    def production(items):
        if len(items) == 2:
            result = []
            for first in items[0]:
                for second in items[1]:
                    result.append((first, second))
            return result
        else:
            other_product = production(items[1:])
            result = []
            for first in other_product:
                for second in items[0]:
                    result.append(first + (second,)) 
            return result

    if len(items) <= 1:
        result = [(x,) for x in items[0]]
        return set(result)
    else:
        result = production(items)  
        return set(result) 


s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])
result = product((s1, s2, s3))
print("Result is:\n", result)

