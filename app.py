import time, traceback, sys, logging,json,os
from flask import Flask,request,render_template,url_for,redirect

app = Flask(__name__)

app.config['DEBUG'] = os.environ['FLASK_DEBUG']

@app.route("/")
def main():
    return render_template("main.html")
    
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
