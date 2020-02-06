from flask import render_template, request, Blueprint, flash, redirect, url_for, jsonify
from pod.picks.forms import ParlayForm, ParlayPickForm
from pod.models import User, Pick, Parlay
import datetime
from flask_login import login_user, logout_user, current_user, login_required
from pod import db
import pod.teamnames
import pdb

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


    form = ParlayForm()
    # if request.method == 'POST' and not form.validate_on_submit():
    #     pdb.set_trace()
    if request.method == 'POST' and not form.validate_on_submit():
        test = 2+2

    if form.validate_on_submit():

        parlay = Parlay()
        db.session.add(parlay)

        for pick in form.picks.data:
            parlay.picks.append(Pick(user_id=current_user.id, date=datetime.date.today(), sport=pick['sport'], team=pick['team'], linetype=pick['linetype'], line=pick['line']))

        db.session.commit()
        flash(f'Pick Submitted Successfully', 'success')

        return redirect(url_for('picks.home'))

    return render_template('mypicks.html', picks=picks, form=form)


@picks.route('/teams/<league>')
def team(league):
    teams = eval(f'pod.teamnames.{league.lower()}')

    return jsonify({'teams': teams})
