import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

# from moc.db import get_db

bp = Blueprint('ookarchyves', __name__, url_prefix='/ookarchyves')

@bp.route('/')
def main():
    module_name = 'Ookarchyves'
    return render_template('module/ookarchyves/main.html',  logg=True, name="Ookamy", menu_active=module_name)
