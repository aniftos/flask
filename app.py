from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__) # __name__ file name

app.config['SECRET_KEY'] = 'ceaa0358f6db721ad45b2e49fce2e7b3'

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
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)


if __name__ == "__main__":
    app.run(debug=True)