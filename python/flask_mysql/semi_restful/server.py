from flask import Flask, request, redirect, render_template, flash, session, url_for, abort
from mysqlconnection import MySQLConnector
from flask_bootstrap import Bootstrap
import os
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'semidb')
app.secret_key = os.urandom(24)
Bootstrap(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# /////////////////// Index() = home ///////////////////

@app.route('/') #Takes you to the front(login) page
def index(): 
    if 'logged_id' in session:
        return redirect('/users')
    users = mysql.query_db('SELECT * FROM users')
    print users
    return render_template('index.html')



# /////////////////// Logging In ///////////////////

@app.route('/login', methods=['POST']) #Logging in/Session starts
def login():
    query = "SELECT * FROM users WHERE email = :email"
    data = {
     'email': request.form['email']     
    }
    dbdata = mysql.query_db(query, data)
    if dbdata > 0:
        user = dbdata[0]
        if user['password'] == request.form['password']:
            session['logged_id'] = user['id']
            return redirect('/users')
    flash('email password does not match.')
    print request.form
    return redirect('/')



# /////////////////// Log Out ///////////////////

@app.route('/logout')
def logout():
    session.pop('logged_id')
    return redirect(url_for('index'))



# /////////////////// show all users ///////////////////

@app.route('/users')  #Display all the users.
def show_users():
    if 'logged_id' not in session:
        return redirect('/')
    logged_id = session['logged_id']
    query = "SELECT id, CONCAT(first_name,' ', last_name) AS full_name, email, password, created_at FROM users;"
    data = {
        'logged_id': session['logged_id']
    }
    logged_user = mysql.query_db(query, data)[0]
    users = mysql.query_db(query, data)
    return render_template('/users.html', all_users=users, current_user=logged_user)



# /////////////////// show user ///////////////////

@app.route('/users/<id>')  #Show method to display the info for a particular user with given id. This will need a template. 
def user(id):
    query = "SELECT * FROM users WHERE id = :id"
    data = {
        'id': id
    }
    user = mysql.query_db(query, data)
    return render_template('user.html', all_users=user, id=id)



# /////////////////// create a user ///////////////////

@app.route('/users/new_user')  #Display a form allowing users to create a new user.
def new_user():
    return render_template('create_user.html')



# /////////////////// processing create a user ///////////////////

@app.route('/users/create_user', methods=['POST'])  #Sent from the form on the page /users/new_user. Have this redirect to /users/<id> once created.
def create_user():
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'logged_id': session['logged_id']
    }
    mysql.query_db(query, data)
    user = mysql.query_db(query, data)
    return redirect('/users', all_users=user, current_user=logged_user)



# /////////////////// editing a user's info ///////////////////

@app.route('/users/<id>/edit') #Edit an existing user with the given id.
def edit_user(id):
    query = "SELECT * FROM users WHERE id = :id"
    data = {
        'id': id
    }
    user = mysql.query_db(query, data)
    return render_template('edit_user.html', all_users=user, id=id)


# /////////////////// updated user's info ///////////////////

@app.route('/users/<id>', methods=['POST'])
def update_user(id):
    query = "INSERT INTO users(first_name, last_name, email, password, updated_at) VALUES(:first_name, :last_name, :email, :password, NOW())"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": request.form['password'],
        "id": id
    }
    mysql.query_db(query, data)
    return redirect('/users/<id>')


# /////////////////// deleting a user ///////////////////

@app.route('/users/<id>/destroy', methods=['POST'])
def delete_user(id):
    query = "DELETE FROM users WHERE id = :id"
    data = {
        'id': id
    }
    users = mysql.query_db(query, data)
    return redirect('/users')



# /////////////////// END ///////////////////

if __name__ == "__main__":
    app.run(debug=True)


