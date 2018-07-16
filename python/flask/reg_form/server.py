from flask import Flask, render_template, request, redirect, session, flash
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
import re

app = Flask(__name__)
app.secret_key = 'ThisIsSecretKey'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# class ContactForm(Form):
#     first_name = TextField("first_name",  [validators.Required()])
#     last_name = TextField("last_name",  [validators.Required()])
#     email = TextField("Email",  [validators.Required()])
#     password = TextField("password",  [validators.Required()])
#     pw_confirm = TextAreaField("pw_confirm",  [validators.Required()])
#     birthday = TextField("birthday",  [validators.Required()])
#     submit = SubmitField("Send")



@app.route('/')
def index():
    # return 'Home Dojo Survey'
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create_user():
    errors = False
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['pw_confirm'] = request.form['pw_confirm']
    session['birthday'] = request.form['birthday']
    first_name = session['first_name']
    last_name = session['last_name']
    password = session['password']
    pw_confirm = session['pw_confirm']

    if len(request.form['first_name']) < 1:
        flash(u'First Name must be PROVIDED', 'error')
        errors = True
    elif not str(first_name).isalpha():
        flash(u'First Name cannot contain numbers', 'error')
        errors = True

    if len(request.form['last_name']) < 1:
        flash(u'Last Name must be PROVIDED.', 'error')
        errors = True
    elif not str(last_name).isalpha():
        flash(u'Last Name cannot contain a number.', 'error')
        errors = True

    if len(request.form['email']) < 1:
        flash(u'Valid Email must be PROVIDED.', 'error')
        errors = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash(u'Invalid Email Address', 'error')
        errors = True

    if len(request.form['password']) < 1:
        flash(u'Valid email must be PROVIDED.', 'error')
        errors = True
    if password != pw_confirm:
        flash(u'Password does not match. Please try again..', 'error')
        errors = True

    if errors:
        return redirect('/')
    
    session['submitted_info'] = request.form
    return redirect('/result')
    # return render_template('/result.html')

@app.route('/result')
def success():
    print session['submitted_info']
    return render_template('result.html', result=session['submitted_info'])
    

app.run(debug=True)