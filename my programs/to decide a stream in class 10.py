# to decide stream in class 10
a = float(input("enter marks obtained in english out of 100 :"))
b = float(input("enter marks obtained in mathematics out of 100 :"))
c = float(input("enter marks obtained in science out of 100 :"))

if 0 < a >= 80 and 0 < b >= 80 and 0 < c >= 80:
    print("you are qualified to take pure science")
elif 0 < a >= 80 and 0 < b >= 60 and 0 < c >= 80:
    print("you are qualified to take Bio.science")
elif 0 < a < 60 and 0 < b < 60 and 0 < c < 60:
    print("you are qualified to take commerce")
elif 0 < a < 33 and 0 < b < 33 and 0 < c < 33:
    print("you have Failed")
else:
    print("wrong input")
