
a = "Y"
list_01 = []
print("enter the marks in first list")
try:
    while a == "y" or a == "Y":
        i = int(input("enter marks the student of list for first list :"))
        list_01.append(i)
        a = input("do you want to add another item in your list - 1 [Y/N]:")
    list_02 = []
finally:
    print("now enter the marks in second list")
a = "y"
try:
    while a == "Y" or a == "y":
        i = int(input("enter marks the student of list for second list :"))
        list_02.append(i)
        a = input("do you want to add another item in your list - 2 [Y/N]:")
finally:
    list_01.sort()
    list_02.sort()
    if list_01 == list_02:
        print("Both lists are equal.")
    else:
        print("Both lists are NOT equal.")
