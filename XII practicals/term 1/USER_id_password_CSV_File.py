
import csv
DATA = [['SR_NO', "username", "password"]]
n = int(input("Enter the number of entries :"))
for a in range(n):
    sr = int(input("enter sr no :"))
    user = input("enter username :")
    password = input("enter your password :")
    DATA.append([sr, user, password])

with open('DATA.csv', 'w+', newline="") as f:
    wr = csv.writer(f)
    wr.writerows(DATA)

sr_new = int(input("enter your serial number"))

with open('DATA.csv', 'r') as file:
    re = csv.reader(file)
    rows = []
    for a in re:
        rows.append(a)
    c = 0
    for x in rows:
        try:
            if int(x[0]) == sr_new:
                print(x[0], "--->user_id and user_name ", x[1], "has the following password: ", x[2])
                c += 1
            else:
                pass
        except:
            pass
    if c == 0:
        print("invalid input")
    else:
        pass
