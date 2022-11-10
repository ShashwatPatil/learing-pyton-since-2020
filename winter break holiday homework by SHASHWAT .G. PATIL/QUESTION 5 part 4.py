num = int(input("Enter the value of X :"))
power = int(input("Enter the value of N :"))
ans1 = 0
ans2 = 0
x1 = None
x2 = None
for a in range(2, (power + 1), 2):
    b = 1
    for c in range(1, (a + 1)):
        b = b * c
        x1 = (num ** a)/b
    ans1 = ans1 + x1
for a in range(1, (power + 1), 2):
    b = 1
    for c in range(1, (a + 1)):
        b = b * c
        x2 = (num ** a)/b
    ans2 = ans2 + x2
ans = ans1 - ans2 + (2*num)
print(ans, "is the answer of the following question")
