import services
from flask import redirect, render_template, request, url_for
from utils import WebsiteData, count_total_visits_amount, log, logf
from database.mongo import Torrents
from flask_paginate import Pagination


def torrents_index_no_page():
    count_total_visits_amount()
    logf(request=request, page="torrents")
    log(f'Requested `/torrents` - torrents_index_no_page()',
        ipaddr=request.remote_addr)

    return redirect(url_for('torrents_index', page="1"))


def torrents_index(page):
    count_total_visits_amount()
    logf(request=request, page="torrents/<page>")
    log(f'Requested `/torrents/<page>` - torrents_index()',
        ipaddr=request.remote_addr)

    try:
        current_page = int(page)
    except:
        return redirect(url_for('torrents_search_no_query'))

    torrents_list_all = Torrents.getAllTorrents()
    torrents_list_length = len(torrents_list_all)

    try:
        per_page = int(WebsiteData.torrents_catgories['per_page'])
    except:
        per_page = 25

    max_possible_page = (torrents_list_length // per_page)+1
    if current_page > max_possible_page:
        current_page = max_possible_page

    pagination = Pagination(
        torrents_list_all,
        per_page=per_page,
        page=current_page,
        total=torrents_list_length,
        href=str(url_for('torrents_index', page=1))[:-1] + "{0}"

    )

    min_index = (current_page*per_page) - per_page
    max_index = (min_index + per_page)

    torrents_list_sliced = torrents_list_all[min_index:max_index]

    return render_template(
        "torrents/index.html",
        web_title="Torrents | GifGang",
        torrents_usage=True,
        torrents_list=torrents_list_sliced,
        torrents_title=f"All Torrents | Page {current_page}",
        pagination=pagination
    )


def torrents_pins_no_page():
    count_total_visits_amount()
    logf(request=request, page="torrents/pins")
    log(f'Requested `/torrents/pins` - torrents_pins_no_page()',
        ipaddr=request.remote_addr)
    return redirect(url_for('torrents_pins', page=1))


def torrents_pins(page):
    count_total_visits_amount()
    logf(request=request, page="torrents/pins")
    log(f'Requested `/torrents/pins` - torrents_pins()',
        ipaddr=request.remote_addr)

    try:
        current_page = int(page)
    except:
        return redirect(url_for('torrents_pins_no_page'))

    torrents_list_all = Torrents.getTorrentsByFilter(page="pins")
    torrents_list_length = len(torrents_list_all)

    try:
        per_page = int(WebsiteData.torrents_catgories['per_page'])
    except:
        per_page = 25

    max_possible_page = (torrents_list_length // per_page)+1
    if current_page > max_possible_page:
        current_page = max_possible_page

    pagination = Pagination(
        torrents_list_all,
        per_page=per_page,
        page=current_page,
        total=torrents_list_length,
        href=str(url_for('torrents_pins', page=1))[:-1] + "{0}"
    )

    min_index = (current_page*per_page) - per_page
    max_index = (min_index + per_page)

    torrents_list_sliced = torrents_list_all[min_index:max_index]

    return render_template(
        "torrents/index.html",
        web_title="Pins - Torrents | GifGang",
        torrents_usage=True,
        torrents_list=torrents_list_sliced,
        torrents_title=f"Pinned Torrents",
        pagination=pagination
    )


def torrent_channel_no_page(name):
    count_total_visits_amount()
    logf(request=request, page="torrents/channel/<name>")
    log(f'Requested `/torrents/channel/<name>` - torrent_channel_no_page()',
        ipaddr=request.remote_addr)

    return redirect(url_for('torrent_channel', name=name, page=1))


def torrent_channel(name, page):
    count_total_visits_amount()
    logf(request=request, page="torrents/channel/<name>/<page>")
    log(f'Requested `/torrents/channel/<name>/<page>` - torrents_channel(name, page)',
        ipaddr=request.remote_addr)

    if name is None:
        log('Returning the url for `torrents_channel` - torrents_channels()\n\tbecause name is None. Nothing to search for!')
        return redirect(url_for('torrents_channels'))

    if page is None:
        log('No page to go, defaulting to 1!')
        page = 1
    try:
        current_page = int(page)
    except:
        return redirect(url_for('torrents_search_no_query'))

    all_names = []
    for channel_dict in WebsiteData.torrents_catgories['all_cat_list']:
        all_names.append(channel_dict["name"].lower())

    name = str(name).lower()
    if not(name in all_names):
        name = "other"

    if name == "other":
        torrents_list_all = Torrents.getTorrentsOtherChannel(nin=all_names)
    else:
        torrents_list_all = Torrents.getTorrentsByFilter(
            channel=str(name).lower()
        )
    torrents_list_length = len(torrents_list_all)

    try:
        per_page = int(WebsiteData.torrents_catgories['per_page'])
    except:
        per_page = 25

    max_possible_page = (torrents_list_length // per_page)+1
    if current_page > max_possible_page:
        current_page = max_possible_page

    pagination = Pagination(
        torrents_list_all,
        per_page=per_page,
        page=current_page,
        total=torrents_list_length,
        href=str(url_for('torrent_channel', name=name, page=1))[:-1] + "{0}"
    )

    min_index = (current_page*per_page) - per_page
    max_index = (min_index + per_page)

    torrents_list_sliced = torrents_list_all[min_index:max_index]

    return render_template(
        "torrents/index.html",
        web_title="Channels - Torrents | GifGang",
        torrents_usage=True,
        torrents_list=torrents_list_sliced,
        torrents_title=f"{name}",
        pagination=pagination
    )


def torrent_channel_no_args():
    count_total_visits_amount()
    logf(request=request, page="torrents/channel")
    log(f'Requested `/torrents/channel` - torrent_channel_no_args()',
        ipaddr=request.remote_addr)

    return redirect(url_for('torrents_channels'))


def torrents_channels():
    count_total_visits_amount()
    logf(request=request, page="torrents/channels")
    log(f'Requested `/torrents/channels` - torrents_channels()',
        ipaddr=request.remote_addr)

    return render_template(
        "torrents/index.html",
        web_title="Channels - Torrents | GifGang",
        show_categories=True,
        all_pins_list=WebsiteData.torrents_catgories['all_cat_list']
    )


def search_torrent_post():
    count_total_visits_amount()

    logf(request=request, page="torrents/search_post")

    log(f'Request `/torrents/search_post` - search_torrent_post()',
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
            return redirect(url_for('torrents_index'))

    if (query is None) or len(str(query)) == 0:
        log(f'query is None. Nothing to search for!',
            ipaddr=request.remote_addr)
        return redirect(url_for('torrents_index'))

    query = query.replace("/", "%2F")

    log(f'Processed Query: {query}',
        ipaddr=request.remote_addr)
    log(
        f'Returning the url for `torrents_search` with query',
        ipaddr=request.remote_addr)

    return redirect(url_for('torrents_search_no_page', query=query))


def torrents_search_no_query():
    count_total_visits_amount()

    logf(request=request, page=f"torrents/search")

    log(f'Request `/torrents/search` - torrents_search_no_query()',
        ipaddr=request.remote_addr)

    return render_template(
        "search.html",
        search_type="torrents",
        web_title="NSFW Torrents | GifGang",
        search_title="Search for NSFW Torrents"
    )


def torrents_search_no_page(query):
    count_total_visits_amount()

    logf(request=request, page=f"torrents/search/{query}")

    log(f'Request `/torrents/search/<query>` - torrents_search_no_page(query)',
        ipaddr=request.remote_addr)

    if query is None:
        log('Returning the url for `torrents_index` - torrents_index()\n\tbecause query is None. Nothing to search for!')
        return redirect(url_for('torrents_index'))

    return redirect(url_for('torrents_search', query=query, page=1))


def torrents_search(query, page):
    count_total_visits_amount()

    logf(request=request, page=f"torrents/search/{query}/<page>")

    log(f'Request `/torrents/search/<query>/<page>` - torrents_search(query, page)',
        ipaddr=request.remote_addr)

    if query is None:
        log('Returning the url for `torrents_index` - torrents_index()\n\tbecause query is None. Nothing to search for!')
        return redirect(url_for('torrents_index'))

    if page is None:
        log('No page to go, defaulting to 1!')
        page = 1

    try:
        current_page = int(page)
    except:
        return redirect(url_for('torrents_search_no_query'))

    torrents_list_all = Torrents.getTorrentByTitle(title=f"{query}")
    torrents_list_length = len(torrents_list_all)

    try:
        per_page = int(WebsiteData.torrents_catgories['per_page'])
    except:
        per_page = 25

    max_possible_page = (torrents_list_length // per_page)+1
    if current_page > max_possible_page:
        current_page = max_possible_page

    pagination = Pagination(
        torrents_list_all,
        per_page=per_page,
        page=current_page,
        total=torrents_list_length,
        href=str(url_for('torrents_search', query=query, page=1))[:-1] + "{0}"
    )

    min_index = (current_page*per_page) - per_page
    max_index = (min_index + per_page)

    torrents_list_sliced = torrents_list_all[min_index:max_index]

    return render_template(
        "torrents/index.html",
        web_title=f"Results for {query} - Torrents | GifGang",
        torrents_usage=True,
        torrents_list=torrents_list_sliced,
        torrents_title=f"Results for {query}",
        pagination=pagination
    )
