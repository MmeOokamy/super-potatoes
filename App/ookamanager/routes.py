from flask import current_app as app
from flask_login import current_user, login_required
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from .. import login_manager
from .models import db, Projects, Modules, Steps, Status
from .forms import ProjectForm, ModuleForm


om_bp = Blueprint('ookamanager', __name__,
    url_prefix='/ookamanager',
    template_folder='templates'
)

NAME_MENU= 'Ookamanager'

@om_bp.route('/')
@login_required
def om_index():
    projects = Projects.query.filter_by(project_user_id=current_user.id).all()
    return render_template('om_i.html', menu_active=NAME_MENU,  projects=projects)


@om_bp.route('/projet', methods=['GET', 'POST'])
@login_required
def om_project():
    form = ProjectForm()
    if form.validate_on_submit():
        existing_theme = Projects.query.filter_by(project_name=form.project_name.data).first()
        if existing_theme is None:
            project = Projects(
                project_name=form.project_name.data,
                project_description=form.project_description.data,
                project_user_id= current_user.id,
                project_estimation= form.project_estimation.data,
                project_deadline= form.project_deadline.data,
            )
            db.session.add(project)
            db.session.commit()  # Create new theme
            return redirect(url_for('ookamanager.om_index'))
        flash('Ce projet existe déjà')
    return render_template(
        'om_project_form.jinja2',
        form=form,
        menu_active=NAME_MENU
    )


@om_bp.route('/module', methods=['GET', 'POST'])
@login_required
def om_module():
    form = ModuleForm()
    modules = Modules.query.all()
    if form.validate_on_submit():
        existing_theme = Modules.query.filter_by(module_name=form.module_name.data).first()
        if existing_theme is None:
            m = Modules(
                module_name=form.module_name.data,
                module_color=form.module_color.data,
            )
            db.session.add(m)
            db.session.commit()  # Create new theme
            return redirect(url_for('ookamanager.om_module'))
        flash('Ce module existe déjà')
    return render_template(
        'om_module_form.jinja2',
        menu_active=NAME_MENU,
        form=form,
        modules=modules
    )


@om_bp.route('/dashboard/<dashboard_id>', methods=['GET', 'POST'])
@login_required
def om_dashboard(dashboard_id):
    # on va chercher le projet
    dashboard = Projects.query.filter_by(id=dashboard_id).first()
    # Les colonnes steps
    steps = Steps.query.all()
    
    # Si le projet exist on accede au dashboard
    if dashboard is not None and dashboard.project_user_id == current_user.id:
        return render_template(
            'om_dashboard.html',
            dashboard = dashboard,
            steps = steps,
            menu_active=NAME_MENU
        )
    else:
        # redirection si on entre une numero d'id inconnue
        return redirect(url_for('ookamanager.om_index'))
    

@om_bp.route('/dashboard/<dashboard_id>/todo', methods=['GET', 'POST'])
@login_required
def om_add_todo(dashboard_id):
    dashboard = Projects.query.filter_by(id=dashboard_id).first()
    if dashboard is not None:
        return render_template(
            'om_dashboard.html',
            dashboard = dashboard,
            menu_active=NAME_MENU
        )
    return render_template(
            'om_dashboard.html',
            menu_active=NAME_MENU
    )
