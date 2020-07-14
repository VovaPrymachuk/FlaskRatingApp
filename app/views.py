from flask import render_template, request
from app import app, db
from app.models import Feedback


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        framework = request.form['framework']
        rating = request.form['rating']
        comments = request.form['comments']

        if user == '' or framework == '':
            return render_template('index.html', message='Please enter '
                                                         'required fields')

        if db.session.query(Feedback).filter(Feedback.user == user).count() == 0:
            data = Feedback(user, framework, rating, comments)
            db.session.add(data)
            db.session.commit()
            return render_template('success.html')
        return render_template('index.html', message='You have already '
                                                     'submitted feedback')
