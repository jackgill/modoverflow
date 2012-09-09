from modoverflow import app
from modoverflow.database import db_session
from modoverflow.models import *
from flask import render_template, request, redirect, url_for, session, flash

@app.route('/')
def root():
    return render_template('index.html')

# Users
@app.route('/users/new', methods=['GET', 'POST'])
def users_new():
    if request.method == 'POST':
        # Builder User object from form values
        user = User()
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.email = request.form['email']
        user.set_password(request.form['password_text'])

        # Save user to database
        db_session.add(user)
        db_session.commit()
        
        return redirect(url_for('users'))
    else:
        return render_template('users/new.html')

# Questions
@app.route('/questions')
def questions():
    questions = Question.query.all()
    return render_template('questions/questions.html', questions=questions)

@app.route('/questions/<id>')
def question(id):
    questions = Question.query.filter(Question.id == id)
    if questions.count() > 0:
        return render_template('questions/question.html', question=questions[0])
    else:
        flash('Question not found.')
        return redirect(url_for('root'))

@app.route('/questions/new', methods=['GET', 'POST'])
def questions_new():
    if request.method == 'POST':
        users = User.query.filter(User.email == session['email'])
        if users.count() == 0:
            raise Exception('No user found')
        user = users[0]
        
        # Builder Question object from form values
        question = Question()
        question.title = request.form['title']
        question.body = request.form['body']
        question.submitter_id = user.id
        question.votes = 0

        # Save user to database
        db_session.add(question)
        db_session.commit()
        
        return redirect(url_for('questions'))
    else:
        return render_template('questions/new.html')

# Login / Logout
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = False
    if request.method == 'POST':
        error = True
        users = User.query.filter(User.email == request.form['email'])
        if users.count() > 0 and users.first().is_valid_password(request.form['password']):
            session['email'] = users.first().email
            session['first_name'] = users.first().first_name
            return redirect(url_for('root'))
        
    return render_template('login/form.html', alert=error, hide_login = True)

@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('first_name', None)
    flash('You have successfully logged out.')
    return redirect(url_for('login'))
