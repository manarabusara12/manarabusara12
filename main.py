from flask import Flask, jsonify, request, render_template
import random
import requests,json
import  redirect
from database import *

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'

@app.route("/")
def index():
  return render_template("home.html")

@app.route("/form", methods=['GET', 'POST'])
def form():
  if request.method=="GET": 
    return render_template("form.html")
  else:
    username= request.form['username']
    namethebook=request.form['namethebook']
    post_by_Level= request.form.get('levels')
    create_post(username,post_by_Level,namethebook)
    if len(namethebook) < 180:
      if post_by_Level=="A2 Elementary books":
        A2_post= post_by_Level
        return render_template('A2 Elementary books.html', A2_post = A2_post)
      elif Level=="A1 Starter books":
        A1= post_by_Level
        return render_template('A1 Starter books', A1_post = A1_post)
    else:
      return render_template("form.html", errormsg = "Sorry! To many characters! limit is 180. :)")

@app.route("/A1 Starter books", methods=['GET', 'POST'])
def A1Starterbooks():
  return render_template("A1 Starter books.html")

    
@app.route("/A2 Elementary books", methods=['GET', 'POST'])
def A2Elementarybooks():
    return render_template("A2 Elementary books.html" )


@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
