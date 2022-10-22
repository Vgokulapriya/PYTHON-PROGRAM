# Half Pyramid of Stars (*)
num = int(input())
print("Half Pyramid Pattern of Stars (*):")
for i in range(num):
    for j in range(i + 1):
        print("* ", end="")
    print()
