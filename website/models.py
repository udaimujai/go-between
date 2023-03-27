from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


class Emp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    department = db.Column(db.String(150))
    package = db.Column(db.String(150))
    asset_list = db.Column(db.String(150))
    join_date = db.Column(db.String(150))
    address = db.Column(db.String(500))
    swags = db.Column(db.String(300))


class Asset(db.Model):
    asset_id = db.Column(db.Integer, primary_key=True,
                         unique=True,  nullable=False)
    asset_name = db.Column(db.String(150), nullable=False)
    asset_status = db.Column(db.String(150), nullable=False)
    asset_detail = db.Column(db.String(150), nullable=False)


class Package(db.Model):
    pkg_id = db.Column(db.String(150), primary_key=True)
    ast_1 = db.Column(db.String(150))
    ast_2 = db.Column(db.String(150))
    ast_3 = db.Column(db.String(150))
    ast_4 = db.Column(db.String(150))
    ast_5 = db.Column(db.String(150))
    ast_6 = db.Column(db.String(150))
    ast_7 = db.Column(db.String(150))
    ast_8 = db.Column(db.String(150))
    ast_9 = db.Column(db.String(150))
    ast_10 = db.Column(db.String(150))
