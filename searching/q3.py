# Problem 3 — What if it isn't there?

# Given:

numbers = [5, 12, 19, 27, 31]
target = 100
found = False
# Write a linear search that prints:

# Not found

# when the target doesn't exist.

for i in range (len(numbers)):
    if (numbers[i] == target):
        found = True

if not (found):
    print ("Not found")