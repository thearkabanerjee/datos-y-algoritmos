def twosums(a, b):
    a.reverse()
    b.reverse()
    
    def numcreator(list):
        number = 0
        for i in range(len(list)):
            number *=10
            number += list[i]

        return number

    a = numcreator([2,4,3]) + numcreator([5,6,4])
    result = []
    for i in range(len(str(a))):
        result.append(a % 10)
        a = a // 10
        print (a)
    return (result)

print (twosums([2,4,3], [5,6,4]))


# although i was supposed to use linked list to solve this one

# but i am not very familiar with it right now