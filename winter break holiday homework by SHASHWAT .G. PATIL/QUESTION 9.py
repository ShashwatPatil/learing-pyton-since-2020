
num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))
list_01 = []
if num1 == num2:
    print(num1, "is the HCF of the two terms")
elif (num1 < 0) or (num2 < 0):
    print("please Enter only POSITIVE number!!!")
elif (num1 == 0) or (num2 == 0):
    print("the HCF is ", 0)
elif num1 > num2:

    for a in range(1, num1):
        if (num1 % a) == 0 and (num2 % a) == 0:
            list_01.append(a)
    list_new = list_01[::-1]
    print("HCF of ", num1, " and ", num2, " is ", list_new[0])

elif num2 > num1:

    for a in range(1, num2):
        if (num1 % a) == 0 and (num2 % a) == 0:
            list_01.append(a)
    list_new = list_01[::-1]
    print("HCF of ", num1, " and ", num2, " is ", list_new[0])

# lcm(a,b) = (a*b)/hcf(a,b)
try:
    if num1 == num2:
        print(num1, "is the lcm of the two terms")
    else:
        lcm = (num1*num2)/list_new[0]
        print(lcm, "is the LCM of the entered numbers")
except NameError:
    print("")
