from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,DateField,SelectField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from datetime import datetime
from wtforms.fields.html5 import DateField
from reservation.models import User



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')



class reservationForm(FlaskForm):
    package = SelectField('Package', choices=[('Pass-Around Cocktail: MENU1', 'Pass-Around Cocktail: Menu 1'), ('Pass-Around Cocktail: MENU2', 'Pass-Around Cocktail: Menu 2')], validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', default=datetime.now(), validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    occasion = SelectField('Occasion', choices=[('Birthday', 'Birthday'), ('Wedding', 'Wedding'), ('Anniversary', 'Anniversary'), ('Corporate Event', 'Corporate Event'), ('Christening', 'Christening'), ('Reunion', 'Reunion'), ('School Event', 'School Event')], validators=[DataRequired()])
    addons = StringField('Addons', validators=[DataRequired()])
    submit = SubmitField('Reserve')
    id = IntegerField('ID')

'''
    def validate_date(self, date):
        if date.data != current_user.id:
            user = User.query.filter_by(email = str(current_user.email)).first()
            reservation = Reservation.query.filter_by(user_id=user.id).first()
            if reservation:
                raise ValidationError('That date is taken. Please choose a different one.')
'''
'''
    def unique(Reservation, message ='already exists'):
        def unique_validator(reservationForm, date):
            reservation = Reservation.query.filter(date == date.data).first()
            if reservation and reservation.id != reservationForm._reservation_id:
                raise ValidationError(message)
            return unique_validator()
'''


