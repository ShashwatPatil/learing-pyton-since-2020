
def push(arr):
    a = []
    for m in range(len(arr)):
        f = arr.pop()
        if int(f) % 5 == 0:
            a.append(f)
        else:
            pass

    if len(a) == 0:
        print("The stack is empty !")
        pass
    else:
        print(a)


stk = list(input("Enter numbers to be inserted in stack :"))

push(stk)