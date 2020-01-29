from flask import render_template, request, Blueprint, jsonify, flash
from pod.models import User, Pick
import datetime
from flask_login import login_user, logout_user, current_user, login_required
from pod.picks.forms import ParlayPickForm
import pod.teamnames

picks = Blueprint('picks', __name__)


@picks.route("/")
@picks.route("/home")
def home():
    todayspicks = Pick.query.filter(Pick.date.like('%' + datetime.datetime.now().strftime('%Y-%m-%d') + '%')).all()
    users = User.query.order_by(User.firstname).all()
    return render_template('home.html', users=users, todayspicks=todayspicks)


@picks.route("/mypicks", methods=['GET', 'POST'])
@login_required
def mypicks():
    picks = Pick.query.filter(Pick.user_id == current_user.id).order_by(Pick.date.desc()).all()
    form = ParlayPickForm()

    if form.validate_on_submit():
        flash(f'Pick Submitted Successfully', 'success')
        return redirect(url_for('picks.mypicks'))
    else:
        flash(f'Unable to Submit pick, check fields', 'danger')

    return render_template('mypicks.html', picks=picks, form=form)


@picks.route('/teams/<league>')
def team(league):
    teams = eval(f'pod.teamnames.{league.lower()}')

    return jsonify({'teams': teams})
