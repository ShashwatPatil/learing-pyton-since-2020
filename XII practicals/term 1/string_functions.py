
c = True
while c:
    print('''
    *********************************************************
    *          1.   split                                   *
    *          2.   strip                                   *
    *          3.   upper                                   *
    *          4.   lower                                   *
    *          5.   find                                    *
    *          6.   capitalize                               *
    *          7.   index                                   *
    *          8.   isalnum                                 *
    *          9.   isalpha                                 *
    *          10.  isdecimal                               *
    *          11.  isdigit                                 *
    *          12.  islower                                 *
    *          13.  isupper                                 *
    *          14.  len                                     *
    *          15.  ord                                     *
    *          16.  chr                                     *
    *********************************************************
    ''')

    a = int(input("enter your choice :"))

    if a == 1:
        p = input("enter a str :")
        p = p.split()
        print(p)
    elif a == 2:
        p = input("enter a str :")
        p = p.strip()
        print(p)
    elif a == 3:
        p = input("enter a str :")
        p = p.upper()
        print(p)
    elif a == 4:
        p = input("enter a str :")
        p = p.lower()
        print(p)
    elif a == 5:
        p = input("enter a str :")
        q = input("letter to be searched :")
        w = p.find(q)
        print(w + 1)
    elif a == 6:
        p = input("enter a str :")
        p = p.capitalize()
        print(p)
    elif a == 7:
        p = input("enter a str :")
        q = input("letter to find index :")
        w = p.index(q)
        print(w + 1)
    elif a == 8:
        p = input("enter a str :")
        p = p.isalnum()
        print(p)
    elif a == 9:
        p = input("enter a str :")
        p = p.isalpha()
        print(p)
    elif a == 10:
        p = input("enter a str :")
        p = p.isdecimal()
        print(p)
    elif a == 11:
        p = input("enter a str :")
        p = p.isdigit()
        print(p)
    elif a == 12:
        p = input("enter a str :")
        p = p.islower()
        print(p)
    elif a == 13:
        p = input("enter a str :")
        p = p.isupper()
        print(p)
    elif a == 14:
        p = input("enter a str :")
        q = len(p)
        print(q)
    elif a == 15:
        p = input("enter a character :")
        q = ord(p)
        print(q)
    elif a == 16:
        p = int(input("enter a num :"))
        q = chr(p)
        print(q)
    else:
        print("invalid input!!!!!!")

    x = input("do you want to continue [Y/N]")
    if x == "Y" or x == "y":
        pass
    else:
        c = False
