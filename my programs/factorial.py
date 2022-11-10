# factorial
try:
    a = int(input("enter factorial : "))
    i = a
    s = i
    if a == 1:
        print(1)
    elif a == 0:
        print(0)
    elif a < 0:
        print("enter non negative value")
    else:
        while s > 1:
            i *= (a - 1)
            s -= 1
            a -= 1
        print(i)
except ValueError:
    print("enter integer only")
