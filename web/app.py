import logging
import os
import random
import time
from threading import Thread

import requests
from flask import Flask, redirect, render_template, request, send_file, url_for, session

import services
from utils import Config, FileNames, Important, WebsiteData, log, logf, Settings

app = Flask(__name__)
log("Initiated Flask App: 'app'")
logger = logging.getLogger('werkzeug')
logger.setLevel(logging.ERROR)
log("Disabled the default `werkzeug` logging")

app.secret_key = "VerySecret12345"


COUNT = None
COUNT_TODAY = None


def reload_daily_count():
    global COUNT_TODAY

    # Reset every 24 hours
    while True:
        COUNT_TODAY = 0
        time.sleep(86400)


def count_total_visits_amount():
    global COUNT, COUNT_TODAY

    # Main
    if not(os.path.isfile(FileNames.count_file)):
        # log(f'Visit count file does not exist')
        with open(FileNames.count_file, "w", encoding="utf-8") as f_make_no_exist:
            if COUNT is None:
                f_make_no_exist.write("1")
                # log(f'Created {FileNames.count_file} and wrote "1"')
            else:
                f_make_no_exist.write(str(int(COUNT)))
                # log(f'Created {FileNames.count_file} and wrote "{COUNT}" as continuable ')

    with open(FileNames.count_file, "r", encoding="utf-8") as f_read:
        current_count = f_read.read()
        # log(f'Current view count is {current_count}')

    try:
        current_count = int(current_count)
        COUNT = current_count
    except ValueError:
        current_count = COUNT

    with open(FileNames.count_file, "r", encoding="utf-8") as f_read:
        current_count = f_read.read()
        # log(f'Current view count is {current_count}')

    # log(f'Analyzed view count is {current_count}')

    with open(FileNames.count_file, "w", encoding="utf-8") as f_write:
        new_count = COUNT + 1
        f_write.write(str(new_count))
        # log(f'New view count is {new_count}')

    # Daily
    if not(os.path.isfile(FileNames.count_file_today)):
        # log(f'Visit count-today file does not exist')
        with open(FileNames.count_file_today, "w", encoding="utf-8") as f_make_no_exist_tdy:
            if COUNT_TODAY is None:
                f_make_no_exist_tdy.write("1")
                # log(f'Created {FileNames.count_file_today} and wrote "1"')
            else:
                f_make_no_exist_tdy.write(str(int(COUNT_TODAY)))
                # log(f'Created {FileNames.count_file_today} and wrote "{COUNT_TODAY}" as continuable ')

    with open(FileNames.count_file_today, "r", encoding="utf-8") as fd_read:
        current_count_daily = fd_read.read()
        # log(f'Current view count-today is {current_count_daily}')

    try:
        current_count_daily = int(current_count_daily)
        COUNT_TODAY = current_count_daily
    except ValueError:
        current_count_daily = COUNT_TODAY

    with open(FileNames.count_file_today, "r", encoding="utf-8") as fd_read:
        current_count_daily = fd_read.read()
        # log(f'Current view count-daily is {current_count}')

    # log(f'Analyzed view count-daily is {current_count_daily}')

    with open(FileNames.count_file_today, "w", encoding="utf-8") as fd_write:
        new_count_daily = COUNT_TODAY + 1
        fd_write.write(str(new_count_daily))
        # log(f'New view count-daily is {new_count_daily}')


@app.route("/about")
def about():
    count_total_visits_amount()

    logf(request=request, page="about")

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

    logf(request=request, page="links")

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

    logf(request=request, page="")

    log(f'Requested `/` - index()',
        ipaddr=request.remote_addr)

    data = services.sfw.index.giphy(request=request)
    giphy_url_list = data["giphy_url_list"]
    giphy_usage = data["giphy_usage"]

    data = services.sfw.index.picsum(request=request)
    picsum_usage = data["picsum_usage"]
    picsum_url_list = data["picsum_url_list"]

    data = services.sfw.index.tenor(request=request)
    tenor_url_list = data["tenor_url_list"]
    tenor_usage = data["tenor_usage"]

    data = services.sfw.index.cats(request=request)
    thecatapi_url_list = data["thecatapi_url_list"]
    thecatapi_usage = data["thecatapi_usage"]

    data = services.sfw.index.dogs(request=request)
    dogceo_url_list = data["dogceo_url_list"]
    dogceo_usage = data["dogceo_usage"]

    data = services.sfw.index.nekos_life(request=request)
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

    logf(request=request, page="pins")

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

    logf(request=request, page="search_post")

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

    logf(request=request, page="restricted")

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

    logf(request=request, page="search")

    log(f'Request `/search` - search_no_query()',
        ipaddr=request.remote_addr)
    log(f'Returning the url for `index` - index()\n\tbecause `/search` route was requested without a query',
        ipaddr=request.remote_addr)

    return redirect(url_for('index'))


