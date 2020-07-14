from app import db


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(155), unique=True)
    framework = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, user, framework, rating, comments):
        self.user = user
        self.framework = framework
        self.rating = rating
        self.comments = comments