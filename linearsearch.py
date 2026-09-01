a = [12, 13, 14, 15, 16, 17]
target = 35
message = ""

for i in range(len(a)):
    if (a[i]== target):
        message = "found it"
        index = i
        break
    else:
        message = "target is not present"
        index = -1

print (message, index)
