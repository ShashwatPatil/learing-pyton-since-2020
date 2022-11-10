
def pop(arr):
    if len(arr) == 0:
        print("The stack is empty !")
        pass
    else:
        a = arr.pop()
        print(a)

stk = list(input("Enter numbers to be inserted in stack :"))

pop(stk)