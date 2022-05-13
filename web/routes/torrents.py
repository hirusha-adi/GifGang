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
        web_tite="Torrents | GifGang",
        torrents_usage=True,
        torrents_list=torrents_list_sliced,
        torrents_title=f"All Torrents | Page {current_page}",
        pagination=pagination
    )


def torrents_pins():
    count_total_visits_amount()
    logf(request=request, page="torrents/pins")
    log(f'Requested `/torrents/pins` - torrents_pins()',
        ipaddr=request.remote_addr)

    torrents_list = Torrents.getTorrentsByFilter(page="pins")

    return render_template(
        "torrents/index.html",
        web_tite="Pins - Torrents | GifGang",
        torrents_usage=True,
        torrents_list=torrents_list,
        torrents_title=f"Pinned Torrents"
    )


def torrent_channel(name):
    count_total_visits_amount()
    logf(request=request, page="torrents/channel")
    log(f'Requested `/torrents/channel/<name>` - torrents_channels()',
        ipaddr=request.remote_addr)

    torrents_list = Torrents.getTorrentsByFilter(channel=str(name).lower())

    return render_template(
        "torrents/index.html",
        web_tite="Channels - Torrents | GifGang",
        torrents_usage=True,
        torrents_list=torrents_list,
        torrents_title=f"{name}"
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
        web_tite="Channels - Torrents | GifGang",
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

    return redirect(url_for('torrents_search', query=query))


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


def torrents_search(query):
    count_total_visits_amount()

    logf(request=request, page=f"torrents/search/{query}")

    log(f'Request `/torrents/search/<query>` - torrents_search()',
        ipaddr=request.remote_addr)

    if query is None:
        log('Returning the url for `torrents_index` - torrents_index()\n\tbecause query is None. Nothing to search for!')
        return redirect(url_for('torrents_index'))

    torrents_list = Torrents.getTorrentByTitle(title=f"{query}")

    return render_template(
        "torrents/index.html",
        web_tite=f"Results for {query} - Torrents | GifGang",
        torrents_usage=True,
        torrents_list=torrents_list,
        torrents_title=f"Results for {query}"
    )
