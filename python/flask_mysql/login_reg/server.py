from flask import Flask, request, redirect, url_for, render_template, session, flash
from mysqlconnection import MySQLConnector

import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'loginregdb')
app.secret_key = 'ThisIsSecretKey'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if "logged_id" in session:
        return redirect('/profile')
    return render_template('/index.html')

@app.route('/register', methods=['POST'])
def register():
    valid = True
    if request.form['first_name'] == '':
        valid = False
        flash('first name cannot be blank')
    if request.form['last_name'] == '':
        valid = False
        flash('last name cannot be blank')
    if request.form['email'] == '':
        valid = False
        flash('email cannot be blank')
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address')
        valid = False   
    if request.form['password'] == '':
        valid = False
        flash('password cannot be blank')
    if request.form['confirm'] == '':
        valid = False
        flash('confirm cannot be blank')
    if not request.form['confirm'] == request.form['confirm']:
        valid = False
        flash('password and confirmation must match')
    if not valid:
        return redirect('/')
    else:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password,  NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': request.form['password']
        }
        mysql.query_db(query, data)
        flash('User registered. Please login.')
        return render_template('/index.html')

@app.route('/login', methods=['POST'])
def login():
    valid = True
    if request.form['email'] == '':
        valid = False
        flash('email cannot be blank')
    if request.form['password'] == '':
        valid = False
        flash('password cannot be blank')
    if not valid:
        return redirect('/')
    else:
        query = "SELECT * FROM users WHERE email = :email"
        data = {
            'email': request.form['email']
        }
        dbdata = mysql.query_db(query, data)
        if len(dbdata) > 0:
            user = dbdata[0]
            if user['password'] == request.form['password']:
                session['logged_id'] = user['id']
                return redirect('/users')
        flash('data does not match database')
        return redirect('/profile')

@app.route('/logout')
def logout():
    session.pop('logged_id')
    return redirect(url_for('index'))
   
@app.route('/users')
def show_users():
    users = mysql.query_db("SELECT * FROM users")
    return render_template('users.html', all_users=users)

@app.route('/profile')
def profile():
    query = "SELECT * FROM users WHERE id = :logged_id"
    data = {
        'logged_id': session['logged_id']
    }
    logged_user = mysql.query_db(query, data)[0]
    return render_template('profile.html', current_user=logged_user)


app.run(debug=True)