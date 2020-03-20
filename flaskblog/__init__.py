from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # __name__ file name
app.config['SECRET_KEY'] = 'ceaa0358f6db721ad45b2e49fce2e7b3'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app) #database instance

from flaskblog import routes