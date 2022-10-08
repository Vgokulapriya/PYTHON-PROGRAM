def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            array[j + 1] = key


data = []
lst = int(input("enter the size of the list:-"))
for n in range(lst):
    new = int(input("enter the %d element:" % n))
    data.append(new)
insertionSort(data)
print("Sort Array in Ascending Order:")
print(data)
