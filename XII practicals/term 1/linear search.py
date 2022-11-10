
L = list(input("enter the list: "))
a = input("enter the element to search in list: ")
f = 0
for x in L:
    if x == a:
        f += 1
    else:
        pass

print(f, "is the frequency of elements.")
