from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os




app = Flask(__name__)

app.secret_key = 'mysecretkey'
file= os.getcwd()+'\\database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
from my_app.views import inicial
app.register_blueprint(inicial)
#return app