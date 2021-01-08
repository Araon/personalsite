from flask import render_template,url_for,redirect
from araon import app



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


@app.route("/resume")
def resume():
    return render_template('resume.html')






