
num = int(input("enter the number: "))
x = num
a = 0
b = 1
print(0)
print(1)
for d in range(1, x - 1):
    sum_is = a + b
    a = b
    b = sum_is
    print(sum_is)
