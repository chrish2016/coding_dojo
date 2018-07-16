from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    # return render_template('user.html')
    return redirect('/show')


@app.route('/show')
def show_users():
    return render_template('user.html')



app.run(debug=True)