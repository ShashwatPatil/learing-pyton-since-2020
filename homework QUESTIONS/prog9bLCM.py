### PRACTICAL FOR XI CS - 2020-21 #
## SOLVED
# 9b. Compute the greatest common divisor (GCF)
#least common multiple of two integers.(LCM)
# Python Program to find the L.C.M. of two input number

num1 = 10
num2 = 15


x=num1
y=num2

# choose the greater number
if x > y:
   greater = x
else:
   greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
print("The L.C.M. is", lcm)
