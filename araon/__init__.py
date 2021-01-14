# moiweb\scripts\activate

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor


app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from araon.code.routes import code
from araon.blog.routes import blog
#blueprints routes
app.register_blueprint(code)
app.register_blueprint(blog)

from araon import routes

ckeditor = CKEditor(app)


