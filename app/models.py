from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func, expression


class User(db.Model, UserMixin):
    """database-model for Users"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    full_name = db.Column(db.String(150))

    target_hours = db.Column(db.Float, default=160)
    worked_hours = db.Column(db.Float, default=0)
    flex_time = db.Column(db.Float, default=0)
    worked_hours_approved = db.Column(db.Boolean, default=False)

    vacation_days = db.Column(db.Integer, default=30)
    vacation_days_taken = db.Column(db.Integer, default=0)

    roles_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    vacation_requests = db.relationship('Vacation', backref='user')

    illness = db.relationship('Illness', backref='user')
    recieved_notification = db.relationship('Notification', backref='user')

    def __repr__(self):
        return '<User %r>' % self.full_name


class Role(db.Model):
    """database-model for Role"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class Vacation(db.Model):
    """database-model for Vacation-Requests"""
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    approved = db.Column(db.Boolean, default=False)
    notify = db.Column(db.Boolean, default=False)
    rejected = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Vacation {id}, start:{start_date}, end:{end_date}, user_id:{user_id}, approved:{approved}>'.format(id=self.id, start_date=self.start_date, end_date=self.end_date, user_id=self.user_id, approved=self.approved)


class Illness (db.Model):
    """database-model for Illness-Cases"""
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    approved = db.Column(db.Boolean, default=False)
    notify = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Illness {id}, start: {start}, end: {end}, approved:{approved}>'.format(id=self.id, start=self.start_date, end=self.end_date, approved=self.approved)


class Notification(db.Model):
    """database-model for Notifications"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.String(1500))
