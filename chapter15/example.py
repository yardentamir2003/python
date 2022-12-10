from flask import Flask


class Bank:
    def __init__(self):
        self.balance = 0

    def add(self):
        self.balance += 1


app = Flask(__name__)
bank = Bank()


@app.route("/")
def hello_world():
    return "<p>Hello, World! {} click to add <a href='/1'> here</a></p>".format(bank.balance)


@app.route("/1")
def yarden():
    bank.add()
    return "<p>yarden was here!<a href='/'> here</a></p>"


app.run()
