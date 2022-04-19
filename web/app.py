import logging
import os
import random

import requests
from flask import Flask, redirect, render_template, request, url_for

import services
from utils import Config, FileNames, Important, WebsiteData, log

app = Flask(__name__)
log("Initiated Flask App: 'app'")
logger = logging.getLogger('werkzeug')
logger.setLevel(logging.ERROR)
log("Disabled the default `werkzeug` logging")

COUNT = None


def count_total_visits_amount():
    global COUNT

    if not(os.path.isfile(FileNames.count_file)):
        log(f'Visit count file does not exist')
        with open(FileNames.count_file, "w", encoding="utf-8") as f_make_no_exist:
            if COUNT is None:
                f_make_no_exist.write("1")
                log(f'Created {FileNames.count_file} and wrote "1"')
            else:
                f_make_no_exist.write(int(COUNT))
                log(f'Created {FileNames.count_file} and wrote "{COUNT}" as continuable ')

    with open(FileNames.count_file, "r", encoding="utf-8") as f_read:
        current_count = f_read.read()
        log(f'Current view count is {current_count}')

    try:
        current_count = int(current_count)
        COUNT = current_count
    except ValueError:
        current_count = COUNT

    log(f'Analyzed view count is {current_count}')

    with open(FileNames.count_file, "w", encoding="utf-8") as f_write:
        new_count = COUNT + 1
        f_write.write(str(new_count))
        log(f'New view count is {new_count}')


@app.route("/about")
def about():
    count_total_visits_amount()

    log(f'Requested `/about` - about()',
        ipaddr=request.remote_addr)
    log('Returning `about.html`',
        ipaddr=request.remote_addr)
    return render_template(
        "about.html",
        web_title="About | GifGang"
    )


@app.route("/all_links")
@app.route("/links")
def all_links():
    count_total_visits_amount()
    log(f'Requested `/links` - all_links()',
        ipaddr=request.remote_addr)
    log('Returning `index.html`\n\tall_links_page = True',
        ipaddr=request.remote_addr)
    return render_template(
        "index.html",
        web_title="Links List | GifGang",
        all_links_page=True
    )


@app.route("/")
def index():

    count_total_visits_amount()

    log(f'Requested `/` - index()',
        ipaddr=request.remote_addr)

    data = services.index.giphy(request=request)
    giphy_url_list = data["giphy_url_list"]
    giphy_usage = data["giphy_usage"]

    data = services.index.picsum(request=request)
    picsum_usage = data["picsum_usage"]
    picsum_url_list = data["picsum_url_list"]

    data = services.index.tenor(request=request)
    tenor_url_list = data["tenor_url_list"]
    tenor_usage = data["tenor_usage"]

    data = services.index.cats(request=request)
    thecatapi_url_list = data["thecatapi_url_list"]
    thecatapi_usage = data["thecatapi_usage"]

    data = services.index.dogs(request=request)
    dogceo_url_list = data["dogceo_url_list"]
    dogceo_usage = data["dogceo_usage"]

    data = services.index.nekos_life(request=request)
    nekoslife_url_list = data["nekoslife_url_list"]
    nekoslife_usage = data["nekoslife_usage"]
    # selected_url_list = data["selected_url_list"] # used for debugging purposes

    log(f'Returning `index.html`\n\ttitle={WebsiteData.index["title"]}\n\tgiphy_usage={giphy_usage}\n\tpicsum_usage={picsum_usage}\n\ttenor_usage={tenor_usage}\n\tthecatapi_usage={thecatapi_usage}\n\tdogceo_usage={dogceo_usage}\n\tnekoslife_usage={nekoslife_usage}',
        ipaddr=request.remote_addr)

    return render_template(
        "index.html",
        web_title=WebsiteData.index["title"],
        giphy_usage=giphy_usage,
        giphy_url_list=giphy_url_list,
        picsum_usage=picsum_usage,
        picsum_url_list=picsum_url_list,
        tenor_usage=tenor_usage,
        tenor_url_list=tenor_url_list,
        thecatapi_usage=thecatapi_usage,
        thecatapi_url_list=thecatapi_url_list,
        dogceo_usage=dogceo_usage,
        dogceo_url_list=dogceo_url_list,
        nekoslife_usage=nekoslife_usage,
        nekoslife_url_list=nekoslife_url_list
    )


