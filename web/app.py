import requests
import random
import logging
from flask import Flask, render_template, send_from_directory

from utils import FileNames, Config, Settings, WebsiteData

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route("/")
def index():

    url_list = []

    if Settings.giphy_usage:
        if Settings.giphy_random:
            for _ in range(Settings.giphy_random_limit):
                r = requests.get(
                    f"{Settings.giphy_api_url_base}random?api_key={Settings.giphy_api_key}")
                if 300 > r.status_code >= 200:
                    try:
                        data = r.json()
                        url_list.append(
                            {
                                "url": data["data"]["images"]["original"]["url"],
                                "title": data["data"]["title"]
                            }
                        )
                    except Exception as e:
                        print(e)
        if Settings.giphy_trending:
            offset = random.randint(
                1, 4990 - int(Settings.giphy_trending_limit))
            r = requests.get(
                f"{Settings.giphy_api_url_base}trending?api_key={Settings.giphy_api_key}&limit={Settings.giphy_trending_limit}&offset={offset}")
            if 300 > r.status_code >= 200:
                try:
                    data = r.json()
                    for item in data["data"]:
                        url_list.append(
                            {
                                "url": item["images"]["original"]["url"],
                                "title": item["title"]
                            }
                        )
                except Exception as e:
                    print(e)

    if Settings.picsum_usage:
        for number in range(int(Settings.picsum_limit)):
            url_list.append(str(Settings.picsum_api_url) + str(number))

    return render_template("index.html", url_list=url_list)


@app.route("/pins")
def pins():
    return render_template(
        "pins.html",
        all_pins_list=WebsiteData.pins["all_list"]
    )


def runWebServer():
    print(
        f"[+] The server will run on:\n\t[*] Link: http://{Config.host}:{Config.port}/\n\t[*] Host: {Config.host}\n\t[*] Port: {Config.port}\n\t[*] Debug Mode: {Config.debug}")
    app.run(Config.host,
            port=Config.port,
            debug=Config.debug)


if __name__ == "__main__":
    runWebServer()
