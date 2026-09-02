# Question 3 — Find the Kth smallest

# Use selection-sort logic to find the 3rd smallest number.

numbers = [8, 3, 1, 9, 4, 2, 7]

# Expected:

# 4

# But here's the catch:

# Don't simply call sort() or fully sort the list first.

# Try to stop once you've found the 3rd smallest element.

def selection_sort(array, target_index):
    size = len(array)

    
    for i in range (3):
        min_index = i
        for j in range(i+1, size):
            if(array[min_index]> array[j]):
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]

    return array[2] # finding the 3rd smallest number


print (selection_sort(numbers, -2))