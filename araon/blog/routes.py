from araon.code.routes import post
from flask import Blueprint, render_template, url_for,redirect,request
from araon.models import bloginfo
from datetime import datetime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine



blog = Blueprint('blog',__name__,template_folder="templates",static_url_path='/blog/static',static_folder='static')



engine = create_engine('sqlite:///araon/site.db')

Session = scoped_session(sessionmaker(bind=engine))

@blog.route('/', subdomain = 'blog')
def bloghome():
    posts = bloginfo.query.order_by(bloginfo.date_posted.desc()).all()
    return render_template('blogHome.html', posts = posts)

@blog.route('/about', subdomain = 'blog')
def about():
    return render_template('blogAbout.html')


@blog.route('/post/<int:post_id>', subdomain = 'blog')
def post(post_id):
    post = bloginfo.query.filter_by(id=post_id).one()
    return render_template('blogPost.html', post=post)



@blog.route('/add', subdomain = 'blog')
def add():
    return render_template('blogadd.html')



@blog.route('/addpost', methods=['POST'], subdomain = 'blog')
def addpost():

    session = Session()

    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['ckeditor']
    header = request.form['header_img']

    post = bloginfo(title=title, sub_title = subtitle, author=author, content=content, date_posted=datetime.now(), header_img = header)

    session.add(post)
    session.commit()

    return redirect("/add")






