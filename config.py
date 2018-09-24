import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ASOIF-Gameon8991'
    SQLALCHEMY_DATABASE_URI = 'mysql://liftingmonoami:LiftingAnonos2018@localhost/liftingasistencia'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


