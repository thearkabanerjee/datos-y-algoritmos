# Write:

# def binary_search(numbers, target):
#     ...

# It should return the index if the target exists and -1 if it doesn't.

# For example:

# print(binary_search([1, 3, 5, 7, 9], 7))

# should give:

# 3

# And:

# print(binary_search([1, 3, 5, 7, 9], 4))

# should give:

# -1

def binary(numbers, target):
    high = len(numbers) - 1
    low = 0

    while (high >= low):
        mid = (high + low) // 2

        if (numbers[mid] == target) :
            return (mid)
        elif (numbers[mid] > target):
            high = mid -1
        elif (numbers[mid] < target):
            low = mid +1
    else:
        return -1

print(binary([1, 3, 5, 7, 9], 7))