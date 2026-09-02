# Modify your selection sort so that it returns both the sorted list and the number of swaps performed.

# For example:

numbers = [5, 4, 3, 2, 1]

# Your function should produce something like:

# ([1, 2, 3, 4, 5], 2)

# You need to figure out why the answer is 2, rather than simply counting every comparison.

def selection_sort(numbers):
    size = len(numbers)
    count = 0

    for i in range(size):
        min_index = i

        for j in range(i+1, size):
            if (numbers[min_index] > numbers[j]):
                min_index = j

        if min_index != i:
            numbers[min_index], numbers[i] = numbers[i], numbers[min_index]
            count += 1
        
    return (numbers, count)

print(selection_sort(numbers))