from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from flask import flash, redirect

app = Flask(__name__) # __name__ file name

app.config['SECRET_KEY'] = 'ceaa0358f6db721ad45b2e49fce2e7b3'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app) #database instance

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True)

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