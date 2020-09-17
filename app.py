from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
pg_user = "postgres"
pg_pwd = "qwerty10253"
pg_port = "5432"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{username}:{password}@localhost:{port}/bet_scanner".format(
    username=pg_user, password=pg_pwd, port=pg_port)
db = SQLAlchemy(app)

from Bookmaker import Bookmaker

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()