
# Flask and Environment
 
## Flask run
      - $ mkdir back
      - $ python3 -m venv menv # for manjaro_env
      - $ . menv/bin/activate  # for linux 
      - $ venv\Scripts\activate.bat  # for windows 

   ### Possible de configurer dans le .env
      - DEBUG=True
      - FLASK_APP=App
      - FLASK_ENV=development
      - SK="nop"
      - [postgresql]
      - SQLALCHEMY_DATABASE_URI='postgresql://USER:PWD@HOST/DATABASE'
      - HOST='localhost'
      - DATABASE='nomDeLaBaseDeDonnee'
      - USER='NomDeL'Utilisateur'
      - PWD='BahMotDeP@SSE'
      - PORT='5432'  # port postgresql
      - STATIC_FOLDER = 'App/static'
      - TEMPLATES_FOLDER = 'App/templates'
     

   flask run
----
### En cas de bug flask et pip 
      - on supprime le dossier menv
      - $ cd Dev/super-potatoes/
      - $ python3 -m venv menv
      - $ . menv/bin/activate
      - (menv) $ pip install -r requirements.txt 

----
### paquet important
      <!-- Micro frameworks -->
      * (menv) $ pip install Flask
         <!-- pour .env -->
      * (menv) $ pip install python-dotenv
      <!-- ORM -->
      * (menv) $ pip install Flask-SQLAlchemy
      <!-- geré les donnée de session -->
      * (menv) $ pip install Flask-Sessions
      <!-- Pour les formulaires -->
      * (menv) $ pip install flask-wtf
      <!-- L'authentification -->
      * (menv) $ pip install Flask-Login
      <!-- Token d'authentification -->
      * (menv) $ pip install flask-jwt-extended

----
## Install requirement
      - $  pip install -r /path/to/requirements.txt

## Requirements files
      - $ pip freeze > requirements.txt
      - $ python -m pip freeze > requirements.txt

----
### config_db.ini || ***autre forme pour le dotenv***
      - [postgresql]
      - host=localhost
      - database=dbname
      - user=dbuser
      - password=dbpassword

----
## Mysql config (sur le serveur prod)
      - pip install mysqlclient
      - pip install flask_mysqldb
----
