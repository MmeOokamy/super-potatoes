import json
from flask import Flask
from user_crud import users_list
from dotenv import load_dotenv


app = Flask(__name__)

@app.route("/members")
def members():
    users = users_list()
    return json.dumps(users)


if __name__ == "__main__":
    app.run(dotenv)