import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
set FLASK_APP=test_flask.a_5_1_flask_sqlaichemy.py
flask shell
>>> from test_flask.a_5_1_flask_sqlaichemy import db
>>> db.create_all()
"""


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY DATABASE URI'] = \
    f'mysql://ibmp_test:XZdfjXIEsrumGrfFTmfltbtAuQCECUdl@172.16.4.83:3306/ibmp'
app.config['SQLALCHEMY TRACK MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Role(db.Model):
    tablename = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    """
    db.relationship()的第一个参数表明这个关系的另一端是哪个模型
    db.relationship()中的backref参数向User模型中添加一个role属性，从而定义反向关系。通过User实例的这个属性可以获取对应的Role模型对象，而不用再通过role id外键获取
    """
    users = db.relationship('User', backref='roles')

    def repr(self):
        return '<Role %r>' % self.name


class User(db.Model):
    tablename = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def repr(self):
        return '<User %r>' % self.username
