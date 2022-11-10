
a = "Y"
dictionary_01 = {}
roll_no = 0
while a == "y" or a == "Y":
    roll_no += 1
    key = str(input("enter the name of the student :"))
    value = int(input("enter the marks of the student :"))
    a = input("do you want to add another item in your dictionary[Y/N]:")
    dictionary_01[roll_no] = [key, value]
for a in dictionary_01:
    if dictionary_01[a][1] >= 75:
        print(dictionary_01[a][0], "has got marks above 75.")
    else:
        continue