@app.route("/pins")
def pins():
    count_total_visits_amount()

    log(f'{request.remote_addr} requested `/pins` - pins()',
        ipaddr=request.remote_addr)
    log(
        f'Returning `pins.html`\n\tTitle={WebsiteData.pins["title"]}\n\tPins List from `website.json`',
        ipaddr=request.remote_addr)

    return render_template(
        "pins.html",
        web_title=WebsiteData.pins["title"],
        all_pins_list=WebsiteData.pins["all_list"]
    )


@app.route("/search_post", methods=['POST', 'GET'])
def search_post():
    count_total_visits_amount()

    log(f'Request `/search_post` - search_post()',
        ipaddr=request.remote_addr)

    try:
        try:
            query = request.form['q']
            log(f'Query taken from `POST` request\'s `q`',
                ipaddr=request.remote_addr)
        except KeyError:
            query = request.form['query']
            log(f'Query taken from `POST` request\'s `query`',
                ipaddr=request.remote_addr)
    except KeyError:
        try:
            try:
                query = request.args.get("q")
                log(f'Query taken from `GET` request\'s `q`',
                    ipaddr=request.remote_addr)
            except KeyError:
                query = request.args.get("query")
                log(f'Query taken from `GET` request\'s `query`',
                    ipaddr=request.remote_addr)
        except:
            log(f'Unable to find the query from the request',
                ipaddr=request.remote_addr)
            return redirect(url_for('index'))

    if (query is None) or len(str(query)) == 0:
        log(f'query is None. Nothing to search for!',
            ipaddr=request.remote_addr)
        return redirect(url_for('index'))

    query = query.replace("/", "%2F")

    log(f'Processed Query: {query}',
        ipaddr=request.remote_addr)
    log(
        f'Returning the url for `search` with query',
        ipaddr=request.remote_addr)

    return redirect(url_for('search', query=query))


@app.route("/restricted")
def restricted():
    count_total_visits_amount()

    log(f'Request `/restricted` - restricted()',
        ipaddr=request.remote_addr)
    log(
        f'Returning `age_verify.html`\n\tTitle={WebsiteData.age_verify["title"]}\n\tBody Title={WebsiteData.age_verify["body_title"]}\n\tBody Text={WebsiteData.age_verify["text"]}\n\tYes Button Text={WebsiteData.age_verify["buttons"]["yes"]}\n\tNo Button Text={WebsiteData.age_verify["buttons"]["no"]}',
        ipaddr=request.remote_addr)

    return render_template(
        "age_verify.html",
        web_title=WebsiteData.age_verify["title"],
        body_title=WebsiteData.age_verify["body_title"],
        age_verify_text=WebsiteData.age_verify["text"],
        button_yes=WebsiteData.age_verify["buttons"]["yes"],
        button_no=WebsiteData.age_verify["buttons"]["no"],
    )


@app.route("/search")
def search_no_query():
    count_total_visits_amount()

    log(f'Request `/search` - search_no_query()',
        ipaddr=request.remote_addr)
    log(f'Returning the url for `index` - index()\n\tbecause `/search` route was requested without a query',
        ipaddr=request.remote_addr)

    return redirect(url_for('index'))


