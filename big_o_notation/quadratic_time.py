def quadratic_time_example(lst):
    for i in lst:
        for j in lst:
            print(i, j)

# Explanation: This function takes time proportional to the square of the size of 'lst'.
# As the size of 'lst' increases, the time taken to print pairs of elements grows quadratically.

print(quadratic_time_example([1, 2, 3]))  # 1 1 1 2 1 3 2 1 2 2 2 3 3 1 3 2 3 3

# Time Complexity: O(n^2) (Quadratic Time)
# Explanation: The time complexity of this function is quadratic because it has two nested loops that iterate over the list 'lst'.
# As the size of 'lst' increases, the number of iterations (steps) required grows quadratically.