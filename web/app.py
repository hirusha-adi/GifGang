import logging
import random

import requests
from flask import (Flask, redirect, render_template,
                   url_for, request)
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
        if WebsiteData.index["api_usage"]["tenor"]["usage"]:
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
        web_title=WebsiteData.pins["title"],
        all_pins_list=WebsiteData.pins["all_list"]
    )


@app.route("/search_post", methods=['POST'])
def search_post():
    try:
        try:
            query = request.form['q']
        except KeyError:
            query = request.form['query']
    except KeyError:
        try:
            try:
                query = request.args.get("q")
            except KeyError:
                query = request.args.get("query")
        except:
            return redirect(url_for('index'))

    if (query is None) or len(str(query)) == 0:
        return redirect(url_for('index'))

    query = query.replace("/", "%2F")

    return redirect(url_for('search', query=query))


@app.route("/restricted")
def restricted():
    return "restricted"


@app.route("/search/<query>")
def search(query):
    if query is None:
        return redirect(url_for('index'))

    thecatapi_url_list = []
    thecatapi_usage = False
    dogceo_url_list = []
    dogceo_usage = False
    nekoslife_url_list = []
    nekoslife_usage = False

    if WebsiteData.search["custom_api_usage"]:
        query_lowered = str(query).lower()
        if any(word in query_lowered.split() for word in WebsiteData.search["custom_api_data_all_keywords_list"]):

            for one_custom in WebsiteData.search["custom_api_data"]:
                if any(word in query_lowered.split() for word in one_custom["keywords"]):

                    # The Cat API
                    if one_custom["api_info"]["name"] == "theCatAPI":
                        if Important.thecatapi_usage:  # global check
                            if one_custom["api_info"]["usage"]:  # local check
                                thecatapi_usage = True
                                r = requests.get(
                                    str(one_custom["api_info"]["api_url"])
                                    + "?limit=" +
                                    str(one_custom["api_info"]["limit"]) +
                                    "&size=" + str(one_custom["api_info"]["size"]) +
                                    "&mime_types=" +
                                    str(one_custom["api_info"]["mime_types"]) +
                                    "&order=" +
                                    str(one_custom["api_info"]["order"]) +
                                    "&has_breeds=" +
                                    str(one_custom["api_info"]["has_breeds"])
                                )
                                if 300 > r.status_code >= 200:
                                    data = r.json()
                                    for result in data:
                                        thecatapi_url_list.append(
                                            result["url"])
                                else:
                                    thecatapi_usage = False

                    # dogCEO API
                    if one_custom["api_info"]["name"] == "dogCEO":
                        if Important.dogceo_usage:
                            if one_custom["api_info"]["usage"]:
                                dogceo_usage = True
                                r = requests.get(
                                    str(one_custom["api_info"]["api_url"])
                                    + "/" +
                                    str(one_custom["api_info"]["limit"])
                                )
                                if 300 > r.status_code >= 200:
                                    data = r.json()
                                    for result in data["message"]:
                                        dogceo_url_list.append(result)
                                else:
                                    dogceo_usage = False

                    # Anime Stuff - (nekoslife)
                    if one_custom["api_info"]["name"] == "nekoslife":
                        if Important.nekoslife_usage:
                            if one_custom["api_info"]["usage"]:
                                nekoslife_usage = True
                                _limit = int(
                                    one_custom["api_info"]["limit"]) - 1
                                while len(nekoslife_url_list) <= _limit:
                                    r1 = requests.get(one_custom["api_info"]["api_url_list"][random.randint(
                                        0, int(len(one_custom["api_info"]["api_url_list"]))-1)])
                                    if 300 > r1.status_code >= 200:
                                        data = r1.json()
                                        try:
                                            nekoslife_url_list.append(
                                                data["url"])
                                        except KeyError:
                                            nekoslife_url_list.append(
                                                data["neko"])

    # GIPHY and TENOR will be used to search, no matter what is entered if enabled by json
    giphy_url_list = []
    giphy_usage = False
    if Important.giphy_usage:
        if WebsiteData.search["api_usage"]["giphy"]["usage"]:
            giphy_usage = True
            offset = random.randint(
                1, 4990 - int(WebsiteData.search["api_usage"]["giphy"]["limit"]))
            r = requests.get(
                f'{WebsiteData.search["api_usage"]["giphy"]["api_url"]}?api_key={Important.giphy_api_key}&limit={WebsiteData.search["api_usage"]["giphy"]["limit"]}&offset={offset}&q={query}')
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

        if len(giphy_url_list) == 0:
            giphy_usage = False

    tenor_url_list = []
    tenor_usage = False
    if Important.tenor_usage:
        if WebsiteData.search["api_usage"]["tenor"]["usage"]:
            tenor_usage = True
            r = requests.get(
                f'{WebsiteData.search["api_usage"]["tenor"]["api_url"]}?key={Important.tenor_api_key}&limit={WebsiteData.search["api_usage"]["tenor"]["limit"]}&locale={WebsiteData.search["api_usage"]["tenor"]["locale"]}&ar_range={WebsiteData.search["api_usage"]["tenor"]["ar_range"]}&contentfilter={WebsiteData.search["api_usage"]["tenor"]["contentfilter"]}&q={query}')
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

    return render_template(
        "search.html",
        web_title=WebsiteData.search["title"].format(query=query),
        giphy_usage=giphy_usage,
        giphy_url_list=giphy_url_list,
        tenor_usage=tenor_usage,
        tenor_url_list=tenor_url_list,
        thecatapi_usage=thecatapi_usage,
        thecatapi_url_list=thecatapi_url_list,
        dogceo_usage=dogceo_usage,
        dogceo_url_list=dogceo_url_list,
        nekoslife_usage=nekoslife_usage,
        nekoslife_url_list=nekoslife_url_list
    )


