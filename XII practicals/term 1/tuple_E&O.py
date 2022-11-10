
def tuple_e_o(a):
    p = 0
    q = 0
    for x in a:
        if int(x) % 2 == 0:
            p += 1
        elif int(x) % 2 == 1:
            q += 1
        else:
            break
    return p, q


L = list(input("enter the list: "))
D = tuple_e_o(L)
print(D[0], "is the number of even num. ")
print(D[1], "is the number of odd num. ")
