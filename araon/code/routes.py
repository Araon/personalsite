from flask import Blueprint, render_template, url_for,redirect,request
from araon.models import blogPost
from araon.code.forms import LoginForm
from datetime import datetime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine



code = Blueprint('code',__name__,template_folder="templates",static_url_path='/code/static',static_folder='static')



engine = create_engine('sqlite:///araon/code.db')
Session = scoped_session(sessionmaker(bind=engine))

@code.route('/', subdomain = 'code')
def codehome():
    posts = blogPost.query.order_by(blogPost.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@code.route('/about', subdomain = 'code')
def about():
    return render_template('about.html')


@code.route('/post/<int:post_id>', subdomain = 'code')
def post(post_id):
    post = blogPost.query.filter_by(id=post_id).one()
    return render_template('post.html', post=post)




@code.route('/login', methods=['GET', 'POST'] ,subdomain = 'code')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'test' and form.password.data == 'test':
            return redirect('/add')
        else:
            return redirect('/error')
    return render_template('about.html')



@code.route('/add', subdomain = 'code')
def add():
    return render_template('add.html')



@code.route('/addpost', methods=['POST'], subdomain = 'code')
def addpost():

    session = Session()

    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['ckeditor']
    header = request.form['header_img']

    post = blogPost(title=title, sub_title = subtitle, author=author, content=content, date_posted=datetime.now(), header_img = header)

    session.add(post)
    session.commit()

    return redirect("/")





