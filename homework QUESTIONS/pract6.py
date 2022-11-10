### PRACTICAL FOR XI CS - 2020-21 #
## SOLVED
import math 


# 6 Determine whether a number is
#    (a) a perfect number =  (divisor sum is equal to number)
#    (b) an armstrong number 153 = 1*1*1 + 5*5*5 + 3*3*3
#    (c) a palindrome.   151 =   151 ,   181 = 181

## (a) Perfect Number program

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


    
## (b) Python program to check if the number is an Armstrong number or not

num = int(input("Enter a number: ")) # take input from the user
sum = 0                                             # initialize sum
temp = num                                      # find the sum of the cube of each digit
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
########################


# (c) a palindrome.   151 =   151 ,   181 = 181
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
#############



