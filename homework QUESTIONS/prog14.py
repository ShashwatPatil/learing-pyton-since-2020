### PRACTICAL FOR XI CS - 2020-21 #
#14. Input a list/tuple of elements, search for a given element in the list/tuple.

classlist = ('mangilal', 'sohanlal', 'kumar', 'mohan', 'ram', 'sita', 'gita')
student=input("Enter item to be searched ")
x=0
found=False
for name in classlist  :
        if name==student :
                print ("found at location no", x+1)
                found=True 
        x=x+1
##################
if found==False :
        print(student, " is Not Found in class")

        


