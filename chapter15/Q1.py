from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World!<a></a></p>"


@app.route("/moon")
def moon():
    return "<p>Hello Moon<a href='/'></a></p>"


@app.route("/sun")
def sun():
    return "<p>good morning<a href='/1'></a></p>"


app.run()
