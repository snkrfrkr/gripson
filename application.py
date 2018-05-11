from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import time, bcrypt
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy

#mysql = MySQL()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://service:schubert@localhost:3306/gripson_db"
db = SQLAlchemy(app)

class gripson_t(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    text = db.Column(db.String(4096))
    description = db.Column(db.String(4096))
    before = db.Column(db.String(4096))
    after = db.Column(db.String(4096))

def __init__ (self, text, description, before, after):
    self.text = text
    self.description = description
    self.before = before
    self.after = after

a = gripson_t.query.all()
for i in a:
    print(i)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        try:
            return render_template("index.html", data=gripson_t.query.all(), db_len=5 )
        except:
            print("NOK")
        

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
            return render_template("login.html", data=gripson_t.query.all() )

if __name__ == '__main__':
    app.run()
