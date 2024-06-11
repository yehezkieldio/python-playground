def linear_time_example(lst):
    for item in lst:
        print(item)

# Explanation: This function takes time proportional to the size of the list 'lst'.
# As the size of 'lst' increases, the time taken to print each element increases linearly.

print(linear_time_example([1, 2, 3]))  # 1 2 3

# Time Complexity: O(n) (Linear Time)
# Explanation: The time complexity of this function is linear because it has a single loop that iterates over the list 'lst'.
# As the size of 'lst' increases, the number of iterations (steps) required grows linearly.