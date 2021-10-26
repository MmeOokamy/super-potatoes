import json
from flask import Flask
from users import users_list
from dotenv import load_dotenv


app = Flask(__name__)

@app.route("/")
def get_all_user():
    users = users_list()
    return json.dumps(users)


if __name__ == "__main__":
    app.run(debug=True)