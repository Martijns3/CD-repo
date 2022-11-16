from ipaddress import v4_int_to_packed
import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method =='GET':
        return render_template("login.html", title="Login Page")
    if request.method == 'POST':
        d1 = get_users()
        hash_list = []
        for k,v in d1.items():
            if k==request.form["username"]:
                hash_list.append(v)
        if len(hash_list):
            qq =str(hash_list[0])
            passw = request.form["password"]
            if hash_password(passw) == qq:
                return "great"
            else: 
                return 'no pass'
        else:
            return redirect(url_for('loginerror', error=True))
            
     
            
@app.route("/login")
def loginerror():
    return render_template("login.html", title="Error")

@app.route("/dashboard")
def dashboard():
    # YOUR SOLUTION HERE
    pass


@app.route("/logout", methods=["GET", "POST"])
def logout():
    # YOUR SOLUTION HERE
    pass

# def test(q):
#     d1 = get_users()
#     hash_list = []
#     for k,v in d1.items():
#         if k== q:
#             hash_list.append(v)
#     return(hash_list)
            
# print(test('Alice'))