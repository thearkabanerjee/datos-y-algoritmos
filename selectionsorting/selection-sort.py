

def selection_sort(a, size):
    for x in range(size):
        min_index = x

        for j in range (x+1, size):
            if a[j] < a[min_index]:
                min_index = j

        a[x], a[min_index] = a[min_index], a[x]

    return (a)


a = [12, 2, 4, 21, 1, 32]
size = len(a)
print (selection_sort(a, size))

