from flask import Flask, __main__

app = Flask(__main__)


def home():
    return ""


if __name__ == "__main__":
    app.run()
