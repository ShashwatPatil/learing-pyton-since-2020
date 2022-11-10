import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="Shashwat28102004", database="school")

mycr = db.cursor()
acc = input("Enter your Acc_no :")
field = input("Which field do you want to update :")
new = input("enter the updated value :")
up = "UPDATE EMPLOYEE SET "+field+" = "+"'"+new+"'"+" WHERE Acc_no = "+acc
mycr.execute(up)
db.commit()
print("Data updated successfully .")
