### PRACTICAL FOR XI CS - 2020-21 #
## SOLVED
# 7 Program to check if a number is prime or not

num = int(input("Enter a number: "))
# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print("Its composite Number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       

else:   # if input number is less than or equal to 1, it is not prime
   print(num,"is not a prime number \n Its composite Number")
