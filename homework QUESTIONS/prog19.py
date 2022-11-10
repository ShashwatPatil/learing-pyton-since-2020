### PRACTICAL FOR XI CS - 2020-21 #
# 19.	Write a program to count frequency of  a character in a string/list

# Python program to count the frequency of 
# elements in a list using a dictionary 


#my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

str1="quick quick"
my_list= list(str1)
print("Origional List=", my_list)
# Creating an empty dictionary 
freq = {} 
for items in my_list: 
        freq[items] = my_list.count(items) 
for key, value in freq.items(): 
        print ("% s : % s"%(key, value)) # %s for string %d for int







