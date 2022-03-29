import requests
import random
import logging
from flask import Flask, redirect, render_template, send_from_directory, url_for

from utils import FileNames, Config, Important, WebsiteData

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route("/")
def index():

    url_list = []

    if Important.giphy_usage:
        if WebsiteData.index["api_usage"]["giphy"]["usage"]:
            if WebsiteData.index["api_usage"]["giphy"]["random"]:
                for _ in range(int(WebsiteData.index["api_usage"]["giphy"]["random_limit"])):
                    r = requests.get(
                        f'{WebsiteData.index["api_usage"]["giphy"]["random_api_url"]}?api_key={Important.giphy_api_key}')
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
            if WebsiteData.index["api_usage"]["giphy"]["trending"]:
                offset = random.randint(
                    1, 4990 - int(WebsiteData.index["api_usage"]["giphy"]["trending_limit"]))
                r = requests.get(
                    f'{WebsiteData.index["api_usage"]["giphy"]["trending_api_url"]}?api_key={Important.giphy_api_key}&limit={WebsiteData.index["api_usage"]["giphy"]["trending_limit"]}&offset={offset}')
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

    if Important.picsum_usage:
        if WebsiteData.index["api_usage"]["picsum"]["usage"]:
            for number in range(int(WebsiteData.index["api_usage"]["picsum"]["limit"])):
                url_list.append(
                    str(WebsiteData.index["api_usage"]["picsum"]["api_url"]) + str(number))

    return render_template("index.html", url_list=url_list)


@app.route("/pins")
def pins():
    return render_template(
        "pins.html",
        all_pins_list=WebsiteData.pins["all_list"]
    )


@app.route("/search")
def search_no_parameter():
    return redirect(url_for('index'))


@app.route("/search/<query>")
def search(query):
    if query is None:
        query = "random"
    print(query)
    return render_template("search.html")


def runWebServer():
    print(
        f"[+] The server will run on:\n\t[*] Link: http://{Config.host}:{Config.port}/\n\t[*] Host: {Config.host}\n\t[*] Port: {Config.port}\n\t[*] Debug Mode: {Config.debug}")
    app.run(Config.host,
            port=Config.port,
            debug=Config.debug)


if __name__ == "__main__":
    runWebServer()
