from datetime import datetime
from reservation import db



class Reservation(db.Model):

    __tablename__ = 'reservation'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime, unique=True)
    package = db.Column(db.String(100), nullable=False, unique=False)
    location = db.Column(db.String(100), nullable=False, unique=False)
    occasion = db.Column(db.String(100), nullable=False, unique=False)
    addons = db.Column(db.String(100), nullable=False, unique=False)
   # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Reservation('{self.package}', '{self.date}', '{self.occasion}', '{self.addons}' )"

