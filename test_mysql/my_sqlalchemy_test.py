from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


"""
把SQLAlchemy查询对象转换成字典/json使用(汇总)：  https://www.cnblogs.com/sanduzxcvbnm/p/10220718.html
"""

HOSTNAME = 'v81'
PORT = '3306'
DATABASE = 'python_crawl'
USERNAME = 'root'
PASSWORD = '123456'

DB_URI = "mysql+mysqlconnector://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                               password=PASSWORD,
                                                                                               host=HOSTNAME, port=PORT,
                                                                                               db=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))

    # 单个对象方法1
    def to_dict(self):
        model_dict = dict(self.__dict__)
        del model_dict['_sa_instance_state']
        return model_dict

    Base.to_dict = to_dict  # 注意:这个跟使用flask_sqlalchemy的有区别

    # 单个对象方法2
    def single_to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # 多个对象
    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result


# 配合多个对象使用的函数
def to_json(all_vendors):
    v = [ven.dobule_to_dict() for ven in all_vendors]
    return v


# 示例代码1.单个对象:
users = session.query(User).first()
print(users.single_to_dict())  # {'id': 1, 'username': 'admin', 'email': 'admin@example.com'}
print(users.to_dict())  # {'username': 'admin', 'email': 'admin@example.com', 'id': 1}
print(type(users.single_to_dict()))  # <class 'dict'>
print(type(users.to_dict()))  # <class 'dict'>

# 2.多个对象
users = session.query(User).all()
data = to_json(users)
print(
    data)  # [{'id': '1', 'username': 'admin', 'email': 'admin@example.com'}, {'id': '2', 'username': 'guest', 'email': 'guest@example.com'}]
print(type(data))  # <class 'list'>
print(data[0])  # {'id': '1', 'username': 'admin', 'email': 'admin@example.com'}
print(type(data[0]))  # <class 'dict'>

# 2.使用Flask - SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    # 单个对象方法1
    def to_dict(self):
        model_dict = dict(self.__dict__)
        del model_dict['_sa_instance_state']
        return model_dict

    db.to_dict = to_dict  # 注意:这个跟使用SQLAlchemy的有区别

    # 单个对象方法2
    def single_to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # 多个对象
    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result


# 配合多个对象使用的函数
def to_json(all_vendors):
    v = [ven.dobule_to_dict() for ven in all_vendors]
    return v


# 示例代码1.单个对象:
users = User.query.first()
print(users.single_to_dict())  # {'id': 1, 'username': 'admin', 'email': 'admin@example.com'}
print(users.to_dict())  # {'username': 'admin', 'email': 'admin@example.com', 'id': 1}
print(type(users.single_to_dict()))  # <class 'dict'>
print(type(users.to_dict()))  # <class 'dict'>

# 2.多个对象
users = User.query.all()
data = to_json(users)
print(
    data)  # [{'id': '1', 'username': 'admin', 'email': 'admin@example.com'}, {'id': '2', 'username': 'guest', 'email': 'guest@example.com'}]
print(type(data))  # <class 'list'>
print(data[0])  # {'id': '1', 'username': 'admin', 'email': 'admin@example.com'}
print(type(data[0]))  # <class 'dict'>
