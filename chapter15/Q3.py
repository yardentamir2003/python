from flask import Flask, request

app = Flask(__name__)


@app.route('/add')
def add():
    number1 = int(request.args.get('number1'))
    number2 = int(request.args.get('number2'))
    return str(number1 + number2)


@app.route('/minus')
def minus():
    number1 = int(request.args.get('number1'))
    number2 = int(request.args.get('number2'))
    return str(number1 - number2)


@app.route('/multiply')
def multiply():
    number1 = int(request.args.get('number1'))
    number2 = int(request.args.get('number2'))
    return str(number1 * number2)


@app.route('/divide')
def divide():
    number1 = int(request.args.get('number1'))
    number2 = int(request.args.get('number2'))
    return str(number1 / number2)


app.run()
