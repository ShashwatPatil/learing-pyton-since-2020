
def my_func():
    print('''
    1.   add
    2.   sub
    3.   mul
    4.   div
    ''')

    a = input("enter your choice :")
    x = int(input("enter num 1: "))
    y = int(input("enter num 2: "))
    if a == '1':
        print(x + y)
    elif a == '2':
        print(x - y)
    elif a == '3':
        print(x * y)
    elif a == '4':
        print(x / y)
    else:
        print("invalid input !!!!!")

