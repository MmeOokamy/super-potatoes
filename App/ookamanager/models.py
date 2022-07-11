from .. import db
from datetime import datetime

class Projects(db.Model):
    __tablename__ = 'ookamanager_projects'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    project_name = db.Column(
        db.String(50),
        nullable=False,
    )
    project_description = db.Column(
        db.Text,
        nullable=False
    )
    project_user_id = db.Column(
        db.Integer,
        nullable=False
    )
    project_create_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow()
    )
    project_update_at  = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow()
    )
    project_finish_at  = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow()
    )
    project_estimation = db.Column(
        db.String(50),
        nullable=False,
    )
    project_deadline = db.Column(
        db.DateTime,
        nullable=True,
    )

    def __repr__(self):
        return '{}'.format(self.project_name)


class Modules(db.Model):
    __tablename__ = 'ookamanager_modules'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    module_name = db.Column(
        db.String(255),
        nullable=False,
    )
    module_visible = db.Column(
        db.Integer,
        default = 1,
    )
    module_color = db.Column(
        db.String(30),
        nullable=True,
    )


class Steps(db.Model):
    __tablename__ = 'ookamanager_steps'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    steps_name = db.Column(
        db.String(255),
        nullable=False,
    )
    steps_order = db.Column(
        db.Integer,
        default = 1,
    )
    steps_visible = db.Column(
        db.Integer,
        default = 1,
    )
    steps_color = db.Column(
        db.String(30),
        nullable=True,
    )


class Status(db.Model):
    __tablename__ = 'ookamanager_status'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    status_name = db.Column(
        db.String(255),
        nullable=False,
    )
    status_order = db.Column(
        db.Integer,
        default = 1,
    )
    status_visible = db.Column(
        db.Integer,
        default = 1,
    )


class Tasks(db.Model):
    __tablename__ = 'ookamanager_tasks'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    task_title  = db.Column(
        db.String(255),
        nullable=False,
    )
    task_body  = db.Column(
        db.Text,
    )
    task_order = db.Column(
        db.Integer,
    ) 
    task_project_id = db.Column(
        db.Integer,
    )
    task_module = db.Column(
        db.Integer,
    )
    task_deadline = db.Column(
        db.String(80),
        nullable=True,
    )
    task_step_id = db.Column(
        db.Integer,
    )
    task_user_id= db.Column(
        db.Integer,
        default = 1,
    )
    task_create_at = db.Column(
        db.DateTime,
        nullable=True,
    )
    task_update_at = db.Column(
        db.DateTime,
        nullable=True,
    )
