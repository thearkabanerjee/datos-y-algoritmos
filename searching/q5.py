# Problem 5 — Find the index

# Given:

numbers = [3, 7, 11, 15, 19, 24, 30]
target = 19

# Write a binary search that prints the index of the target.

# Expected: 4

high = len(numbers) -1
low = 0

while high >= low:
    mid = (high + low )//2

    if (numbers[mid] == target):
        print (mid)
        break
    elif ( numbers[mid] > target):
        high = mid -1
    else:
        low = mid + 1
else:
    print ("target is not in the list")