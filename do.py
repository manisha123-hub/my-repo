from flask import Flask,request,render_template,redirect,url_for
app = Flask(__name__)
users=[]

@app.route('/')
def home():
    return render_template("do.html")

@app.route("/add",methods=["POST"])
def add():
    name=request.form["name"]
    age=request.form["age"]
    roll=request.form["roll_no"]
    email=request.form["email"]
    
    user = {
        "name":name,
        "age":age,
        "roll":roll,
        "email":email
        }
    users.append(user)
    return redirect(url_for('show'))    #move to next page which is /show

@app.route("/show")     
def show():
     return render_template("result.html", users=users)  #show ke liye file result>html hai


    
if __name__=="__main__":
        app.run(debug=True)     # app run krao agr vo main hai to

