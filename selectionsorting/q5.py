# This one tests whether you really understand what selection sort is doing.

# Write selection sort for:

numbers = [64, 25, 12, 22, 11]

# with these restrictions:

# Don't use .sort()
# Don't use sorted()
# Don't create another list
# Don't use min()
# Modify the original list in place
# Return the sorted list

def selection_sort(array):
    size = len(array)
    for i in range(size):
        min_index = i

        for j in range(i+1,size):
            if (array[min_index] > array[j]):
                min_index = j

        array[i],array[min_index] = array[min_index], array[i] 

    return array

print (selection_sort(numbers))