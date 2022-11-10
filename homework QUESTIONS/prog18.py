### PRACTICAL FOR XI CS - 2020-21 #
# 18.	Write a program to store marks of students in two different
#    list and find out whether they are identical or different

"""
Method 1 : Using list.sort() and == operator
sort() coupled with == operator can achieve this task.
We first sort the list, so that if both the lists are identical,
then they have elements at the same position.
But this doesn’t take into account the ordering of elements in list.
"""
###############################################################
# Python 3 code to demonstrate 
# check if list are identical 
# using sort() + == operator 

# initializing lists 
test_list1 = [1, 2, 4, 3, 5] 
test_list2 = [5, 4, 3, 2, 1] 

# printing lists 
print ("The first list is : " + str(test_list1)) 
print ("The second list is : " + str(test_list2)) 

# sorting both the lists 
test_list1.sort() 
test_list2.sort() 

# using == to check if 
# lists are equal 
if test_list1 == test_list2: 
	print ("The lists are identical") 
else : 
	print ("The lists are not identical") 
