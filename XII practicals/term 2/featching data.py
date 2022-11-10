import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="Shashwat28102004", database="school")

mycr = db.cursor()
tb = "CREATE TABLE EMPLOYEE(Acc_no int(12) PRIMARY KEY, Full_name varchar(30), Age int(3), Phone_no int(12))"
mycr.execute(tb)
db.commit()
insert = "INSERT INTO EMPLOYEE(Acc_no, Full_name, Age, Phone_no) VALUES (%s, %s, %s, %s)"
p = True
while p:
    try:
        acc = int(input("enter your Acc_no to be added :"))
        f = input("enter your Full name :")
        age = int(input("enter your age:"))
        ph_no = int(input("enter your Phone_no(last 6 digits):"))
        if len(str(acc)) >= 10 or len(str(ph_no)) > 6:
            p = False
        if not p:
            print("run again , INVALID INPUT!!!!!")
            break
        val = (acc, f, age, ph_no)
        mycr.execute(insert, val)
        db.commit()
        print("Data added successfully .")
        ch = input("do you want to continue [Y/y]")
        if ch == 'y' or ch == 'Y':
            pass
        else:
            p = False
    except:
        print("Invalid input")

select = "SELECT * FROM EMPLOYEE"
mycr.execute(select)

for a in mycr:
    print(a)
