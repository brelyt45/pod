import datetime
from flask import render_template, request, Blueprint, flash, redirect, url_for
from pod import db
from pod.models import User, Pick, Parlay
from pod.users.forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, current_user, login_required

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created, please log in', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('picks.home'))
        else:
            flash(f'Login unsuccessful, check email', 'danger')
    return render_template('login.html', title='Register', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('picks.home'))


@users.route("/")
@login_required
def account():
    picks = Pick.query.filter(Pick.user_id == current_user.id).order_by(Pick.date.desc()).all()
    return render_template('account.html', picks=picks)
