import random

def score_grades():
    score = random.randint(0, 100)
    # random_num = random.randint()

    if(score >= 90 and score <= 100):
        print "Your score is",score, ";", " Your grade is an A."
    elif(score >= 80 and score <= 90):
        print "Your score is",score, ";", " Your grade is a B."
    elif(score >= 70 and score <= 80):
        print "Your score is",score, ";", " Your grade is a C."
    elif(score >= 60 and score <= 70):
        print "Your score is",score, ";", " Your grade is a D."
    else:
        print "Your score is",score, ";", " FAILED! YOU GET AN 'F'"   
    
score_grades()
