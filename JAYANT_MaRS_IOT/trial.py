import mysql.connector
from datetime import datetime
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="jayant",
database="rotf"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE order (orderid INT NOT NULL, item VARCHAR(255), category VARCHAR(10), tableno INT, time INT NOT NULL)")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO `mars_iot_not_prepare` (idprepared,orderid,item,category,t1,t2,tab,name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
val = ("5","5","MOMO","A","115","13","4",datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")