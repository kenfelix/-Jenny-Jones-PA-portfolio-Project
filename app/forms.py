from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.fields.html5 import DateTimeField, DateField, TimeField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError


class LoginForm(FlaskForm):
    email = StringField(label='Email address', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=8, max=32), DataRequired()])
    submit = SubmitField(label='Authenticate')


class RegisterForm(FlaskForm):
    email = StringField(label='Email address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=8, max=32), DataRequired()])
    password2 = PasswordField(label='Re-enter Password', validators=[DataRequired(), EqualTo('password1')])
    first_name = StringField(label='First name', validators=[DataRequired()])
    last_name = StringField(label='Last name', validators=[DataRequired()])
    date_of_birth = DateField(label='Birthday', validators=[DataRequired()])
    submit = SubmitField(label='Get a PA')


class ConfirmForm(FlaskForm):
    otp = StringField(label='Confirm email address', validators=[Length(min=6, max=6), DataRequired()])
    verify = SubmitField(label='Verify')
    resend = SubmitField(label='Resend otp')


class ScheduleForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    start_date = DateField(label='Start date', validators=[DataRequired()])
    start_time = TimeField(label='Start time', validators=[DataRequired()])
    end_date = DateField(label='End date', validators=[DataRequired()])
    end_time = TimeField(label='End time', validators=[DataRequired()])
    description = TextAreaField(label='Description', validators=[DataRequired()])
    venue = StringField(label='Venue', validators=[DataRequired()])
    submit = SubmitField(label='Schedule')