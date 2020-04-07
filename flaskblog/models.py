from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flaskblog import db, login_manager, app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin): #Each class is an individual table on the database with the name of "user" (lowercase)
    id = db.Column(db.Integer, primary_key = True) #primary key means a unique id for a user
    username = db.Column(db.String(20), unique = True, nullable = False) #unique means again same us above, cant be empty
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg') #no unique = True because there is going to be a default picture
    password = db.Column(db.String(60), nullable = True) #generate hash of 60 characters
    posts = db.relationship('Post', backref='author', lazy = True) #defines a relationship not a column!
    '''Our post attritube has relationship to the Post model(class). 
    Backref (is like creating a new column but not actuall) and uses the author attribute to get the user who created the post!
    Lazy defines when to pull all the posts data from that specific user. '''

    def get_reset_token(self, expires_sec = 1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8') #return token with paylod of userid

    @staticmethod #not to expect that self as an arguent
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self): # How our object will be printed a user object. This function is called dunder method or magic method
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model): #Each class is an individual table on the database with the name "post" (lowercase)
    id = db.Column(db.Integer, primary_key = True) #unique post
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # specify is a foreign key.


    def __repr__(self): # How our object will be printed a user object. This function is called dunder method or magic method
        return f"Post('{self.title}', '{self.date_posted}')"