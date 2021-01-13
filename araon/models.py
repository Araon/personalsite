from datetime import datetime
from araon import db


class blogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    sub_title = db.Column(db.String(200), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author = db.Column(db.String(100), nullable=False, default = 'System')
    content = db.Column(db.Text, nullable=False)
    header_img = db.Column(db.String(500))
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class bloginfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    sub_title = db.Column(db.String(200), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author = db.Column(db.String(100), nullable=False, default = 'System')
    content = db.Column(db.Text, nullable=False)
    header_img = db.Column(db.String(500))
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"