from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


db = SQLAlchemy() #database instance
bcrypt = Bcrypt()
login_manager = LoginManager()
# this is how the login manager know where to redirect us when a page requires login!
login_manager.login_view = 'users.login' #. We show the login_manager where the login route is located. So we passed the function name of our route
                                    # Is for the decorator to work in the account routes
login_manager.login_message_category = 'info' #to have a beeter visualasiation for flash messages (blue info alert in bootstrap)

mail = Mail() #initialise extention!


# initalize extention witouth the app variable so it can used for every app.
#then initialize the app
def create_app(config_class=Config):
    app = Flask(__name__) # __name__ file name
    app.config.from_object(Config)

    db.init_app(app) #initialize the these extentions with the app.
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users #import blueprints object
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app