@app.route("/search/<query>")
def search(query):
    count_total_visits_amount()

    log(f'Request `/search/<query>` - search(query)',
        ipaddr=request.remote_addr)

    if query is None:
        log(f'query is None\n\tRedirecting to the url of `index`',
            ipaddr=request.remote_addr)
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

                            log(f'TheCatAPI: Random Cat Images\n\tLimit: {one_custom["api_info"]["api_url"]}\n\tSize: {one_custom["api_info"]["size"]}\n\tMime Types: {one_custom["api_info"]["mime_types"]}\n\tOrder: {one_custom["api_info"]["order"]}\n\tHas Breeds: {one_custom["api_info"]["has_breeds"]}',
                                ipaddr=request.remote_addr)

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

                            log(f'DogCEO: Random Dog Images\n\tLimit: {one_custom["api_info"]["limit"]}',
                                ipaddr=request.remote_addr)

                    # Anime Stuff - (nekoslife)
                    if one_custom["api_info"]["name"] == "nekoslife":
                        if Important.nekoslife_usage:
                            if one_custom["api_info"]["usage"]:
                                nekoslife_usage = True
                                full_url_list_nekos_life = []
                                _limit = int(
                                    one_custom["api_info"]["limit"]) - 1
                                while len(nekoslife_url_list) <= _limit:
                                    _final_url = one_custom["api_info"]["api_url_list"][random.randint(
                                        0, int(len(one_custom["api_info"]["api_url_list"]))-1)]
                                    full_url_list_nekos_life.append(_final_url)
                                    r1 = requests.get(_final_url)
                                    if 300 > r1.status_code >= 200:
                                        data = r1.json()
                                        try:
                                            nekoslife_url_list.append(
                                                data["url"])
                                        except KeyError:
                                            nekoslife_url_list.append(
                                                data["neko"])

                            log(f'Nekos.Life: Random Anime Images\n\tLimit: {_limit}\n\tURL List: {full_url_list_nekos_life}',
                                ipaddr=request.remote_addr)

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

            log(
                f'GIPHY: Search GIF\n\tCount: {WebsiteData.search["api_usage"]["giphy"]["limit"]}\n\tOffset: {offset}', ipaddr=request.remote_addr)

        if len(giphy_url_list) == 0:
            giphy_usage = False
            log(f'GIPHY: GIF Url List was empty.\n\tDisabling `giphy_usage`',
                ipaddr=request.remote_addr)

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

            log(
                f'TENOR: Search GIF\n\tCount: {WebsiteData.search["api_usage"]["tenor"]["limit"]}\n\tLocale: {WebsiteData.search["api_usage"]["tenor"]["locale"]}\n\tAR-Range: {WebsiteData.search["api_usage"]["tenor"]["ar_range"]}\n\tContent Filter: {WebsiteData.search["api_usage"]["tenor"]["contentfilter"]}', ipaddr=request.remote_addr)

    log(f'Returning `search.html`\n\tTitle: {WebsiteData.search["title"].format(query=query)}\n\tGIPHY Usage: {giphy_usage}\n\tTenor Usage: {tenor_usage}\n\tTheCatAPI Usage: {thecatapi_usage}\n\tDogCEO API Usage: {dogceo_usage}\n\tNekos.Life: {nekoslife_usage}',
        ipaddr=request.remote_addr)

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

    count_total_visits_amount()

    log(f'Request `/adult` - adult_index()', ipaddr=request.remote_addr)

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

            log(
                f'EPORNER: Search Videos\n\tCount: {WebsiteData.adult_index["api_usage"]["eporner"]["limit"]}\n\tThumbnail Size: {WebsiteData.adult_index["api_usage"]["eporner"]["thumbsize"]}\n\tOrder: {WebsiteData.adult_index["api_usage"]["eporner"]["order"]}\n\tQuery: {_random_search_text}', ipaddr=request.remote_addr)

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

            log(
                f'RedTube: Search Videos\n\tData: {WebsiteData.adult_index["api_usage"]["redtube"]["data"]}\n\tThumbnail Size: {WebsiteData.adult_index["api_usage"]["redtube"]["thumbsize"]}\n\tQuery: {_random_search_text}', ipaddr=request.remote_addr)

    log(
        f'Returning `adult_index.html`\n\tTitle={WebsiteData.adult_index["title"]}\n\tEPORNER API Usage={eporner_usage}\n\tRedtube API Usage={redtube_usage}', ipaddr=request.remote_addr)

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
    count_total_visits_amount()

    log(f'Request `/adult/pins` - adult_pins()',
        ipaddr=request.remote_addr)
    log(
        f'Returning `adult_pins.html`\n\tTitle={WebsiteData.adult_pins["title"]}')

    return render_template(
        "adult_pins.html",
        web_title=WebsiteData.adult_pins["title"],
        all_body_list=WebsiteData.adult_pins["all_pins_list"],
        title_of_body=WebsiteData.adult_pins["all_pins_title"]
    )


