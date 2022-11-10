
def list_alter(a):
    for x in a:
        if int(x) % 2 == 0:
            p = a.index(x)
            a[p] = int(int(x) / 2)
        elif int(x) % 2 == 1:
            q = a.index(x)
            a[q] = int(x) * 2
        else:
            break
    return a


L = list(input("enter the list: "))
D = list_alter(L)
print(D, "\nis the modified list.")
