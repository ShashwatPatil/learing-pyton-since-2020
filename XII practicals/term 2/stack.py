
stk = []
el = int(input("enter the no of elements in the stack : "))
for a in range(el):
    vl = input("Enter element in the stack :")
    stk.append(vl)

print("Push operation successful in stack !")
print(stk)

for m in range(len(stk)):
    print(stk.pop())

print("POP operation successful !")
