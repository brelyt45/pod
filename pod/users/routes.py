import datetime
from flask import render_template, request, Blueprint
from pod import db
from pod.models import User, Pick, Parlay
from pod.users.forms import LoginForm, RegistrationForm

users = Blueprint('users', __name__)


@users.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@users.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Register', form=form)
