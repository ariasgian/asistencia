from flask import Flask
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

from my_app.views import inicial
app.register_blueprint(inicial)