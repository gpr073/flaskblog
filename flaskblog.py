from flask import Flask, render_template, url_for
app = Flask(__name__)

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