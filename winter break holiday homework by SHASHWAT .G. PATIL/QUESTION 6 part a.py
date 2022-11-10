
num = int(input("Enter a number :"))
list_01 = []
for a in range(1, num):
    if num % a == 0:
        list_01.append(int(a))
c = 0
for b in list_01:
    c += b
if num == c:
    print("the number", num, "is a PERFECT NUMBER.")
else:
    print("the number", num, "is not a PERFECT NUMBER.")
