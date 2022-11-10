
num = int(input("enter a number :"))
for a in range(num, 0, -1):
    for b in range(0, a):
        print("*", end="")
    print()
