from flask import redirect, render_template, request, url_for

import services
from utils import WebsiteData, log, logf, count_total_visits_amount



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


def adult_stars_no_page():
    count_total_visits_amount()

    logf(request=request, page="adult/stars")

    log(f'Request `/adult/stars` - adult_stars_no_page()',
        ipaddr=request.remote_addr)
    log(f'Returning the url for `adult_stars` - adult_stars()\n\tbecause `<page>` is not included in the request and will default to `1`',
        ipaddr=request.remote_addr)

    return redirect(url_for('adult_stars', page=1))


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


def adult_search_no_query():
    count_total_visits_amount()

    logf(request=request, page=f"adult/search")

    log(f'Request `/adult/search` - adult_search_no_query()',
        ipaddr=request.remote_addr)

    return redirect(url_for('adult_index'))


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
