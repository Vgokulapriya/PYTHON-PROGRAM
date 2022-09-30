number = int(input("enter the number:"))
list = []
for var in range(0,number,1):
 ele = int(input("enter the integer:"))
 list.append(ele)
print("circulating the element of list:",list)
for val in range(0,number,1):
 ele = list.pop(0)
 list.append(ele)
 print(list)
