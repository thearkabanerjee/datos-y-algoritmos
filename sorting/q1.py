# Write:

# def selection_sort(numbers):
#     # your code

# Sort this list in ascending order:

numbers = [7, 3, 9, 2, 5]

# Expected output:

# [2, 3, 5, 7, 9]


def selection_sort(numbers):
    size = len(numbers)

    for i in range (size):
        min_index = i

        for j in range (i+1, size):
            if (numbers[j] < numbers[min_index]):
                min_index = j

        numbers[min_index], numbers[i] = numbers[i],numbers[min_index]

    
    return numbers

print (selection_sort(numbers))