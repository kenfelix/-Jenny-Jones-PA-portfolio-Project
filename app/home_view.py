from asyncio import events
from app import app
from flask import flash, make_response, render_template, redirect, url_for, jsonify, abort, request
from app import otp
from app.forms import RegisterForm, LoginForm, ConfirmForm, ScheduleForm
from auth.auth import Auth
from db.db import DB
from model.model import Schedule

auth = Auth()
db = DB()


@app.route('/home', methods=['GET', 'POST'], strict_slashes=False)
@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def home():
    form = ScheduleForm()
    session_id = request.cookies.get("session_id", None)
    user = auth.get_user_from_session_id(session_id)
    if user is None:
        return render_template('home.html')

    # if user.login == 1:  

    if form.validate_on_submit():
        title = form.title.data
        start_date= form.start_date.data
        start_time = form.start_time.data
        end_date = form.end_date.data
        end_time = form.end_time.data
        description = form.description.data
        venue = form.venue.data
        auth.create_schedule(session_id, title, description, start_date, \
            end_date, start_time, end_time, venue)
        
    events = db._session.query(Schedule).filter_by(user_id=user.id).all()

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash("{}".format(jsonify(err_msg)))
    return render_template('user_home.html', form=form, events=events, user=user)
