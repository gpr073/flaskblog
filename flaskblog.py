from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

#Need to make this environment variable before committing.
app.config['SECRET_KEY'] = '0f615fc37299e4d68ad5624ed7278ecd'

posts = [
    {
        'author': 'John Doe',
        'title': 'Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 20, 2023'
    },
    {
        'author': 'Jane Doe',
        'title': 'Post 2',
        'content': 'Second Post Content',
        'date_posted': 'May 20, 2023'
    }
]

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run()