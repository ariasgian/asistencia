from flask import Flask
#from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

file= os.getcwd()+'\\database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://lear:1234@localhost/mqtt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

# setting
app.secret_key = 'mysecretkey'

#mysql = MySQL(app)

db = SQLAlchemy(app)
from my_app.views import inicial
app.register_blueprint(inicial)