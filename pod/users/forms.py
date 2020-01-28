from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, IntegerField, BooleanField, SubmitField,
from wtforms.validators import DataRequired, Length, Email, ValidationError
from pod import db
from pod.models import User, Pick


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(max=30)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(max=30)])
    email = StringField('Email', validators=[DataRequired(), Length(max=120), Email()])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        exists = User.query.filter_by(email=email.data).first()
        if exists:
            raise ValidationError('Account already exists with that email')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(max=120), Email()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
