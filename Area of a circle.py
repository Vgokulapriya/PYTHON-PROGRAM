# Python program to find Area of a circle
r = int(input())


def findArea(r):
    PI = 3.142
    return PI * (r * r)


# Driver metho
print("Area is %.6f" % findArea(r))
