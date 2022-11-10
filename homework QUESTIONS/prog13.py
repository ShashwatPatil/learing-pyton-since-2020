### PRACTICAL FOR XI CS - 2020-21 #
#13. Input a list of numbers and swap elements at the
#       even location with the elements at the odd location

nums = list(input("enter a list :"))
length = len(nums)
print("Origional List= ", nums)
for i in range(0,length,2):
        nums[i], nums[i+1] = nums[i+1], nums[i]

print("After Exchange", nums)
