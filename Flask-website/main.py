import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password


__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.secret_key = os.urandom(16)


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-store max-age=0"
    return r


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    args = request.args
    logout = args.get("logout", default="False")
    if logout == "False":
        user = session.get("username")
        if user is None:
            return render_template(
                "index.html", title="Index", logout_message="You are not logged in"
            )
        else:
            return render_template(
                "index.html", title="Index", logout_message=f"Welcome {user}"
            )
    else:
        return render_template(
            "index.html", title="Index", logout_message="Logout successful"
        )


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        args = request.args
        error = args.get("error", default="False")
        if error == "False":
            return render_template("login.html", title="Login Page")
        else:
            return render_template(
                "login.html",
                title="Login Page",
                error_message="Wrong username or password",
            )

    if request.method == "POST":
        d1 = get_users()
        for k, v in d1.items():
            if k == request.form["username"]:
                passw = request.form["password"]
                if hash_password(passw) == v:
                    session["username"] = request.form["username"]
                    return redirect(url_for("dashboard", name=request.form["username"]))
                else:
                    return redirect(url_for("login", error=True))
        else:
            return redirect(url_for("login", error=True))


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    if request.method == "GET":
        user_id = session.get("username")
        if user_id is None:
            return redirect(url_for("index"))
        else:
            args = request.args
            name = args.get("name")
            return render_template("dashboard.html", title="Dashbord", user=name)

    if request.method == "POST":
        if request.form["logout"] == True:
            return redirect(url_for("/logout"))


@app.route("/logout", methods=["GET", "POST"])
def logout():
    try:
        session.pop("username")
    except:
        pass
    return redirect(url_for("index", logout=True))


if __name__ == "__main__":
    app.run()
