### PRACTICAL FOR XI CS - 2020-21 #
## SOLVED
#3.	Input three numbers and display the largest / smallest number.
    
num1=int(input("Enter first No. ?"))
num2=int(input("Enter second No. ?"))
num3=int(input("Enter third No ? "))

#Smallest
if num1 <=num2 and num1 <=num3 :
    print(num1, "is the smallest")
elif num2<=num1 and num2 <=num3 :
    print(num2, "is the smallest")
elif num3 <= num1 and num3 <=num2 :
    print(num3, "is the smallest")

## Largest
largest=num1
if largest <= num1:
    largest= num1
if largest <= num2:
    largest=num2
if largest <=num3:
    largest=num3

print("Largest No is ", largest)