@app.route("/adult")
def adult_index():

    # E-Porner API
    eporner_usage = False
    eporner_list = []
    if Important.eporner_usage:
        if WebsiteData.adult_index["api_usage"]["eporner"]["usage"]:
            eporner_usage = True
            _final_url = WebsiteData.adult_index["api_usage"]["eporner"]["api_url"]
            _final_url += f'?per_page={int(WebsiteData.adult_index["api_usage"]["eporner"]["limit"]) + 2}'
            _final_url += f'&thumbsize={WebsiteData.adult_index["api_usage"]["eporner"]["thumbsize"]}'
            _final_url += f'&order={WebsiteData.adult_index["api_usage"]["eporner"]["order"]}'
            _final_url += f'&format=json'

            _random_search_text = random.choice(
                WebsiteData.adult_index["api_usage"]["random_search_word"])
            _final_url += f'&query={_random_search_text}'

            r = requests.get(_final_url)
            if 300 > r.status_code >= 200:
                data = r.json()
                for result in data["videos"]:
                    eporner_list.append(
                        {
                            "title": result["title"],
                            "url": result["default_thumb"]["src"],
                            "src_url": result["url"]
                        }
                    )
            else:
                eporner_usage = False

    redtube_usage = False
    redtube_list = []
    if Important.redtube_usage:
        if WebsiteData.adult_index["api_usage"]["redtube"]["usage"]:
            redtube_usage = True
            _final_url = WebsiteData.adult_index["api_usage"]["redtube"]["api_url"]
            _final_url += f'?data={WebsiteData.adult_index["api_usage"]["redtube"]["data"]}'
            _final_url += f'&thumbsize={WebsiteData.adult_index["api_usage"]["redtube"]["thumbsize"]}'
            _final_url += f'&search=json'

            _random_search_text = random.choice(
                WebsiteData.adult_index["api_usage"]["random_search_word"])
            _final_url += f'&search={_random_search_text}'
            r = requests.get(_final_url)
            if 300 > r.status_code >= 200:
                data = r.json()
                for result in data["videos"]:
                    redtube_list.append(
                        {
                            "title": result["video"]["title"],
                            "url": result["video"]["default_thumb"],
                            "src_url": result["video"]["url"]
                        }
                    )
            else:
                redtube_usage = False

    return render_template(
        "adult_index.html",
        web_title=WebsiteData.adult_index["title"],
        eporner_usage=eporner_usage,
        eporner_list=eporner_list[:int(
            WebsiteData.adult_index["api_usage"]["eporner"]["limit"])],
        redtube_usage=redtube_usage,
        redtube_list=redtube_list
    )


@app.route("/adult/pins")
def adult_pins():
    return render_template(
        "adult_pins.html",
        web_title=WebsiteData.adult_pins["title"],
        all_body_list=WebsiteData.adult_pins["all_pins_list"],
        title_of_body=WebsiteData.adult_pins["all_pins_title"]
    )


@app.route("/adult/categories")
def adult_categories():
    return render_template(
        "adult_pins.html",
        web_title=WebsiteData.adult_pins["title"],
        all_body_list=WebsiteData.adult_pins["all_categories_list"],
        title_of_body=WebsiteData.adult_pins["all_categories_title"]
    )


@app.route("/adult/pornstars/")
@app.route("/adult/stars/")
def adult_stars_no_page():
    return redirect(url_for('adult_stars', page=1))


