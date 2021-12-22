"""Routes for user authentication."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user

from .. import login_manager
from .forms import LoginForm, SignupForm
from .models import User, db

# Blueprint Configuration
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    User sign-up page.
    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                name=form.user_name.data,
                email=form.user_email.data,
            )
            user.set_password(form.user_password.data)
            db.session.add(user)
            db.session.commit()  # Create new user
            login_user(user)  # Log in as newly created user
            return redirect(url_for('news.html'))
        flash('A user already exists with that email address.')
    return render_template(
        'signup.jinja2',
        form=form
    )


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Log-in page for registered users.
    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard.
    """
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('module'))  

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.user_email.data).first()  
        if user and user.check_password(password=form.user_password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('news'))
        flash('Email ou Mot de passe invalide')
        return redirect(url_for('auth_bp.login'))
    return render_template(
        'auth/login.jinja2',
        form=form
    )


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in upon page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))