
# flask and her Environment
 * $ mkdir back
 * $ python3 -m venv menv # for manjaro_env
 * $ . menv/bin/activate
## Flask run
 - possible de configurer dans le .env
export FLASK_ENV=development
export FLASK_APP=App
flask run

In menv
 * $ pip install Flask
 * $ pip install python-dotenv
 * $ pip install Flask-SQLAlchemy
 * $ pip install flask-jwt-extended


## Install requirement
* $  pip install -r /path/to/requirements.txt

## Requirements files
 * $ pip freeze > requirements.txt



### config_db.ini
   * [postgresql]
   * host=localhost
   * database=dbname
   * user=dbuser
   * password=dbpassword
