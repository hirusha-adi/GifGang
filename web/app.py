import requests
import random
import logging
from flask import Flask, render_template, send_from_directory

from utils import FileNames, Settings, Secrets

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route("/")
def index():

    url_list = []

    if Secrets.giphy_usage:
        if Secrets.giphy_random:
            for _ in range(Secrets.giphy_random_limit):
                data = requests.get(
                    f"{Secrets.giphy_api_url_base}random?api_key={Secrets.giphy_api_key}").json()
                url_list.append(
                    {
                        "url": data["data"]["images"]["original"]["url"],
                        "title": data["data"]["title"]
                    }
                )
        if Secrets.giphy_trending:
            offset = random.randint(
                1, 4990 - int(Secrets.giphy_trending_limit))
            data = requests.get(
                f"{Secrets.giphy_api_url_base}trending?api_key={Secrets.giphy_api_key}&limit={Secrets.giphy_trending_limit}&offset={offset}").json()
            for item in data["data"]:
                url_list.append(
                    {
                        "url": item["images"]["original"]["url"],
                        "title": item["title"]
                    }
                )

    if Secrets.picsum_usage:
        for number in range(int(Secrets.picsum_limit)):
            url_list.append(str(Secrets.picsum_api_url) + str(number))

    return render_template("index.html", url_list=url_list)


def runWebServer():
    app.run(Settings.host,
            port=Settings.port,
            debug=Settings.debug)


if __name__ == "__main__":
    runWebServer()
