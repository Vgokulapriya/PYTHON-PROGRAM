def Cloning(li1):
    li_copy = li1[:]
    return li_copy


li1 = [4, 8, 2, 10, 15, 38]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
