from araon.code.routes import post
from flask import Blueprint, render_template, url_for,redirect,request
from araon.models import bloginfo
from datetime import datetime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine



blog = Blueprint('blog',__name__,template_folder="templates",static_url_path='/blog/static',static_folder='static')



engine = create_engine('sqlite:///araon/site.db')

Session = scoped_session(sessionmaker(bind=engine))

@blog.route('/blog')
def bloghome():
    posts = bloginfo.query.order_by(bloginfo.date_posted.desc()).all()
    return render_template('blogHome.html', posts = posts)

@blog.route('/blog/about')
def about():
    return render_template('blogAbout.html')


@blog.route('/blog/post/<int:post_id>')
def post(post_id):
    post = bloginfo.query.filter_by(id=post_id).one()
    return render_template('blogPost.html', post=post, prev = post_id - 1, nex = post_id + 1)



@blog.route('/blog/supersecretlinktoaddpost')
def add():
    return render_template('blogadd.html')



@blog.route('/blog/addblogpost', methods=['POST'])
def addblogpost():

    session = Session()

    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['ckeditor']
    header = request.form['header_img']

    post = bloginfo(title=title, sub_title = subtitle, author=author, content=content, date_posted=datetime.now(), header_img = header)

    session.add(post)
    session.commit()

    return redirect("/blog/supersecretlinktoaddpost")






