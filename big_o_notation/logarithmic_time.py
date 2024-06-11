def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Explanation: This function reduces the search space by half in each iteration.
# As the size of 'lst' increases, the number of iterations (steps) required grows logarithmically.

print(binary_search([1, 2, 3, 4, 5], 3))  # 2

# Time Complexity: O(log n) (Logarithmic Time)
# Explanation: The time complexity of binary search is logarithmic because the search space is halved in each iteration.
# This means that the time taken to search for an element in a sorted list grows logarithmically as the size of the list increases.