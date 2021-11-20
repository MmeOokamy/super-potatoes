from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, RadioField, SelectField, HiddenField, DateField, IntegerField
from wtforms.validators import DataRequired


class ProjectForm(FlaskForm):
    project_name = StringField(
        'Nom du Projet',
        [DataRequired()]
    )
    project_description = TextAreaField(
        'Description du projet'
    )

    project_estimation = StringField(
        'Estimation de l\'importance'
    )
    project_deadline = DateField(
        'Deadline',
    )
    submit = SubmitField('Submit')


class ModuleForm(FlaskForm):
    module_name = StringField(
        'Nom du Module',
        [DataRequired()]
    )
    module_color = StringField(
       'Couleur Materialize : https://materializecss.com/color.html'
   )
    submit = SubmitField('Submit')