from flask import Flask, request

app = Flask(__name__)


@app.route('/greet')
def login():
    name = request.args.get('name')
    return "Hello {}".format(name)


app.run()