@app.route("/adult/pornstars/<page>")
@app.route("/adult/stars/<page>")
def adult_stars(page):
    if (page is None) or (len(str(page)) == 0):
        page = 1

    stars_usage = False
    stars_list = []
    if Important.redtube_usage:
        if WebsiteData.adult_stars["api_usage"]["usage"]:
            stars_usage = True

            # API Request for pornstars list
            # https://api.redtube.com/
            # ?data=redtube.Stars.getStarDetailedList   | ["redtube.Stars.getStarList", "redtube.Stars.getStarDetailedList"]
            # &output=json                              | ["json", "xml"]
            # &page=5                                   | [1-1046]

            _final_url = str(WebsiteData.adult_stars["api_usage"]["api_url"])
            _final_url += f'?data={WebsiteData.adult_stars["api_usage"]["data"]}'
            _final_url += f'&output=json'
            _final_url += f'&page={page}'

            r = requests.get(_final_url)
            if 300 > r.status_code >= 200:
                data = r.json()
                for star in data["stars"]:
                    stars_list.append(
                        {
                            "title": star["star"],
                            "url": star["star_thumb"],
                            "src_url": star["star_url"]
                        }
                    )
            else:
                stars_usage = False

            current_page = int(page)
            first_page = 1
            last_page = 1046

            if current_page == 1:
                previous_page_1 = 1
                previous_page_2 = 1
                previous_page_3 = 1
                previous_page_4 = 1
                show_dots_left = False
            elif current_page == 2:
                previous_page_1 = 1
                previous_page_2 = 1
                previous_page_3 = 1
                previous_page_4 = 1
                show_dots_left = False
            elif current_page == 3:
                previous_page_1 = 2
                previous_page_2 = 1
                previous_page_3 = 1
                previous_page_4 = 1
                show_dots_left = False
            elif current_page == 4:
                previous_page_1 = 3
                previous_page_2 = 2
                previous_page_3 = 1
                previous_page_4 = 1
                show_dots_left = False
            elif current_page == 5:
                previous_page_1 = 4
                previous_page_2 = 3
                previous_page_3 = 2
                previous_page_4 = 1
                show_dots_left = False
            elif current_page == 6:
                previous_page_1 = 5
                previous_page_2 = 4
                previous_page_3 = 3
                previous_page_4 = 2
                show_dots_left = True
            else:
                previous_page_1 = current_page - 1
                previous_page_2 = previous_page_1 - 1
                previous_page_3 = previous_page_2 - 1
                previous_page_4 = previous_page_3 - 1
                show_dots_left = True

            if current_page == (last_page):
                next_page_1 = last_page
                next_page_2 = last_page
                next_page_3 = last_page
                next_page_4 = last_page
                show_dots_right = False
            elif current_page == (last_page-1):
                next_page_1 = last_page + 1
                next_page_2 = last_page
                next_page_3 = last_page
                next_page_4 = last_page
                show_dots_right = False
            elif current_page == (last_page-2):
                next_page_1 = last_page + 1
                next_page_2 = last_page + 2
                next_page_3 = last_page
                next_page_4 = last_page
                show_dots_right = False
            elif current_page == (last_page-3):
                next_page_1 = last_page + 1
                next_page_2 = last_page + 2
                next_page_3 = last_page + 3
                next_page_4 = last_page
                show_dots_right = False
            elif current_page == (last_page-4):
                next_page_1 = last_page + 1
                next_page_2 = last_page + 2
                next_page_3 = last_page + 3
                next_page_4 = last_page + 4
                show_dots_right = False
            else:
                next_page_1 = current_page + 1
                next_page_2 = next_page_1 + 1
                next_page_3 = next_page_2 + 1
                next_page_4 = next_page_3 + 1
                show_dots_right = True

    return render_template(
        "adult_index.html",
        web_title=WebsiteData.adult_stars["title"].format(
            page_number=current_page),
        eporner_usage=False,
        redtube_usage=False,
        stars_usage=stars_usage,
        stars_list=stars_list,
        current_page=current_page,
        first_page=first_page,
        last_page=last_page,
        previous_page_1=previous_page_1,
        previous_page_2=previous_page_2,
        previous_page_3=previous_page_3,
        previous_page_4=previous_page_4,
        next_page_1=next_page_1,
        next_page_2=next_page_2,
        next_page_3=next_page_3,
        next_page_4=next_page_4,
        show_dots_right=show_dots_right,
        show_dots_left=show_dots_left
    )


def runWebServer():
    print(
        f"[+] The server will run on:\n\t[*] SFW: http://{'localhost' if (Config.host == '0.0.0.0') or (Config.host == '127.0.0.1') else Config.host}:{Config.port}/\n\t[*] NSFW: http://{'localhost' if (Config.host == '0.0.0.0') or (Config.host == '127.0.0.1') else Config.host}:{Config.port}/adult\n\t[*] Host: {Config.host}\n\t[*] Port: {Config.port}\n\t[*] Debug Mode: {Config.debug}")
    app.run(Config.host,
            port=Config.port,
            debug=Config.debug)


if __name__ == "__main__":
    runWebServer()
