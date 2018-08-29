import time, traceback, sys, logging,json,os
from flask import Flask,request,render_template,url_for,redirect

app = Flask(__name__)

app.config['DEBUG'] = os.environ['DEBUG']

@app.route("/")
def main():
    return render_template("main.html")
