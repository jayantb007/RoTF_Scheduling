from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
from datetime import datetime
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='jayant'
app.config['MYSQL_DB']='rotf'

mysql=MySQL(app)

######## for ordered database

@app.route('/',methods=['GET','POST'])
def home ():
    cur=mysql.connection.cursor()
    r=cur.execute("SELECT * FROM kitchen")
    userdetails=cur.fetchall()
    if request.method=='POST':
        userdetails=request.form
        order_no=(userdetails["order_no"])
        # return order_no
        cur=mysql.connection.cursor()

        r= cur.execute("SELECT * from kitchen WHERE order_no=(%s)",order_no)
        mysql.connection.commit()
        if r>0:
            r=cur.execute("INSERT INTO scheduled(order_no,Table_no,OrderID,OrderName, OrderTime, BrewingTime) SELECT order_no,Table_no,OrderID,OrderName, OrderTime, BrewingTime FROM ordered WHERE order_no=(%s) ",(order_no))
            mysql.connection.commit()
            #################
            r=cur.execute("UPDATE scheduled SET PreparedTime =(%s) WHERE order_no=(%s) ",(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),order_no))
            mysql.connection.commit()

            cur.execute("DELETE FROM kitchen WHERE order_no=(%s)",(order_no))
            mysql.connection.commit()
            cur.close()
        return redirect('/')
        
    return render_template('form2.html',userdetails=userdetails)

@app.route('/ordered')
def ordered():
        cur=mysql.connection.cursor()
        r=cur.execute("SELECT * FROM ordered")
        if r>0:
            userdetails=cur.fetchall()
            return render_template('try.html',userdetails=userdetails)

@app.route('/kitchen')
def kitchen():
        cur=mysql.connection.cursor()
        r=cur.execute("SELECT * FROM kitchen")
        if r>0:
            userdetails=cur.fetchall()
            return render_template('try.html',userdetails=userdetails)

@app.route('/scheduled')
def scheduled():
        cur=mysql.connection.cursor()
        r=cur.execute("SELECT * FROM scheduled")
        if r>0:
            userdetails=cur.fetchall()
            return render_template('try.html',userdetails=userdetails)
        else:
            return render_template('empty.html')

########under development
# try to get the last entry and extract its order_no then add 1 to get new order_no
@app.route('/insert')
def insert():
    if request.method=='POST':
        userdetails=request.form
        table_no=(userdetails["table_no"])
        order_id=userdetails["order_id"]
        cur=mysql.connection.cursor()
        List=["","COFFEE","TEA","RAMEN","WUFFLE","DOSA","PANCAKE","MOMO","CHOLE BHATURE"]
        order_name=List[order_id]
        order_no+=1
        cur.execute("INSERT INTO ordered(roll_no,name,age) VALUES (%s,%s,%s)",(roll_no,name,age))
        mysql.connection.commit()
        cur.close()
        return redirect('/database')

    return render_template('form3.html')



if __name__ == "__main__":
    app.run(debug=True)