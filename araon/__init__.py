# moiweb\scripts\activate

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_ckeditor import CKEditor


app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///code.db'

db = SQLAlchemy(app)

from araon.code.routes import code
#blueprints routes
app.register_blueprint(code)


from araon import routes

ckeditor = CKEditor(app)


