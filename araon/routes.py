from flask import render_template,url_for,redirect
from araon import app
from araon.forms import LoginForm




@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/project")
def project():
    return render_template('projects.html')

@app.route("/blog")
def blog():
    return "<h1>blog part</h1>"


@app.route("/resume")
def resume():
    return render_template('resume.html')




@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            return redirect(url_for('home'))
        else:
            return redirect(url_for('home'))
    return render_template('login.html', form=form)