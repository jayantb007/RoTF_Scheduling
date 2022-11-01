import mysql.connector
from datetime import datetime
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jayant",
  database="rotf"
)

mycursor = mydb.cursor()

sql1 = "SELECT PreparedTime FROM try"


mycursor.execute(sql1)
PreparedTime = mycursor.fetchall()
sql1 = "SELECT ExpectedTime FROM try"
mycursor.execute(sql1)
ExpectedTime = mycursor.fetchall()

sql1 = "SELECT Order_no FROM try"
mycursor.execute(sql1)
Order_no = mycursor.fetchall()

now=datetime.now()
print(ExpectedTime[0][0])
print(now)
A=[0 for i in range(7)]

for i in range(7):
        A[i]=(ExpectedTime[i][0]-now)

A.sort()
for i in range(7):
    print(A[i])
        