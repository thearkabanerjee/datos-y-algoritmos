# Problem 2 — Find the position
# Given:

numbers = [10, 20, 30, 40, 50]
target = 40


# Find the index of target.
# Expected output: 3

for i in range (len(numbers)):
    if (numbers[i] == target):
        print (i)