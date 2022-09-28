from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, EmailField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email,EqualTo

class RegistrationForm(FlaskForm):
    firstname = StringField('Firstname', validators = [DataRequired(), Length(min=1, max=20)])
    lastname = StringField('Lastname', validators = [DataRequired(), Length(min=1, max=20)])
    email = EmailField('Email', validators = [DataRequired(), Email()])
    age = IntegerField('Age', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


