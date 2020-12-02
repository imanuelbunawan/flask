from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/html")
def html():
	page = render_template("learnhtml/portofolio.html")
	return page
