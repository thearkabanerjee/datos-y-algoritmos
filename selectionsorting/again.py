a = [12, 2, 4, 21, 1, 32]
size = len(a)

def selection_sort(array, size):
    for i in range (size):
        min_index = i
        for j in range (i+1,size):
            if (array[j] < array[min_index]):
                min_index = j

        array[min_index], array[i] = array[i] , array[min_index]

    return (array)





print (selection_sort(a, size))