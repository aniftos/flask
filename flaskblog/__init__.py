from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__) # __name__ file name
app.config['SECRET_KEY'] = 'ceaa0358f6db721ad45b2e49fce2e7b3'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app) #database instance
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #. We show the login_manager where the login route is located. So we passed the function name of our route
                                    # Is for the decorator to work in the account routes
login_manager.login_message_category = 'info' #to have a beeter visualasiation for flash messages (blue info alert in bootstrap)


from flaskblog import routes