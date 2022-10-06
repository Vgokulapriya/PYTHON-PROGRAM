def binarySearchAlgo(xlist, key):
    a = 0
    b = len(xlist)
    while a < b:
        c = (a + b) // 2
        if xlist[c] > key:
            b = c
        elif xlist[c] < key:
            a = c + 1
        else:
            return c
            return -1


lst = []
num = int(input("enter size of list :-"))
for n in range(num):
    xlist = int(input("Enter thr array of %d element :-" % n))
    lst.append(xlist)
    lst.sort()
print("sort list is:", lst)
key = int(input("the number to search for:"))
index = binarySearchAlgo(lst, key)
if index < 0:
    print("{} was not found.".format(key))
else:
    print("{} was found at index {}.".format(key, index))
