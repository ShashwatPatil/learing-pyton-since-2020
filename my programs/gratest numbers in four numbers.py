# greatest numbers in four numbers
a = float(input("enter first number:"))
b = float(input("enter second number:"))
c = float(input("enter third number:"))
d = float(input("enter fourth number:"))
if a > b and a > c and a > d:
    print("greatest no is:", a)
elif b > c and b > d:
    print("greatest no is:", b)
elif c > d:
    print("greatest no is:", c)
elif d > c:
    print("greatest no is:", d)
else:
    print("Either any two values or all the four values are equal")
