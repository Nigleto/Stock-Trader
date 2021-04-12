from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/admin")
def admin():
    return 'hello banana'


@app.route("/")
def home():
    return render_template("index.html", content='hello', r=3)


@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")


@app.route("/<user>")
def user(user):
    return f"<h1>{user}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
