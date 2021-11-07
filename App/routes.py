
@app.route("/")  # index ookamy
def home():
    # Template completement independant
    return render_template('index.html')
    app.add_url_rule('/', endpoint='index')


@app.route("/connect", methods=['GET', 'POST'])  # formulaire de login authentification.auth | template auth.login
def login():
    # GET => affiche le form
    # POST => envoie les données
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']
    return render_template('auth/login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# enregistrement de compte qui ne sera pas mis en place
# Il y aura juste 2 comptes : visitor et ookamy
@app.route("/register", methods=['GET', 'POST'])  # formulaire de login authentification.auth | template auth.login
def register():
    return render_template('auth/register.html')


@app.route("/modules")  # liste des modules
def module():
    return render_template('module/modules.html')

# 
# 

@app.route("/ookarchyves")  # index de ookarchyves
def ookarchyves_index():
    return render_template('module/ookarchyves/main.html')

@app.route("/ookarchyves/ftheme", methods=['GET', 'POST'])  # formulaire d'ajout de theme + liste des themes deja existant avec possibilité de supprimer une theme vide d'article
def ookarchyves_form_add_theme():
    return render_template('module/ookarchyves/fTheme.html')

@app.route("/ookarchyves/farticle", methods=['GET', 'POST'])  # 
def ookarchyves_form_add_article():
    return render_template('module/ookarchyves/fArticle.html')

@app.route("/ookarchyves/article")  # voir l'article avec la possibilité de naviger vers suppression de l'article ou la modification 
def ookarchyves_article():
    return render_template('module/ookarchyves/article.html')

# 
# 

@app.route("/modules/ookamanager")  # index du kanban
def moddule():
    return render_template('module/ookamanager/main.html')


# @app.route("/chemin/url")  
# def nomvariable():
#     return render_template('dossier/fichier.html')
