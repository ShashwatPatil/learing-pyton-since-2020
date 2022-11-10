### PRACTICAL FOR XI CS - 2020-21 #
## SOLVED
import math 

# 5 sum of different Series
#a=1/2 + 1/2 + 1/3 + ….. + 1/N. The program output is also shown below.
#b=1.x0+x1+x2+x3 …………..xn (0,1,2,3,...n are powers of x
#c=1.x0-x1+x2-x3+x4………..xn
#d=x^1/1+x^2/2-x^3/3+x^4/4-…………+.x^n/n
#e=x^1/1!+x^2/2!-x^3/3!+x^4/4!-………….+x^n/n!

# Series a 
n=int(input("Enter the number of terms:"))
x=int(input("Enter the value of x:"))
sum1=1
for i in range(2,n+1):
    sum1=sum1+((x**i)/i)
print("The sum of series is",round(sum1,2))
###############################################


# Series b
n=int(input("Enter the number of terms:"))
x=int(input("Enter the value of x:"))
sum1=0
for i in range(n+1):
    sum1=sum1+math.pow(x,i)
print("The sum of series is",round(sum1,2))

##################################################
#e=x^1/1!   +   x^2/2!  +  x^3/3!  +   x^4/4!-………….+   x^n/n!
n=int(input("Enter the number of terms:"))
x=int(input("Enter the value of x:"))

sum2=0
terms=1
while terms<=n :
    sum2 = sum2 + math.pow(x, terms) / math.factorial(terms)
    terms = terms + 1
print("sum of x power= " , sum2)
