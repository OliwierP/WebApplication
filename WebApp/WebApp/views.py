from WebApp import app
from flask import render_template, request

"""
"""

@app.route("/")
def home_route():
    """
	Funkcja home_route

	Paramters
	---------

	Returns
	-------
	render_template("index.html"): templatka
    """
    return render_template("index.html")

@app.route("/api/<var>")
def api_route(var):
    """
	Funkcja api_route

	Parameters
	----------
	var(int):

	Returns
	-------
	render_template("api.html", var=var): templatka
    """
    return render_template("api.html", var=var)

@app.route("/login", methods=["GET", "POST"])
def login_route():
    """
	Funkcja login_route

	Parameters
	---------

	Returns
	-------
	render_template("login.html", state=state)
    """
    state = "Unauthenticated"
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        state = f"{state} {login}:{password}"
    return render_template("login.html", state=state)


               


  


               

               

               

               
