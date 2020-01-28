from flask import render_template, request, Blueprint
from pod.models import User, Pick
import datetime
from flask_login import login_user, logout_user, current_user, login_required

picks = Blueprint('picks', __name__)


@picks.route("/")
@picks.route("/home")
def home():
    todayspicks = Pick.query.filter(Pick.date.like('%' + datetime.datetime.now().strftime('%Y-%m-%d') + '%')).all()
    users = User.query.order_by(User.firstname).all()
    return render_template('home.html', users=users, todayspicks=todayspicks)


@picks.route("/mypicks")
@login_required
def mypicks():
    picks = Pick.query.filter(Pick.user_id == current_user.id).order_by(Pick.date.desc()).all()
    return render_template('mypicks.html', picks=picks)
