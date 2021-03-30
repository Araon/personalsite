from flask import Blueprint, render_template, url_for,redirect,request
from araon.models import blogPost
from araon.code.forms import LoginForm
from datetime import datetime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine


code = Blueprint('code',__name__,template_folder="templates",static_url_path='/code/static',static_folder='static')


engine = create_engine('sqlite:///araon/site.db')
Session = scoped_session(sessionmaker(bind=engine))


@code.route('/code')
def codehome():
    posts = blogPost.query.order_by(blogPost.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@code.route('/code/about')
def about():
    return render_template('about.html')


@code.route('/code/post/<int:post_id>')
def post(post_id):
    post = blogPost.query.filter_by(id=post_id).one()
    return render_template('post.html', post=post,  prev = post_id -1)

@code.route('/code/supersecretlinktoaddpost')
def add():
    return render_template('add.html')


@code.route('/code/addcodepost', methods=['POST'])
def addcodepost():

    session = Session()

    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['ckeditor']
    header = request.form['header_img']

    post = blogPost(title=title, sub_title = subtitle, author=author, content=content, date_posted=datetime.now(), header_img = header)

    session.add(post)
    session.commit()

    return redirect("/code")





