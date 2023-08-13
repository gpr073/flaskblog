from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Need to make this environment variable before committing.
app.config['SECRET_KEY'] = '0f615fc37299e4d68ad5624ed7278ecd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

from flaskblog import routes