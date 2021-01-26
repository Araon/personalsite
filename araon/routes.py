from flask import render_template,redirect,url_for
from araon import app


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404

@app.errorhandler(500)
def page_not_found(error):
    return render_template('error.html'), 500


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/project")
def project():
    return render_template('projects.html')


@app.route("/XD")
def egg():
    return "<h1>Nice</h1>"

@app.route("/resume")
def resume():
    return redirect("https://drive.google.com/file/d/1t9JxoWBs5MQX-yUwVqJhMf9V3Xq0_Vjl/view?usp=sharing")





