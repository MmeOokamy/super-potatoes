from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    user = StringField(
        'username',
        [DataRequired()]
    )
    password = PasswordField(
        'userpwd',
        [DataRequired()]
    )
    magical = StringField(
        'usermagicalword',
        [DataRequired()]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')