from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecretKey'

@app.route('/')
def index():
    # return 'Home Dojo Survey'
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create_user():
    errors = False
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        errors = True
    # else:
    #     flash("Success! Your name is {}".format(request.form['name']))
    if len(request.form['comment']) > 120:
        flash("You've reached the max limit(120 characters)")
        errors = True
    if len(request.form['comment']) < 0:
        flash("Are you sure you don't want to share?")
        errors = True
    # else:
    #     flash("Success! Your commment was passed: {}".format(request.form['comment']))
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