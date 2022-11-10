a = "Y"
list_01 = []
list_swapped = []
while a == "y" or a == "Y":
    i = int(input("enter an element of list :"))
    list_01.append(i)
    a = input("do you want to add another item in your list[Y/N]:")
for x in list_01:
    index = list_01.index(x)
    if index % 2 == 0:
        c = list_01.index(x)
        list_swapped.insert((c + 1), x)
    else:
        c = list_01.index(x)
        list_swapped.insert((c - 1), x)
print(list_swapped)
