
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, RadioField, SelectField, HiddenField
from wtforms.validators import DataRequired


class ThemeForm(FlaskForm):
    theme_title = StringField(
        'Thèmatique',
        [DataRequired()]
    )
    theme_description = TextAreaField(
        'Description'
    )
    theme_private = RadioField(
        'Visibilité',
         choices=[('0','Publique'),('1','Privée')]
    )
    
    submit = SubmitField('Submit')


class ArticleForm(FlaskForm):
    article_title = StringField(
        'Titre de l\'article : ',
        [DataRequired()]
    )
    article_author_id = HiddenField(
        "user_id"
    )
    article_body = TextAreaField(
        'Article',
        [DataRequired()]
    )
    article_theme_id = SelectField(
        'Thematique'
    )
    article_private = RadioField(
        'Visibilité',
        choices=[('0','Publique'),('1','Privée')]
    )    
    submit = SubmitField('Submit')