@app.route("/search/<query>")
def search(query):
    count_total_visits_amount()

    logf(request=request, page=f"search/{query}")

    log(f'Request `/search/<query>` - search(query)',
        ipaddr=request.remote_addr)

    if query is None:
        log(f'query is None\n\tRedirecting to the url of `index`',
            ipaddr=request.remote_addr)
        return redirect(url_for('index'))

    # Others - will be searched be used only by analyzing the query
    data = services.sfw.search.others(request=request, query=query)
    thecatapi_url_list = data["thecatapi_url_list"]
    thecatapi_usage = data["thecatapi_usage"]
    dogceo_url_list = data["dogceo_url_list"]
    dogceo_usage = data["dogceo_usage"]
    nekoslife_url_list = data["nekoslife_url_list"]
    nekoslife_usage = data["nekoslife_usage"]

    # GIPHY and TENOR will be used to search, no matter what the query is entered if enabled by json
    data = services.sfw.search.gihpy(request=request, query=query)
    giphy_url_list = data["giphy_url_list"]
    giphy_usage = data["giphy_usage"]

    data = services.sfw.search.tenor(request=request, query=query)
    tenor_url_list = data["tenor_url_list"]
    tenor_usage = data["tenor_usage"]

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

    logf(request=request, page="adult")

    count_total_visits_amount()

    log(f'Request `/adult` - adult_index()', ipaddr=request.remote_addr)

    data = services.nsfw.index.eporner(request=request)
    eporner_usage = data["eporner_usage"]
    eporner_list = data["eporner_list"]

    data = services.nsfw.index.redtube(request=request)
    redtube_usage = data["redtube_usage"]
    redtube_list = data["redtube_list"]

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

    logf(request=request, page="adult/pins")

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

    logf(request=request, page="adult/categories")

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

    logf(request=request, page="adult/stars")

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

    logf(request=request, page=f"adult/stars/{page}")

    data = services.nsfw.stars.getAll(request=request, page=page)
    stars_list = data["stars_list"]
    stars_usage = data["stars_usage"]

    current_page = data["current_page"]
    first_page = data["first_page"]
    last_page = data["last_page"]
    previous_page_1 = data["previous_page_1"]
    previous_page_2 = data["previous_page_2"]
    previous_page_3 = data["previous_page_3"]
    previous_page_4 = data["previous_page_4"]
    next_page_1 = data["next_page_1"]
    next_page_2 = data["next_page_2"]
    next_page_3 = data["next_page_3"]
    next_page_4 = data["next_page_4"]
    show_dots_right = data["show_dots_right"]
    show_dots_left = data["show_dots_left"]

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

    logf(request=request, page="adult/search_post")

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


@app.route("/adult/search")
def adult_search_no_query():
    count_total_visits_amount()

    logf(request=request, page=f"adult/search")

    log(f'Request `/adult/search` - adult_search_no_query()',
        ipaddr=request.remote_addr)

    return redirect(url_for('adult_index'))


@app.route("/adult/search/<query>")
def adult_search(query):
    count_total_visits_amount()

    logf(request=request, page=f"adult/search/{query}")

    log(f'Request `/adult/search/<query>` - adult_search()',
        ipaddr=request.remote_addr)

    if query is None:
        log('Returning the url for `adult_index` - adult_index()\n\tbecause query is None. Nothing to search for!')
        return redirect(url_for('adult_index'))

    # E-Porner API
    data = services.nsfw.search.eporner(request=request, query=query)
    eporner_usage = data["eporner_usage"]
    eporner_list = data["eporner_list"]

    # RedTube API
    data = services.nsfw.search.redtube(request=request, query=query)
    redtube_usage = data["redtube_usage"]
    redtube_list = data["redtube_list"]

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

    logf(request=request, page=f"adult/hentai")

    log(f'Request `/adult/hentai` - adult_hentai()',
        ipaddr=request.remote_addr)

    count_total_visits_amount()

    data = services.nsfw.hentai.localserverml(request=request)
    hentai_localserverml_api_usage = data["hentai_localserverml_api_usage"]
    hentai_localserverml_api_list = data["hentai_localserverml_api_list"]
    hentai_localserverml_api_list_request_list = data["hentai_localserverml_api_list_request_list"]

    data = services.nsfw.hentai.nekos_life(request=request)
    hentai_nekoslife_usage = data["hentai_nekoslife_usage"]
    hentai_nekoslife_list = data["hentai_nekoslife_list"]
    hentai_nekoslife_list_request_list = data["hentai_nekoslife_list_request_list"]

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


