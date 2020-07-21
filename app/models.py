from app import db


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(155), unique=True)
    worker = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, user, worker, rating, comments):
        self.user = user
        self.worker = worker
        self.rating = rating
        self.comments = comments