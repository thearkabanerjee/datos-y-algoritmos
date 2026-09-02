# Now let's make it actually hard:

# Given a sorted list that may contain duplicates, find the first occurrence of the target.

# For example:

# numbers = [1, 2, 2, 2, 4, 5, 7]
# binary_search(numbers, 2)

# should return:

# 1

# Not 2 or 3.

def binary_search(numbers, target):
    high = len(numbers) -1
    low = 0
    index = -1

    while (low <= high):
        mid = (high+low) // 2
        
        if (numbers[mid] == target ):
            index = mid
            high = mid -1


        elif (numbers[mid] >target):
            high = mid -1
        else:
            low = mid +1

    return index  


numbers = [1, 2, 2, 2, 4, 5, 7]
print (binary_search(numbers, 2))