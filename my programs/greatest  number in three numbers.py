# greatest  number in three numbers


a = float(input("enter first no :"))
b = float(input("enter second no :"))
c = float(input("enter third no :"))
if a > b:
    if a > c:
        print("the greatest no is:", a)
    else:
        print("the greatest no is:", c)
else:
    if b > c:
        print("the greatest no is:", b)
    else:
        print("the greatest no is:", c)
