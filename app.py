from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Tsacolah1'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.189.212.51'
mysql.init_app(app)

#cur = mysql.connection.cursor()

select_var = "SELECT * FROM students"

@app.route("/")
def hello():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM students''')
    rv = cur.fetchall()
    return str(rv)
    #cur.close()
    
@app.route("/add")
def add():
    cur = mysql.connection.cursor() 
    cur.execute("""INSERT INTO students(studentName,email)VALUES(%s,%s)""",("John Smith","email@"))
    cur.execute('''SELECT * FROM students''')
    ab = cur.fetchall()
   # app.commit() how to commit changes to DB??????
    return str(ab)
   # cur.close()

@app.route("/update")
def update():
    cur = mysql.connection.cursor()

    querey = "Update students SET studentName = %s WHERE studentID =%s"
    cur.execute(querey,("Ronan",1))
    cur.execute(select_var)
    ab = cur.fetchall()

    return "Update" + str(ab)
    
@app.route("/delete")
def delete():
    cur = mysql.connection.cursor()

    deleteQ = "DELETE FROM students WHERE studentID = %s" % ("2")
    cur.execute(deleteQ)
    cur.execute(select_var)
    ab = cur.fetchall()
    return "Delete page" + str(ab)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000')
