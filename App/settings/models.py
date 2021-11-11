from datetime import datetime

from .. import db

class Params(db.Model):
    __tablename__ = "settings"
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    setting_parameter = db.Column(
        db.String(100),
        nullable=False,
        unique=False
    )
    setting_module = db.Column(
        db.String(100),
        nullable=False,
        unique=False
    )
    setting_commentary = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
	)
    setting_default_value = db.Column(
        db.Boolean,
        default=1,
        nullable=False
    )
    setting_value = db.Column(
        db.Boolean,
        default=1,
        nullable=False
    )

    def __repr__(self):
        return '{}'.format(self.setting_parameter)

    def check_statue(self):
        return '{}'.format(self.setting_value)



