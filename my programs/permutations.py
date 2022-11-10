
def permutations():
    a = int(input("Enter only the number : "))
    while a >= 1:
        a -= 1
        a *= (a - 1)
    print(a)

print(permutations())
