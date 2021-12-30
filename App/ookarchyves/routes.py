
from flask import current_app as app
from flask_login import current_user, login_required
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
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

NAME_MENU= 'Ookarchyves'

@oa_bp.route('/')
@login_required
def oa_index():
    
    c_theme = Themes.query.count()
    c_article = Articles.query.count()
    themes = Themes.query.all()
    articles = Articles.query.all()

    #Init une list pour y inserer les dict des themes
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
        menu_active=NAME_MENU,
        themes=menu,
        c_theme = Themes.query.count(),
        c_article = Articles.query.count()
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
        menu_active=NAME_MENU,
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
        menu_active=NAME_MENU,
        form=form,
        themes=themes
    )

@oa_bp.route('/article-view/')
@login_required
def oa_article_by_id():
    art_id = request.args.get('id')
    if art_id:
        art_request = Articles.query.filter(Articles.id==art_id).all()
        for ar in art_request:
            a={}
            a['id']=ar.id
            a['title']=ar.article_title
            a['create_at']=ar.article_create_at
            a['update_at']=ar.article_update_at
            a['body']=ar.article_body
            a['theme_id']=ar.article_theme_id
            a['private']=ar.article_private
            
    return jsonify(
        response=art_id,
        art_obj=a
    )


@oa_bp.route('/article-d/')
@login_required
def oa_d():
    art_id = request.args.get('id')
    a = Articles.query.filter_by(id=art_id).one()
    if a:
        try:
            db.session.delete(a)
            db.session.commit()
            return jsonify(
                response='D'
            )
        except:
            return jsonify(
            response="l'article n'a pu etre delete"
            )
        