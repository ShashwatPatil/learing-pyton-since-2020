a = float(input("enter the percent you got in class 10th :"))

if 0 < a < 33:
    print("failed")
elif 33 <= a < 50:
    print("third division")
elif 50 <= a < 60:
    print("second division")
elif 100 >= a >= 60:
    print("first division")
else:
    print("wrong input")
