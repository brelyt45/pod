from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(max=30)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(max=30)])
    email = StringField('Email', validators=[DataRequired(), Length(max=120), Email()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(max=120), Email()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
