
# flask and her Environment
 * $ mkdir back
 * $ python3 -m venv menv # for manjaro_env
 * $ . menv/bin/activate
## Flask run
 - possible de configurer dans le .env
      * DEBUG=True
      * FLASK_APP=App
      * FLASK_ENV=development
      * SK="nop"

      * [postgresql]
      * SQLALCHEMY_DATABASE_URI='postgresql://USER:PWD@HOST/DATABASE'
      * HOST='localhost'
      * DATABASE='nomDeLaBaseDeDonnee'
      * USER='NomDeL'Utilisateur'
      * PWD='BahMotDeP@SSE'
      * PORT='5432'  # port postgresql

      * STATIC_FOLDER = 'App/static'
      * TEMPLATES_FOLDER = 'App/templates'
     

   flask run

In menv
<!-- Micro frameworks -->
 * $ pip install Flask
   <!-- pour .env -->
 * $ pip install python-dotenv
 <!-- ORM -->
 * $ pip install Flask-SQLAlchemy
<!-- geré les donnée de session -->
 * $ pip install Flask-Sessions
 <!-- Pour les formulaires -->
 * $ pip install flask-wtf
 <!-- L'authentification -->
 * $ pip install Flask-Login
 <!-- Token d'authentification -->
 * $ pip install flask-jwt-extended


## Install requirement
* $  pip install -r /path/to/requirements.txt

## Requirements files
 * $ pip freeze > requirements.txt
 * $ python -m pip freeze > requirements.txt


### config_db.ini || ***autre forme pour le dotenv***
   * [postgresql]
   * host=localhost
   * database=dbname
   * user=dbuser
   * password=dbpassword
