### PRACTICAL FOR XI CS - 2020-21 #
## SOLVED


import math 
# 6 (a) a perfect number =  (divisor sum is equal to number)
# 6  = 1+2+3=6 


n = int(input("Enter a Number " ) )
sum1 = 0
for x in range(1, n):
    if n % x == 0:
        sum1 += x

if sum1 == n :
    print( " No is perfect ")
else :
    print("No is not perfect ")
#########################




