from datetime import datetime
from reservation import db, login_manager
from flask_login import UserMixin
from flask_marshmallow import Marshmallow
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property


ma=Marshmallow()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    reservations = relationship('Reservation', backref='user')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Reservation(db.Model):

    __tablename__ = 'reservation'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime, nullable=False, default=datetime, unique=True)
    package = db.Column(db.String(100), nullable=False, unique=False)
    location = db.Column(db.String(100), nullable=False, unique=False)
    occasion = db.Column(db.String(100), nullable=False, unique=False)
    addons = db.Column(db.String(100), nullable=False, unique=False)

    def __repr__(self):
        return f"Reservation('{self.package}', '{self.date}', '{self.location}', '{self.occasion}', '{self.addons}' )"


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

class ReservationSchema(ma.ModelSchema):
    class Meta:
        model = Reservation
