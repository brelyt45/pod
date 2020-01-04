from flask import current_app
from pod import db, login_manager
from flask_login import UserMixin


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    picks = db.relationship('Pick', backref='picker', lazy=True)

    def __repr__(self):
        return f"User('{self.firstname}','{self.lastname}','{self.email}')"


class Pick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    sport = db.Column(db.String(60), nullable=False)
    team = db.Column(db.String(60), nullable=False)
    linetype = db.Column(db.String(60), nullable=False)
    line = db.Column(db.Float, nullable=False)
    odds = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Boolean)

    #boxscore = db.relationship('BoxScore', backref='')

    def __repr__(self):
        return f"Pick('{self.date}', '{self.team}', '{self.line}', '{self.odds}', '{self.result}')"
