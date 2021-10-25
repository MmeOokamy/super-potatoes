

# flask and her Environment
 * $ mkdir back
 * $ python3 -m venv menv # for manjaro_env
 * $ . menv/bin/activate
In menv
 * $ pip install Flask
 * $ pip install python-dotenv
 * $ pip install Flask-SQLAlchemy
 * $ pip install flask-jwt-extended

## Requirements files
 * $ pip freeze > requirements.txt



### config_db.ini
   * [postgresql]
   * host=localhost
   * database=dbname
   * user=dbuser
   * password=dbpassword
