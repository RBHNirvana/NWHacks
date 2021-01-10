#Sqllite stuff

from app import db
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
from app import login


class Organization(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    org_name = db.Column(db.String(100))
    password_hash = db.Column(db.String(128))
    org_email = db.Column(db.String(128))
    org_summary = db.Column(db.String(1000))
    positions = db.Relationship('Position', backref = 'owner', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Position(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    num_spots = db.Column(db.Integer)
    spots_filled = db.Column(db.Integer)
    pos_name = db.Column(db.String(100))
    pos_summary = db.Column(db.String(1000))
    applicants = db.Relationship('Applicant', backref = 'owner', lazy='dynamic')

class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    about = db.Column(db.String(500))
