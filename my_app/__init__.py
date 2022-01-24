from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib
import os
cwd = os.getcwd()
app = Flask(__name__)

app.secret_key = 'mysecretkey'

# connection_string = (
#     r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
#     r"DBQ="+ cwd+"\my_app\database.mdb;"
    
# )

# connection_uri = f"access+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lear:1234@localhost/lear' 
#app.config['SQLALCHEMY_DATABASE_URI'] = connection_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
from my_app.views import inicial
app.register_blueprint(inicial)
#return app