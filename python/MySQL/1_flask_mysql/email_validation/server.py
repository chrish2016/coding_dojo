from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'emaildb')
app.secret_key = 'ThisIsSecretKey'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    users = mysql.query_db("SELECT * FROM users")
    print users
    return render_template('/index.html', all_users=users)

@app.route('/process', methods=['POST'])
def create():
    query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    data = {
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    users = mysql.query_db("SELECT * FROM users")
    
    if len(request.form['email']) < 1:
        flash(u'Valid Email must be PROVIDED.', 'error')
        errors = True
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash(u'Invalid Email Address', 'error')
        errors = True   
        return redirect('/')
    else:
        flash(u'The Address is approved.')
        return render_template('/result.html', all_users=users)

@app.route('/remove_email/<user_id>', methods=['POST'])
def delete(user_id):
    print request.form
    query = "DELETE FROM users WHERE id = :specific_id"
    data = {'specific_id': user['id']}
    mysql.query_db(query, data)
    users = mysql.query_db("SELECT * FROM users")
    return render_template('/result.html', all_users=users)

app.run(debug=True)