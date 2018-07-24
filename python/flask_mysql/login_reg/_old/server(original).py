from flask import Flask, request, redirect, url_for, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import re
import md5  # basic encryption
import hashlib
import os, binascii  # salt encryption added

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login = LoginManager(app)
mysql = MySQLConnector(app, 'loginregdb')
bcrypt = Bcrypt(app)
app.secret_key = 'ThisIsSecretKey'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
salt = binascii.b2a_hex(os.urandom(15))


@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/register', methods=['POST'])
def register():
    valid = True
    if request.form['first_name'] == '':
        valid = False
        flash("first name cannot be blank")
    if request.form['last_name'] == '':
        valid = False
        flash("last name cannot be blank")
    if request.form['email'] == '':
        valid = False
        flash("email cannot be blank")
    if request.form['pw_hash'] == '':
        valid = False
        flash("password cannot be blank")
    if request.form['confirm'] == '':
        valid = False
        flash("confirm cannot be blank")
    if not request.form['pw_hash'] == request.form['confirm']:
        valid = False
        flash("password and confirmation do not match")
    if not valid:
        return redirect('/')
    else:
        query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_bcrypt,  NOW(), NOW())"
        data = {
            session['first_name']: request.form['first_name'],
            session['last_name']: request.form['last_name'],
            session['email']: request.form['email'],
            session['pw_hash']: request.form['pw_hash'],
            'pw_bcrypt': bcrypt.generate_password_hash('pw_hash')
        }
        mysql.query_db(query, data)
        flash("User registered. Please login.")
        return redirect('/users')

@app.route('/login', methods=['POST'])
def login():
    users = mysql.query_db("SELECT * FROM users")
    email = request.form['email']
    password = request.form['pw_hash']
    pw_hash = bcrypt.generate_password_hash(password)
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data)
    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        flash("SUCCESS")
        print "SUCCESS"
        return redirect('/users')
    else:
        flash("FAILURE")
        print "FAILURE"
        return redirect('/')

@app.route('/users')
def show_users():
    users = mysql.query_db("SELECT * FROM users")
    return render_template('users.html', all_users=users)

app.run(debug=True)