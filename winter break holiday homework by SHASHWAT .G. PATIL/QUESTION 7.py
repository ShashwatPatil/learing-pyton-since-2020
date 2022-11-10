
num = int(input("Enter a number :"))
list_01 = []
if num == 1:
    print("1 is UNIQUE number.")
elif num == 0:
    print("0 is 0")
elif num < 0:
    print("please enter only positive number.")
else:
    for a in range(1, num):
        if num % a == 0:
            list_01.append(int(a))
    length = len(list_01)
    if length == 1:
        print("it is a PRIME number.")
    else:
        print("it is NOT a PRIME number, it is a COMPOSITE number ")
