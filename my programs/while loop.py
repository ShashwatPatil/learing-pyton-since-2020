var = int(input("enter a no: "))
a = 1
while a <= var:
    print(a)
    a += 1
print("done!!!!!!!!!!!")
b = "ERROR"
c = True
try:
    while c is True:
        print(b)
except KeyboardInterrupt:
    print("saved")
