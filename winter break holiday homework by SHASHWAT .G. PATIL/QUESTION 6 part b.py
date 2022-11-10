
num = str(input("Enter a Number:"))
a = len(num)
ans = 0
for x in range(0, a):
    s = int(num[x]) ** 3
    ans += s

if ans == int(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is NOT an Armstrong number.")
