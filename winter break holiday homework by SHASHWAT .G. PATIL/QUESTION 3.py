a = float(input("Enter first No. :"))
b = float(input("Enter Second No. :"))
c = float(input("Enter Third No. :"))

if a > b and a > c:
    print(a, "is Greatest of them all.")
elif b > c:
    print(b, "is Greatest of them all.")
elif c > b:
    print(c, "is Greatest of them all.")
else:
    print("ALL number are equal or two of them are equal.")

if a < b and a < c:
    print(a, "is Smallest of them all.")
elif b < c:
    print(b, "is Smallest of them all.")
elif c < b:
    print(c, "is Smallest of them all.")
else:
    print("")
