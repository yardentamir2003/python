from flask import Flask
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)


@app.route('/get-time')
def index():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


app.run()
