
limit = int(input("Enter the limit :"))
limit_01 = limit
for a in range(1, (limit+1)):
    print("*" * a)
for b in range(1, (limit+1)):
    for a in range(1, (b + 1)):
        print(a, end="")
    print("")
for b in range(1, (limit+1)):
    for a in range(1, (b + 1)):
        print(a, end="#")
    print("")
for b in range(1, (limit+1)):
    for c in range(limit_01, 1, -1):
        print(" ", end="")
    for a in range(1, (b + 1)):
        print(a, end="")
    print("")
    limit_01 -= 1
