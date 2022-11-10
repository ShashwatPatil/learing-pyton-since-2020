### PRACTICAL FOR XI CS - 2020-21 #
## SOLVED
# 6 (b) an armstrong number 153 = 1*1*1 + 5*5*5 + 3*3*3

import math 

num = int(input("Enter a number: "))  # take input from the user
sum = 0                                              # initialize sum
temp = num                                       # find the sum of the cube of each digit
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:          # display the result
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")




