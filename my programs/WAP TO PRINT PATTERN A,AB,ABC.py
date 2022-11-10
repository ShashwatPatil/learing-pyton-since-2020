
num = str(input("enter a alphabet :"))
ch = ord(num.upper())
for a in range(65, ch + 1):
    for b in range(65, a + 1):
        print(chr(b), end="")
    print()
