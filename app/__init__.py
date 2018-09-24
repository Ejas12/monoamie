from flask import Flask, render_template, flash, redirect, url_for
from config import Config
from forms import Loginform
from flask_mysqldb import MySQLdb
from flask_table import Table, Col, LinkCol
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

sqlserverip = '172.31.36.62'
sqlserveruser = 'liftingmonoami'
sqlpass = 'LiftingAnonos2018'
sqlattendanceserver = '127.0.0.1'

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models
