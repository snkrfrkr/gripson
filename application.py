from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, BooleanField, TextAreaField 
from wtforms.validators import DataRequired, InputRequired, Length, Email
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
import os, time, datetime, bcrypt

#mysql = MySQL()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://service:schubert@localhost:3306/gripson_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "GRIPSWORLD"
db = SQLAlchemy(app)

Bootstrap(app)

class gripson_t(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    dtime = db.Column(db.String(4096))
    go_improvement = db.Column(db.String(2048))
    go_dept_1 = db.Column(db.String(256))
    go_dept_2 = db.Column(db.String(256))
    go_dept_3 = db.Column(db.String(256))
    go_dept_4 = db.Column(db.String(256))
    go_why_1 = db.Column(db.String(2048))
    go_why_2 = db.Column(db.String(2048))
    go_why_3 = db.Column(db.String(2048))
    go_what_1 = db.Column(db.String(2048))
    go_what_2 = db.Column(db.String(2048))
    go_what_3 = db.Column(db.String(2048))
    go_high_1 = db.Column(db.String(2048))
    go_high_2 = db.Column(db.String(2048))
    go_high_3 = db.Column(db.String(2048))

    def __init__ (self, dtime, go_improvement,go_dept_1, go_dept_2, go_dept_3, go_dept_4, go_why_1, go_why_2, go_why_3, go_what_1, go_what_2, go_what_3, go_high_1, go_high_2, go_high_3):
        self.dtime = dtime
        self.go_improvement = go_improvement
        self.go_dept_1 = go_dept_1
        self.go_dept_2 = go_dept_2
        self.go_dept_3 = go_dept_3
        self.go_dept_4 = go_dept_4
        self.go_why_1 = go_why_1
        self.go_why_2 = go_why_2
        self.go_why_3 = go_why_3
        self.go_what_1 = go_what_1
        self.go_what_2 = go_what_2
        self.go_what_3 = go_what_3
        self.go_high_1 = go_high_1
        self.go_high_2 = go_high_2
        self.go_high_3 = go_high_3

class GripsInput(FlaskForm):
    go_improvement = StringField('Verbesserung', validators=[InputRequired(message="Pflichtfeld")])
    go_dept_1 = StringField('Abteilung*', validators=[InputRequired(message="Pflichtfeld")])
    go_dept_2 = StringField('Abteilung')
    go_dept_3 = StringField('Abteilung')
    go_dept_4 = StringField('Abteilung')
    go_why_1 = StringField('Punkt 1*', validators=[InputRequired(message="Pflichtfeld")])
    go_why_2 = StringField('Punkt 2')
    go_why_3 = StringField('Punkt 3')
    go_what_1 = StringField('Punkt 1*', validators=[InputRequired(message="Pflichtfeld")])
    go_what_2 = StringField('Punkt 2')
    go_what_3 = StringField('Punkt 3')
    go_high_1 = StringField('Punkt 1*', validators=[InputRequired(message="Pflichtfeld")])
    go_high_2 = StringField('Punkt 2')
    go_high_3 = StringField('Punkt 3')

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
    if form.validate_on_submit():
        #f = form.image.data
        #filename = secure_filename(f.filename)
        #f.save(os.path.join(
        #    app.instance_path, 'photos', filename
        #))
        g_time = datetime.datetime.now()
        g_improvement = form.go_improvement.data
        g_dept_1 = form.go_dept_1.data
        g_dept_2 = form.go_dept_2.data
        g_dept_3 = form.go_dept_3.data
        g_dept_4 = form.go_dept_4.data
        g_why_1 = form.go_why_1.data
        g_why_2 = form.go_why_2.data
        g_why_3 = form.go_why_3.data
        g_what_1 = form.go_what_1.data
        g_what_2 = form.go_what_2.data
        g_what_3 = form.go_what_3.data
        g_high_1 = form.go_high_1.data
        g_high_2 = form.go_high_2.data
        g_high_3 = form.go_high_3.data
        db_write = gripson_t(g_time, g_improvement, g_dept_1, g_dept_2, g_dept_3, g_dept_4, g_why_1, g_why_2, g_why_3, g_what_1, g_what_2, g_what_3, g_high_1, g_high_2, g_high_3)
        db.session.add(db_write)
        db.session.commit()
        return render_template("ok.html" )
    return render_template("form.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)