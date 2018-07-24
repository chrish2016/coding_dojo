from flask import Flask, request, redirect, render_template, flash, session, url_for
from mysqlconnection import MySQLConnector
app = Flask(__name__)

import re
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'walldb')
app.secret_key = 'ThisIsSecretKey'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if "logged_id" in session:
        return redirect('/wall')
    users = mysql.query_db("SELECT * FROM users")
    return render_template('index.html')

@app.route('/registration', methods=['POST'])
def registration():
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password']
    }
    user = mysql.query_db(query, data)
    flash('REGISTERED. Login immediately.')
    return redirect('/')

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
            return redirect('/wall')
    flash('data does not match database')
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('logged_id')
    return redirect(url_for('index'))

@app.route('/wall')
def user():
    if "logged_id" in session:
        users = mysql.query_db("SELECT * FROM users")
        return render_template('user.html', all_users=users)

@app.route('/messages', methods=['POST'])
def messages():
    query = "INSERT INTO messages (message, created_at, updated_at) VALUES (:messages, NOW(), NOW())"
    data = {
        'message': request.form['messages']
    }
    mysql.query_db(query, data)
    print request.form
    return redirect('/')

app.run(debug=True)
