
from flask import current_app as app
from flask_login import current_user, login_required
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .. import login_manager
from .models import db, Themes, Articles
from .forms import ThemeForm, ArticleForm

oa_bp = Blueprint(
    'ookarchyves', __name__,
    url_prefix='/ookarchyves',
    template_folder='templates',
    static_folder='static'
)

@oa_bp.route('/')
@login_required
def oa_index():
    module_name = 'Ookarchyves'
    count = [{
        "theme": Themes.query.count(),
        "article": Articles.query.count(),
    },]
    themes = Themes.query.all()
    articles = Articles.query.all()

    #Init list de dict
    menu = []

    # crée l'object theme avec les articles
    for theme in themes:
        t={}
        t['id']= theme.id
        t['nom']= theme.theme_title
        t['description']= theme.theme_description

        # va chercher les articles correspondants
        arts = Articles.query.filter(Articles.article_theme_id==theme.id).all()
        t['articles']= arts
        menu.append(t)

    return render_template(
        'oa_i.html', 
        menu_active=module_name,
        themes=menu,
        counter=count
    )


@oa_bp.route('/thematique', methods=['GET', 'POST'])
@login_required
def oa_theme():
    form = ThemeForm()
    if form.validate_on_submit():
        existing_theme = Themes.query.filter_by(theme_title=form.theme_title.data).first()
        if existing_theme is None:
            theme = Themes(
                theme_title=form.theme_title.data,
                theme_description=form.theme_description.data,
                theme_private=form.theme_private.data,
            )
            db.session.add(theme)
            db.session.commit()  # Create new theme
            return redirect(url_for('ookarchyves.oa_index'))
        flash('Ce theme existe déjà')
    return render_template(
        'oa_theme_form.jinja2',
        form=form
    )

@oa_bp.route('/article', methods=['GET', 'POST'])
@login_required
def oa_article():
    form = ArticleForm()
    themes = Themes.query.all()
    # Pour remplir le selectfield \o/ avec la liste de thème
    form.article_theme_id.choices = [(t.id, t.theme_title) for t in Themes.query.order_by('theme_title')]
    if form.validate_on_submit():
        existing_theme = Articles.query.filter_by(article_title=form.article_title.data).first()
        if existing_theme is None:
            article = Articles(
                article_title=form.article_title.data,
                article_author_id=current_user.id,
                article_body=form.article_body.data,
                article_theme_id=form.article_theme_id.data,
                article_private=form.article_private.data,
            )
            db.session.add(article)
            db.session.commit()  # Create new article
            return redirect(url_for('ookarchyves.oa_index'))
        flash('Cette article existe déjà')
    return render_template(
        'oa_article_form.jinja2',
        form=form,
        themes=themes
    )