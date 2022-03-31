import logging
import random

import requests
from flask import (Flask, redirect, render_template,
                   url_for)
from imgurpython import ImgurClient

from utils import Config, FileNames, Important, WebsiteData

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route("/")
def index():

    giphy_url_list = []
    giphy_usage = False
    if Important.giphy_usage:
        if WebsiteData.index["api_usage"]["giphy"]["usage"]:
            giphy_usage = True

            # Random
            if WebsiteData.index["api_usage"]["giphy"]["random"]:
                for _ in range(int(WebsiteData.index["api_usage"]["giphy"]["random_limit"])):
                    r = requests.get(
                        f'{WebsiteData.index["api_usage"]["giphy"]["random_api_url"]}?api_key={Important.giphy_api_key}')
                    if 300 > r.status_code >= 200:
                        try:
                            data = r.json()
                            giphy_url_list.append(
                                {
                                    "url": data["data"]["images"]["original"]["url"],
                                    "title": data["data"]["title"]
                                }
                            )
                        except Exception as e:
                            print(e)

            # Trending
            if WebsiteData.index["api_usage"]["giphy"]["trending"]:
                offset = random.randint(
                    1, 4990 - int(WebsiteData.index["api_usage"]["giphy"]["trending_limit"]))
                r = requests.get(
                    f'{WebsiteData.index["api_usage"]["giphy"]["trending_api_url"]}?api_key={Important.giphy_api_key}&limit={WebsiteData.index["api_usage"]["giphy"]["trending_limit"]}&offset={offset}')
                if 300 > r.status_code >= 200:
                    try:
                        data = r.json()
                        for item in data["data"]:
                            giphy_url_list.append(
                                {
                                    "url": item["images"]["original"]["url"],
                                    "title": item["title"]
                                }
                            )
                    except Exception as e:
                        print(e)

    picsum_url_list = []
    picsum_usage = False
    if Important.picsum_usage:
        if WebsiteData.index["api_usage"]["picsum"]["usage"]:
            picsum_usage = True
            for number in range(int(WebsiteData.index["api_usage"]["picsum"]["limit"])):
                picsum_url_list.append(
                    str(WebsiteData.index["api_usage"]["picsum"]["api_url"]) + str(number))

    tenor_url_list = []
    tenor_usage = False
    if Important.tenor_usage:
        if WebsiteData.index["api_usage"]["imgur"]["usage"]:
            tenor_usage = True
            r = requests.get(
                f'{WebsiteData.index["api_usage"]["tenor"]["api_url"]}?key={Important.tenor_api_key}&limit={WebsiteData.index["api_usage"]["tenor"]["limit"]}&locale={WebsiteData.index["api_usage"]["tenor"]["locale"]}&ar_range={WebsiteData.index["api_usage"]["tenor"]["ar_range"]}&contentfilter={WebsiteData.index["api_usage"]["tenor"]["contentfilter"]}')
            if 300 > r.status_code >= 200:
                data = r.json()
                for result in data["results"]:
                    tenor_url_list.append(
                        {
                            "title": str(result["content_description"]),
                            "url": result["media"][0]["gif"]["url"]
                        }
                    )
            else:
                tenor_usage = False

    unsplash_url_list = []
    unsplash_usage = False
    if Important.unsplash_usage:
        if WebsiteData.index["api_usage"]["unsplash"]["usage"]:
            unsplash_usage = True
            final_url = WebsiteData.index["api_usage"]["unsplash"]["api_url"]

            final_url += f'?client_id={Important.unsplash_api_key}'
            final_url += f'&count={WebsiteData.index["api_usage"]["unsplash"]["limit"]}'

            if isinstance(WebsiteData.index["api_usage"]["unsplash"]["username"], bool):
                pass
            elif isinstance(WebsiteData.index["api_usage"]["unsplash"]["username"], str):
                if WebsiteData.index["api_usage"]["unsplash"]["username"].strip():
                    final_url += f'&username={WebsiteData.index["api_usage"]["unsplash"]["username"]}'

            if isinstance(WebsiteData.index["api_usage"]["unsplash"]["orientation"], bool):
                pass
            elif isinstance(WebsiteData.index["api_usage"]["unsplash"]["orientation"], str):
                if WebsiteData.index["api_usage"]["unsplash"]["orientation"].strip():
                    final_url += f'&orientation={WebsiteData.index["api_usage"]["unsplash"]["orientation"]}'

            r = requests.get(final_url)
            if 300 > r.status_code >= 200:
                data = r.json()
                for result in data["results"]:
                    tenor_url_list.append(
                        {
                            "title": "Will be updated soon",
                            "url": "Will be u updated soon"
                        }
                    )
            else:
                tenor_usage = False

    thecatapi_url_list = []
    thecatapi_usage = False
    if Important.thecatapi_usage:
        if WebsiteData.index["api_usage"]["theCatAPI"]["usage"]:
            thecatapi_usage = True
            r = requests.get(
                str(WebsiteData.index["api_usage"]["theCatAPI"]["api_url"])
                + "?limit=" +
                str(WebsiteData.index["api_usage"]["theCatAPI"]["limit"]) +
                "&size=" + str(WebsiteData.index["api_usage"]["theCatAPI"]["size"]) +
                "&mime_types=" +
                str(WebsiteData.index["api_usage"]["theCatAPI"]["mime_types"]) +
                "&order=" +
                str(WebsiteData.index["api_usage"]["theCatAPI"]["order"]) +
                "&has_breeds=" +
                str(WebsiteData.index["api_usage"]["theCatAPI"]["has_breeds"])
            )
            if 300 > r.status_code >= 200:
                data = r.json()
                for result in data:
                    thecatapi_url_list.append(result["url"])
            else:
                thecatapi_usage = False

    dogceo_url_list = []
    dogceo_usage = False
    if Important.dogceo_usage:
        if WebsiteData.index["api_usage"]["dogCEO"]["usage"]:
            dogceo_usage = True
            r = requests.get(
                str(WebsiteData.index["api_usage"]["dogCEO"]["api_url"])
                + "/" +
                str(WebsiteData.index["api_usage"]["dogCEO"]["limit"])
            )
            if 300 > r.status_code >= 200:
                data = r.json()
                for result in data["message"]:
                    dogceo_url_list.append(result)
            else:
                dogceo_usage = False

    nekoslife_url_list = []
    nekoslife_usage = False
    if Important.nekoslife_usage:
        if WebsiteData.index["api_usage"]["nekoslife"]["usage"]:
            nekoslife_usage = True
            _limit = int(
                WebsiteData.index["api_usage"]["nekoslife"]["limit"]) - 1
            while len(nekoslife_url_list) <= _limit:
                r1 = requests.get(WebsiteData.index["api_usage"]["nekoslife"]["api_url_list"][random.randint(
                    0, int(len(WebsiteData.index["api_usage"]["nekoslife"]["api_url_list"]))-1)])
                if 300 > r1.status_code >= 200:
                    data = r1.json()
                    try:
                        nekoslife_url_list.append(data["url"])
                    except KeyError:
                        nekoslife_url_list.append(data["neko"])

    imgur_url_list = []
    imgur_usage = False
    if Important.imgur_usage:
        if WebsiteData.index["api_usage"]["imgur"]["usage"]:
            imgur_usage = True
            client = ImgurClient(Important.imgur_client_id,
                                 Important.imgur_clinet_secret)
            try:
                items = client.gallery()
            except:
                imgur_usage = False

            if imgur_usage:
                imgur_url_list = [item.link for item in items]

    return render_template(
        "index.html",
        web_title=WebsiteData.index["title"],
        giphy_usage=giphy_usage,
        giphy_url_list=giphy_url_list,
        picsum_usage=picsum_usage,
        picsum_url_list=picsum_url_list,
        imgur_usage=imgur_usage,
        imgur_url_list=imgur_url_list[:int(
            WebsiteData.index["api_usage"]["imgur"]["limit"])],
        tenor_usage=tenor_usage,
        tenor_url_list=tenor_url_list,
        unsplash_usage=unsplash_usage,
        unsplash_url_list=unsplash_url_list,
        thecatapi_usage=thecatapi_usage,
        thecatapi_url_list=thecatapi_url_list,
        dogceo_usage=dogceo_usage,
        dogceo_url_list=dogceo_url_list,
        nekoslife_usage=nekoslife_usage,
        nekoslife_url_list=nekoslife_url_list
    )


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
        return redirect(url_for('index'))

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
