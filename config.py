import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ASOIF-Gameon8991'


# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Anonos123'
app.config['MYSQL_DATABASE_DB'] = 'liftinghands'
app.config['MYSQL_DATABASE_HOST'] = '172.31.25.244'
mysql.init_app(app)