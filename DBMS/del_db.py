
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="Shashwat28102004")

mycr = db.cursor()
mycr.execute("DROP DATABASE BANK_007")

db.commit()
