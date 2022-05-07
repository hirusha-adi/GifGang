import services
from flask import redirect, render_template, request, url_for
from utils import WebsiteData, count_total_visits_amount, log, logf


def torrents_index():
    torrents_list = [
        {
            "title": "Send Boobies",
            "size": "6969 MB",
            "link": "LongAssMagnetURL",
            "se": 5,
            "le": 20
        },
        {
            "title": "Send Pussy Cat",
            "size": "6969 MB",
            "link": "LongAssMagnetURL",
            "se": 10,
            "le": 15
        },
    ]
    return render_template(
        "torrents/index.html",
        show_torrents_index=True,
        torrents_list=torrents_list
    )