@app.route("/adult/categories")
def adult_categories():
    count_total_visits_amount()

    log(f'Request `/adult/categories` - adult_categories()',
        ipaddr=request.remote_addr)
    log(
        f'Returning `adult_pins.html`\n\tTitle={WebsiteData.adult_pins["title"]}')

    return render_template(
        "adult_pins.html",
        web_title=WebsiteData.adult_pins["title"],
        all_body_list=WebsiteData.adult_pins["all_categories_list"],
        title_of_body=WebsiteData.adult_pins["all_categories_title"]
    )


@app.route("/adult/pornstars/")
@app.route("/adult/stars/")
def adult_stars_no_page():
    count_total_visits_amount()

    log(f'Request `/adult/stars` - adult_stars_no_page()',
        ipaddr=request.remote_addr)
    log(f'Returning the url for `adult_stars` - adult_stars()\n\tbecause `<page>` is not included in the request and will default to `1`',
        ipaddr=request.remote_addr)

    return redirect(url_for('adult_stars', page=1))


@app.route("/adult/pornstars/<page>")
@app.route("/adult/stars/<page>")
def adult_stars(page):
    count_total_visits_amount()

    log(f'Request `/adult/stars/<page>` - adult_stars()',
        ipaddr=request.remote_addr)

    if (page is None) or (len(str(page)) == 0):
        page = 1
        log(f'`<page>` was set 1 because no value has been passed',
            ipaddr=request.remote_addr)

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

            log(f'REDTUBE: Pornstar List\n\tData: {WebsiteData.adult_stars["api_usage"]["data"]}\n\tPage Number: {page}',
                ipaddr=request.remote_addr)

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

            log(f'Processed all Page Numbers List', ipaddr=request.remote_addr)

    log(
        f'Returning `adult_index.html`\n\tTitle: {WebsiteData.adult_stars["title"].format(page_number=current_page)}\n\tStars Usage: {stars_usage}\n\tCurrent Page: {current_page}\n\tFirst Page: {first_page}\n\tLast Page: {last_page}\n\tPrevious Page 1: {previous_page_1}\n\tPrevious Page 2: {previous_page_2}\n\tPrevious Page 3: {previous_page_3}\n\tPrevious Page 4: {previous_page_4}\n\tNext Page 1: {next_page_1}\n\tNext Page 2: {next_page_2}\n\tNext Page 3: {next_page_3}\n\tNext Page 4: {next_page_4}\n\tShow Left Dots: {show_dots_left}\n\tShow Right Dots: {show_dots_right}', ipaddr=request.remote_addr)

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


