# Problem 4 — Basic binary search

# Given:

numbers = [2, 5, 8, 12, 16, 23, 38, 56]
target = 232

numbers.sort() # i know they are sorted but a real life question might not do me such a beautiful gesture
# Write a binary search that prints: Found

# Try doing it using:
# low
# high
# mid

high = len(numbers)-1
low = 0

while low <= high:
    mid = (high + low) // 2

    if (numbers[mid] == target):
        print ("Found at index", mid) # i know i am only supposed to display found but index is important so bonus for practice
        break
    elif (numbers[mid] > target):
        high = mid - 1
    elif (numbers[mid] < target):
        low = mid +1

else:
    print ("target number is not here")

