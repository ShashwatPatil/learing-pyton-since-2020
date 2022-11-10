### PRACTICAL FOR XI CS - 2020-21 #
#11. Input a string and determine whether it is a palindrome or not;
#      convert the case of characters in a string is palindrom

str1=input("Enter a string  to be checked") 
result = True 
        # Run loop from 0 to len/2
for i in range(0, int(len(str1)/2)): 
    if str1[i] != str1[len(str1)-i-1]:
        result = False
        break 
# if result variable is not modified in loop
if result ==True:
    print("String is palindrom ")
    print("String in Capital letters ", str1.upper()) 
else:
    print("String is not palindrom")



