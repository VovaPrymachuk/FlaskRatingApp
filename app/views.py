from flask import render_template, request
from app import app, db
from app.models import Feedback
from app.send_email import send_mail


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        worker = request.form['worker']
        rating = request.form['rating']
        comments = request.form['comments']

        if user == '' or worker == '':
            return render_template('index.html', message='Please enter '
                                                         'required fields')

        if db.session.query(Feedback).filter(Feedback.user == user).count() == 0:
            data = Feedback(user, worker, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(user, worker, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message='You have already '
                                                     'submitted feedback')
