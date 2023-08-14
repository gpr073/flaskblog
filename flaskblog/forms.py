from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', [
            InputRequired(), 
            Length(min=2, max=20)
        ])
    email = EmailField('Email', [
            InputRequired(), 
            Email()
        ])
    password = PasswordField('Password', [
            InputRequired(), 
            Length(min=5, max=20)
        ])
    confirm_password = PasswordField('Confirm_Password', [
            InputRequired(), 
            Length(min=5, max=20), 
            EqualTo('password', message="Passwords must match")
        ])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('An account already exists with this email id.')

class LoginForm(FlaskForm):
    email = EmailField('Email', [
            InputRequired(), 
            Email()
        ])
    password = PasswordField('Password', [InputRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')