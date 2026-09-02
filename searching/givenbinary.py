# given a list perform binary search to solve it
# You are given a sorted list of integers:

# numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

# Write a function:

def binary_search(numbers, target):
    # your code
    high = len(numbers) -1
    low = 0
    index = 0

    while (low <= high):
        mid = (low +high) // 2

        if (numbers[mid] == target):
            index = mid
            break
        elif (numbers[mid] > target):
            high = mid -1
        else:
            low = mid+1
    else:
        index = -1

    return index



# It should:

# Return the index of target if it exists.

# Return -1 if it doesn't exist.
# You must use binary search.
# You cannot use .index(), in, or any other built-in searching method.
# Example
numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search(numbers, 23))

# should give:

# 5

# And:

# print(binary_search(numbers, 50))

# should give:

# -1