@app.route("/adult/search_post", methods=['GET', 'POST'])
def adult_search_post():
    count_total_visits_amount()

    log(f'Request `/adult/search_post` - adult_search_post()',
        ipaddr=request.remote_addr)

    try:
        try:
            query = request.form['q']
            log(f'Query taken from `POST` request\'s `q`',
                ipaddr=request.remote_addr)
        except KeyError:
            query = request.form['query']
            log(f'Query taken from `POST` request\'s `query`',
                ipaddr=request.remote_addr)
    except KeyError:
        try:
            try:
                query = request.args.get("q")
                log(f'Query taken from `GET` request\'s `q`',
                    ipaddr=request.remote_addr)
            except KeyError:
                query = request.args.get("query")
                log(f'Query taken from `GET` request\'s `query`',
                    ipaddr=request.remote_addr)
        except:
            log(f'Unable to find the query from the request',
                ipaddr=request.remote_addr)
            return redirect(url_for('adult_index'))

    if (query is None) or len(str(query)) == 0:
        log(f'query is None. Nothing to search for!',
            ipaddr=request.remote_addr)
        return redirect(url_for('adult_index'))

    query = query.replace("/", "%2F")

    log(f'Processed Query: {query}',
        ipaddr=request.remote_addr)
    log(
        f'Returning the url for `adult_search` with query',
        ipaddr=request.remote_addr)

    return redirect(url_for('adult_search', query=query))


@app.route("/adult/search/<query>")
def adult_search(query):
    count_total_visits_amount()

    log(f'Request `/adult/search/<query>` - adult_search()',
        ipaddr=request.remote_addr)

    if query is None:
        log('Returning the url for `adult_index` - adult_index()\n\tbecause query is None. Nothing to search for!')
        return redirect(url_for('adult_index'))

    # E-Porner API
    eporner_usage = False
    eporner_list = []
    if Important.eporner_usage:
        if WebsiteData.adult_search["api_usage"]["eporner"]["usage"]:
            eporner_usage = True
            _final_url = WebsiteData.adult_search["api_usage"]["eporner"]["api_url"]
            _final_url += f'?per_page={int(WebsiteData.adult_search["api_usage"]["eporner"]["limit"]) + 2}'
            _final_url += f'&thumbsize={WebsiteData.adult_search["api_usage"]["eporner"]["thumbsize"]}'
            _final_url += f'&order={WebsiteData.adult_search["api_usage"]["eporner"]["order"]}'
            _final_url += f'&format=json'
            _final_url += f'&query={query}'

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

                log(f'EPORNER: Search Videos\n\tQuery: {query}\n\tLimit: {WebsiteData.adult_search["api_usage"]["eporner"]["limit"]}\n\tThumbnail Size: {WebsiteData.adult_search["api_usage"]["eporner"]["thumbsize"]}\n\tOrder: {WebsiteData.adult_search["api_usage"]["eporner"]["order"]}',
                    ipaddr=request.remote_addr)

            else:
                eporner_usage = False

    # RedTube API
    redtube_usage = False
    redtube_list = []
    if Important.redtube_usage:
        if WebsiteData.adult_search["api_usage"]["redtube"]["usage"]:
            redtube_usage = True
            _final_url = WebsiteData.adult_search["api_usage"]["redtube"]["api_url"]
            _final_url += f'?data={WebsiteData.adult_search["api_usage"]["redtube"]["data"]}'
            _final_url += f'&thumbsize={WebsiteData.adult_search["api_usage"]["redtube"]["thumbsize"]}'
            _final_url += f'&search=json'
            _final_url += f'&search={query}'

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

                log(
                    f'REDTUBE: Search Videos\n\tQuery: {query}\n\tData: {WebsiteData.adult_search["api_usage"]["redtube"]["data"]}\n\tThumbnail Size: {WebsiteData.adult_search["api_usage"]["redtube"]["thumbsize"]}',
                    ipaddr=request.remote_addr)

            else:
                redtube_usage = False

    log(
        f'Returning `adult_index.html`\n\tTitle={WebsiteData.adult_search["title"].format(query=query)}\n\tEPORNER API Usage={eporner_usage}\n\tREDTUBE API Usage={redtube_usage}', ipaddr=request.remote_addr)

    return render_template(
        "adult_index.html",
        web_title=WebsiteData.adult_search["title"].format(query=query),
        eporner_usage=eporner_usage,
        eporner_list=eporner_list,
        redtube_usage=redtube_usage,
        redtube_list=redtube_list
    )


