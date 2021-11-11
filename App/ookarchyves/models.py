from .. import db
from datetime import datetime

class Themes(db.Model):

    __tablename__ = 'ookarchyves_themes'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    theme_title = db.Column(
        db.String(50),
        nullable=False,

    )
    theme_description = db.Column(
        db.Text,
        nullable=False

    )
    theme_private = db.Column(
        db.Integer,
        default=1,
        nullable=False
    )

    def __repr__(self):
        return '{}'.format(self.theme_title)


class Articles(db.Model):
    __tablename__ = 'ookarchyves_articles'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    article_title = db.Column(
        db.String(100),
        nullable=False,
    )
    article_author_id = db.Column(
        db.Integer
    )
    article_create_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow()
    )
    article_update_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow()
    )
    article_body = db.Column(
        db.Text,
        nullable=False
    )
    article_theme_id = db.Column(
        db.Integer
    )
   
    article_private = db.Column(
        db.Integer,
        default=1,
        nullable=False
    )
    
    def __repr__(self):
        return '<Article {}>'.format(self.article_title)
    