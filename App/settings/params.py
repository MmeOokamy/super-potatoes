from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask_login import current_user, login_required

p_bp = Blueprint('params', __name__, url_prefix='/setting')

@p_bp.route('/')
@login_required
def params():
    module_name = 'Params'
    return render_template('setting/setting.html',menu_active=module_name)
