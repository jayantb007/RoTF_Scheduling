from flask import Flask,render_template 

#create a flask instance
app=Flask(__name__)

#create a route decorator
@app.route('/')

def index():
        data=["jayant","dosa",2]
        return render_template("index.html",data=data)


@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)

if __name__ == "__main__":
    app.run(debug=True)