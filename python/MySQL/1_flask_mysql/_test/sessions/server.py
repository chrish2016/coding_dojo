from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
 
app = Flask(__name__)
app.secret_key = os.urandom(12) #secret key generator!

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return index()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()
 
if __name__ == "__main__":
    app.run(debug=True)