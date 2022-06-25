from app import app
from flask import flash, make_response, render_template, redirect, url_for, jsonify, abort, request
from app import otp
from app.forms import RegisterForm, LoginForm, ConfirmForm
from auth.auth import Auth


AUTH = Auth()


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        user = AUTH.valid_login(email, password)
        if user is False:
            flash("User not registered with us")
        else:
            session_id = AUTH.create_session(email)

            response = make_response(redirect(url_for('home')))
            response.set_cookie("session_id", session_id)
            return response

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash("{}".format(jsonify(err_msg)))
        
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password1.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        date_of_birth = form.date_of_birth.data

        
        try:
            user = AUTH.register_user(email, password, first_name, last_name, date_of_birth)
            # if user is not None:
            #     new_otp = otp.send_otp(email)
            #     response = make_response(redirect(url_for('confirm')))
            #     response.set_cookie("otp", new_otp, max_age=600)
            #     return response
        except (ValueError):
            flash(ValueError)

        return redirect(url_for('login'))


    if form.errors != {}:
        for err_msg in form.errors.values():
            flash("{}".format(jsonify(err_msg)))
    return render_template('register.html', form=form) 


# @app.route('/confirm', methods=['GET', 'POST'], strict_slashes=False)
# def confirm():
#     form = ConfirmForm()
#     new_otp = request.cookies.get("otp", None)
#     if form.validate_on_submit():
#         if form.verify.data and form.otp.data == new_otp:
#             return redirect(url_for("login"))
#     if new_otp is not None:  
#         return render_template('otp.html', form=form)
#     return redirect(url_for('home'))


@app.route('/logout', methods=['GET'], strict_slashes=False)
def logout():
    """destroys session and logs user out"""
    session_id = request.cookies.get("session_id", None)
    user = AUTH.get_user_from_session_id(session_id)
    
    if session_id is None or user is None:
        return redirect('/')

    AUTH.destroy_session(user.id)

    return redirect('/')