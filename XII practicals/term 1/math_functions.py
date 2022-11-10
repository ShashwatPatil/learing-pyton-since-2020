
from math import *
c = True
while c:
    print('''
    *********************************************************
    *          1.   ceil                                    *
    *          2.   fabs                                    *
    *          3.   factorial                               *
    *          4.   floor                                   *
    *          5.   log                                     *
    *          6.   pow                                     *
    *          7.   sqrt                                    *
    *          8.   pi                                      *
    *          9.   e                                       *
    *********************************************************
    ''')

    a = int(input("enter your choice :"))

    if a == 1:
        p = input("enter a num :")
        p = ceil(int(p))
        print(p)
    elif a == 2:
        p = input("enter a num :")
        p = fabs(int(p))
        print(p)
    elif a == 3:
        p = input("enter a num :")
        p = factorial(int(p))
        print(p)
    elif a == 4:
        p = input("enter a num :")
        p = floor(int(p))
        print(p)
    elif a == 5:
        p = input("enter a num :")
        q = log10(int(p))
        print(q)
    elif a == 6:
        p = input("enter a num :")
        q = int(input("enter the power :"))
        p = pow(int(p), q)
        print(p)
    elif a == 7:
        p = input("enter a num :")
        p = sqrt(int(p))
        print(p)
    elif a == 8:
        print(pi)
    elif a == 9:
        print(e)
    else:
        print("invalid input!!!!!!")

    x = input("do you want to continue [Y/N]")
    if x == "Y" or x == "y":
        pass
    else:
        c = False
