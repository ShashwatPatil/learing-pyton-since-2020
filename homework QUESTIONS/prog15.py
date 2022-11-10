### PRACTICAL FOR XI CS - 2020-21 #
## SOLVED
# 15.	Input a list of numbers and test if a number is
#              equal to the sum of the cubes of its digits. (Same as arm strong ) – 6 b 

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




