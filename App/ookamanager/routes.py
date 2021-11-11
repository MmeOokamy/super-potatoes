from flask import current_app as app
from flask_login import current_user, login_required
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from .. import login_manager
# from moc.db import get_db

om_bp = Blueprint('ookamanager', __name__,
    url_prefix='/ookamanager',
    template_folder='templates'
)

@om_bp.route('/')
@login_required
def om_index():
    module_name = 'Ookamanager'
    return render_template('om_i.html', menu_active=module_name)
