import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="Shashwat28102004", database="school")

mycr = db.cursor()
acc = input("Enter your Acc_no :")
select = "SELECT * FROM EMPLOYEE WHERE Acc_no = "+acc
mycr.execute(select)
for a in mycr:
    print(a)
