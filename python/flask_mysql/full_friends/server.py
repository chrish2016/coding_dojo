from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'fullfriendsdb')
app.secret_key = 'ThisIsSecretKey'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    users = mysql.query_db("SELECT * FROM users")
    return render_template('/index.html', all_users=users)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO users(first_name, last_name, email, created_at, updated_at) VALUES(:first_name, :last_name, :email, NOW(), NOW())"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/friends/<id>/edit', methods=['GET','POST'])
def edit(id):
    data = { "id": id }
    query = "SELECT * FROM users WHERE id = :id"
    user = mysql.query_db(query, data)
    return render_template('/edit.html', user=user, id=id)


@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = "INSERT INTO users(first_name, last_name, email, updated_at) VALUES(:first_name, :last_name, :email, NOW())"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "specific_id": id
    }
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/friends/<user_id>/delete', methods=['POST'])
def destroy(user_id):
    print request.form
    query = "DELETE FROM users WHERE id = :specific_id"
    users = mysql.query_db("SELECT * FROM users")
    data = { "specific_id": user_id }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)