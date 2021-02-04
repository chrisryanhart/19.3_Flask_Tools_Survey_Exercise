   if q_count != q_index and q_index!=q_max:
        if q_index!=q_max:
            flash('Wrong question number!')
            return redirect(f"/questions/{q_index}")
        elif q_index==q_max:
            flash("survey completed")
            return redirect('/test')

return redirect(f'/questions/<int:{q_index}>')     
     
     return redirect(f"/test", responses=responses, test=test_var



     from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# store user's survey responses here
responses = []
question_count = {"num": 0}
# q_length = len(satisfaction_survey.questions)
q_index = question_count['num']
q_count = q_index + 1 
print(q_count)

@app.route('/')
def ask_survey():
    flash('Now in survey')
    # also have to add initial flash msg here
    responses.clear()
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('base.html', instructions=instructions, title=title)

@app.route('/questions/<int:q_index>')
def answer_question(q_index):
    global q_count
 
    if q_index>0 and q_index<3:
        # flash('Now in survey')
        response = request.args[f"q{q_index}"]
        responses.append(response)

    if q_index>=4:
        test_var="entered final if statement"
        response = request.args[f"q{q_index}"]
        responses.append(response)
        flash('On 4th question')
        
        return redirect("/test")
    # raise
    # params in query string are updated each time the form is submitted
    # if q_num == 4:
    #     # flash('Survey completed')
    #     return render_template('complete.html')
    q_index+=1
    q_count+=1
    question = satisfaction_survey.questions[q_index]

    return render_template('questions.html',q_index=q_index, q_count=q_count, question=question, responses=responses)

# when does the answer q string parameter get added to the response list

# need to post to answers

@app.route('/answers', methods=["POST"])
def post_answers():
    global q_index
    
    return redirect(f'/questions/<int:{q_index}>')

@app.route('/complete/<int:q_index>')
def completed_survey(q_index):
    # add argument answers here to response list?
    response = request.args['q4']
    responses.append(response)
    print(responses)
    

    return render_template('complete.html', responses=responses, q_index=q_index)

@app.route('/test')
def test_redirect():
    return render_template('test.html', responses=responses)



    <!-- can add if statement with different forms  -->
   
    <!-- <p>Now I'm on the question 1 page</p> -->
    <!-- <form action="/answers" method="POST">
        <!-- add drop down menu with possible answers -->
        <!-- <p>{{test}}</p>
        <p>q_index: {{q_index}}</p>
        <p>Question: {{question}}</p>
        <p>Responses: {{responses}}</p>
        <input type="text" placeholder="answer" name="answer">
        <button>Next</button>


            <!-- {% else %} -->

    <!-- {% for msg in get_flashed_messages() %}
    <p>{{msg}}</p>
    {% endfor %} -->
    <!-- <form action="/complete/{{q_index}}">
        <!-- add drop down menu with possible answers -->
        <!-- <p>q_index: {{q_index}}</p>
        <p>Question: {{question}}</p>
        <input type="text" placeholder="answer" name="q{{q_index}}">
        <button>Next</button>
    </form> --> -->