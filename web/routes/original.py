import services
from flask import redirect, render_template, request, url_for
from utils import WebsiteData, count_total_visits_amount, log, logf, Vars


def about():
    count_total_visits_amount()

    logf(request=request, page="about")

    log(f'Requested `/about` - about()',
        ipaddr=request.remote_addr)
    log('Returning `sfw/about.html`',
        ipaddr=request.remote_addr)
    return render_template(
        "sfw/about.html",
        web_title="About | GifGang"
    )


def all_links():
    count_total_visits_amount()

    logf(request=request, page="links")

    log(f'Requested `/links` - all_links()',
        ipaddr=request.remote_addr)

    log('Returning `sfw/index.html`\n\tall_links_page = True',
        ipaddr=request.remote_addr)

    return render_template(
        "sfw/index.html",
        web_title="Links List | GifGang",
        all_links_page=True
    )


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

    log(f'Returning `sfw/index.html`\n\ttitle={WebsiteData.index["title"]}\n\tgiphy_usage={giphy_usage}\n\tpicsum_usage={picsum_usage}\n\ttenor_usage={tenor_usage}\n\tthecatapi_usage={thecatapi_usage}\n\tdogceo_usage={dogceo_usage}\n\tnekoslife_usage={nekoslife_usage}',
        ipaddr=request.remote_addr)

    return render_template(
        "sfw/index.html",
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


def pins():
    count_total_visits_amount()

    logf(request=request, page="pins")

    log(f'{request.remote_addr} requested `/pins` - pins()',
        ipaddr=request.remote_addr)
    log(
        f'Returning `sfw/pins.html`\n\tTitle={WebsiteData.pins["title"]}\n\tPins List from `website.json`',
        ipaddr=request.remote_addr)

    return render_template(
        "sfw/pins.html",
        web_title=WebsiteData.pins["title"],
        all_pins_list=WebsiteData.pins["all_list"]
    )


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


def search_no_query():
    count_total_visits_amount()

    logf(request=request, page="search")

    log(f'Request `/search` - search_no_query()',
        ipaddr=request.remote_addr)
    log(f'Returning the url for `index` - index()\n\tbecause `/search` route was requested without a query',
        ipaddr=request.remote_addr)

    return redirect(url_for('index'))


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
        "sfw/search.html",
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


def public_stats():
    count_total_visits_amount()

    logf(request=request, page=f"stats")

    log(f'Request `/stats` - public_stats()',
        ipaddr=request.remote_addr)

    return render_template("sfw/index.html", show_gifgang_stats=True, request_count=Vars.COUNT, web_title="Stats - Public | GifGang")
