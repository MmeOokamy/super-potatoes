
"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class SignupForm(FlaskForm):
    user_user = StringField(
        'Name',
        [DataRequired()]
    )
    user_password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8, message='Select a stronger password.')
        ]
    )
    user_magical_word = StringField(
        'Super Magical Spell',
        [DataRequired()]
    ) 
    user_email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    """User Log-in Form."""
    user_email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.')
        ]
    )
    user_password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')