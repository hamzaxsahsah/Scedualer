from flask import render_template, request, redirect, session, url_for
from app import app

# Mock user data
users = {"admin": "admin"}

@app.route("/")
def home():
    if "username" in session:
        return render_template("home.html", username=session["username"])
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.get(username) == password:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return "Invalid username/password"
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))