@app.route("/stats")
def public_stats():
    count_total_visits_amount()

    global COUNT

    logf(request=request, page=f"stats")

    log(f'Request `/stats` - public_stats()',
        ipaddr=request.remote_addr)

    return render_template("stats.html", request_count=COUNT)


@app.route("/admin")
def adult_route_main():
    count_total_visits_amount()

    logf(request=request, page=f"admin")

    log(f'Request `/admin` - adult_route_main()',
        ipaddr=request.remote_addr)

    return redirect(url_for('admin_login_page'))


@app.route("/admin/login")
def admin_login_page():
    count_total_visits_amount()

    logf(request=request, page=f"admin/login")

    log(f'Request `/admin/login` - admin_login_page()',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:
            return redirect(url_for('admin_panel_page'))
    except KeyError:
        session["token"] = ""

    return render_template(
        "admin_login.html"
    )


@app.route("/admin/login/verify", methods=['POST'])
def admin_login_page_verify():
    count_total_visits_amount()

    logf(request=request, page=f"admin/login/verify")

    log(f'Request `/admin/login/verify` - admin_login_page_verify()',
        ipaddr=request.remote_addr)

    try:
        username = request.form.get("uname")
        password = request.form.get("pass")
    except:
        return redirect(url_for('admin_login_page'))

    if (username == Settings.Admin.username) and (password == Settings.Admin.password):
        session["token"] = Settings.Admin.token
        return redirect(url_for("admin_panel_page"))


@app.route("/admin/download/log/latest")
def admin_download_log_file():
    count_total_visits_amount()

    logf(request=request, page="admin/download/log/latest")

    log(f'Requested `/admin/download/log/latest` - admin_download_log_file()',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:
            return send_file(FileNames._log_file)

        else:
            return redirect(url_for("admin_login_page"))
    except:
        return redirect(url_for("admin_login_page"))


@app.route("/admin/panel")
def admin_panel_page():
    count_total_visits_amount()

    logf(request=request, page="admin/panel")

    log(f'Requested `/admin/panel` - admin_panel_page()',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:

            global COUNT, COUNT_TODAY

            percentage_of_today_from_total = round(
                ((COUNT_TODAY/COUNT)*100), 2)

            percentage_target_today = round(
                ((COUNT_TODAY/Settings.Admin.targets_today)*100), 2)
            percentage_target_all = round(
                ((COUNT/Settings.Admin.targets_all)*100), 2)

            try:
                final_log_file_name = os.listdir(
                    os.path.join(os.getcwd(), "logs"))[-1]
                final_log_file = os.path.join(
                    os.getcwd(),
                    "logs",
                    final_log_file_name
                )

                with open(final_log_file, "r", encoding="utf-8") as log_file_content:
                    log_file_lines = log_file_content.readlines()[-5:]

                log_file_lines_last_5 = log_file_lines[::-1]

            except Exception as e:
                print(e)
                final_log_file_name = str(e)
                log_file_lines_last_5 = []

            return render_template(
                "admin_panel.html",
                total_requests_all_time=COUNT,
                total_requests_last_24h=COUNT_TODAY,
                percentage_of_today_from_total=percentage_of_today_from_total,
                final_log_file_name=final_log_file_name,
                log_file_lines_last_5=log_file_lines_last_5,
                percentage_target_today=percentage_target_today,
                percentage_target_all=percentage_target_all,
                admin_profile_picture=Settings.Admin.profile_pic,
            )

        else:
            return redirect(url_for("admin_login_page"))
    except:
        return redirect(url_for("admin_login_page"))


@app.route("/admin/settings")
def admin_settings():
    count_total_visits_amount()

    logf(request=request, page="admin/settings")

    log(f'Requested `/admin/settings` - admin_settings()',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:
            return redirect(url_for('admin_settings_admin'))
        else:
            return redirect(url_for("admin_login_page"))
    except Exception as e:
        return redirect(url_for("admin_login_page"))


@app.route("/admin/settings/admin")
def admin_settings_admin():
    count_total_visits_amount()

    logf(request=request, page="admin/settings/admin")

    log(f'Requested `/admin/settings/admin` - admin_settings_admin()',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:
            return render_template(
                "admin_settings.html",
                show_admin_settings=True,
                admin_settings_data=Settings.Admin,
                show_important_settings=False,
                show_index=False,
                show_search=False,
                show_pins=False,
                show_age_verify=False,
                show_adult_index=False,
                show_adult_pins=False,
                show_adult_stars=False,
                show_adult_search=False,
                show_adult_hentai=False,
            )

        else:
            return redirect(url_for("admin_login_page"))
    except Exception as e:
        print(e)
        return redirect(url_for("admin_login_page"))


@app.route("/admin/settings/important")
def admin_settings_important():
    count_total_visits_amount()

    logf(request=request, page="admin/settings/important")

    log(f'Requested `/admin/settings/important` - admin_settings_important()',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:
            return render_template(
                "admin_settings.html",
                show_admin_settings=False,
                show_important_settings=True,
                import_settings_data=Important,
                show_index=False,
                show_search=False,
                show_pins=False,
                show_age_verify=False,
                show_adult_index=False,
                show_adult_pins=False,
                show_adult_stars=False,
                show_adult_search=False,
                show_adult_hentai=False,
            )

        else:
            return redirect(url_for("admin_login_page"))
    except:
        return redirect(url_for("admin_login_page"))


@app.route("/admin/settings/index")
def admin_settings_index():
    count_total_visits_amount()

    logf(request=request, page="admin/settings/index")

    log(f'Requested `/admin/settings/index` - admin_settings_index()',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:
            return render_template(
                "admin_settings.html",
                show_admin_settings=False,
                show_important_settings=False,
                show_index=True,
                index_data=WebsiteData.index,
                show_search=False,
                show_pins=False,
                show_age_verify=False,
                show_adult_index=False,
                show_adult_pins=False,
                show_adult_stars=False,
                show_adult_search=False,
                show_adult_hentai=False,
            )

        else:
            return redirect(url_for("admin_login_page"))
    except:
        return redirect(url_for("admin_login_page"))


@app.route("/admin/settings/search")
def admin_settings_search():
    count_total_visits_amount()

    logf(request=request, page="admin/settings/search")

    log(f'Requested `/admin/settings/search` - admin_settings_search()',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:
            return render_template(
                "admin_settings.html",
                show_admin_settings=False,
                show_important_settings=False,
                show_index=False,
                show_search=True,
                search_data=WebsiteData.search,
                show_pins=False,
                show_age_verify=False,
                show_adult_index=False,
                show_adult_pins=False,
                show_adult_stars=False,
                show_adult_search=False,
                show_adult_hentai=False,
            )

        else:
            return redirect(url_for("admin_login_page"))
    except Exception:
        return redirect(url_for("admin_login_page"))


@app.route("/admin/settings/pins")
def admin_settings_pins():
    count_total_visits_amount()

    logf(request=request, page="admin/settings/pins")

    log(f'Requested `/admin/settings/pins` - admin_settings_pins()',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:
            return render_template(
                "admin_settings.html",
                show_admin_settings=False,
                show_important_settings=False,
                show_index=False,
                show_search=False,
                show_pins=True,
                pins_data=WebsiteData.pins,
                show_age_verify=False,
                show_adult_index=False,
                show_adult_pins=False,
                show_adult_stars=False,
                show_adult_search=False,
                show_adult_hentai=False,
            )

        else:
            return redirect(url_for("admin_login_page"))
    except Exception:
        return redirect(url_for("admin_login_page"))


@app.route("/logout")
def admin_logout():
    count_total_visits_amount()

    logf(request=request, page="/logout")

    log(f'Requested `/logout` - count_total_visits_amount()',
        ipaddr=request.remote_addr)

    session["token"] = ""
    return redirect(url_for('admin_login_page'))


@app.errorhandler(404)
def page_not_found(e):
    count_total_visits_amount()
    return render_template('404.html'), 404


def runWebServer():
    reset_count_24h = Thread(target=reload_daily_count)
    reset_count_24h.start()

    print(
        f"[+] The server will run on:\n\t[*] SFW: http://{'localhost' if (Config.host == '0.0.0.0') or (Config.host == '127.0.0.1') else Config.host}:{Config.port}/\n\t[*] NSFW: http://{'localhost' if (Config.host == '0.0.0.0') or (Config.host == '127.0.0.1') else Config.host}:{Config.port}/adult\n\t[*] Host: {Config.host}\n\t[*] Port: {Config.port}\n\t[*] Debug Mode: {Config.debug}")
    app.run(Config.host,
            port=Config.port,
            debug=Config.debug,
            )


if __name__ == "__main__":
    runWebServer()
