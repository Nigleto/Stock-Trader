from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/<name>")
def user(name):
    return render_template("index.html", content=name)
    #return f"Hello {name}!"


@app.route("/admin")
def admin():
    return 'hello banana'
        #redirect(url_for("user", name='Admin'))


@app.route("/")
def home(name):
    return render_template("index.html", content=name)


if __name__ == "__main__":
    app.run()
