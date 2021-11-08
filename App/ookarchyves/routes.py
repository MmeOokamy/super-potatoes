import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

# from moc.db import get_db

oa_bp = Blueprint(
    'ookarchyves', __name__,
    url_prefix='/ookarchyves',
    template_folder='templates',
    static_folder='static'
)

@oa_bp.route('/')
def main():
    module_name = 'Ookarchyves'
    return render_template('index.html', name="Ookamy", menu_active=module_name)