@app.route("/adult/hentai")
def adult_hentai():

    log(f'Request `/adult/hentai` - adult_hentai()',
        ipaddr=request.remote_addr)

    count_total_visits_amount()

    hentai_localserverml_api_usage = False
    hentai_localserverml_api_list = []
    hentai_localserverml_api_list_request_list = []
    if Important.localserverml_usage:
        if WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["usage"]:
            hentai_localserverml_api_usage = True
            for _ in range(int(WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["limit"])):
                _final_url = WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["api_url"]
                _random_choice = random.choice(
                    WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["localserverml_enpoints"])
                _final_url += f'{_random_choice}'

                hentai_localserverml_api_list_request_list.append(
                    _final_url)

                try:
                    r = requests.get(_final_url)
                    if 300 > r.status_code >= 200:
                        url = r.text
                        if url.startswith('"') or url.endswith('"'):
                            hentai_localserverml_api_list.append(url[1:-2])
                        else:
                            hentai_localserverml_api_list.append(url)
                except:
                    pass

            log(
                f'LocalServer.ml API\n\tCount: {WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["limit"]}\n\tAll URL List: {hentai_localserverml_api_list_request_list}', ipaddr=request.remote_addr)

    hentai_nekoslife_usage = False
    hentai_nekoslife_list = []
    hentai_nekoslife_list_request_list = []
    if Important.nekoslife_usage:
        if WebsiteData.adult_hentai["api_usage"]["nekoslife"]["usage"]:
            hentai_nekoslife_usage = True
            for _ in range(int(WebsiteData.adult_hentai["api_usage"]["nekoslife"]["limit"])):
                _final_url = WebsiteData.adult_hentai["api_usage"]["nekoslife"]["api_url"]
                _random_choice = random.choice(
                    WebsiteData.adult_hentai["api_usage"]["nekoslife"]["nekoslife_endpoints"])
                _final_url += f'{_random_choice}'

                hentai_nekoslife_list_request_list.append(_final_url)

                try:
                    r = requests.get(_final_url)
                    if 300 > r.status_code >= 200:
                        data = r.json()
                        try:
                            hentai_localserverml_api_list.append(data["url"])
                        except KeyError:
                            hentai_localserverml_api_list.append(data["neko"])
                except:
                    pass

            log(
                f'Nekos.Life API:\n\tCount: {WebsiteData.adult_hentai["api_usage"]["nekoslife"]["limit"]}\n\tAll Url List: {hentai_nekoslife_list_request_list}', ipaddr=request.remote_addr)

    log(
        f'Returning `adult_index.html`\n\tTitle={WebsiteData.adult_hentai["title"]}\n\tLocalServer.ml API Usage={hentai_localserverml_api_usage}\n\tNekos.Life API Usage: {hentai_nekoslife_usage}', ipaddr=request.remote_addr)

    return render_template(
        "adult_index.html",
        web_title=WebsiteData.adult_hentai["title"],
        hentai_localserverml_api_usage=hentai_localserverml_api_usage,
        hentai_localserverml_api_list=hentai_localserverml_api_list,
        hentai_nekoslife_usage=hentai_nekoslife_usage,
        hentai_nekoslife_list=hentai_nekoslife_list
    )


@app.errorhandler(404)
def page_not_found(e):
    count_total_visits_amount()
    return render_template('404.html'), 404


def runWebServer():
    print(
        f"[+] The server will run on:\n\t[*] SFW: http://{'localhost' if (Config.host == '0.0.0.0') or (Config.host == '127.0.0.1') else Config.host}:{Config.port}/\n\t[*] NSFW: http://{'localhost' if (Config.host == '0.0.0.0') or (Config.host == '127.0.0.1') else Config.host}:{Config.port}/adult\n\t[*] Host: {Config.host}\n\t[*] Port: {Config.port}\n\t[*] Debug Mode: {Config.debug}")
    app.run(Config.host,
            port=Config.port,
            debug=Config.debug,
            )


if __name__ == "__main__":
    runWebServer()
