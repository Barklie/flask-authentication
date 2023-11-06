from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class addUserForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[InputRequired()],
    )
    password = StringField(
        "Password",
        validators=[InputRequired()],
    )
    email = StringField(
        "Email",
        validators=[InputRequired()],
    )
    first_name = StringField(
        "First Name",
        validators=[InputRequired()],
    )
    last_name = StringField(
        "Last Name",
        validators=[InputRequired()],
    )

class loginUserForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[InputRequired()],
    )
    password = StringField(
        "Password",
        validators=[InputRequired()],
    )