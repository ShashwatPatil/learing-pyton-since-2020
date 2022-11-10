a = "Y"
list_01 = []
while a == "y" or a == "Y":
    i = input("enter an element of list :")
    list_01.append(i)
    a = input("do you want to add another item in your list[Y/N]:")
string = str(input("enter the element you want to search:"))
index = list_01.index(string)
print("the element", string, "is at index position ", index, "in the list")
print(list_01)
