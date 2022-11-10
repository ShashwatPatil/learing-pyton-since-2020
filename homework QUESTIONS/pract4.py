### PRACTICAL FOR XI CS - 2020-21 #
## SOLVED

import math as m

#   4 given two integers x and n computer x to the power of n
# Method 1 with math module

x = int(input("Enter a Number"))
n = int(input("Enter power of x"))
p1=m.pow(x,n)

print(x, "to the power ", n , "is", p1)

## Method2 Without Maths module
p2=1
for  i in range(1,n+1) :
    p2=p2*x
print(x, "to the power ", n , "is", p2)
######################################
