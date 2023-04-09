from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship


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
# empAsset = db.Table("emp_asset",
#                     db.Column("id", db.Integer, primary_key=True),
#                     db.Column("Emp", db.Integer,
#                               db.ForeignKey("Emp.id")),
#                     db.Column("Asset", db.Integer, db.ForeignKey("Asset.asset_id")))


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
    # emp_assets = db.relationship(
    #     "EmpAsset", backref="asset")


class EmpAsset(db.Model):
    __tablename__ = 'user_devices'
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer, db.ForeignKey("emp.id"), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey(
        "asset.asset_id"), nullable=False)

    # emp = db.relationship('Emp', back_populates='emp_assets')
    # asset = db.relationship('Asset', back_populates='followers')


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
