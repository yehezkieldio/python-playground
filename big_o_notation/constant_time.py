def constant_time_example(lst):
    return lst[0]

# Explanation: This function always takes the same amount of time to execute,
# regardless of the size of the list, because it only accesses the first element.

print(constant_time_example([1, 2, 3]))  # 1

# Time Complexity: O(1) (Constant Time)
# Explanation: The time complexity of this function is constant because it always takes the same amount of time to execute,
# regardless of the size of the list. The number of operations does not depend on the input size.