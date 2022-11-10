num = int(input("Enter the value of X :"))
power = int(input("Enter the value of N :"))
ans = 0
x = None
for a in range(0, (power + 1)):
    x = num ** a
    ans = ans + x
print(ans, "is the answer of the following question")
