from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import time, bcrypt
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, BooleanField 
from wtforms.validators import DataRequired, InputRequired, Length, Email
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
import os, time, datetime

#mysql = MySQL()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://service:schubert@localhost:3306/gripson_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "GRIPSWORLD"
db = SQLAlchemy(app)

Bootstrap(app)

class gripson_t(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    dtime = db.Column(db.DateTime)
    text = db.Column(db.String(4096))
    description = db.Column(db.String(4096))
    before = db.Column(db.String(4096))
    after = db.Column(db.String(4096))

    def __init__ (self, text, description, before, after):
        self.dtime = dtime
        self.text = text
        self.description = description
        self.before = before
        self.after = after

class GripsInput(FlaskForm):
    text = StringField('text')
    description = StringField('description')
    before = StringField('before')
    after = StringField('after')
    image = FileField(validators=[FileRequired()])
    check = BooleanField('check')

db_in = gripson_t.query.all()
db_len = len(db_in)
print(str(db_len) + " Einträge in der Datenbank")

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
    names = ["Entry1", "Entry2", "Entry3"]
    if form.validate_on_submit():
        f = form.image.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, 'photos', filename
        ))
        g_time = datetime.datetime.now()
        g_text = form.text.data
        g_description = form.description.data
        g_before = form.before.data
        g_after = form.after.data
        g_image = form.image.data
        #print(f.value)
        db_write = gripson_t(g_time, g_text, g_description, g_before, g_after)
        db.session.add(db_write)
        db.session.commit()
        return render_template("ok.html" )
    return render_template("form.html", form=form, names=names )

if __name__ == '__main__':
    app.run(debug=True)