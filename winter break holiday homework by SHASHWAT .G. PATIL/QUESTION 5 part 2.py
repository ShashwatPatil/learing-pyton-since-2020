num = int(input("Enter the value of X :"))
power = int(input("Enter the value of N :"))
ans2 = 0
ans1 = 0
x1 = None
x2 = None
for a in range(0, (power + 1), 2):
    x1 = num ** a
    ans1 = ans1 + x1

for a in range(1, (power + 1), 2):
    x2 = num ** a
    ans2 = ans2 + x2
ans = ans1 - ans2
print(ans, "is the answer of the following question")
