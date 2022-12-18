from flask import Flask, request


class Visitors:
    def __init__(self):
        self.visitors_list = []

    def add_visitor(self, visitor):
        self.visitors_list.append(visitor)


app = Flask(__name__)
visitors = Visitors()


@app.route("/")
def hello_visitors():
    visitor = request.args.get('name')
    visitors.add_visitor(visitor)
    visitors_str = ""
    for visitor in visitors.visitors_list:
        if visitor in visitors_str:
            continue
        else:
            visitors_str = visitors_str + visitor + " and "

    visitors_str = visitors_str[:-4]

    return "<p>Hello {}<a></a></p>".format(visitors_str)


app.run()
