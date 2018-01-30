from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class Loginform(FlaskForm):
    username = StringField('Usuario:', validators=[DataRequired()])
    pasword = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField ('Entrar')
    