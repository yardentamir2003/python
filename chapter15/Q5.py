from flask import Flask, request


class Visitors:
    def __init__(self):
        self.visitors_list = []

    def add_visitor(self, visitor):
        self.visitors.append(visitor)


app = Flask(__name__)
# visitors = Visitors()


@app.route("/")
def hello_visitors():
    visitors = Visitors()
    visitor = request.args.get('visitor')
    visitors.add_visitor(visitor)
    visitors_str = ""
    for visitor in visitors.visitors_list:

        if len(visitors_str) == 0:
            visitors_str = visitors_str + visitor

        else:
            if visitor in visitors_str:
                continue
            else:
                visitors_str = visitors_str + visitor + "and"

    visitors_str = visitors_str[:-3]

    return "<p>Hello, you are visitor number {}.<a></a></p>".format(visitors.visitors)


app.run()