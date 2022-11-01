import paho.mqtt.client as mqtt #import the client1
import time
import json
from datetime import datetime
import mysql.connector
##############################################
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    y=message.payload.decode("utf-8")
    f=json.loads(y)
    order_no_=f["order"][0]["order_no"]
    table_no_=f["order"][0]["Table_no"]
    orderID=f["order"][0]["OrderID"]
    OrderName=f["order"][0]["OrderName"]
    OrderTime=f["order"][0]["OrderTime"]
    orderTime=datetime.strptime(OrderTime, '%Y-%m-%d %H:%M:%S')       #to convert the string OrderTime to datetime format
    BrewingTime=f["order"][0]["BrewingTime"]
    brewingTime=datetime.strptime(BrewingTime, '%H:%M:%S').time()
    print(order_no_,table_no_,orderID,OrderName, orderTime, brewingTime)
    print(type(OrderTime))
    print(type(orderTime))
    print(type(BrewingTime))
    print(type(brewingTime))
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jayant",
    database="rotf"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO ordered (order_no,Table_no,OrderID,OrderName, OrderTime, BrewingTime) VALUES (%s, %s, %s, %s,%s,%s)"
    val = (order_no_,table_no_,orderID,OrderName, orderTime.strftime('%Y-%m-%d %H:%M:%S'), brewingTime.strftime('%H:%M:%S'))
    # val = (order_no,table_no,orderID,OrderName, OrderTime, BrewingTime)
    # val = (order_no_,table_no_,orderID,OrderName, datetime.now().strftime('%Y-%m-%d %H:%M:%S'),datetime.now().strftime('%H:%M:%S'))

    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    #print(k)
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain) 
                                                                                        
##############################################
#broker_address="local host"
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password="abrupa22"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE trialdb")


#mycursor.execute("CREATE TABLE order (orderid INT NOT NULL, item VARCHAR(255), category VARCHAR(10), tableno INT, time INT NOT NULL)")
broker_address="broker.hivemq.com"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","IOT/CK")
client.subscribe("IOT/CK")
with open('C:/Users/Hp/Desktop/RoTF/JAYANT_MaRS_IOT/Exp_order.json') as f:
   data = json.load(f)

data1=json.dumps(data)
print("Publishing message to topic","IOT/CK")
client.publish("IOT/CK",data1)
time.sleep(4) # wait
client.loop_stop() #stop the loop