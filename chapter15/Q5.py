from flask import Flask


class Visitors:
    def __init__(self):
        self.visitors = 0

    def add(self):
        self.visitors += 1


app = Flask(__name__)
visitors = Visitors()


@app.route("/")
def hello_world():
    return "<p>Hello, you are visitor number {}<a href='/1'> here</a></p>".format(visitors.visitors)


@app.route("/1")
def yarden():
    visitors.add()



app.run()