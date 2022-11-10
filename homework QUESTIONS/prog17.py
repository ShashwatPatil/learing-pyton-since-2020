### PRACTICAL FOR XI CS - 2020-21 #
# 17.	Write a Program to Print the following pattern
######################################################
"""
(a)                         (b)                           (c)                        (d) 
*		1		1#		  1
**		22		1#2#		12
***		333 		1#2#3#	              123
****		4444		1#2#3#4#            1234
*****		55555	               1#2#3#4#5#       12345
"""
#####################################################

#(b) and (a) 
rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end=" ")  # print number
    # line after each row to display pattern correctly
    print(" ")
print("-----------------")
######################################################## 
#(d) Left align
rows = 5
for row in range(1, rows+1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")
print("-----------------")
#########################################################
print("-------------")
#pyramid down 
rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
###########################################
# Reverse Decresing Numbers
print("------------------")
rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")
##########################################
print("------------------------")
rows = 6
for i in range(1, rows + 1):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
############################################
print("----------------------")

rows = 6
for i in range(0, rows):
    for j in range(rows - 1, i, -1):
        print(j, '', end='')
    for l in range(i):
        print('    ', end='')
    for k in range(i + 1, rows):
        print(k, '', end='')
    print('\n')
#############################################
#Right Align
print("-----------------")
rows = 6
for row in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > row:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")
##############################################
# Pascle's Triangle
print("Python's Triangle")
print("----------------------------------------------------------------------------------")
def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()
###############################################
def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

rows = 7
print_pascal_triangle(rows)
################################################
print("----------------------")
rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
################################################
print("----------------------")

rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
####################################
#Print Alphabets and Letters pattern in python

print("Print Alphabets and Letters pattern in Python ")
asciiNumber = 65
for i in range(0, 7):
    for j in range(0, i + 1):
        character = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber += 1
    print(" ")
#######################################
print("--------------------------------------------------------------")

word = "Python"
x = ""
for i in word:
    x += i
    print(x)
