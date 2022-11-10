a = int(input("enter the cost of total purchase :"))

if 0 < a < 5000:
    print("the discount on your purchase is ", (a*5)/100)
elif 5000 <= a <= 10000:
    print("the discount on your purchase is ", (a*8)/100)
else:
    print("the discount on your purchase is ", a/10)
