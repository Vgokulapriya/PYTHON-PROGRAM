# Python code
# to print cube sum of first n natural numbers
# using inbuilt function pow()

number = int(input("Enter the number:"))
sum = 0
# iterating loop up to given number n
for i in range(1, number + 1):
    # adding cube sum using pow() function
    sum = sum + pow(i, 3)
print(sum)

# this code is contributed by gangarajula laxmi
