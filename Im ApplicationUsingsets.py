set1 = set()
set2 = set()

for i in range(1, 6):
    set1.add(i)

for i in range(3, 8):
    set2.add(i)
print("set1 =", set1)
print("set2=", set2)
print("\n")

set3 = set1 | set2
print("Union of set1 & set2:set3 = ", set3)
set4 = set1 & set2
print("Intersection of set1 & set2:set4=", set4)
print("\n")

if set3 > set4:
    print("set3 is superset of set4")

elif set3 < set4:
    print("set3 is subset of set4")
else:
    set3 == set4
    print("set3 is same of set4")

if set4 < set3:
    print("set4 is subset of set3")
    print("\n")

set5 = set3 - set4
print("Elements in the set3 and not in set4:set5 =", set5)
print("\n")
if set4.isdisjoint(set5):
    print("set4 and set5 have nothing is comman \n")
set5.clear()
print("after appling on sets set5 =", set5)
print("set5=", set5)
