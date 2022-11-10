### PRACTICAL FOR XI CS - 2020-21 #
## SOLVED
# 9a. Compute the greatest common divisor (GCF)
#     least common multiple of two integers.(LCM)

# Python program to find H.C.F of two numbers
# define a function

num1 = 12
num2 = 18

x=num1
y=num2
# choose the smaller number
if x > y:
    smaller = y
else:
    smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
print("The H.C.F. is",hcf)
