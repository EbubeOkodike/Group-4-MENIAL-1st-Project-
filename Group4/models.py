from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Client(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer)
    password = db.Column(db.String(10))
    created_at = db.Column(db.DateTime(timezone=True), server_default = func.now() )

class Serv_prov(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer)
    password = db.Column(db.String(10))
    created_at = db.Column(db.DateTime(timezone=True), server_default = func.now() )

class Hybrid(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer)
    password = db.Column(db.String(10))
    created_at = db.Column(db.DateTime(timezone=True), server_default = func.now() )

