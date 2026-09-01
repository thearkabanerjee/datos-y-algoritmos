# Problem 6 — Target doesn't exist

# Given:

numbers = [1, 4, 8, 12, 16, 20, 25]
target = 10

# Write a binary search that prints:

# Not found

high = len(numbers) -1
low= 0

while (low <= high):
    mid = (high + low) // 2

    if (numbers[mid] == target):
        break # not printing cz not needed
    elif (numbers[mid] > target):
        high = mid -1
    else:
        low = mid +1

else :
    print ("Not Found") ## the solution 