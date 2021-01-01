from flask import render_template,url_for
from araon import app



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

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404
