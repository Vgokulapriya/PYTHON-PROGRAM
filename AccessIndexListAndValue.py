# list comprehension to access and return the list items or values and the respective index positions.
# Access List Index and Values

orgList = [13, 43, 56, 78, 65]

list2 = [list((i, orgList[i])) for i in range(len(orgList))]
print("List Index and Values are")
print(list2)

list3 = [(i, orgList[i]) for i in range(len(orgList))]
print("List Index and Values are")
print(list3)


# Python Program to access List Index and Values using enumerate
# Access List Index and Values

orgList = [2, 4, 6, 8, 10, 12]

print("List Index and Values are")
for index, value in enumerate(orgList):
    print("Index Number = ", index, " and Value = ", value)
