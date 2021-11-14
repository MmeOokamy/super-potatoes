
"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class SignupForm(FlaskForm):
    user_name = StringField(
        'Name',
        [DataRequired()]
    )
    user_password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8, message='Créer un mot de pass fort')
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
            Email(message='Entrer un email valide'),
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
            Email(message='Entrer un email valide.')
        ]
    )
    user_password = PasswordField('Mots de passe', validators=[DataRequired()])
    submit = SubmitField('Connexion')