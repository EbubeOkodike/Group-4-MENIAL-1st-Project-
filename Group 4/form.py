from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, EmailField, PasswordField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, Length, Email,EqualTo


class Form(FlaskForm):
    name =StringField('Full Name:',validators=[DataRequired(), Length( min=7, max=10)])
    email =EmailField('Email Address:', validators=[DataRequired(),Email()])
    password =PasswordField('Create Password:',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password:',validators=[DataRequired(),EqualTo(password)])
    home_address =StringField('Home Address:',validators=[DataRequired()])
    phone_number =StringField('Phone No:',validators=[DataRequired()])
    submit= SubmitField('sign up')


