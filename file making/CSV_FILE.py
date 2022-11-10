
import csv
L = []
with open(r"E:\practical\file making\New_content.txt", "r+") as _1:
    data = _1.read()
    for a in data:
        L.append(a)

print(L)

with open(r"E:\practical\file making\New_content.csv", "w+", newline="") as _02:
    csvw = csv.writer(_02, delimiter='|')
    for x in L:
        csvw.writerow(x)
