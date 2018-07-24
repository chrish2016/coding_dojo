from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = 'ThisIsSecretKey'


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/ninja/<username>')
# def show_user_profile(username):
#     username = 'Ninja Turtle Michelangelo'
#     return render_template("user.html", username=username)

@app.route('/ninja')
def show_all():
    username = 'Michelangelo, Raphael, Leonardo, and Donatello'
    return render_template("user.html", username=username)

@app.route('/ninja/orange')
def show_orange():
    username = 'michelangelo'
    return render_template("user.html", username=username)

@app.route('/ninja/red')
def show_red():
    username = 'raphael'
    return render_template("user.html", username=username)

@app.route('/ninja/blue')
def show_blue():
    username = 'leonardo'
    return render_template("user.html", username=username)

@app.route('/ninja/purple')
def show_purple():
    username = 'donatello'
    return render_template("user.html", username=username)

# @app.route('/ninja/de)
# def show_default():
#     username = 'donatello'
#     return render_template("user.html", username=username)

app.run(debug=True)