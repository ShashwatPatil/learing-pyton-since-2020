
a = int(input("enter a number : "))
b = int(input("enter a number : "))

if a == 0:
    print("ANS IS ZERO (0)")
elif b == 0:
    print("CANNOT DIVIDE BU ZERO !!!!!!")
else:
    if a % b == 0:
        print("answer is : ", a/b)
