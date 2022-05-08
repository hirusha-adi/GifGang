import services
from flask import redirect, render_template, request, url_for
from utils import count_total_visits_amount, log, logf
from db import Torrents


def torrents_index():
    count_total_visits_amount()
    logf(request=request, page="torrents")
    log(f'Requested `/torrents` - torrents_index()',
        ipaddr=request.remote_addr)

    torrents_list = Torrents.getAllTorrents()

    return render_template(
        "torrents/index.html",
        torrents_list=torrents_list,
        torrents_title=f"All Torrents"
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

    return redirect(url_for('torrents_index'))


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
        torrents_list=torrents_list,
        torrents_title=f"Results for {query}"
    )
