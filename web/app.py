import os
from re import L

import requests
from flask import Flask, render_template

from utils import FileNames, Settings

app = Flask(__name__)


@app.route("/")
def index():
    # return "hello"
    return render_template("index.html")


def runWebServer():
    app.run(Settings.host,
            port=Settings.port,
            debug=Settings.debug)


if __name__ == "__main__":
    runWebServer()
