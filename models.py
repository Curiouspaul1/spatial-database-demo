from core import db
from datetime import datetime as d
from geoalchemy2 import Geometry

# Base class
class Base:
    id = db.Column(db.Integer, primary_key=True, nullable=False)


class User(Base, db.Model):
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    signup_date = db.Column(db.DateTime, default=d.utcnow())
    profile_photo = db.Column(db.String(200))
    telephone = db.Column(db.String(20), unique=True)
    address = db.Column(db.String(100))
    lon = db.Column(db.Float)
    lat = db.Column(db.Float)
    is_handyman = db.Column(db.Boolean, default=False)
    email_verified = db.Column(db.Boolean, default=False)
    personal_id = db.Column(db.String(200))
    # relationships
    gigs_ = db.relationship('Gig', backref='owner')
    geometry = db.Column(Geometry(geometry_type='POINT', management = True, srid='4269'))


class Gig(Base, db.Model):
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    glat = db.Column(db.Float)
    glon = db.Column(db.Float)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_created = db.Column(db.DateTime(), default=d.utcnow())
    gig_geometry = db.Column(Geometry(geometry_type='POINT', management = True))
