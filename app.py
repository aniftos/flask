from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from flask import flash, redirect
from datetime import datetime

app = Flask(__name__) # __name__ file name

app.config['SECRET_KEY'] = 'ceaa0358f6db721ad45b2e49fce2e7b3'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app) #database instance

class User(db.Model): #Each class is an individual table on the database with the name of "user" (lowercase)
    id = db.Column(db.Integer, primary_key = True) #primary key means a unique id for a user
    username = db.Column(db.String(20), unique = True, nullable = False) #unique means again same us above, cant be empty
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg') #no unique = True because there is going to be a default picture
    password = db.Column(db.String(60), nullable = True) #generate hash of 60 characters
    posts = db.relationship('Post', backref='author', lazy = True) #defines a relationship not a column!
    '''Our post attritube has relationship to the Post model(class). 
    Backref (is like creating a new column but not actuall) and uses the author attribute to get the user who created the post!
    Lazy defines when to pull all the posts data from that specific user. '''

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

posts = [
    {
        'author': 'George Aniftos',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted': 'October 09, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content':'Second post content',
        'date_posted': 'October 11, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


@app.route('/register', methods =['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "test@gmail.com" and form.password.data == "password":
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)


if __name__ == "__main__":
    app.run(debug=True)