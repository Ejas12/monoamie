from flask_wtf import FlaskForm
from flask import url_for
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class Loginform(FlaskForm):
    username = StringField('Usuario:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField ('Entrar')
    