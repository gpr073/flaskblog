from flask import Flask, render_template, url_for, flash, redirect
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
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'gptaz101@gmail.com' and form.password.data == "password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run()