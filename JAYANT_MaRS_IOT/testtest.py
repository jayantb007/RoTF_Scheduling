from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="jayant",
database="try"
)

mycursor = mydb.cursor()

mycursor.execute("UPDATE try1 SET VALUES(%s) WHERE name=(%s) ",(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"ABC"))
mydb.commit()
