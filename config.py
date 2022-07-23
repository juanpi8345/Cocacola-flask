import os
class Config(object):
    SECRET_KEY = "cocacola2022"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL=True
    MAIL_USE_TLS=False
    MAIL_USERNAME= 'pregliasco123@gmail.com'
    MAIL_PASSWORD= 'ytsgpppknfnsfdpd'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:1411Juan@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False