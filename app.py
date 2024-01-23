import re
from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    content = "Hello There, " + name + "! It's " + formatted_now
    return content


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)