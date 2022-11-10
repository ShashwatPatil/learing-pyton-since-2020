
num = int(input("enter a number :"))
for a in range(0, num):
    for b in range(0, num - a - 1):
        print(" ", end="")
    for c in range(0, a + 1):
        print("*", end="")
    print()
