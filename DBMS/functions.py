
import mysql.connector


def default():
    db = mysql.connector.connect(host="localhost", user="root", password="Shashwat28102004", database="bank_007")
    mycr = db.cursor()
    return db, mycr


def add():
    db, mycr = default()
    insert = "INSERT INTO Accounts(Acc_no, Adhar_no, Full_name, Age, Address, Phone_no, Password, Balance,\
        loan_amount, DOB) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    p = True
    while p:
        try:
            acc = int(input("enter your Acc_no to be added :"))
            adh = int(input("enter your Adhar_no :"))
            f = input("enter your Full name :")
            age = int(input("enter your age:"))
            address = input("enter your Address:")
            ph_no = int(input("enter your Phone_no(last 6 digits):"))
            pass_ = input("enter your password :")
            bal = int(input("enter your Balance:"))
            lone = int(input("enter your loan_amount:"))
            dob = int(input("enter your DOB(YYYY-MM-DD) :"))
            if len(str(acc)) >= 10 or len(str(adh)) >= 10 or len(str(ph_no)) > 6:
                p = False
            if not p:
                print("run again , INVALID INPUT!!!!!")
                break
            val = (acc, adh, f, age, address, ph_no, pass_, bal, lone, dob)
            mycr.execute(insert, val)
            db.commit()
            print("Data added successfully .")
            p = False
        except:
            print("Invalid input")


def show():
    db, mycr = default()
    dis = "SHOW TABLES"
    mycr.execute(dis)
    print("the tables are :")
    for a in mycr:
        print(a)


def data():
    db, mycr = default()
    select = "SELECT * FROM Accounts"
    mycr.execute(select)
    print("Acc_no, Adhar_no, Full_name, Age, Address, Phone_no, Password, Balance, loan_amount, DOB, status")
    for a in mycr:
        print(a)


def search():
    db, mycr = default()
    acc = input("Enter your Acc_no :")
    password = input("Enter your Password :")
    select = "SELECT * FROM Accounts WHERE Acc_no = "+acc+" AND Password = '"+password+"'"
    mycr.execute(select)
    print("Acc_no, Adhar_no, Full_name, Age, Address, Phone_no, Password, Balance, loan_amount, DOB, status")
    for a in mycr:
        print(a)


def update():
    db, mycr = default()
    acc = input("Enter your acc_no :")
    password = input("Enter your Password :")
    field = input("Which field do you want to update :")
    new = input("enter the updated value :")
    up = "UPDATE accounts SET "+field+" = "+"'"+new+"'"+" WHERE Acc_no = "+acc+" AND Password = '"+password+"'"
    mycr.execute(up)
    db.commit()
    print("Data updared successfully .")


def delete():
    db, mycr = default()
    acc = input("Enter your acc_no :")
    password = input("Enter your Password :")
    de = "DELETE FROM accounts WHERE Acc_no = "+acc+" AND Password = '"+password+"'"
    mycr.execute(de)
    db.commit()
    print("Data deleted successfully .")
