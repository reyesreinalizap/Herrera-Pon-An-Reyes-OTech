from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,DateField,SelectField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.fields.html5 import DateField
#from reservation.models import User


class reservationForm(FlaskForm):
    package = SelectField('Package', choices=[('Menu1', 'PACM'), ('Menu2', 'PACM'), ('Menu3', 'CB'), ('Menu4', 'CB')], validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', default=datetime.now(), validators=[DataRequired()])
    location = TextAreaField('Location', validators=[DataRequired()])
    occasion = SelectField('Occasion', choices=[('Birthday', 'Bd'), ('Wedding', 'Wed'), ('Anniversary', 'Anniv'), ('Corporate Event', 'CE'), ('Christening', 'CH'), ('Reunion', 'Re'), ('School Event', 'SE')], validators=[DataRequired()])
    addons = TextAreaField('Addons', validators=[DataRequired()])
    submit = SubmitField('Reserve')
    id = IntegerField('ID')
