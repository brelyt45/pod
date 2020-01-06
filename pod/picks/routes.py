from flask import render_template, request, Blueprint
from pod.models import User, Pick
import datetime

picks = Blueprint('picks', __name__)


@picks.route("/")
@picks.route("/home")
def home():
    todayspicks = Pick.query.filter(Pick.date.like('%' + datetime.datetime.now().strftime('%Y-%m-%d') + '%')).all()
    users = User.query.order_by(User.firstname).all()
    return render_template('home.html', users=users, todayspicks=todayspicks)
