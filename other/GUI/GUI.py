from flask import Flask, render_template
from flaskwebgui import FlaskUI   # get the FlaskUI class


app = Flask(__name__)
ui = FlaskUI(app)                 # feed the parameters


# do your logic as usual in Flask

#@app.route("/")
#def index():
#    return "It works!"

#@app.route("/hello/<string:name>/")
#def hello(name):
#    return render_template(
#    'test.html',name=name)</string:name>3

#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=80)


#ui.run()                           # call the 'run' method

#127.0.0.1:5000