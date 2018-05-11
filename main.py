from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import time, bcrypt
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
Bootstrap(app)

app.config['MYSQL_DATABASE_USER'] = 'service'
app.config['MYSQL_DATABASE_PASSWORD'] = 'schubert'
app.config['MYSQL_DATABASE_DB'] = 'gripson_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
mysql.connect()
if mysql:
    print ("OK")


@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        try:
            cur1 = mysql.connect().cursor()
            sql_id = "SELECT id FROM gripson_t"
            cur1.execute(sql_id)
            id_t = cur1.fetchall()
            
            cur2 = mysql.connect().cursor()
            sql_text = "SELECT text FROM gripson_t"
            cur2.execute(sql_text)
            text_t = cur2.fetchall()

            cur3 = mysql.connect().cursor()
            sql_desc = "SELECT description FROM gripson_t"
            cur3.execute(sql_desc)
            desc_t = cur3.fetchall()

            db_len = (len(id_t))

            return render_template("index.html", db_len=db_len, idt=id_t, text=text_t, desc=desc_t)
        except:
            print("NOK")
        

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
            return render_template("login.html")

if __name__ == '__main__':
    app.run()
