from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='jayant'
app.config['MYSQL_DB']='rotf'

mysql=MySQL(app)

######## for ordered database
@app.route('/test')
def test():
        cur=mysql.connection.cursor()
        r=cur.execute("SELECT * FROM ordered")
        if r>0:
            userdetails=cur.fetchall()
            return render_template('try.html',userdetails=userdetails)


@app.route('/',methods=['GET','POST'])
def home ():
    if request.method=='POST':
        userdetails=request.form
        roll_no=(userdetails["roll"])
        name=userdetails["name"]
        age=(userdetails["age"])
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO new_table(roll_no,name,age) VALUES (%s,%s,%s)",(roll_no,name,age))
        mysql.connection.commit()
        cur.close()
        return redirect('/database')

    return render_template('form.html')

@app.route('/database')
def database():
        cur=mysql.connection.cursor()
        r=cur.execute("SELECT * FROM new_table")
        if r>0:
            userdetails=cur.fetchall()
            return render_template('try.html',userdetails=userdetails)



if __name__ == "__main__":
    app.run(debug=True)