import sqlite3

db = sqlite3.connect("abc.db")

rollno=input("Enter the roll_no:")
name=input("Enter the name:")
db.execute("UPDATE SUNDAY SET NAME=(?)WHERE ROLL_NO=(?)",(name,rollno))
print("Data upadated")

db.execute("ALTER TABLE SUNDAY RENAME TO MONDAY")

SHOW=db.execute("SELECT * FROM MONDAY")
print(SHOW)
DATA=sqlite3.Cursor.fetchall(SHOW)
print(DATA)
print(type(DATA))
for i in DATA:
    print(i)