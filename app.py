from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

def connectDB():
    return mysql.connector.connect(
        host = "localhost",
        user="root",
        password="Shru@011",
        database="office"
    )

@app.route("/", methods=["GET","POST"])
def home():
    con = connectDB()
    cur = con.cursor()


# Insert records
    if request.method == "POST":
      emp_name = request.form["emp_name"]
      department = request.form["department"]
      salary = request.form["salary"]

      cur.execute("INSERT INTO employees(emp_name, department, salary) VALUES (%s, %s, %s)",
                (emp_name, department, salary))
      con.commit()

# Fetch records
    cur.execute("SELECT * FROM employees")
    data = cur.fetchall()

    con.close()

    return render_template("index.html", employees=data)

if __name__ == "__main__":
    app.run(debug=True)
