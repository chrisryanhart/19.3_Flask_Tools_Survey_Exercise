"""Note:  Have not covered session material yet.  Therefore, I will return to step 8 at a later time.  """

from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

# store user's survey responses here.  Delete by restarting the server until step 8 complete.
responses = []
question_count = {"num": 0}
q_index=0
q_max=len(satisfaction_survey.questions)


@app.route('/')
def ask_survey():
    responses.clear()
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('base.html', instructions=instructions, title=title)


@app.route('/questions/<int:q_count>')
def answer_question(q_count):
    """ask questions to user"""
    global q_index
    global q_max

    if q_index>=q_max:
        flash('Survey has been Completed!')
        return redirect('/complete')
    
    if q_count != q_index and q_index!=q_max:
        flash('Wrong question number!')
        return redirect(f"/questions/{q_index}")

    
    question = satisfaction_survey.questions[q_count]
    choices = satisfaction_survey.questions[q_count].choices
    
    return render_template('questions.html',q_count=q_count, question=question, responses=responses, choices=choices)


@app.route('/answers', methods=["POST"])
def post_answers():
    global q_index

    choice = request.form['choice']
    responses.append(choice)

    q_index+=1
    return redirect(f"/questions/{q_index}")


@app.route('/complete')
def survey_complete():
    
    return render_template('complete.html', responses=responses)

