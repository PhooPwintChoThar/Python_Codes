
def powerset(a):
    sets = list(a)
    
    # Base case: return set containing empty set
    if len(sets) == 0:
        return {frozenset()}  # Return set containing empty frozenset instead of {}
    
    # Take first element as a frozenset
    add = frozenset({sets[0]})
    
    # Recursive call for remaining elements
    remain_sets = powerset(set(sets[1:]))
    
    result = []
    # For each subset in remaining sets
    for x in remain_sets:
        result.append(x)  # Add subset without first element
        result.append(frozenset.union(add, x))  # Add subset with first element
    
    return set(result)

# Test the function
print(powerset({1,2,3}))