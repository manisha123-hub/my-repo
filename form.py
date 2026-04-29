import mysql.connector
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="negi123",
    database="student_details"
)

cursor = conn.cursor()

# Home page (form)
@app.route("/")
def home():
    return render_template("form.html")





# Show all data
@app.route("/data")
def show_data():
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return render_template("data.html", data=data)


# Delete data
@app.route("/delete/<int:id>")
def delete(id):
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()
    return redirect("/data")


# Edit page
@app.route("/edit/<int:id>")
def edit(id):
    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cursor.fetchone()
    return render_template("edit.html", user=user)


# Update data
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    name = request.form["name"].title()
    age = request.form["age"]
    email = request.form["email"]

    cursor.execute(
        "UPDATE users SET name=%s, age=%s, email=%s WHERE id=%s",
        (name, age, email, id)
    )
    conn.commit()

    return redirect("/data")



if __name__ == "__main__":
    app.run(debug=True)