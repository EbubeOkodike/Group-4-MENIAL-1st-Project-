from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, EmailField, PasswordField, SubmitField,TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email,EqualTo

class RegistrationForm(FlaskForm):
    firstname = StringField('Firstname', validators = [DataRequired()])
    lastname = StringField('Lastname', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    age = IntegerField('Age', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


