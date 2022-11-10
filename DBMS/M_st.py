
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="Shashwat28102004", database="bank_007")


mycr = db.cursor()

tb = "CREATE TABLE Accounts(Acc_no int(12) PRIMARY KEY, Adhar_no int(12) UNIQUE , Full_name varchar(30) , Age int(3) ,\
        Address BLOB , Phone_no int(12) , Password varchar(10) NOT NULL , Balance int(12) , loan_amount int(12) ,\
        DOB date , status varchar(10) DEFAULT \"Active\" )"

mycr.execute(tb)

db.commit()
