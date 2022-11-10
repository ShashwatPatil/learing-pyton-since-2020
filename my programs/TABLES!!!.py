list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("enter a number: "))
b = n
t = 1
m = 1
while t <= b:
    if m <= n:
        for a in list_1:
            print(m, "X", a, "=", a*m)
        t += 1
        m += 1
