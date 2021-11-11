
from flask import current_app as app
from flask_login import current_user, login_required
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .. import login_manager
from .models import db, Themes, Articles

oa_bp = Blueprint(
    'ookarchyves', __name__,
    url_prefix='/ookarchyves',
    template_folder='templates'
)

@oa_bp.route('/')
@login_required
def oa_index():
    module_name = 'Ookarchyves'
    return render_template('oa_i.html', menu_active=module_name)
