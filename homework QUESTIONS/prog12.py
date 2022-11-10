### PRACTICAL FOR XI CS - 2020-21 #
#12.	Find the largest/smallest number in a list/tuple

List1 = [10,20,30,10,40,70]

largest  = List1[0]
smallest = List1[0]
# Compare each element with largest/smallest
for  element in List1 :
    if largest< element :
        largest=element
    if smallest > element :
        smallest = element 

####################
print ("Largest element is ", largest)
print ("Smallest element is ",smallest)
