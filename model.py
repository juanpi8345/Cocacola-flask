from flask_sqlalchemy import SQLAlchemy
import datetime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'Usuarios'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50),unique=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(352))
    comments = db.relationship('Comment')
    created_date = db.Column(db.DateTime, default = datetime.datetime.now())

    def __init__(self,username,email,password):
        self.username = username
        self. password = self.create_password(password)
        self.email = email

    def create_password(self,password):
      return generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password, password)

class Comment(db.Model):
    __tablename__ ='Comentarios'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Usuarios.id'))
    name = db.Column(db.String(40))
    text = db.Column(db.Text())
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())