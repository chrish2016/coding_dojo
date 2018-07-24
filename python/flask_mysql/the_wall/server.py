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
    if "logged_id" not in session:
        return redirect('/')
    query = "SELECT * FROM users WHERE id = :logged_id"
    data = {
        'logged_id': session['logged_id']
    }
    logged_user = mysql.query_db(query, data)[0]
    # messages_query = "SELECT first_name, messages.message, messages.created_at FROM messages JOIN users ON users.id = user_id;"
    
    # messages_query = "SELECT first_name, messages.message, messages.created_at FROM messages JOIN users ON users.id = user_id;"
    messages_query = "SELECT users.first_name, messages.message, messages.created_at, messages.user_id, comments.comment, comments.created_at, comments.user_id, users.id FROM users JOIN messages ON users.id = messages.user_id JOIN comments ON users.id = comments.user_id;"
    messages = mysql.query_db(messages_query)
    return render_template('user.html', current_user=logged_user, all_messages=messages)

@app.route('/messages', methods=['POST'])
def messages():
    query = "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:slot_one, :slot_two, NOW(), NOW());"
    data = {
        'slot_one':request.form['message'],
        'slot_two':session['logged_id']
    }
    inserted_id = mysql.query_db(query, data)
    print request.form
    return redirect('/wall')

@app.route('/comments', methods=['POST'])
def comments():
    query = "INSERT INTO comments (comment, user_id, created_at, updated_at) VALUES (:slot_one, :slot_two, NOW(), NOW());"
    data = {
        'slot_one':request.form['comment'],
        'slot_two':session['logged_id']
    }
    inserted_id = mysql.query_db(query, data)
    print request.form
    return redirect('/')    # return redirect('/wall')

@app.route('/delete/<message_id>', methods=['POST'])
def delete(user_id):
    if "logged_id" not in session:
        return redirect('/')
    query = "DELETE FROM messages, comments WHERE id = :logged_id"
    data = { 'logged_id': session['logged_id'] }
    logged_user = mysql.query_db(query, data)[0]
    return redirect('/')


app.run(debug=True)
