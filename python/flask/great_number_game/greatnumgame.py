import random
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    session['number'] = request.form['number']
    session['machine'] = random.randint(1, 4)
    
    print "Machine: ", session['machine']
    print "Me", session['number']
    if(session['machine'] > session['number']):
        print "too low"
    elif(session['machine'] < session['number']):
        print "too high"
    elif(session['machine'] == session['number']):
        print "YOU WON!"
    
    return redirect('/show')

@app.route('/show')
def show():
    return render_template('/guess.html')




app.run(debug=True)