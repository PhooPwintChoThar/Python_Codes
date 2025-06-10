def subset_sum(arr, n, subset):
    if sum(subset) == 0 and len(subset) > 0:
        return True, [subset]
    if n == 0:
        return False, []
    
    found_with, subsets_with = subset_sum(arr, n - 1, subset + [arr[n - 1]])
    found_without, subsets_without = subset_sum(arr, n - 1, subset)

    return (found_with or found_without), subsets_with + subsets_without


def find_zero_sum_subsets(arr):
    found, subsets = subset_sum(arr, len(arr), [])
    if found:
        return "Yes, subsets: " + str(tuple(subsets))
    else:
        return "No"


print(find_zero_sum_subsets([-7, -3, -2, 5, 7]))
print(find_zero_sum_subsets([2, -3, 5, 8, 11, 23, -1]))