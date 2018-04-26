from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import time, bcrypt

app = Flask(__name__)
Bootstrap(app)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
            return render_template("index.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
            return render_template("login.html")

if __name__ == '__main__':
    app.run()
