import requests
from flask import Flask, render_template, send_from_directory

from utils import FileNames, Settings

app = Flask(__name__)


@app.route("/")
def index():
    data = {
        "picsum_api_links": ["https://picsum.photos/200/300?random=" + str(x)
                             for x in range(30)],
    }
    return render_template("index.html", **data)


def runWebServer():
    app.run(Settings.host,
            port=Settings.port,
            debug=Settings.debug)


if __name__ == "__main__":
    runWebServer()
