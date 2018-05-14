from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import time, bcrypt
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField

#mysql = MySQL()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://service:schubert@localhost:3306/gripson_db"
app.config["SECRET_KEY"] = "GRIPSWORLD"
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

class GripsInput(FlaskForm):
    text = StringField('text')
    description = StringField('description')
    before = StringField('before')
    after = StringField('after')

db_in = gripson_t.query.all()
db_len = len(db_in)
print(db_len)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        try:
            return render_template("index.html", data=gripson_t.query.all(), db_len=db_len )
        except:
            print("NOK")
        

@app.route("/form", methods = ['GET', 'POST'])
def form():
    form = GripsInput()
    if form.validate_on_submit():
        g_text = form.text.data
        g_description = form.description.data
        g_before = form.before.data
        g_after = form.after.data
        db_write = gripson_t(g_text, g_description, g_before, g_after)
        db.session.add(db_write)
        db.session.commit()
        return "OK"
        time.sleep(1)
        return render_template("form.html", form=form )
    return render_template("form.html", form=form )

if __name__ == '__main__':
    app.run()