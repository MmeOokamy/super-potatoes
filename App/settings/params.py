import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

# from moc.db import get_db

bp = Blueprint('params', __name__, url_prefix='/setting')

@bp.route('/')
def params():
    module_name = 'Params'
    return render_template('module/setting/setting.html',  logg=True, name="Ookamy", menu_active=module_name)
