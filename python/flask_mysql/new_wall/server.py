from flask import Flask, request, redirect, render_template, flash, session, url_for
from mysqlconnection import MySQLConnector
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import os
import re

app = Flask(__name__)

mysql = MySQLConnector(app, 'walldb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
Bootstrap(app)
app.secret_key = os.urandom(24)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


#///////////////// Classes /////////////////

@app.route('/')
def index():
    if "logged_id" in session:
        return redirect('/main')
    # users = mysql.query_db("SELECT * FROM users")
    # print users
    return render_template('index.html')
 
@app.route('/login', methods=['POST'])
def login():
    query = "SELECT * FROM users WHERE email = :email"
    data = {
        'email': request.form['email']
    }
    dbdata = mysql.query_db(query, data)
    if len(dbdata) > 0:
        user = dbdata[0]
        if user['password'] == request.form['password']:
            session['logged_id'] = user['id']
            print "SUCCESS", request.form
            return redirect('/main')
    print "FAILED!", request.form
    return redirect('/')

@app.route('/main')
def main():
    if "logged_id" not in session:
        return redirect('/')
    query = "SELECT * FROM users WHERE id = :logged_id"
    data = {
        'logged_id': session['logged_id']
    }
    logged_user = mysql.query_db(query, data)[0]
    print request.form
    return render_template('main.html', current_user=logged_user)

@app.route('/logout')
def logout():
    session['logged_user'] = False
    return render_template('index.html')
 
if __name__ == "__main__":
    app.run(debug=True)