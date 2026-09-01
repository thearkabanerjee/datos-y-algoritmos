a = [12, 73, 64, 15, 26, 17]
target = 73

a.sort()

print (a)

low = 0
high = len(a) -1

print (a[low], a[high])





while low <= high :
    mid = low + high //2

    if a[mid] == target:
        print ("found at index", a.index(target))
        break
    elif (a[mid] < target):
        low += 1
    elif (a[mid] > target):
        high -= 1
    else:
        print ("not found")
