from datetime import datetime
from araon import db


class blogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
<<<<<<< HEAD
    title = db.Column(db.String(100), nullable=False)
    sub_title = db.Column(db.String(200), nullable=False)
=======
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    sub_title = db.Column(db.String(500), nullable=False)
>>>>>>> 27f36eed2bb107b9fd8bb918f3710118b2eceef2
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author = db.Column(db.String(100), nullable=False, default = 'System')
    content = db.Column(db.Text, nullable=False)
    header_img = db.Column(db.String(500))
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"