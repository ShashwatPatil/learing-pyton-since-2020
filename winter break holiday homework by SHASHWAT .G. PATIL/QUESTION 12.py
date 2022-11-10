a = "Y"
list_01 = []
while a == "y" or a == "Y":
    i = int(input("enter an element of list :"))
    list_01.append(i)
    a = input("do you want to add another item in your list[Y/N]:")
list_01.sort()
x = int(len(list_01))
lowest = list_01[0]
highest = list_01[x - 1]
print(lowest, "is the smallest number in the list.")
print(highest, "is the greatest number in the list.")
