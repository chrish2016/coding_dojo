from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def count():
    try:
        session['count'] += 1
    except:
        session['count'] = 1
    return render_template('index.html')

app.run(debug=True)