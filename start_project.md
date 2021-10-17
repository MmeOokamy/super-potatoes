
# need to have 
    - nodejs and create-react-app
    - python3.9 and flask
    - react 


# flask and her Environment
 * $ mkdir back
 * $ python3 -m venv menv # for manjaro_env
 * $ . menv/bin/activate
In menv
 * $ pip install Flask
 * $ pip install python-dotenv
 * $ pip install Flask-SQLAlchemy


## Requirements files
 * $ pip freeze > requirements.txt



### config_db.ini
   * [postgresql]
   * host=localhost
   * database=dbname
   * user=dbuser
   * password=dbpassword

# react

* $ npm install -g create-react-app

* $ npx create-react-app front
* $ cd front/
* $ yarn start