from flask_backend import db


# SQL Models
attendance = db.Table('attendance', db.Model.metadata,
    db.Column('user_id', db.ForeignKey('user.id', ondelete='CASCADE'), primary_key = True), # ondelete cascade
    db.Column('session_id', db.ForeignKey('session.id', ondelete='CASCADE'), primary_key = True) # ondelete cascade
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    
    sessions = db.relationship("Session", secondary = attendance, back_populates = "users")

    def __repr__(self):
        return f'<User {self.name}>'

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)

    users = db.relationship("User", secondary = attendance, back_populates="sessions")

    def __repr__(self):
        return f'<Session {self.id} - {self.date}'

