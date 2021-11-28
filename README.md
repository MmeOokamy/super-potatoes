# Super-Potatoes:

   Application qui a pour but de monter en compétences sur Python, Flask et JavaScript.

*****************************************************
Good News! le site est en prod xD  => ***https://mme.ookamy.fr/*** 
 * Il a fallu que je modifie la base de données. De postgreSQL vers MySQL friendly xD 
*****************************************************
## Languages
   * Python 3.8
   * Flask 2 & Jinja2
   * SQL : Postgres [dev] et Mysql [prod]
   * Javascript , Jquery (peut-être rajouter une lib JS)

## Modules
*La construction sera par module. Il sera important d'avoir chaque module indépendant des uns des autres afin de pouvoir ajouter/modifier / supprimer facilement des modules sans interférer avec le core de l'application.*
Pour le moment l'application a comme core ou module principale/moteur legend schema (Core)
 > pour lier les modules il faudra rajouter dans le fichier App/__init__.py
 > et aussi rajouter dans le fichier routes.py a la racine du dossier du module
 ```
# __init__.py
 with app.app_context():
        from . import routes

        from .ookamanager import routes
        app.register_blueprint(routes.om_bp)

# routes.py
om_bp = Blueprint('ookamanager', __name__,
    url_prefix='/ookamanager',
    template_folder='templates'
)


@om_bp.route('/')

 ```
## Application Schema 
   *les fichiers qui ne sont pas dans cette arborescence ne sont pas "utiliser"*
   
```
 . Super-Potatoes
 ├── wsgi.py (Core)
 ├── config.py (Core)
 ├── requirements.txt (Core)
 ├── .env (Core)
 ├── [.menv] (Core)
 └── [App]
        ├── __init__.py (Core)
        ├── ooka_tools.py (Core)
        ├── routes.py (Core) 
        ├── [authentication] (Core)
        |      ├── auth.py
        |      ├── forms.py
        |      └── models.py
        |
        ├── [ookamanager]
        |      ├── forms.py
        |      ├── models.py
        |      ├── routes.py
        |      └── [templates]
        |              ├── om_dashboard.html
        |              ├── om_i.html
        |              ├── om_module_form.jinja2
        |              ├── om_project_form.jinja2
        |              └── om_task_form.jinja2
        |
        ├── [ookarchyves]
        |      ├── forms.py
        |      ├── models.py
        |      ├── routes.py
        |      ├── [static]
        |      |       └── oa.js
        |      └── [templates]
        |              ├── oa_i.html
        |              ├── oa_article_form.jinja2
        |              └── om_theme_form.jinja2
        |
        ├── [settings] (Core)
        |      ├── models.py
        |      ├── params.py
        |      └── params.sql
        |      
        |
        ├── [sql] (Core)
        |      ├── insert.sql
        |      └── schema.sql
        |
        ├── [static] (Core)
        |      ├── [css]
        |      ├── [fonts]
        |      ├── [img]
        |      └── [js]
        |      
        └── [templates] (Core)
               ├── base.html
               ├── index.html
               ├── modules.html
               ├── navigation.html
               ├── [auth]
               |       └── login.jinja2
               ├── [error]
               |       ├── 404.html
               |       └── 500.html
               └── [setting]
                       └── login.jinja2

```

