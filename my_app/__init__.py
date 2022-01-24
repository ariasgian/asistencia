from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib
import os
cwd = os.getcwd()
app = Flask(__name__)

#tets
app.secret_key = 'mysecretkey'
#IP servidor PostgreSQL server lsd
ip='localhost' 

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lear:1234@'+ip+'/lear' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
from my_app.views import inicial
app.register_blueprint(inicial)
