from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="negi123",
    database="student_details",
    port=3306
)

cursor = conn.cursor()

cursor.execute("SELECT DATABASE()")
print("CURRENT DB:", cursor.fetchone())

cursor.execute("SELECT @@hostname")
print("MYSQL HOST:", cursor.fetchone())

# Home
@app.route('/')
def home():
    return render_template("do.html")

#  Add Data
@app.route('/add', methods=['POST'])
def add():
    id = request.form["id"]
    name = request.form["name"]
    age = request.form["age"]
    email = request.form["email"]

    cursor.execute(
        "INSERT INTO users (id, name, age, email) VALUES (%s, %s, %s, %s)",
        (id, name, age, email)
    )
    conn.commit()

    return redirect(url_for('show'))

#  Show Data
@app.route('/show')
def show():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    print("DATA FROM DB:", data)
    return render_template("result.html", users=data)

#  Delete
@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()
    return redirect(url_for('show'))

#  Edit
@app.route('/edit/<int:id>')
def edit(id):
    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cursor.fetchone()
    return render_template("edit.html", user=user)

# Update
@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']

    cursor.execute(
        "UPDATE users SET name=%s, age=%s, email=%s WHERE id=%s",
        (name, age, email, id)
    )
    conn.commit()

    return redirect(url_for('show'))

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="negi123",
        database="student_details"
    )

if __name__ == "__main__":
    app.run(debug=True)