
a = "Y"
list_01 = []
while a == "y" or a == "Y":
    i = int(input("enter an element of list :"))
    list_01.append(i)
    a = input("do you want to add another item in your list[Y/N]:")
length = len(list_01)
for x in range(0, length):
    ans = 0
    number = len(str(list_01[x]))
    num = str(list_01[x])
    for d in range(0, number):
        s = int(num[d]) ** 3
        ans += s
    if ans == int(num):
        print(num, "is an Armstrong number.")
    else:
        print(num, "is NOT an Armstrong number.")
