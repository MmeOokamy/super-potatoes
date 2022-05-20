from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask_login import current_user, login_required

from .models import Params, db
from ..authentication.models import User


p_bp = Blueprint('params', __name__, url_prefix='/setting')

@p_bp.route('/', methods=['GET', 'POST'])
@login_required
def params():
    pref = Params.query.all()
    users = User.query.all()
    module_name = 'Params'
    return render_template('setting/setting.html', menu_active=module_name, pref=pref, users=users)



