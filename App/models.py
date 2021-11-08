"""Database models."""
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = 'users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    user_name = db.Column(
        db.String(50),
        nullable=False,
        unique=False
    )
    user_email = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )
    user_password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False
	)
    user_magical_word= db.Column(
        db.String(50),
        index=False,
        unique=False,
        nullable=False
	)
    user_power= db.Column(
        db.String(200),
        index=False,
        unique=False,
        nullable=False
	)
    user_token= db.Column(
        db.String(50),
        index=False,
        unique=False,
        nullable=False
	)
    user_created_on = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    user_last_login = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)