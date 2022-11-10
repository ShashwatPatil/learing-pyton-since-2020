### PRACTICAL FOR XI CS - 2020-21 #
## SOLVED

#2. Input two numbers and display the larger / smaller number.

num1=int(input("Enter first No. ?"))
num2=int(input("Enter second No. ?"))

if num1==num2:
    print("Both Numbers are equal")
elif num1>num2 :
    small=num2
    large=num1
    print("Large No is : ", large)
    print("Small No is " ,  small)
elif num2>num1:
    small=num1
    large=num2
    print("Large No is : ", large)
    print("Small No is " ,  small)
