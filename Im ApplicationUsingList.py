regnum = input("enter the register number of student :").split()
namelist = [int(x) for x in regnum]
marklist = input("Enter the percentage marks of student:").split()
marklist = [int(y) for y in marklist]
print("the original list 1 :" + str(regnum))
print("the original list 2 :" + str(marklist))
res = {key: [] for key in regnum}
for key, val in zip(regnum, marklist):
    res[key].append(val)
print("the mapped dictionary:" + str(res))
