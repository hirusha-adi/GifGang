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
        show_torrents_index=True,
        torrents_list=torrents_list
    )
