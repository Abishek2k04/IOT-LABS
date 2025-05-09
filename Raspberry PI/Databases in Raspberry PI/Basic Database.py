import sqlite3
import datetime
conn=sqlite3.connect("Temperature.db")
cursor=conn.cursor()
cursor.execute('''CREATE TABLE TempData(Temperature FLOAT,Time FLOAT,Status VARCHAR(10))''')

# cursor.execute("DROP TABLE IF EXISTS TempData")

currecntdatetime=datetime.datetime.now()

cursor.execute("INSERT INTO TempData(Temperature,Time,Status) VALUES(96.2,1.26,'Normal')")
cursor.execute("INSERT INTO TempData(Temperature,Time,Status) VALUES(95.4,1.30,'Normal')")
cursor.execute("INSERT INTO TempData(Temperature,Time,Status) VALUES(100.2,1.34,'Abnormal')")
cursor.execute("INSERT INTO TempData(Temperature,Time,Status) VALUES(101.2,1.40,'Abnormal')")
cursor.execute("INSERT INTO TempData(Temperature,Time,Status) VALUES(92.2,1.16,'Normal')")

var = cursor.execute("SELECT Temperature FROM TempData")
conn.commit()
conn.close()
