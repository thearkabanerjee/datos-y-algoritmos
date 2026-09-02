# Modify selection sort so that it sorts from largest → smallest.

numbers = [12, 4, 19, 7, 1, 15]

# Expected:

# [19, 15, 12, 7, 4, 1]

# Hint: You don't need to create a completely new algorithm. Think about what condition you used to find the minimum.

def selection_sort(array):
    size = len(array)

    for i in range(size):
        max_index = i

        for j in range (i+1, size):
            if (array[j] > array[max_index]):
                max_index = j 

        array[i], array[max_index] = array[max_index], array[i]
   
    return array


print (selection_sort(numbers))