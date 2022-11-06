# sum function
def sum_(arr, n):
    # using built-in function
    return sum(arr)


# main
arr = [11, 22, 33, 44, 55, 66]

# length
n = len(arr)
print(n)
ans = sum_(arr, n)
# display sum
print("Sum of the array is ", ans)
