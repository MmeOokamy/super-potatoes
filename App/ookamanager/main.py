import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

# from moc.db import get_db

bp = Blueprint('ookamanager', __name__, url_prefix='/ookamanager')

@bp.route('/main')
def main():
    module_name = 'Ookamanager'
    return render_template('module/ookamanager/main.html',  logg=True, name="PageTest", menu_active=module_name)
