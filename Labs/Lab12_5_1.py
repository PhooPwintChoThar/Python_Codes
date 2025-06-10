
import math

def power(s: set):
    s_list = list(s)
    
    power_set: list = []
    
    # total number of subsets
    pow_set_size = int(math.pow(2, len(s)))

    # all subsets using bit manipulation
    for counter in range(pow_set_size):
        temp = []
        for j in range(len(s)):
            # Check if jth bit in the counter is set
            if counter & (1 << j):
                temp.append(s_list[j])
        # appending to power_set as a frozenset
        power_set.append(frozenset(temp))
    # convert list to set again
    return set(power_set)

s = {1, 2, 3}
print(power(s))