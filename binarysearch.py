a = [12, 73, 64, 15, 26, 17]
target = 73


a.sort()


low = 0
high = len(a) - 1

while low <= high:
    mid = (low + high )// 2

    if a[mid] == target:
        print ("found")
        print (mid)
        break

    elif a[mid] < target:
        low = mid + 1
    else:
        high = mid -1
