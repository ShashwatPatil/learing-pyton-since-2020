import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="Shashwat28102004", database="school")

mycr = db.cursor()
acc = input("Enter your Acc_no :")
de = "DELETE FROM EMPLOYEE WHERE Acc_no = "+acc
mycr.execute(de)
db.commit()
print("Data deleted successfully .")
