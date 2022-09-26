from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, EmailField, PasswordField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, Length, Email,EqualTo


class Customerform(FlaskForm):
    name=StringField('name',validators=[DataRequired()])

