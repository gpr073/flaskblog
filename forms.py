from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField, validators
#from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=2, max=20)])
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm_Password', [validators.DataRequired(), validators.Length(min=5, max=20), validators.EqualTo('password', message="Passwords must match")])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')