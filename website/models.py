from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship


class Package(db.Model):
    __tablename__ = 'package'
    pkg_id = db.Column(db.String(150), primary_key=True)
    pkg_assets = db.relationship(
        'Asset', secondary='pkg_devices', backref='packages')


class PkgDevices(db.Model):
    __tablename__ = 'pkg_devices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pkg_id = db.Column(db.Integer, db.ForeignKey(
        "package.pkg_id"), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey(
        "asset.asset_id"), nullable=False)

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

# Many-to-Many relation between Employee and Asset


class Emp(db.Model):
    __tablename__ = 'emp'
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
    emp_assets = db.relationship(
        'Asset', secondary='user_devices', backref='followers')


class Asset(db.Model):
    __tablename__ = 'asset'
    asset_id = db.Column(db.Integer, primary_key=True,
                         unique=True,  nullable=False, autoincrement=True)
    asset_name = db.Column(db.String(150))
    asset_status = db.Column(db.String(150))
    asset_detail = db.Column(db.String(150))


class EmpAsset(db.Model):
    __tablename__ = 'user_devices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    emp_id = db.Column(db.Integer, db.ForeignKey("emp.id"), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey(
        "asset.asset_id"), nullable=False)



