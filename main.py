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
            cur = mysql.connect().cursor()
            sql = "SELECT text FROM gripson_t"
            cur.execute(sql)
            data = cur.fetchall()
            return str(data)            
            #return render_template("index.html")
        except:
            print("NOK")
        

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
            return render_template("login.html")

if __name__ == '__main__':
    app.run()
