# Problem 1 — Find a number

# Given:
numbers = [12, 45, 7, 23, 89, 34]
target = 23

# Write a linear search that prints:

# Found

# if target exists in the list.

for i in range (len(numbers)):
    if (numbers[i] == target):
        print ("Found at", numbers.index(numbers[i]))
        break

# notes : since this is not binary search we dont need to sort
# the array out first

