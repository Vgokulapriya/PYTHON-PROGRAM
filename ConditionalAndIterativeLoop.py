def conditional_iterative(n, a):
    for i in range(1, n + 1):
        print(i, sep="", end="")
        if i < n:
            print("+", sep="", end="")
        a.append(i)
    print("=", sum(a))
    print()


n = int(input("enter the number:"))
a = []
conditional_iterative(n, a)
